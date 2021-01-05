# [JVM G1（Garbage-First Garbage Collector）收集器全过程剖析](https://segmentfault.com/a/1190000022537037)

[![img](JVM G1（Garbage-First Garbage Collector）收集器全过程剖析_个人文章 - SegmentFault 思否.assets/868271510-54cb382abb7a1_small) java](https://segmentfault.com/t/java)[jvm](https://segmentfault.com/t/jvm)

发布于 2020-05-03

![img](JVM G1（Garbage-First Garbage Collector）收集器全过程剖析_个人文章 - SegmentFault 思否.assets/lg.php)

![img](JVM G1（Garbage-First Garbage Collector）收集器全过程剖析_个人文章 - SegmentFault 思否.assets/bVbGI4I)

`G1`垃圾收集器的设计原则是“首先收集尽可能多的垃圾(Garbage First)”，目标是为了尽量缩短处理超大堆（超过4GB）产生的停顿。

因此，`G1`并不会等内存耗尽（比如`Serial` 串行收集器、`Parallel`并行收集器 ）者快耗尽(`CMS`)的时候才开始垃圾回收，而是在内部采用了启发式算法，在老年代中找出具有高收集收益的分区（`Region`）进行收集。

同时 `G1` 可以根据用户设置的`STW`（Stop-The-World）停顿时间目标（响应时间优先）自动调整年轻代和总堆的大小，停顿时间越短年轻代空间就可能越小，总堆空间越大。

`G1`相对于`CMS`一个比较明显的优势是，内存碎片的产生率大大降低。

`G1`在 JDK7u4以上都可以使用，在JDK9开始，`G1`为默认的垃圾收集器，以替代`CMS`。

## G1算法

**算法：三色标记 + SATB**

## G1的特性

- 面向服务端应用的垃圾收集器
- 并行与并发：G1能充分利用多CPU、**多核**环境使用多个CPU或CPU核心来缩短`STW`（Stop-The-World）停顿时间。
- 分代收集：G1物理上不分代，但逻辑上仍然有分代的概念。
- 空间整合：不会产生内存空间碎片，收集后可提供规整的可用内存，整理空闲空间更快。
- 可预测的停顿(它可以有计划的避免在整个JAVA堆中进行全区域的垃圾收集)
- 适用于不需要实现很高吞吐量的场景
- JAVA堆内存布局与其它收集器存在很大差别，它将整个JAVA堆划分为多个大小相等的独立区域或分区(`Region`)。
- G1收集器中，虚拟机使用`Remembered Set`来避免全堆扫描。

## G1的内存模型

![img](JVM G1（Garbage-First Garbage Collector）收集器全过程剖析_个人文章 - SegmentFault 思否.assets/bVbGI4J)

### 分区概念

传统的GC收集器将连续的内存空间划分为新生代、老年代和永久代（JDK 8去除了永久代，引入了元空间Metaspace），

这种划分的特点是各代的存储地址（逻辑地址，下同）是连续的。如下图所示：

而G1的各代存储地址是不连续的，每一代都使用了n个不连续的大小相同的`Region`，每个`Region`占有一块连续的虚拟内存地址。

##### `Region` （区域，分区）

G1采用了分区(`Region`)的思路，将整个堆空间分成若干个大小相等的内存区域，每次分配对象空间将逐段地使用内存。

虽然还保留了新生代和老年代的概念，但新生代和老年代不再是物理隔离，它们都是一部分`Region`(不需要连续)的集合。

因此，在堆的使用上，G1并不要求对象的存储一定是物理上连续的，只要逻辑上连续即可；

**每个分区`Region`也不会确定地为某个代服务，可以按需在年轻代和老年代之间切换。**

启动时可以通过参数`-XX:G1HeapRegionSize=n`可指定分区大小(1MB~32MB，且必须是2的幂)，默认将整堆划分为2048个分区。

##### `Card` （卡片）

在每个分区`Region` 内部又被分成了若干个大小为512 Byte卡片(Card)，标识堆内存最小可用粒度。

所有分区`Region` 的卡片将会记录在全局卡片表(`Global Card Table`)中。

分配的对象会占用物理上连续的若干个卡片。

当查找对分区`Region` 内对象的引用时便可通过记录卡片来查找该引用对象(见`RSet`)。

每次对内存的回收，都是对指定分区的卡片进行处理。

##### `Heap` （堆）

G1同样可以通过`-Xms/-Xmx`来指定堆空间大小。

当发生年轻代收集（`YGC`）或混合收集（`Mixed GC`）时，通过计算GC与应用的耗费时间比，自动调整堆空间大小。

如果GC频率太高，则通过增加堆尺寸，来减少GC频率，相应地GC占用的时间也随之降低；

目标参数`-XX:GCTimeRatio`即为GC与应用的耗费时间比，G1默认为12（JDK7,8为99，JDK11+开始为12），而CMS默认为99，因为CMS的设计原则是耗费在GC上的时间尽可能的少。

另外，当空间不足，如对象空间分配或转移失败时，G1会首先尝试增加堆空间，如果扩容失败，则发起担保的`Full GC`。

`Full GC`后，堆尺寸计算结果也会调整堆空间。

### 分代概念

##### `Generation` （分代 ）

分代垃圾收集可以将关注点集中在最近被分配的对象上，而无需整堆扫描，避免长命对象的拷贝，同时独立收集有助于降低响应时间。

虽然分区使得内存分配不再要求紧凑的内存空间，但G1依然使用了分代的思想。

与其他垃圾收集器类似，G1将内存在逻辑上划分为年轻代和老年代，其中年轻代又划分为Eden空间和Survivor空间。

但年轻代空间并不是固定不变的，当现有年轻代分区占满时，JVM会分配新的空闲分区加入到年轻代空间。

整个年轻代内存会在初始空间`-XX:NewSize`与最大空间`-XX:MaxNewSize`之间动态变化，且由参数目标暂停时间`-XX:MaxGCPauseMillis`、需要扩缩容的大小以及分区的已记忆集合(`RSet`)计算得到。

> 当然，G1依然可以设置固定的年轻代大小(参数`-XX:NewRatio`、`-Xmn`)，但同时暂停目标将失去意义。

##### `Local allocation buffer` (`LAB`) （本地分配缓冲）

值得注意的是，由于分区的思想，每个线程均可以"认领"某个分区`Region`用于线程本地的内存分配，而不需要顾及分区是否连续。

因此，每个应用线程和GC线程都会独立的使用分区，进而减少同步时间，提升GC效率，这个分区`Region`称为本地分配缓冲区(`LAB`)。

- 应用线程本地缓冲区`TLAB`：

应用线程可以独占一个本地缓冲区(`TLAB`)来创建的对象，而大部分都会落入Eden区域(巨型对象或分配失败除外)，因此TLAB的分区属于Eden空间；

- GC线程本地缓冲区`GCLAB`：

每次垃圾收集时，每个GC线程同样可以独占一个本地缓冲区(`GCLAB`)用来转移对象，每次回收会将对象复制到Suvivor空间或老年代空间；

- 晋升本地缓冲区`PLAB`：

对于从Eden/Survivor空间晋升(Promotion)到Survivor/老年代空间的对象，同样有GC独占的本地缓冲区进行操作，该部分称为晋升本地缓冲区(`PLAB`)。

### 分区模型

##### `Humongous Object` （巨型对象）

一个大小达到甚至超过分区`Region` 50%以上的对象称为巨型对象(`Humongous Object`)。
巨型对象会独占一个、或多个连续分区，其中第一个分区被标记为开始巨型(`StartsHumongous`)，相邻连续分区被标记为连续巨型(`ContinuesHumongous`)。
`Humongous Object` 有以下特点：

- `Humongous Object`直接分配到了 老年代，防止了反复拷贝移动。

> 当线程为巨型分配空间时，不能简单在`TLAB`进行分配，因为巨型对象的移动成本很高，而且有可能一个分区不能容纳巨型对象。
> 因此，巨型对象会直接在老年代分配，所占用的连续空间称为巨型分区(`Humongous Region`)。

- `Humongous Object` 在 `YGC`阶段， `Global Concurrent Marking` 阶段的 `Cleanup` 和 `FGC` 阶段 回收。

> 由于无法享受`LAB`带来的优化，并且确定一片连续的内存空间需要扫描整堆`Heap`，因此确定巨型对象开始位置的成本非常高，如果可以，应用程序应避免生成巨型对象。

- 在分配`Humongous Object` 之前先检查是否超过 initiating heap occupancy percent （由参数`-XX:InitiatingHeapOccupancyPercent`控制） 和 the marking threshold。

如果超过的话，就启动并发收集周期`Concurrent Marking Cycle` ，为的是提早回收，防止 `Evacuation Failure` 和 `Full GC`。

##### `RSet` （`Remember Set`，已记忆集合)

在串行和并行收集器中，GC通过整堆扫描，来确定对象是否处于可达路径中。

然而G1为了避免`STW`式的整堆`Heap`扫描，在每个分区`Region`记录了一个已记忆集合(`RSet`)，内部类似一个反向指针，记录引用分区`Region`内对象的卡片`Card`的索引。

当要回收该分区`Region`时，通过扫描分区的RSet，来确定引用本分区内的对象是否存活，进而确定本分区内的对象存活情况。

事实上，并非所有的引用都需要记录在`RSet`中，如果一个分区`Region`确定需要扫描，那么无需`RSet`也可以无遗漏的得到引用关系。

那么引用源自本分区`Region`的对象，当然不用落入`RSet`中；

同时，G1 GC每次都会对年轻代进行整体收集，因此引用源自年轻代的对象，也不需要在`RSet`记录。

最后只有老年代的分区`Region`可能会有RSet记录，这些分区称为拥有RSet分区(an RSet’s owning region)。

##### `Per Region Table` (PRT)

`RSet`在内部使用`Per Region Table`(PRT)记录分区`Region`的引用情况。
由于`RSet`的记录要占用分区`Region`的空间，如果一个分区非常"受欢迎"，那么`RSet`占用的空间会上升，从而降低分区`Region`的可用空间。
G1应对这个问题采用了改变`RSet`的密度的方式，在`PRT`中将会以三种模式记录引用：

- 稀少：直接记录引用对象的卡片`Card`的索引
- 细粒度：记录引用对象的分区`Region`的索引
- 粗粒度：只记录引用情况，每个分区对应一个比特位

由上可知，粗粒度的`PRT`只是记录了引用数量，需要通过整堆`Heap`扫描才能找出所有引用，因此扫描速度也是最慢的。

##### `CSet`（`Collection Set`，收集集合）

收集集合(`CSet`)代表每次GC暂停时回收的一系列目标分区`Region`。

在任意一次收集暂停中，`CSet`所有分区都会被释放，内部存活的对象都会被转移到分配的空闲分区中。

因此无论是年轻代收集，还是混合收集，工作的机制都是一致的。

年轻代收集（`YGC`）的`CSet`只容纳年轻代分区，而混合收集（`Mixed GC`）会通过启发式算法，在老年代候选回收分区中，筛选出回收收益最高的分区添加到`CSet`中。

- 候选老年代分区的`CSet`准入条件，可以通过活跃度阈值`-XX:G1MixedGCLiveThresholdPercent`(默认85%)进行设置，从而拦截那些回收开销巨大的对象；
- 同时，每次混合收集可以包含候选老年代分区，可根据`CSet`对堆的总大小占比`-XX:G1OldCSetRegionThresholdPercent`(默认10%)设置数量上限。

由上述可知，G1的收集都是根据`CSet`进行操作的，年轻代收集（`YGC`）与混合收集（`Mixed GC`）没有明显的不同，最大的区别在于两种收集的触发条件。

##### 年轻代收集集合 `CSet of Young Collection`

应用线程不断活动后，年轻代空间会被逐渐填满。当JVM分配对象到Eden区域失败(Eden区已满)时，便会触发一次`STW`式的年轻代收集。
在年轻代收集中，Eden分区存活的对象将被拷贝到Survivor分区；
原有Survivor分区存活的对象，将根据任期阈值(tenuring threshold)分别晋升到`PLAB`中，新的survivor分区和老年代分区。而原有的年轻代分区将被整体回收掉。

同时，年轻代收集还负责维护对象的年龄(存活次数)，辅助判断老化(tenuring)对象晋升的时候是到Survivor分区还是到老年代分区。
年轻代收集首先先将晋升对象尺寸总和、对象年龄信息维护到年龄表中，再根据年龄表、Survivor尺寸、Survivor填充容量`-XX:TargetSurvivorRatio`(默认50%)、最大任期阈值`-XX:MaxTenuringThreshold`(默认15)，计算出一个恰当的任期阈值，凡是超过任期阈值的对象都会被晋升到老年代。

##### 混合收集集合 `CSet of Mixed Collection`

年轻代收集不断活动后，老年代的空间也会被逐渐填充。当老年代占用空间超过整堆比IHOP阈值`-XX:InitiatingHeapOccupancyPercent`(默认45%)时，G1就会启动一次混合垃圾收集周期。

为了满足暂停目标，G1可能不能一口气将所有的候选分区收集掉，因此G1可能会产生连续多次的混合收集与应用线程交替执行，每次`STW`的混合收集与年轻代收集过程相类似。

- 为了确定包含到年轻代收集集合CSet的老年代分区，JVM通过参数混合周期的最大总次数`-XX:G1MixedGCCountTarget`(默认8)、堆废物百分比`-XX:G1HeapWastePercent`(默认5%)。

通过候选老年代分区总数与混合周期最大总次数，确定每次包含到`CSet`的最小分区数量；

根据堆废物百分比，当收集达到参数时，不再启动新的混合收集。而每次添加到`CSet`的分区，则通过计算得到的GC效率进行安排。

## G1的活动周期

![img](JVM G1（Garbage-First Garbage Collector）收集器全过程剖析_个人文章 - SegmentFault 思否.assets/1460000022537041)

G1的垃圾回收包括了以下几种：

- Concurrent Marking Cycle （并发收集）

类似 `CMS`的并发收集过程。

- Young Collection （YGC，年轻代收集，`STW`）
- Mixed Collection Cycle （混合收集，`STW`）
- Full GC（FGC， `STW`）

**JDK10以前FGC是串行回收，JDK10+可以是并行回收。**

### 并发标记周期 `Concurrent Marking Cycle`

并发标记周期是G1中非常重要的阶段，这个阶段将会为混合收集周期识别垃圾最多的老年代分区。

整个周期完成根标记、识别所有(可能)存活对象，并计算每个分区的活跃度，从而确定GC效率等级。

当达到IHOP阈值`-XX:InitiatingHeapOccupancyPercent`(老年代占整堆比，默认45%)时，便会触发并发标记周期。

整个并发标记周期将由初始标记(Initial Mark)、根分区扫描(Root Region Scanning)、并发标记(Concurrent Marking)、重新标记(Remark)、清除(Cleanup)几个阶段组成。

其中，初始标记(随年轻代收集一起活动)、重新标记、清除是STW的，**而并发标记如果来不及标记存活对象，则可能在并发标记过程中，G1又触发了几次年轻代收集（`YGC`）。**

##### `Initial Marking` （初始标记， STW）

它标记了从GC Root开始直接可达的对象。

> 事实上，当达到IHOP阈值时，G1并不会立即发起并发标记周期，而是等待下一次年轻代收集，利用年轻代收集的STW时间段，完成初始标记，这种方式称为借道(Piggybacking)。

##### `Root region scanning` （根分区扫描）

在初始标记暂停结束后，年轻代收集也完成的对象复制到Survivor的工作，应用线程开始活跃起来。此时为了保证标记算法的正确性，所有新复制到Survivor分区的对象，都需要被扫描并标记成根，这个过程称为根分区扫描(Root Region Scanning)，同时扫描的Suvivor分区也被称为根分区(Root Region)。

##### `Concurrent Marking`（并发标记）

这个阶段从GC Root开始对heap中的对象标记，标记线程与应用程序线程并行执行，并且收集各个`Region`的存活对象信息。
和应用线程并发执行，并发标记线程在并发标记阶段启动，由参数`-XX:ConcGCThreads`(默认GC线程数的1/4，即-XX:ParallelGCThreads/4)控制启动数量，
每个线程每次只扫描一个分区`Region`，从而标记出存活对象图。

> 所有的标记任务必须在堆满前就完成扫描，如果并发标记耗时很长，那么有可能在并发标记过程中，又经历了几次年轻代收集。
> 如果堆满前没有完成标记任务，则会触发担保机制，经历一次长时间的串行Full GC。

##### `Remark` （ 重新标记，STW）

标记那些在并发标记阶段发生变化的对象，将被回收。
这个阶段也是并行执行的，通过参数`-XX:ParallelGCThread`可设置GC暂停时可用的GC线程数。

##### `Cleanup` （清理，STW）

清除阶段主要执行以下操作：

- `RSet`梳理，启发式算法会根据活跃度和`RSet`尺寸对分区定义不同等级，同时`RSet`数理也有助于发现无用的引用。参数`-XX:+PrintAdaptiveSizePolicy`可以开启打印启发式算法决策细节；
- 整理堆分区，为混合收集周期识别回收收益高(基于释放空间和暂停目标)的老年代分区集合；
- 识别所有空闲分区，即发现无存活对象的分区。该分区可在清除阶段直接回收，无需等待下次收集周期。

### 年轻代收集 Young Collection /混合收集周期 Mixed Collection Cycle

当应用运行开始时，堆内存可用空间还比较大，只会在年轻代满时，触发年轻代收集；

随着老年代内存增长，当到达IHOP阈值`-XX:InitiatingHeapOccupancyPercent`(老年代占整堆比，默认45%)时，G1开始着手准备收集老年代空间。

首先经历并发标记周期 `Concurrent Marking Cycle`，识别出高收益的老年代分区，前文已述。

但随后G1并不会马上开始一次混合收集，而是让应用线程先运行一段时间，等待触发一次年轻代收集。

在这次STW中，G1将保准整理混合收集周期。接着再次让应用线程运行，当接下来的几次年轻代收集时，将会有老年代分区加入到CSet中，

即触发混合收集，这些连续多次的混合收集称为混合收集周期(`Mixed Collection Cycle`)。

##### 年轻代收集 Young Collection,`YGC`

每次收集过程中，既有并行执行的活动，也有串行执行的活动，但都可以是多线程的。

在并行执行的任务中，如果某个任务过重，会导致其他线程在等待某项任务的处理，需要对这些地方进行优化。

> **以下部分部分可以结合日志查看**

- 并行活动
  - 外部根分区扫描 Ext Root Scanning：

此活动对堆外的根(JVM系统目录、VM数据结构、JNI线程句柄、硬件寄存器、全局变量、线程对栈根)进行扫描，发现那些没有加入到暂停收集集合CSet中的对象。如果系统目录(单根)拥有大量加载的类，最终可能其他并行活动结束后，该活动依然没有结束而带来的等待时间。

- 更新已记忆集合 Update RS：

并发优化线程会对脏卡片的分区进行扫描更新日志缓冲区来更新RSet，但只会处理全局缓冲列表。作为补充，所有被记录但是还没有被优化线程处理的剩余缓冲区，会在该阶段处理，变成已处理缓冲区(Processed Buffers)。为了限制花在更新RSet的时间，可以设置暂停占用百分比`-XX:G1RSetUpdatingPauseTimePercent`(默认10%，即-XX:MaxGCPauseMills/10)。值得注意的是，如果更新日志缓冲区更新的任务不降低，单纯地减少RSet的更新时间，会导致暂停中被处理的缓冲区减少，将日志缓冲区更新工作推到并发优化线程上，从而增加对Java应用线程资源的争夺。

- RSet扫描 Scan RS：

在收集当前CSet之前，考虑到分区外的引用，必须扫描CSet分区的RSet。如果RSet发生粗化，则会增加RSet的扫描时间。
开启诊断模式`-XX:UnlockDiagnosticVMOptions`后，
通过参数`-XX:+G1SummarizeRSetStats`可以确定并发优化线程是否能够及时处理更新日志缓冲区，并提供更多的信息，来帮助为RSet粗化总数提供窗口。
参数`-XX：G1SummarizeRSetStatsPeriod=n`可设置RSet的统计周期，即经历多少此GC后进行一次统计

- 代码根扫描 Code Root Scanning：对代码根集合进行扫描，扫描JVM编译后代码Native Method的引用信息(nmethod扫描)，进行RSet扫描。事实上，只有CSet分区中的RSet有强代码根时，才会做nmethod扫描，查找对CSet的引用。
- 转移和回收 Object Copy：

通过选定的CSet以及CSet分区完整的引用集，将执行暂停时间的主要部分：CSet分区存活对象的转移、CSet分区空间的回收。通过工作窃取机制来负载均衡地选定复制对象的线程，并且复制和扫描对象被转移的存活对象将拷贝到每个GC线程分配缓冲区GCLAB。G1会通过计算，预测分区复制所花费的时间，从而调整年轻代的尺寸。

- 终止 Termination：

完成上述任务后，如果任务队列已空，则工作线程会发起终止要求。如果还有其他线程继续工作，空闲的线程会通过工作窃取机制尝试帮助其他线程处理。而单独执行根分区扫描的线程，如果任务过重，最终会晚于终止。

- GC外部的并行活动 GC Worker Other：

该部分并非GC的活动，而是JVM的活动导致占用了GC暂停时间(例如JNI编译)。

- 串行活动
  - 代码根更新 Code Root Fixup：根据转移对象更新代码根。
  - 代码根清理 Code Root Purge：清理代码根集合表。
  - 清除全局卡片标记 Clear CT：在任意收集周期会扫描CSet与RSet记录的PRT，扫描时会在全局卡片表中进行标记，防止重复扫描。在收集周期的最后将会清除全局卡片表中的已扫描标志。
  - 选择下次收集集合 Choose CSet：该部分主要用于并发标记周期后的年轻代收集、以及混合收集中，在这些收集过程中，由于有老年代候选分区的加入，往往需要对下次收集的范围做出界定；但单纯的年轻代收集中，所有收集的分区都会被收集，不存在选择。
  - 引用处理 Ref Proc：主要针对软引用、弱引用、虚引用、final引用、JNI引用。当Ref Proc占用时间过多时，可选择使用参数`-XX:ParallelRefProcEnabled`激活多线程引用处理。G1希望应用能小心使用软引用，因为软引用会一直占据内存空间直到空间耗尽时被Full GC回收掉；即使未发生Full GC，软引用对内存的占用，也会导致GC次数的增加。
  - 引用排队 Ref Enq：此项活动可能会导致RSet的更新，此时会通过记录日志，将关联的卡片标记为脏卡片。
  - 卡片重新脏化 Redirty Cards：重新脏化卡片。
  - 回收空闲巨型分区 Humongous Reclaim：G1做了一个优化：通过查看所有根对象以及年轻代分区的RSet，如果确定RSet中巨型对象没有任何引用，则说明G1发现了一个不可达的巨型对象，该对象分区会被回收。
  - 释放分区 Free CSet：回收CSet分区的所有空间，并加入到空闲分区中。
  - 其他活动 Other：GC中可能还会经历其他耗时很小的活动，如修复JNI句柄等。

##### 并发标记周期后的年轻代收集 Young Collection Following Concurrent Marking Cycle

当G1发起并发标记周期之后，并不会马上开始混合收集。
G1会先等待下一次年轻代收集，然后在该收集阶段中，确定下次混合收集的CSet(Choose CSet)。

##### 混合收集周期 Mixed Collection Cycle, `Mixed GC`

单次的混合收集与年轻代收集并无二致。

根据暂停目标，老年代的分区可能不能一次暂停收集中被处理完，G1会发起连续多次的混合收集，称为混合收集周期(Mixed Collection Cycle)。

G1会计算每次加入到CSet中的分区数量、混合收集进行次数，并且在上次的年轻代收集、以及接下来的混合收集中，G1会确定下次加入CSet的分区集(Choose CSet)，并且确定是否结束混合收集周期。

### 转移失败的担保机制 `Full GC`

转移失败(`Evacuation Failure`)是指当G1无法在堆空间中申请新的分区时，G1便会触发担保机制，执行一次`STW`式的、单线程（JDK10支持多线程）的Full GC。

![img](JVM G1（Garbage-First Garbage Collector）收集器全过程剖析_个人文章 - SegmentFault 思否.assets/bVbGI4K)

Full GC会对整堆做标记清除和压缩，最后将只包含纯粹的存活对象。参数`-XX:G1ReservePercent`(默认10%)可以保留空间，来应对晋升模式下的异常情况，最大占用整堆50%，更大也无意义。

G1在以下场景中会触发Full GC，同时会在日志中记录`to-space exhausted`以及`Evacuation Failure`：

- 从年轻代分区拷贝存活对象时，无法找到可用的空闲分区
- 从老年代分区转移存活对象时，无法找到可用的空闲分区
- 分配巨型对象`Humongous Object` 时在老年代无法找到足够的连续分区

**由于G1的应用场合往往堆内存都比较大，所以Full GC的收集代价非常昂贵，应该避免Full GC的发生。**

## 问题

- 什么时候触发concurrent marking ？

```
# 启动并发周期 Concurrent Marking Cycle （以及后续的混合周期 MixedGC）时的堆内存占用百分比. G1用它来触发并发GC周期,基于整个堆的使用率,而不只是某一代内存的使用比例。默认45%
# 当堆存活对象占用堆的45%，就会启动G1 中并发标记周期 Concurrent Marking Cycle
-XX:InitiatingHeapOccupancyPercent
```

- 什么时候发生Mixed GC?

  concurrent marking 主要是为Mixed GC提供标记服务的，并不是一次GC过程的一个必须环节。

  由一些参数控制，另外也控制着哪些老年代Region会被选入CSet（收集集合）。

```
# 一次 concurrent marking之后，最多执行Mixed GC的次数(默认8)
-XX:G1MixedGCCountTarget
# 堆废物百分比(默认5%)，在每次YGC之后和再次发生Mixed GC之前，会检查垃圾占比是否达到此参数，只有达到了，下次才会发生Mixed GC。
-XX:G1HeapWastePercent
# old generation region中的存活对象的占比，只有在此参数之下，才会被选入CSet。
-XX:G1MixedGCLiveThresholdPercent
# 一次Mixed GC中能被选入CSet的最多old generation region数量。
-XX:G1OldCSetRegionThresholdPercent
```

## GC日志详解

##### 并发标记周期 Concurrent Marking Cycle

```
[GC concurrent-root-region-scan-start]
[GC concurrent-root-region-scan-end, 0.0094252 secs]
# 根分区扫描，可能会被 YGC 打断，那么结束就是如：[GC pause (G1 Evacuation Pause) (young)[GC concurrent-root-region-scan-end, 0.0007157 secs]
[GC concurrent-mark-start]
[GC concurrent-mark-end, 0.0203881 secs]
# 并发标记阶段
[GC remark [Finalize Marking, 0.0007822 secs] [GC ref-proc, 0.0005279 secs] [Unloading, 0.0013783 secs], 0.0036513 secs]
#  重新标记，STW
 [Times: user=0.01 sys=0.00, real=0.00 secs] 
[GC cleanup 13985K->13985K(20480K), 0.0034675 secs]
 [Times: user=0.00 sys=0.00, real=0.00 secs] 
# 清除
```

##### 年轻代收集 YGC

```
[GC pause (G1 Evacuation Pause) (young), 0.0022483 secs]
# young -> 年轻代      Evacuation-> 复制存活对象 
   [Parallel Time: 1.0 ms, GC Workers: 10] # 并发执行的GC线程数，以下阶段是并发执行的
      [GC Worker Start (ms): Min: 109.0, Avg: 109.1, Max: 109.1, Diff: 0.2] 
      [Ext Root Scanning (ms): Min: 0.1, Avg: 0.2, Max: 0.3, Diff: 0.2, Sum: 2.3] # 外部根分区扫描
      [Update RS (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.0] # 更新已记忆集合 Update RSet，检测从年轻代指向老年代的对象
         [Processed Buffers: Min: 0, Avg: 0.0, Max: 0, Diff: 0, Sum: 0] 
      [Scan RS (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.0]# RSet扫描
      [Code Root Scanning (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.1] # 代码根扫描
      [Object Copy (ms): Min: 0.3, Avg: 0.3, Max: 0.4, Diff: 0.1, Sum: 3.5] # 转移和回收，拷贝存活的对象到survivor/old区域
      [Termination (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.0] # 完成上述任务后，如果任务队列已空，则工作线程会发起终止要求。
         [Termination Attempts: Min: 1, Avg: 5.8, Max: 9, Diff: 8, Sum: 58]
      [GC Worker Other (ms): Min: 0.0, Avg: 0.0, Max: 0.0, Diff: 0.0, Sum: 0.1] # GC外部的并行活动，该部分并非GC的活动，而是JVM的活动导致占用了GC暂停时间(例如JNI编译)。
      [GC Worker Total (ms): Min: 0.5, Avg: 0.6, Max: 0.7, Diff: 0.2, Sum: 5.9]
      [GC Worker End (ms): Min: 109.7, Avg: 109.7, Max: 109.7, Diff: 0.0]
   [Code Root Fixup: 0.0 ms] # 串行任务，根据转移对象更新代码根
   [Code Root Purge: 0.0 ms] #串行任务， 代码根清理
   [Clear CT: 0.5 ms] #串行任务，清除全局卡片 Card Table 标记
   [Other: 0.8 ms]
      [Choose CSet: 0.0 ms] # 选择下次收集集合  CSet
      [Ref Proc: 0.4 ms] # 引用处理 Ref Proc，处理软引用、弱引用、虚引用、final引用、JNI引用
      [Ref Enq: 0.0 ms] # 引用排队 Ref Enq
      [Redirty Cards: 0.3 ms] # 卡片重新脏化 Redirty Cards：重新脏化卡片
      [Humongous Register: 0.0 ms] 
      [Humongous Reclaim: 0.0 ms] # 回收空闲巨型分区 Humongous Reclaim，通过查看所有根对象以及年轻代分区的RSet，如果确定RSet中巨型对象没有任何引用，该对象分区会被回收。
      [Free CSet: 0.0 ms]  # 释放分区 Free CSet
   [Eden: 12288.0K(12288.0K)->0.0B(11264.0K) Survivors: 0.0B->1024.0K Heap: 12288.0K(20480.0K)->832.0K(20480.0K)]
 [Times: user=0.01 sys=0.00, real=0.00 secs] 
# 从年轻代分区拷贝存活对象时，无法找到可用的空闲分区
# 从老年代分区转移存活对象时，无法找到可用的空闲分区 这两种情况之一导致的 YGC
[GC pause (G1 Evacuation Pause) (young) (to-space exhausted), 0.0916534 secs]
# 并发标记周期 Concurrent Marking Cycle 中的 根分区扫描阶段，被 YGC中断
[GC pause (G1 Evacuation Pause) (young)[GC concurrent-root-region-scan-end, 0.0007157 secs]
```

##### 混合收集周期 Mixed Collection Cycle, Mixed GC

```
# 并发标记周期 Concurrent Marking Cycle 的开始
[GC pause (G1 Evacuation Pause) (young) (initial-mark) , 0.0443460 secs]
```

##### Full GC

```
[Full GC (Allocation Failure) 20480K->9656K(20480K), 0.0189481 secs]
   [Eden: 0.0B(1024.0K)->0.0B(5120.0K) Survivors: 0.0B->0.0B Heap: 20480.0K(20480.0K)->9656.8K(20480.0K)], [Metaspace: 4960K->4954K(1056768K)]
 [Times: user=0.03 sys=0.00, real=0.02 secs] 
```

## 参考资料

- [https://www.oracle.com/techni...](https://www.oracle.com/technical-resources/articles/java/g1gc.html)

- JDK8 G1： [https://docs.oracle.com/javas...](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/g1_gc.html)

- Other Blog：

- - [https://www.infoq.com/article...](https://www.infoq.com/articles/G1-One-Garbage-Collector-To-Rule-Them-All/)
  - [https://tech.meituan.com/2016...](https://tech.meituan.com/2016/09/23/g1.html)

- - [https://www.infoq.com/article...](https://www.infoq.com/articles/tuning-tips-G1-GC/)
  - [https://blog.csdn.net/coderli...](https://blog.csdn.net/coderlius/article/details/79272773)
    - [https://www.cnblogs.com/webor...](https://www.cnblogs.com/webor2006/p/11146273.html)
    - [https://www.cnblogs.com/webor...](https://www.cnblogs.com/webor2006/p/11147545.html)
    - [1] Charlie H, Monica B, Poonam P, Bengt R. Java Performance Companion
    - [2] 周志明. 深入理解JVM虚拟机