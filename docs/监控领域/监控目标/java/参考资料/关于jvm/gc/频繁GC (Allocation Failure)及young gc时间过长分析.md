# 频繁GC (Allocation Failure)及young gc时间过长分析

## 序

本文主要分析一个频繁GC (Allocation Failure)及young gc时间过长的case。

## 症状

- gc throughput percent逐步下降，从一般的99.96%逐步下降，跌破99%，进入98%，最低点能到94%
- young gc time逐步增加，从一般的十几毫秒逐步上升，突破50，再突破100，150，200，250
- 在8.5天的时间内，发生了9000多次gc，其中full gc为4次，平均将近8秒，大部分是young gc(`allocation failure为主`)，平均270多毫秒，最大值将近7秒
- 平均对象创建速率为10.63 mb/sec，平均的晋升速率为2 kb/sec，cpu使用率正常，没有明显的飙升

### jvm参数

```
-XX:+UseParallelGC -XX:+UseParallelOldGC -XX:ParallelGCThreads=4 -XX:+UseAdaptiveSizePolicy -XX:MaxHeapSize=2147483648 -XX:MaxNewSize=1073741824 -XX:NewSize=1073741824 -XX:+PrintGCDetails -XX:+PrintTenuringDistribution -XX:+PrintGCTimeStamps
复制代码
```

*jdk版本*

```
java -version
java version "1.8.0_66"
Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)
复制代码
```

## full gc

```
27.066: [Full GC (Metadata GC Threshold) [PSYoungGen: 19211K->0K(917504K)] [ParOldGen: 80K->18440K(1048576K)] 19291K->18440K(1966080K), [Metaspace: 20943K->20943K(1069056K)], 0.5005658 secs] [Times: user=0.24 sys=0.01, real=0.50 secs] 
100.675: [Full GC (Metadata GC Threshold) [PSYoungGen: 14699K->0K(917504K)] [ParOldGen: 18464K->23826K(1048576K)] 33164K->23826K(1966080K), [Metaspace: 34777K->34777K(1081344K)], 0.7937738 secs] [Times: user=0.37 sys=0.01, real=0.79 secs]
195.073: [Full GC (Metadata GC Threshold) [PSYoungGen: 24843K->0K(1022464K)] [ParOldGen: 30048K->44782K(1048576K)] 54892K->44782K(2071040K), [Metaspace: 58220K->58220K(1101824K)], 3.7936515 secs] [Times: user=1.86 sys=0.02, real=3.79 secs] 
242605.669: [Full GC (Ergonomics) [PSYoungGen: 67276K->0K(882688K)] [ParOldGen: 1042358K->117634K(1048576K)] 1109635K->117634K(1931264K), [Metaspace: 91365K->90958K(1132544K)], 22.1573804 secs] [Times: user=2.50 sys=3.51, real=22.16 secs]
复制代码
```

> 可以发现发生的4次full gc，前三次都是由于Metadata GC Threshold造成的，只有最后一次是由于Ergonomics引发的。

### Full GC (Metadata GC Threshold)

这里使用的是java8，参数没有明确指定metaspace的大小和上限，查看一下

```
jstat -gcmetacapacity 7
   MCMN       MCMX        MC       CCSMN      CCSMX       CCSC     YGC   FGC    FGCT     GCT
       0.0  1136640.0    99456.0        0.0  1048576.0    12160.0 38009    16  275.801 14361.992
复制代码
```

- 忽略后面的FGC，因为分析的日志只是其中四分之一
- 这里可以看到MCMX(Maximum metaspace capacity (kB))有一个多G，而MC(Metaspace capacity (kB))才97M左右，为啥会引起Full GC (Metadata GC Threshold)

*相关参数*

- -XX:MetaspaceSize，初始空间大小(也是初始的阈值，即初始的high-water-mark)，达到该值就会触发垃圾收集进行类型卸载，同时GC会对该值进行调整：如果释放了大量的空间，就适当降低该值；如果释放了很少的空间，那么在不超过MaxMetaspaceSize时，适当提高该值。
- -XX:MaxMetaspaceSize，最大空间，默认是没有限制的，取决于本地系统空间容量。
- -XX:MinMetaspaceFreeRatio，在GC之后，最小的Metaspace剩余空间容量的百分比(`即元数据在当前分配大小的最大占用大小`)，如果空闲比小于这个参数(`即超过了最大占用大小`)，那么将对meta space进行扩容。
- -XX:MaxMetaspaceFreeRatio，在GC之后，最大的Metaspace剩余空间容量的百分比(`即元数据在当前分配大小的最小占用大小`)，如果空闲比大于这个参数(`即小于最小占用大小`)，那么将对meta space进行缩容.

> 由于没有设置，在机器上的默认值为：

```
java -XX:+PrintFlagsFinal | grep Meta
    uintx InitialBootClassLoaderMetaspaceSize       = 4194304                             {product}
    uintx MaxMetaspaceExpansion                     = 5451776                             {product}
    uintx MaxMetaspaceFreeRatio                     = 70                                  {product}
    uintx MaxMetaspaceSize                          = 18446744073709547520                    {product}
    uintx MetaspaceSize                             = 21807104                            {pd product}
    uintx MinMetaspaceExpansion                     = 339968                              {product}
    uintx MinMetaspaceFreeRatio                     = 40                                  {product}
     bool TraceMetadataHumongousAllocation          = false                               {product}
     bool UseLargePagesInMetaspace                  = false                               {product}
复制代码
```

> 可以看到MinMetaspaceFreeRatio为40，MaxMetaspaceFreeRatio为70，MetaspaceSize为20M，Full GC (Metadata GC Threshold)主要分为了三次

- 第一次，[Metaspace: 20943K->20943K(1069056K)]
- 第二次，[Metaspace: 34777K->34777K(1081344K)]
- 第三次，[Metaspace: 58220K->58220K(1101824K)]

> 可以看到metaspace的阈值不断动态调整，至于具体调整的逻辑，官方文档貌似没讲，这里暂时不深究。只要没有超过Max值就没有致命影响，但是对于低延时的应用来讲，是要尽量避免动态调整引起的gc耗时，可以根据调优计算并设置初始阈值来解决。

### Full GC (Ergonomics)

这里可以到full gc的reason是Ergonomics，是因为开启了UseAdaptiveSizePolicy，jvm自己进行自适应调整引发的full gc

## GC (Allocation Failure)

分析完full gc之后我们看下young gc，看log里头99%都是GC (Allocation Failure)造成的young gc。Allocation Failure表示向young generation(eden)给新对象申请空间，但是young generation(eden)剩余的合适空间不够所需的大小导致的minor gc。

### -XX:+PrintTenuringDistribution

```
Desired survivor size 75497472 bytes, new threshold 2 (max 15)
- age   1:   68407384 bytes,   68407384 total
- age   2:   12494576 bytes,   80901960 total
- age   3:      79376 bytes,   80981336 total
- age   4:    2904256 bytes,   83885592 total
复制代码
```

- 这个Desired survivor size表示survivor区域允许容纳的最大空间大小为75497472 bytes
- 下面的对象列表为此次gc之后，survivor当前存活对象的年龄大小分布，total大小为83885592 > 75497472，而age1大小为68407384 < 75497472，因此new threshold变为2(`作用于下次gc`)。下次gc如果对象没释放的话，超过阈值的对象将晋升到old generation。

### age list为空

```
59.463: [GC (Allocation Failure) 
Desired survivor size 134217728 bytes, new threshold 7 (max 15)
[PSYoungGen: 786432K->14020K(917504K)] 804872K->32469K(1966080K), 0.1116049 secs] [Times: user=0.10 sys=0.01, real=0.20 secs] 
复制代码
```

> 这里Desired survivor size这行下面并没有各个age对象的分布，那就表示此次gc之后，当前survivor区域并没有age小于max threshold的存活对象。而这里一个都没有输出，表示此次gc回收对象之后，没有存活的对象可以拷贝到新的survivor区。

*gc之后survivor有对象的例子*

```
jstat -gcutil -h10 7 10000 10000
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT     GCT
  0.00  99.99  90.38  29.82  97.84  96.99    413  158.501     4   14.597  173.098
 11.60   0.00  76.00  29.83  97.84  96.99    414  158.511     4   14.597  173.109
 11.60   0.00  77.16  29.83  97.84  96.99    414  158.511     4   14.597  173.109
  0.00  13.67  60.04  29.83  97.84  96.99    415  158.578     4   14.597  173.176
  0.00  13.67  61.05  29.83  97.84  96.99    415  158.578     4   14.597  173.176
复制代码
```

- 在ygc之前young generation = eden + S1；ygc之后，young generation = eden + S0
- 观察可以看到ygc之后old generation空间没变，表示此次ygc，没有对象晋升到old generation。
- gc之后，存活对象搬移到了另外一个survivor区域
- 这里由于是每个10秒采样一次，存在延迟，即gc之后，立马有新对象在eden区域分配了，因此这里看到的eden区域有对象占用。

### real time > usr time + sys time

```
722914.974: [GC (Allocation Failure) 
Desired survivor size 109576192 bytes, new threshold 15 (max 15)
[PSYoungGen: 876522K->8608K(941568K)] 1526192K->658293K(1990144K), 0.0102709 secs] [Times: user=0.03 sys=0.00, real=0.01 secs] 
722975.207: [GC (Allocation Failure) 
Desired survivor size 103284736 bytes, new threshold 15 (max 15)
[PSYoungGen: 843168K->39278K(941568K)] 1492853K->688988K(1990144K), 0.3607036 secs] [Times: user=0.17 sys=0.00, real=0.36 secs] 
复制代码
```

> 里头有大于将近300次的gc的real time时间大于usr time + sys time。

- real：指的是操作从开始到结束所经过的墙钟时间（WallClock Time）
- user：指的是用户态消耗的CPU时间；
- sys：指的是内核态消耗的CPU时间。

> 墙钟时间包括各种非运算的等待耗时，例如等待磁盘I/O、等待线程阻塞，而CPU时间不包括这些耗时，但当系统有多CPU或者多核的话，多线程操作会叠加这些CPU时间，所以看到user或sys时间超过real时间是完全正常的。

> user + sys 就是CPU花费的实际时间，注意这个值统计了所有CPU上的时间，如果进程工作在多线程的环境下，叠加了多线程的时间，这个值是会超出 real 所记录的值的，即 user + sys >= real 。

> 这里300多次real time时间大于usr time + sys time，表明可能有两个问题，一个是IO操作密集，另一个是cpu(`分配`)的额度不够。

## 新生代垃圾回收机制

- 新对象尝试栈上分配，不行再尝试TLAB分配，不行则考虑是否直接绕过eden区在年老代分配空间(

  ```
  -XX:PretenureSizeThreshold设置大对象直接进入年老代的阈值，当对象大小超过这个值时，将直接在年老代分配。
  ```

  )，不行则最后考虑在eden申请空间

  ![img](频繁GC (Allocation Failure)及young gc时间过长分析.assets/161ef70439612677)

- 向eden申请空间创建新对象，eden没有合适的空间，因此触发minor gc

- minor gc将eden区及from survivor区域的存活对象进行处理

  - 如果这些对象年龄达到阈值，则直接晋升到年老代
  - 若要拷贝的对象太大，那么不会拷贝到to survivor，而是直接进入年老代
  - 若to survivor区域空间不够/或者复制过程中出现不够，则发生survivor溢出，直接进入年老代
  - 其他的，若to survivor区域空间够，则存活对象拷贝到to survivor区域

- 此时eden区及from survivor区域的剩余对象为垃圾对象，直接抹掉回收，释放的空间成为新的可分配的空间

- minor gc之后，若eden空间足够，则新对象在eden分配空间；若eden空间仍然不够，则新对象直接在年老代分配空间

## 小结

从上面的分析可以看出，young generation貌似有点大，ygc时间长；另外每次ygc之后survivor空间基本是空的，说明新生对象产生快，生命周期也短，原本设计的survivor空间没有派上用场。因此可以考虑缩小下young generation的大小，或者改为G1试试。

关于-XX:+PrintTenuringDistribution有几个要点，要明确一下：

- 这个打印的哪个区域的对象分布(`survivor`)
- 是在gc之前打印，还是在gc之后打印(`gc之后打印`)
- 一个新生对象第一次到survivor时其age算0还是算1

> 对象的年龄就是他经历的MinorGC次数，对象首次分配时，年龄为0，第一次经历MinorGC之后，若还没有被回收，则年龄+1，由于是第一次经历MinorGC，因此进入survivor区。因此对象第一次进入survivor区域的时候年龄为1.

- 晋升阈值(new threshold)动态调整

> 如果底下age的total大小大于Desired survivor size的大小，那么就代表了survivor空间溢出了，被填满，然后会重新计算threshold。

## doc

- [jstat](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html)
- [Size of Huge Objects directly allocated to Old Generation](https://stackoverflow.com/questions/24618467/size-of-huge-objects-directly-allocated-to-old-generation)
- [Java对象分配简要流程](https://segmentfault.com/a/1190000004606059)
- [记一次JVM优化过程](http://sunxiang0918.cn/2014/06/27/记一次JVM优化过程/)
- [Survivor空间溢出实例](https://segmentfault.com/a/1190000004657756)
- [Java 垃圾回收的log，为什么 from和to大小不等？](https://www.zhihu.com/question/65601024/answer/236656917)
- [Useful JVM Flags – Part 5 (Young Generation Garbage Collection)](https://blog.codecentric.de/en/2012/08/useful-jvm-flags-part-5-young-generation-garbage-collection/)
- [JDK-6453675 : Request for documentation of -XX:+PrintTenuringDistribution output](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=6453675)
- [How to read the output of +PrintTenuringDistribution](https://marc.info/?l=openjdk-hotspot-gc-use&m=138267652801021&w=2)
- [一次GC Tuning小记](https://neway6655.github.io/java, gc tuning/2016/09/24/gc-tuning.html)
- [JDK8 的FullGC 之 metaspace](http://tech.dianwoda.com/2018/01/10/jdk8-de-full-gc-zhi-metaspace/)
- [Java PermGen 去哪里了?](http://ifeve.com/java-permgen-removed/)
- [Metaspace](http://blog.csdn.net/xlnjulp/article/details/46763045)
- [MetaspaceSize的坑](http://atbug.com/java8-metaspace-size-issue/)
- [JVM源码分析之Metaspace解密](http://lovestblog.cn/blog/2016/10/29/metaspace/)
- [About G1 Garbage Collector, Permanent Generation and Metaspace](https://blogs.oracle.com/poonam/about-g1-garbage-collector,-permanent-generation-and-metaspace)
- [聊聊jvm的PermGen与Metaspace](https://segmentfault.com/a/1190000012577387)
- [GC LOGGING – USER, SYS, REAL – WHICH TIME TO USE? & GANDHI](https://blog.gceasy.io/2016/04/06/gc-logging-user-sys-real-which-time-to-use/)
- [REAL TIME IS GREATER THAN USER AND SYS TIME](https://blog.gceasy.io/2016/12/08/real-time-greater-than-user-and-sys-time/)
- [GC日志时间分析: user + sys < real](http://tang.love/2017/10/22/gc_analysis_user_sys_real/)
- [What is promotion rate?](https://plumbr.io/blog/garbage-collection/what-is-promotion-rate)