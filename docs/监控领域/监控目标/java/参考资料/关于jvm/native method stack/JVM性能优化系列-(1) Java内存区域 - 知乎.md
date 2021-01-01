# JVM性能优化系列-(1) Java内存区域

[![帅柴](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-29dc6170f7b64078dbbde6148f553b38_xs.jpg)](https://www.zhihu.com/people/vincent946)

[帅柴](https://www.zhihu.com/people/vincent946)

码农/音乐/厨师/阅读，公众号【后端精进之路】

关注他

5 人赞同了该文章





## 1. Java内存区域

### 1.1 运行时数据区

Java虚拟机在执行Java程序的过程中会把它所管理的内存划分为若干个不同的数据区域。主要包括：程序计数器、虚拟机栈、本地方法栈、Java堆、方法区（运 行时常量池）、直接内存。



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-9f926a097d377e90988b9fda50a2aade_720w.jpg)



### 程序计数器

程序计数器（Program Counter Register）是一块较小的内存空间，可以看作是当前线程所执行的字节码的行号指示器。在虚拟机概念模型中，字节码解释器工作时就是通过改变计数器的值来选取下一条需要执行的字节码指令，分支、循环、跳转、异常处理、线程恢复等基础功能都需要依赖这个计数器来完成。

程序计数器是一块“线程私有”的内存，各个线程相互独立存储，互不影响。

### Java虚拟机栈

Java虚拟机栈（Java Virtual Machine Stacks）描述的是Java方法执行的内存模型：每个方法在执行的同时都会创建一个**栈帧（Stack Frame）**，栈帧中存储着局部变量表、操作数栈、动态链接、方法出口等信息。每一个方法从调用直至执行完成的过程，会对应一个栈帧在虚拟机栈中入栈到出栈的过程。与程序计数器一样，Java虚拟机栈也是线程私有的。

### 本地方法栈

本地方法栈（Native Method Stack）与Java虚拟机栈作用很相似，它们的区别在于虚拟机栈为虚拟机执行Java方法（即字节码）服务，而本地方法栈则为虚拟机使用到的Native方法服务。

> 在虚拟机规范中对本地方法栈中使用的语言、方式和数据结构并无强制规定，因此具体的虚拟机可实现它。甚至有的虚拟机（Sun HotSpot虚拟机）直接把本地方法栈和虚拟机栈合二为一。与虚拟机一样，本地方法栈会抛出StackOverflowError和OutOfMemoryError异常。

### Java堆

对于大多数应用而言，Java堆（Heap）是Java虚拟机所管理的内存中最大的一块，它被所有线程共享的，在虚拟机启动时创建。此内存区域唯一的目的是存放对象实例，几乎所有的对象实例都在这里分配内存，且每次分配的空间是不定长的。

在Heap 中分配一定的内存来保存对象实例，实际上只是保存对象实例的属性值，属性的类型和对象本身的类型标记等，并不保存对象的方法（方法是指令，保存在Stack中）,在Heap 中分配一定的内存保存对象实例和对象的序列化比较类似。对象实例在Heap 中分配好以后，需要在Stack中保存一个4字节的Heap 内存地址，用来定位该对象实例在Heap 中的位置，便于找到该对象实例。

> Java虚拟机规范中描述道：所有的对象实例以及数组都要在堆上分配，但是随着JIT编译器的发展和逃逸分析技术逐渐成熟，栈上分配、标量替换优化技术将会导致一些微妙的变化发生，所有的对象都在堆上分配的定论也并不“绝对”了。

### 方法区

方法区（Method Area）与Java堆一样，是各个线程共享的内存区域。Object Class Data(类定义数据)是存储在方法区的，此外，**常量、静态变量、JIT编译后的代码**也存储在方法区。正因为方法区所存储的数据与堆有一种类比关系，所以它还被称为Non-Heap。

> 在Java 7及之前版本，我们也习惯称方法区它为“永久代”（Permanent Generation），更确切来说，应该是“**HotSpot使用永久代实现了方法区**”.

### 运行时常量池

运行时常量池（Runtime Constant Pool）是方法区的一部分，用于存放编译期生成的各种字面量("zdy","123"等)和符号引用。

### 直接内存

直接内存（Direct Memory）并不是虚拟机运行时数据区的一部分，也不是Java虚拟机规范中定义的内存区域。但这部分内存也被频繁运用，而却可能导致OutOfMemoryError异常出现。

本机直接内存的分配不会受到Java堆大小的限制，但是既然是内存，还是会受到本机总内存（包括RAM以及SWAP区或分页文件）大小以及处理器寻址空间的限制。服务器管理员在配置虚拟机参数时，会根据实际内存设置-Xmx等参数信息，但经常忽略直接内存，使得各个内存区域总和大于物理内存限制（包括物理的和操作系统的限制），从而导致动态扩展时出现OutOfMemoryError异常。

以NIO（New Input/Output）类为例，NIO引入了一种基于通道（Channel）与缓冲区（Buffer）的I/O方式，它可以使用Native函数库直接分配堆外内存，然后通过一个存储在Java堆中的DirectByteBuffer对象作为这块内存的引用进行操作。这样能避免在Java堆和Native堆中来回复制数据，在一些场景里显著提高性能。

### 1.2 JDK 6/7/8 内存区域变化

JDK 1.6 中的内存区域如下：此时运行时常量池（Runtime Constant Pool）是方法区的一部分。



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-30bf28479b7f65aa06a98f0844501a7d_720w.jpg)



JDK 1.7 中的内存区域如下：此时运行时常量池放到了堆中。



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-2d82556b002aa8a50480f76b65cfe595_720w.jpg)



JDK 1.8 中的内存区域如下：此时运行时常量池仍在堆中，和JDK7最大的差别就是：**元数据区取代了永久代**，就是JDK8没有了PermSize相关的参数配置了。元空间的本质和永久代类似，都是对JVM规范中方法区的实现。不过元空间与永久代之间最大的区别在于：**元数据空间并不在虚拟机中，而是使用本地内存。**



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-6f21eaf1d09e0886921c6cd551b3f787_720w.jpg)



### 方法区变化

JDK1.8中取消了永久代，那么是不是也就没有方法区了呢？当然不是，**方法区是一个规范，规范没变，它就一直在，只不过取代永久代的是元空间（Metaspace）而已**。

在原来的永久代划分中，**永久代用来存放类的元数据信息、静态常量以及常量池等**。现在**类的元信息存储在元空间中**，**静态变量和常量池等并入堆中**，相当于原来的永久代中的数据，被元空间和堆内存给瓜分了。

为什么废除永久代？Oracle为什么要做这样的改进呢？

1. 容易内存溢出：在原来的永久代划分中，每当一个类初次被加载的时候，它的元数据都会放到永久代中。但是永久代的内存空间也是有大小限制的，如果**加载的类太多，很有可能导致永久代内存溢出**；
2. 大小无法确定：**永久代大小也不容易确定，因为这其中有很多影响因素，比如类的总数，常量池的大小和方法数量等，但是PermSize指定太小又很容易造成永久代内存溢出**；
3. GC回收效率低：HotSpot虚拟机的每种类型的垃圾回收器都需要特殊处理永久代中的元数据。永久代会为GC带来不必要的复杂度，并且回收效率偏低。将元数据从永久代剥离出来，不仅实现了对元空间的无缝管理，还可以简化Full GC以及对以后的并发隔离类元数据等方面进行优化。

### 1.3 Java线程的内存区域划分

从Java线程的角度，按私有和共享划分，可以划分为如下图所示：



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-8c94b533266e2c100e19318b3187b6c6_720w.jpg)



### 1.4 堆和栈

### 区别

**1. 功能不同**

**栈**：以栈帧的方式存储方法调用的过程，并存储方法调用过程中基本数据类型的变量（int、short、long、byte、float、double、boolean、char等）以及对象的引用变量，其内存分配在栈上，变量出了作用域就会自动释放；

**堆**：堆内存用来存储Java中的对象。无论是成员变量，局部变量，还是类变量，它们指向的对象都存储在堆内存中；

**2. 线程的归属不一样**

**栈**内存归属于单个线程，每个线程都会有一个栈内存，其存储的变量只能在其所属线程中可见，即栈内存可以理解成线程的私有内存。

**堆**内存中的对象对所有线程可见。堆内存中的对象可以被所有线程访问。

**3. 空间大小不一样**

栈的内存要远远小于堆内存，栈的深度是有限制的，可能发生StackOverFlowError问题。

**Java栈定义的默认大小是1M。**

更多关于堆和栈的区别，如下图所示：



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-6677e5e57360398a2925f44b3f28559b_720w.jpg)



### 方法的出入栈

当在执行函数时，会把方法打包成栈帧，一个栈帧至少要包含局部变量表、操作数栈和栈数据区。



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-cfd05579903f8ec7097aeb18dad40be1_720w.jpg)



### 栈上分配

虚拟机提供的一种优化技术，基本思想是，对于线程私有的对象，将它打散分配在栈上，而不分配在堆上。好处是对象跟着方法调用自行销毁，不需要进行垃圾回收，可以提高性能。

栈上分配需要的技术基础，逃逸分析。逃逸分析的目的是判断对象的作用域是否会逃逸出方法体。**注意，任何可以在多个线程之间共享的对象，一定都属于逃逸对象。**

下面举例对逃逸分析进行讲解：

- User类型的对象u就没有逃逸出方法test

```text
public void test(int x,inty ){
String x = “”;
User u = ….
….. 
}
```

- User类型的对象u就逃逸出方法test

```text
public  User test(int x,inty ){
String x = “”;
User u = ….
….. 
return u;
}
```

**JVM中如何启用栈上分配：**

对栈上分配发生影响的参数就是三个，-server、-XX:+DoEscapeAnalysis和-XX:+EliminateAllocations，任何一个发生变化都不会发生栈上分配，因为启用逃逸分析和标量替换默认是打开的，所以，一般情况下，JVM的参数只用-server就可以有栈上替换的效果。

以下对三个参数进行详细分析：

**-server**： JVM运行的模式之一, server模式才能进行逃逸分析， JVM运行的模式还有mix/client

**-XX:+DoEscapeAnalysis**：启用逃逸分析(默认打开)

**-XX:+EliminateAllocations**：标量替换(默认打开)，打开后JVM会尝试在栈上分配未逃逸的对象。

**栈上分配会大大加快实例对象的生成和销毁速度。**

### 1.5 虚拟机中的对象

### 对象的创建方法

Java类的创建方法大致有如下4种方法：

- new关键字：这应该是我们最常见和最常用最简单的创建对象的方式。
- 使用newInstance()方法：这里包括Class类的newInstance()方法和Constructor类的newInstance()方法（前者其实也是调用的后者）。
- 使用clone()方法：要使用clone()方法我们必须实现实现Cloneable接口，用clone()方法创建对象并不会调用任何构造函数。即我们所说的浅拷贝。
- 反序列化：要实现反序列化我们需要让我们的类实现Serializable接口。当我们序列化和反序列化一个对象，JVM会给我们创建一个单独的对象，在反序列化时，JVM创建对象并不会调用任何构造函数。即我们所说的深拷贝。

不管使用哪种方法，对象的创建过程都分为以下5个步骤：



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-26e49be0d2f46e776013a73935f2c95a_720w.jpg)



**1. 类加载检查**

虚拟机遇到一条new指令时，首先将去检查这个指令的参数是否能在常量池中定位到一个类的符号引用，并且检查这个符号引用代表的类是否已被加载、解析和初始化过的，如果没有，则必须先执行相应的类加载过程。

**2. 分配内存**

在类加载检查通过后，虚拟机就将为新生对象分配内存。对象所需内存的大小在类加载完成后便可完全确定，为对象分配空间的任务具体便等同于从Java堆中划出一块大小确定的内存空间，可以分如下两种情况讨论：

- Java堆中内存绝对规整

所有用过的内存都被放在一边，空闲的内存被放在另一边，中间放着一个指针作为分界点的指示器，那所分配内存就仅仅是把那个指针向空闲空间那边挪动一段与对象大小相等的距离，这种分配方式称为“指针碰撞”（Bump The Pointer）。

- Java堆中的内存不规整

已被使用的内存和空闲的内存相互交错，那就没有办法简单的进行指针碰撞了，虚拟机就必须维护一个列表，记录哪些内存块是可用的，在分配的时候从列表中找到一块足够大的空间划分给对象实例，并更新列表上的记录，这种分配方式称为“空闲列表”（Free List）。

> 选择哪种分配方式由Java堆是否规整决定，而Java堆是否规整又由所采用的垃圾收集器是否带有压缩整理功能决定。因此在使用Serial、ParNew等带Compact过程的收集器时，系统采用的分配算法是指针碰撞，而使用CMS这种基于Mark-Sweep算法的收集器时（CMS收集器可以通过UseCMSCompactAtFullCollection或CMSFullGCsBeforeCompaction来整理内存），就通常采用空闲列表.

除如何划分可用空间之外，由于对象创建在虚拟机中是非常频繁的行为，即使是仅仅修改一个指针所指向的位置，在并发情况下也并非线程安全的，可能出现正在给对象A分配内存，指针还没来得及修改，对象B又同时使用了原来的指针来分配内存。解决这个问题有如下两个方案：

- 对分配内存空间的动作进行同步

实际上虚拟机是采用CAS配上失败重试的方式保证更新操作的原子性。

- 把内存分配的动作按照线程划分在不同的空间之中进行

即每个线程在Java堆中预先分配一小块内存，称为本地线程分配缓冲（TLAB ，Thread Local Allocation Buffer），哪个线程要分配内存，就在哪个线程的TLAB上分配，只有TLAB用完，分配新的TLAB时才需要同步锁定。虚拟机是否使用TLAB，可以通过-XX:+/-UseTLAB参数来设定。

**3. 初始化**

内存分配完成之后，虚拟机需要将分配到的内存空间都初始化为零值（不包括对象头），如果使用TLAB的话，这一个工作也可以提前至TLAB分配时进行。这步操作保证了对象的实例字段在Java代码中可以不赋初始值就直接使用。

**4. 设置对象头**

虚拟机要设置对象的信息（如这个对象是哪个类的实例、如何才能找到类的元数据信息、对象的哈希码、对象的GC分代年龄等信息）并存放在对象的对象头（Object Header）中。根据虚拟机当前的运行状态的不同，如是否启用偏向锁等，对象头会有不同的设置方式。

**5. 执行方法**

在上面工作都完成之后，在虚拟机的视角来看，一个新的对象已经产生了。但是在Java程序的视角看来，对象创建才刚刚开始——方法还没有执行，所有的字段都还为零值。所以一般来说（由字节码中是否跟随有invokespecial指令所决定），new指令之后会接着执行方法，把对象按照程序员的意愿进行初始化，这样一个真正可用的对象才算完全产生出来。

### 对象的内存布局

HotSpot虚拟机中，对象在内存中存储的布局可以分为三块区域：对象头（Header）、实例数据（Instance Data）和对齐填充（Padding）。

**1. 对象头**

HotSpot虚拟机的对象头包括两部分信息：

- **对象自身的运行时数据 “Mark Word”**: 如哈希码（HashCode）、GC分代年龄、锁状态标志、线程持有的锁、偏向线程ID、偏向时间戳等等.

> 这部分数据的长度在32位和64位的虚拟机（暂不考虑开启压缩指针的场景）中分别为32个和64个Bits，官方称它为“Mark Word”。考虑到虚拟机的空间效率，Mark Word被设计成一个非固定的数据结构以便在极小的空间内存储尽量多的信息，它会根据对象的状态复用自己的存储空间。例如在32位的HotSpot虚拟机中对象未被锁定的状态下，Mark Word的32个Bits空间中的25Bits用于存储对象哈希码（HashCode），4Bits用于存储对象分代年龄，2Bits用于存储锁标志位，1Bit固定为0，在其他状态（轻量级锁定、重量级锁定、GC标记、可偏向）下对象的存储内容如下图所示：



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-64ea82040b0a39e7ec0bee19b676f6f5_720w.jpg)



- **类型指针**: 类型指针即对象指向它的类元数据的指针，虚拟机通过这个指针来确定这个对象是哪个类的实例。

> 并不是所有的虚拟机实现都必须在对象数据上保留类型指针，换句话说查找对象的元数据信息并不一定要经过对象本身，这点我们在下一节讨论。另外，如果对象是一个Java数组，那在对象头中还必须有一块用于记录数组长度的数据，因为虚拟机可以通过普通Java对象的元数据信息确定Java对象的大小，但是从数组的元数据中无法确定数组的大小。

**2. 实例数据**

实例数据是对象真正存储的有效信息，也既是我们在程序代码里面所定义的各种类型的字段内容，无论是从父类继承下来的，还是在子类中定义的都需要记录起来。

> 这部分的存储顺序会受到虚拟机分配策略参数（FieldsAllocationStyle）和字段在Java源码中定义顺序的影响。HotSpot虚拟机默认的分配策略为longs/doubles、ints、shorts/chars、bytes/booleans、oops（Ordinary Object Pointers），从分配策略中可以看出，相同宽度的字段总是被分配到一起。在满足这个前提条件的情况下，在父类中定义的变量会出现在子类之前。如果CompactFields参数值为true（默认为true），那子类之中较窄的变量也可能会插入到父类变量的空隙之中。

**3. 对齐填充**

对齐填充并不是必然存在的，也没有特别的含义，它仅仅起着占位符的作用。由于HotSpot VM的自动内存管理系统要求对象起始地址必须是8字节的整数倍，换句话说就是对象的大小必须是8字节的整数倍。对象头部分正好似8字节的倍数（1倍或者2倍），因此当对象实例数据部分没有对齐的话，就需要通过对齐填充来补全。

### 对象的访问定位

Java程序需要通过栈上的对象引用（reference）数据（存储在栈上的局部变量表中）来操作堆上的具体对象。由于reference类型在Java虚拟机规范里面也只规定了是一个指向对象的引用，并没有定义这个引用的具体实现，对象访问方式也是取决于虚拟机实现而定的。主流的访问方式有使用句柄和直接指针两种。



![img](JVM性能优化系列-(1) Java内存区域 - 知乎.assets/v2-882fd34b1e77c12f5bcb2ec54df26a9a_720w.jpg)



**1. 使用句柄访问**

如果使用句柄访问的话，Java堆中将会划分出一块内存来作为句柄池，reference中存储的就是对象的句柄地址，而句柄中包含了对象实例数据与类型数据的各自的具体地址信息。

**2. 使用直接指针访问**

如果使用直接指针访问的话，Java堆对象的布局中就必须考虑如何放置访问类型数据的相关信息，reference中存储的直接就是对象地址。

**两种方式的对比：**

- 句柄

使用句柄访问的最大好处就是reference中存储的是稳定的句柄地址，在对象被移动（垃圾收集时移动对象是非常普遍的行为）时只会改变句柄中的实例数据指针，而reference本身不需要被修改。

- 直接指针

使用直接指针来访问最大的好处就是速度更快，它节省了一次指针定位的时间开销，由于对象访问的在Java中非常频繁，因此这类开销积小成多也是一项 非常可观的执行成本。从上一部分讲解的对象内存布局可以看出，HotSpot是使用直接指针进行对象访问的。

### 1.6 堆参数设置和内存溢出实战

### Java堆溢出

可以使用`-Xms（堆的最小值）`和`-Xmx（堆的最大值）`参数进行堆大小的配置：

下面的例子中，通过参数`-Xms5m -Xmx5m -XX:+PrintGC`设置堆的大小为5M，程序中不断的往list中添加Object，最后造成堆溢出。

```text
public class OOM {

    public static void main(String[] args) {

        List<Object> list = new LinkedList<>();
        int i=0;
        while(true) {
            i++;
            if(i%10000==0) System.out.println("i="+i);
            list.add(new Object());
        }
    }

}
```

注意到堆溢出时，可能发生两种error，

1. 出现java.lang.OutOfMemoryError: GC overhead limit exceeded 一般是（某个循环里可能性最大）在不停的分配对象，但是分配的太多，把堆撑爆了。
2. 出现java.lang.OutOfMemoryError: Java heap space一般是分配了巨型对象

### 方法区和运行时常量池溢出

前面介绍到，jdk7及以前，通过永久代实现了方法区。jdk8及以后，移除了永久代，采用元数据区，所以两者的参数配置不一样。

jdk1.7及以前：`-XX:PermSize`；`-XX:MaxPermSize` jdk1.8以后：`-XX:MetaspaceSize`； `-XX:MaxMetaspaceSize`

此时采用和上述相同的例子，在jdk11中，通过参数`-XX:MaxMetaspaceSize=3M`设置元数据区的大小最大为3M。

```text
public class OOM {

    public static void main(String[] args) {

        List<Object> list = new LinkedList<>();
        int i=0;
        while(true) {
            i++;
            if(i%10000==0) System.out.println("i="+i);
            list.add(new Object());
        }
    }

}
```

程序启动后初始化失败，提示元数据区过小。

```text
Error occurred during initialization of VM
MaxMetaspaceSize is too small.
```

### 虚拟机栈和本地方法栈溢出

Java栈的默认大小为1M，可以通过–Xss调整大小。

下面的例子中，通过`-Xss256k`设置栈的大小为256k，程序启动后不久发生栈溢出java.lang.StackOverflowError。

```text
public class StackOOM {

    private int stackLength = 1;
    private void diGui(int x,String y) {
        stackLength++;
        diGui(x,y);
    }

    public static void main(String[] args) {
        StackOOM oom = new StackOOM();
        try {
            oom.diGui(12,"Way2backend.tech");
        } catch (Throwable e) {
            System.out.println("stackLength = "+oom.stackLength);
            e.printStackTrace();
        }
    }

}
```

> java.lang.StackOverflowError 一般的方法调用是很难出现的，如果出现了要考虑是否有无限递归。
> 虚拟机栈带给我们的启示：方法的执行因为要打包成栈桢，所以天生要比实现同样功能的循环慢，所以树的遍历算法中：递归和非递归(循环来实现)都有存在的意义。递归代码简洁，非递归代码复杂但是速度较快。

### 本地直接内存溢出

直接内存不是虚拟机运行时数据区的一部分，也不是java虚拟机规范中定义的内存区域；如果使用了NIO,这块区域会被频繁使用，在java堆内可以directByteBuffer对象直接引用并操作；

这块内存不受java堆大小限制，但受本机总内存的限制，可以通过`-XX:MaxDirectMemorySize`来设置（默认与堆内存最大值一样），所以也会出现OOM异常。

下面的例子中，通过参数`-XX:MaxDirectMemorySize=10M`设置直接内存的大小为10M，但是程序中却尝试分配14M的直接内存，导致程序启动后抛出直接内存OutOfMemoryError的错误。

```text
public class DirectMem {
    public static void main(String[] args) {
        ByteBuffer b = ByteBuffer.allocateDirect(1024*1024*14);
    }
}
```

------

参考：

- [https://meandni.com/2019/01/10/jvm_note1/#](https://link.zhihu.com/?target=https%3A//meandni.com/2019/01/10/jvm_note1/%23)
- [http://mosrv.com/java/2018/08/03/java-metaspace.html](https://link.zhihu.com/?target=http%3A//mosrv.com/java/2018/08/03/java-metaspace.html)
- [https://www.javatt.com/p/60329](https://link.zhihu.com/?target=https%3A//www.javatt.com/p/60329)
- [https://juejin.im/post/5d4e2aa7f265da03d15540b9](https://link.zhihu.com/?target=https%3A//juejin.im/post/5d4e2aa7f265da03d15540b9)
- [https://www.itcodemonkey.com/article/8842.html](https://link.zhihu.com/?target=https%3A//www.itcodemonkey.com/article/8842.html)

------

参考：

- [https://www.jianshu.com/p/22d38d5c8c2a](https://link.zhihu.com/?target=https%3A//www.jianshu.com/p/22d38d5c8c2a)
- 《实战Java高并发程序设计》

------

本文由『后端精进之路』原创，首发于博客 [http://teckee.github.io/](https://link.zhihu.com/?target=http%3A//teckee.github.io/) , 转载请注明出处