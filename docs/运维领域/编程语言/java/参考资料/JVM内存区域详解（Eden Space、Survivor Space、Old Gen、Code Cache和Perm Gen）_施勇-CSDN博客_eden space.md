# JVM内存区域详解（Eden Space、Survivor Space、Old Gen、Code Cache和Perm Gen）

![img](JVM内存区域详解（Eden Space、Survivor Space、Old Gen、Code Cache和Perm Gen）_施勇-CSDN博客_eden space.assets/original.png)

[shiyonghm](https://shiyong.blog.csdn.net/) 2016-09-19 14:05:15 ![img](JVM内存区域详解（Eden Space、Survivor Space、Old Gen、Code Cache和Perm Gen）_施勇-CSDN博客_eden space.assets/articleReadEyes.png) 66513 ![img](JVM内存区域详解（Eden Space、Survivor Space、Old Gen、Code Cache和Perm Gen）_施勇-CSDN博客_eden space.assets/tobarCollect.png) 收藏 43

分类专栏： [JAVA虚拟机](https://blog.csdn.net/shiyong1949/category_9518864.html) 文章标签： [jvm](https://www.csdn.net/tags/MtTaEg0sMjUyNTEtYmxvZwO0O0OO0O0O.html) [java](https://www.csdn.net/tags/NtTaIg5sMzYyLWJsb2cO0O0O.html) [虚拟机](https://www.csdn.net/tags/MtTaEg0sMDc3NzQtYmxvZwO0O0OO0O0O.html)

版权

JVM区域总体分两类，heap区和非heap区。
heap区又分为：

- Eden Space（伊甸园）、
- Survivor Space(幸存者区)、
- Old Gen（老年代）。

非heap区又分：

- Code Cache(代码缓存区)；
- Perm Gen（永久代）；
- Jvm Stack(java虚拟机栈)；
- Local Method Statck(本地方法栈)；

下面我们对每一个内存区域做详细介绍。
**Eden Space**字面意思是伊甸园，对象被创建的时候首先放到这个区域，进行垃圾回收后，不能被回收的对象被放入到空的survivor区域。

**Survivor Space**幸存者区，用于保存在eden space内存区域中经过垃圾回收后没有被回收的对象。Survivor有两个，分别为To Survivor、 From Survivor，这个两个区域的空间大小是一样的。执行垃圾回收的时候Eden区域不能被回收的对象被放入到空的survivor（也就是To Survivor，同时Eden区域的内存会在垃圾回收的过程中全部释放），另一个survivor（即From Survivor）里不能被回收的对象也会被放入这个survivor（即To Survivor），然后To Survivor 和 From Survivor的标记会互换，始终保证一个survivor是空的。

![这里写图片描述](JVM内存区域详解（Eden Space、Survivor Space、Old Gen、Code Cache和Perm Gen）_施勇-CSDN博客_eden space.assets/20160920101202448)
Eden Space和Survivor Space都属于新生代，新生代中执行的垃圾回收被称之为Minor GC（因为是对新生代进行垃圾回收，所以又被称为Young GC），每一次Young GC后留下来的对象age加1。

注：GC为Garbage Collection，垃圾回收。

**Old Gen**老年代，用于存放新生代中经过多次垃圾回收仍然存活的对象，也有可能是新生代分配不了内存的大对象会直接进入老年代。经过多次垃圾回收都没有被回收的对象，这些对象的年代已经足够old了，就会放入到老年代。

当老年代被放满的之后，虚拟机会进行垃圾回收，称之为Major GC。由于Major GC除并发GC外均需对整个堆进行扫描和回收，因此又称为Full GC。

heap区即堆内存，整个堆大小=年轻代大小 + 老年代大小。堆内存默认为物理内存的1/64(<1GB)；默认空余堆内存小于40%时，JVM就会增大堆直到-Xmx的最大限制，可以通过MinHeapFreeRatio参数进行调整；默认空余堆内存大于70%时，JVM会减少堆直到-Xms的最小限制，可以通过MaxHeapFreeRatio参数进行调整。

下面我们来认识下非堆内存（非heap区）
**Code Cache**代码缓存区，它主要用于存放JIT所编译的代码。CodeCache代码缓冲区的大小在client模式下默认最大是32m，在server模式下默认是48m，这个值也是可以设置的，它所对应的JVM参数为ReservedCodeCacheSize 和 InitialCodeCacheSize，可以通过如下的方式来为Java程序设置。

```
-XX:ReservedCodeCacheSize=128m
1
```

CodeCache缓存区是可能被充满的，当CodeCache满时，后台会收到CodeCache is full的警告信息，如下所示：
“CompilerThread0” java.lang.OutOfMemoryError: requested 2854248 bytes for Chunk::new. Out of swap space?

注：JIT编译器是在程序运行期间，将Java字节码编译成平台相关的二进制代码。正因为此编译行为发生在程序运行期间，所以该编译器被称为Just-In-Time编译器。

**Perm Gen**全称是Permanent Generation space，是指内存的永久保存区域，因而称之为永久代。这个内存区域用于存放Class和Meta的信息，Class在被 Load的时候被放入这个区域。因为Perm里存储的东西永远不会被JVM垃圾回收的，所以如果你的应用程序LOAD很多CLASS的话，就很可能出现PermGen space错误。默认大小为物理内存的1/64。