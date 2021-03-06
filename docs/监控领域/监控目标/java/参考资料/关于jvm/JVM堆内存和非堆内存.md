# JVM堆内存和非堆内存

目录

- http://www.bingfengsa.com/info/8153.html

## 堆和非堆内存

按照官方的说法：“Java 虚拟机具有一个堆(Heap)，堆是运行时数据区域，所有类实例和数组的内存均从此处分配。堆是在 Java 虚拟机启动时创建的。”“在JVM中堆之外的内存称为非堆内存(Non-heap memory)”。

JVM主要管理两种类型的内存：堆和非堆。

| Heap memory           | Code Cache |
| --------------------- | ---------- |
| Eden Space            |            |
| Survivor Space        |            |
| Tenured Gen           |            |
| non-heap memory       | Perm Gen   |
| native heap?(I guess) |            |

- 堆内存

Java 虚拟机具有一个堆，堆是运行时数据区域，所有类实例和数组的内存均从此处分配。堆是在 Java 虚拟机启动时创建的。对象的堆内存由称为垃圾回收器的自动内存管理系统回收。

堆的大小可以固定，也可以扩大和缩小。堆的内存不需要是连续空间。

- 非堆内存

Java 虚拟机管理堆之外的内存（称为非堆内存）。

Java 虚拟机具有一个由所有线程共享的方法区。方法区属于非堆内存。它存储每个类结构，如运行时常数池、字段和方法数据，以及方法和构造方法的代码。它是在 Java 虚拟机启动时创建的。

方法区在逻辑上属于堆，但 Java 虚拟机实现可以选择不对其进行回收或压缩。与堆类似，方法区的大小可以固定，也可以扩大和缩小。方法区的内存不需要是连续空间。

除了方法区外，Java 虚拟机实现可能需要用于内部处理或优化的内存，这种内存也是非堆内存。例如，JIT 编译器需要内存来存储从 Java 虚拟机代码转换而来的本机代码，从而获得高性能。

- 几个基本概念

PermGen space：全称是Permanent Generation space，即永久代。就是说是永久保存的区域,用于存放Class和Meta信息，Class在被Load的时候被放入该区域，GC(Garbage Collection)应该不会对PermGen space进行清理，所以如果你的APP会LOAD很多CLASS的话，就很可能出现PermGen space错误。

Heap space：存放Instance。

Java Heap分为3个区，Young即新生代，Old即老生代和Permanent。

Young保存刚实例化的对象。当该区被填满时，GC会将对象移到Old区。Permanent区则负责保存反射对象。

- 堆内存分配
  - JVM初始分配的堆内存由-Xms指定，默认是物理内存的1/64；
  - JVM最大分配的堆内存由-Xmx指定，默认是物理内存的1/4。
  - 默认空余堆内存小于40%时，JVM就会增大堆直到-Xmx的最大限制；
  - 空余堆内存大于70%时，JVM会减少堆直到-Xms的最小限制。
  - 因此服务器一般设置-Xms、-Xmx 相等以避免在每次GC 后调整堆的大小。
  - 说明：如果-Xmx 不指定或者指定偏小，应用可能会导致java.lang.OutOfMemory错误，此错误来自JVM，不是Throwable的，无法用try...catch捕捉。

- 非堆内存分配
  - JVM使用-XX:PermSize设置非堆内存初始值，默认是物理内存的1/64；
  - 由XX:MaxPermSize设置最大非堆内存的大小，默认是物理内存的1/4。
    - 还有一说：MaxPermSize缺省值和-server -client选项相关，-server选项下默认MaxPermSize为64m，-client选项下默认MaxPermSize为32m。这个我没有实验。
  - XX:MaxPermSize设置过小会导致java.lang.OutOfMemoryError: PermGen space 就是内存益出。
  - 为什么会内存益出：
    1. 这一部分内存用于存放Class和Meta的信息，Class在被 Load的时候被放入PermGen space区域，它和存放Instance的Heap区域不同。
    2. GC(Garbage Collection)不会在主程序运行期对PermGen space进行清理，所以如果你的APP会LOAD很多CLASS 的话,就很可能出现PermGen space错误。
  - 这种错误常见在web服务器对JSP进行pre compile的时候。

## JVM内存限制(最大值)

- 首先JVM内存限制于实际的最大物理内存，假设物理内存无限大的话，JVM内存的最大值跟操作系统有很大的关系。简单的说就32位处理器虽然可控内存空间有4GB,但是具体的操作系统会给一个限制，这个限制一般是2GB-3GB（一般来说Windows系统下为1.5G-2G，Linux系统下为2G-3G），而64bit以上的处理器就不会有限制了。

- 为什么有的机器我将-Xmx和-XX:MaxPermSize都设置为512M之后Eclipse可以启动，而有些机器无法启动？
  - 通过上面对JVM内存管理的介绍我们已经了解到JVM内存包含两种：堆内存和非堆内存，另外JVM最大内存首先取决于实际的物理内存和操作系统。所以说设置VM参数导致程序无法启动主要有以下几种原因：
    1. 参数中-Xms的值大于-Xmx，或者-XX:PermSize的值大于-XX:MaxPermSize；
    2. -Xmx的值和-XX:MaxPermSize的总和超过了JVM内存的最大限制，比如当前操作系统最大内存限制，或者实际的物理内存等等。说到实际物理内存这里需要说明一点的是，如果你的内存是1024MB，但实际系统中用到的并不可能是1024MB，因为有一部分被硬件占用了。

- 如果你有一个双核的CPU，也许可以尝试这个参数: -XX:+UseParallelGC 让GC可以更快的执行。（只是JDK 5里对GC新增加的参数）

- 如果你的WEB APP下都用了大量的第三方jar，其大小超过了服务器jvm默认的大小，那么就会产生内存益出问题了。解决方法： 设置MaxPermSize大小。
  - 增加服务器启动的JVM参数设置： `-Xms128m -Xmx256m -XX:PermSize=128M -XX:MaxNewSize=256m -XX:MaxPermSize=256m`
  - 如tomcat，修改TOMCAT_HOME/bin/catalina.sh，在`echo "Using CATALINA_BASE: $CATALINA_BASE"`上面加入以下行：`JAVA_OPTS="-server -XX:PermSize=64M -XX:MaxPermSize=128m`

- 建议：将相同的第三方jar文件移置到tomcat/shared/lib目录下，这样可以减少jar 文档重复占用内存

## JVM内存设置参数

- 内存设置参数

| 设置项                                  | 说明                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| -Xms512m                                | 表示JVM初始分配的堆内存大小为512m（JVM Heap(堆内存)最小尺寸，初始分配） |
| -Xmx1024m                               | JVM最大允许分配的堆内存大小为1024m，按需分配（JVM Heap(堆内存)最大允许的尺寸，按需分配） |
| -XX:PermSize=512M                       | JVM初始分配的非堆内存                                        |
| -XX:MaxPermSize=1024M                   | JVM最大允许分配的非堆内存，按需分配                          |
| -XX:NewSize/-XX:MaxNewSize              | 定义YOUNG段的尺寸，NewSize为JVM启动时YOUNG的内存大小；       |
| MaxNewSize为最大可占用的YOUNG内存大小。 |                                                              |
| -XX:SurvivorRatio                       | 设置YOUNG代中Survivor空间和Eden空间的比例                    |

- 说明：
  1. 如果-Xmx不指定或者指定偏小，应用可能会导致java.lang.OutOfMemory错误，此错误来自JVM不是Throwable的，无法用try...catch捕捉。
  2. PermSize和MaxPermSize指明虚拟机为java永久生成对象（Permanate generation）如，class对象、方法对象这些可反射（reflective）对象分配内存限制，这些内存不包括在Heap（堆内存）区之中。
  3. -XX:MaxPermSize分配过小会导致：java.lang.OutOfMemoryError: PermGen space。
  4. MaxPermSize缺省值和-server -client选项相关：-server选项下默认MaxPermSize为64m、-client选项下默认MaxPermSize为32m。

- 申请一块内存的过程
  1. JVM会试图为相关Java对象在Eden中初始化一块内存区域
  2. 当Eden空间足够时，内存申请结束。否则到下一步
  3. JVM试图释放在Eden中所有不活跃的对象（这属于1或更高级的垃圾回收）；释放后若Eden空间仍然不足以放入新对象，则试图将部分Eden中活跃对象放入Survivor区/OLD区
  4. Survivor区被用来作为Eden及OLD的中间交换区域，当OLD区空间足够时，Survivor区的对象会被移到Old区，否则会被保留在Survivor区
  5. 当OLD区空间不够时，JVM会在OLD区进行完全的垃圾收集（0级）
  6. 完全垃圾收集后，若Survivor及OLD区仍然无法存放从Eden复制过来的部分对象，导致JVM无法在Eden区为新对象创建内存区域，则出现”out of memory错误”

- resin服务器典型的响应时间优先型的jvm配置：

  ```
  -Xmx2000M -Xms2000M -Xmn500M
  -XX:PermSize=250M -XX:MaxPermSize=250M
  -Xss256K
  -XX:+DisableExplicitGC
  -XX:SurvivorRatio=1
  -XX:+UseConcMarkSweepGC
  -XX:+UseParNewGC
  -XX:+CMSParallelRemarkEnabled
  -XX:+UseCMSCompactAtFullCollection
  -XX:CMSFullGCsBeforeCompaction=0
  -XX:+CMSClassUnloadingEnabled
  -XX:LargePageSizeInBytes=128M
  -XX:+UseFastAccessorMethods
  -XX:+UseCMSInitiatingOccupancyOnly
  -XX:CMSInitiatingOccupancyFraction=60
  -XX:SoftRefLRUPolicyMSPerMB=0
  -XX:+PrintClassHistogram
  -XX:+PrintGCDetails
  -XX:+PrintGCTimeStamps
  -XX:+PrintHeapAtGC
  -Xloggc:log/gc.log
  ```

## 内存回收算法

Java中有四种不同的回收算法，对应的启动参数为:

```
–XX:+UseSerialGC
–XX:+UseParallelGC
–XX:+UseParallelOldGC
–XX:+UseConcMarkSweepGC
```

### Serial Collector

大部分平台或者强制 java -client 默认会使用这种。

young generation算法 = serial

old generation算法 = serial (mark-sweep-compact)

这种方法的缺点很明显, stop-the-world, 速度慢。服务器应用不推荐使用。

### Parallel Collector

在linux x64上默认是这种，其他平台要加 java -server 参数才会默认选用这种。

young = parallel，多个thread同时copy

old = mark-sweep-compact = 1

优点：新生代回收更快。因为系统大部分时间做的gc都是新生代的，这样提高了throughput(cpu用于非gc时间)

缺点：当运行在8G/16G server上old generation live object太多时候pause time过长

### Parallel Compact Collector (ParallelOld)

young = parallel = 2

old = parallel，分成多个独立的单元，如果单元中live object少则回收，多则跳过

优点：old old generation上性能较 parallel 方式有提高

缺点：大部分server系统old generation内存占用会达到60%-80%, 没有那么多理想的单元live object很少方便迅速回收，同时compact方面开销比起parallel并没明显减少。

### Concurrent Mark-Sweep(CMS) Collector

young generation = parallel collector = 2

old = cms

同时不做 compact 操作。

优点：pause time会降低, pause敏感但CPU有空闲的场景需要建议使用策略4.

缺点：cpu占用过多，cpu密集型服务器不适合。另外碎片太多，每个object的存储都要通过链表连续跳n个地方，空间浪费问题也会增大。

## 内存监控方法

- jmap -heap 查看java 堆（heap）使用情况

  ```
  jmap -heap pid 
   
  using thread-local object allocation.
   
  Parallel GC with 4 thread(s)   #GC 方式
   
  Heap Configuration:  #堆内存初始化配置
   
  MinHeapFreeRatio=40  #对应jvm启动参数-XX:MinHeapFreeRatio设置JVM堆最小空闲比率(default 40)
  MaxHeapFreeRatio=70  #对应jvm启动参数 -XX:MaxHeapFreeRatio设置JVM堆最大空闲比率(default 70)
  MaxHeapSize=512.0MB  #对应jvm启动参数-XX:MaxHeapSize=设置JVM堆的最大大小
  NewSize  = 1.0MB     #对应jvm启动参数-XX:NewSize=设置JVM堆的‘新生代’的默认大小
  MaxNewSize =4095MB   #对应jvm启动参数-XX:MaxNewSize=设置JVM堆的‘新生代’的最大大小
  OldSize  = 4.0MB     #对应jvm启动参数-XX:OldSize=<value>:设置JVM堆的‘老生代’的大小
  NewRatio  = 8        #对应jvm启动参数-XX:NewRatio=:‘新生代’和‘老生代’的大小比率
  SurvivorRatio = 8    #对应jvm启动参数-XX:SurvivorRatio=设置年轻代中Eden区与Survivor区的大小比值
  PermSize= 16.0MB     #对应jvm启动参数-XX:PermSize=<value>:设置JVM堆的‘永生代’的初始大小
  MaxPermSize=64.0MB   #对应jvm启动参数-XX:MaxPermSize=<value>:设置JVM堆的‘永生代’的最大大小
   
  Heap Usage:          #堆内存分步
   
  PS Young Generation
   
  Eden Space:         #Eden区内存分布
   
  capacity = 20381696 (19.4375MB)             #Eden区总容量
  used     = 20370032 (19.426376342773438MB)  #Eden区已使用
  free     = 11664 (0.0111236572265625MB)     #Eden区剩余容量
  99.94277218147106% used                     #Eden区使用比率
   
  From Space:        #其中一个Survivor区的内存分布
   
  capacity = 8519680 (8.125MB)
  used     = 32768 (0.03125MB)
  free     = 8486912 (8.09375MB)
  0.38461538461538464% used
   
  To Space:          #另一个Survivor区的内存分布
   
  capacity = 9306112 (8.875MB)
  used     = 0 (0.0MB)
  free     = 9306112 (8.875MB)
  0.0% used
   
  PS Old Generation  #当前的Old区内存分布
   
  capacity = 366280704 (349.3125MB)
  used     = 322179848 (307.25464630126953MB)
  free     = 44100856 (42.05785369873047MB)
  87.95982001825573% used
   
  PS Perm Generation #当前的 “永生代” 内存分布
   
  capacity = 32243712 (30.75MB)
  used     = 28918584 (27.57891082763672MB)
  free     = 3325128 (3.1710891723632812MB)
  89.68751488662348% used
  ```

  

- JVM内存监控工具

  `<%@ page import="java.lang.management.*" %>``<%@ page import="java.util.*" %>``<``html``>``<``head``>`` ``<``title``>JVM Memory Monitor</``title``>``</``head``>``<``body``>``<``table` `border``=``"0"` `width``=``"100%"``>``  ``<``tr``><``td` `colspan``=``"2"` `align``=``"center"``><``h3``>Memory MXBean</``h3``></``td``></``tr``>``  ``<``tr``><``td` `width``=``"200"``>Heap Memory Usage</``td``><``td``><%=ManagementFactory.getMemoryMXBean().getHeapMemoryUsage()%></``td``></``tr``>``  ``<``tr``><``td``>Non-Heap Memory Usage</``td``><``td``><%=ManagementFactory.getMemoryMXBean().getNonHeapMemoryUsage()%></``td``></``tr``>``  ``<``tr``><``td` `colspan``=``"2"``> </``td``></``tr``>``  ``<``tr``><``td` `colspan``=``"2"` `align``=``"center"``><``h3``>Memory Pool MXBeans</``h3``></``td``></``tr``>``<%``    ``Iterator iter = ManagementFactory.getMemoryPoolMXBeans().iterator();``    ``while (iter.hasNext()) {``      ``MemoryPoolMXBean item = (MemoryPoolMXBean) iter.next();``%>``<``tr``><``td` `colspan``=``"2"``>``  ``<``table` `border``=``"0"` `width``=``"100%"` `style``=``"border: 1px #98AAB1 solid;"``>``    ``<``tr``><``td` `colspan``=``"2"` `align``=``"center"``><``b``><%= item.getName() %></``b``></``td``></``tr``>``    ``<``tr``><``td` `width``=``"200"``>Type</``td``><``td``><%= item.getType() %></``td``></``tr``>``    ``<``tr``><``td``>Usage</``td``><``td``><%= item.getUsage() %></``td``></``tr``>``    ``<``tr``><``td``>Peak Usage</``td``><``td``><%= item.getPeakUsage() %></``td``></``tr``>``    ``<``tr``><``td``>Collection Usage</``td``><``td``><%= item.getCollectionUsage() %></``td``></``tr``>``  ``</``table``>``</``td``></``tr``>``<``tr``><``td` `colspan``=``"2"``> </``td``></``tr``>``<%} %>``</``table``>``</``body``>``</``html``>`

© 2012 - 2015 XStar  | [Powerby:Vimwiki](http://code.google.com/p/vimwiki/) | [Style:丘迟](http://kwiki.github.io/) | [首页](https://xstarcd.github.io/wiki/index.html) | [分类首页](https://xstarcd.github.io/wiki/Java/index.html) | [站点地图](https://xstarcd.github.io/wiki/SiteMap.html)