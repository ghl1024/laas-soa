# [Java8内存模型—永久代(PermGen)和元空间(Metaspace)](https://www.cnblogs.com/paddix/p/5309550.html)

**一、JVM 内存模型**

　　根据 JVM 规范，JVM 内存共分为虚拟机栈、堆、方法区、程序计数器、本地方法栈五个部分。

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160326200119386-756216654.png)

　　1、虚拟机栈：每个线程有一个私有的栈，随着线程的创建而创建。栈里面存着的是一种叫“栈帧”的东西，每个方法会创建一个栈帧，栈帧中存放了局部变量表（基本数据类型和对象引用）、操作数栈、方法出口等信息。栈的大小可以固定也可以动态扩展。当栈调用深度大于JVM所允许的范围，会抛出StackOverflowError的错误，不过这个深度范围不是一个恒定的值，我们通过下面这段程序可以测试一下这个结果：

栈溢出测试源码：

```
package` `com.paddx.test.memory;` `public` `class` `StackErrorMock {``  ``private` `static` `int` `index = ``1``;` `  ``public` `void` `call(){``    ``index++;``    ``call();``  ``}` `  ``public` `static` `void` `main(String[] args) {``    ``StackErrorMock mock = ``new` `StackErrorMock();``    ``try` `{``      ``mock.call();``    ``}``catch` `(Throwable e){``      ``System.out.println(``"Stack deep : "``+index);``      ``e.printStackTrace();``    ``}``  ``}``}
```

代码段 1

运行三次，可以看出每次栈的深度都是不一样的，输出结果如下。

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160326203208120-2065530115.png)

至于红色框里的值是怎么出来的，就需要深入到 JVM 的源码中才能探讨，这里不作详细阐述。

虚拟机栈除了上述错误外，还有另一种错误，那就是当申请不到空间时，会抛出 OutOfMemoryError。这里有一个小细节需要注意，catch 捕获的是 Throwable，而不是 Exception。因为 StackOverflowError 和 OutOfMemoryError 都不属于 Exception 的子类。

　　2、本地方法栈：

　　这部分主要与虚拟机用到的 Native 方法相关，一般情况下， Java 应用程序员并不需要关心这部分的内容。

　　3、PC 寄存器：

　　PC 寄存器，也叫程序计数器。JVM支持多个线程同时运行，每个线程都有自己的程序计数器。倘若当前执行的是 JVM 的方法，则该寄存器中保存当前执行指令的地址；倘若执行的是native 方法，则PC寄存器中为空。

　　4、堆

　　堆内存是 JVM 所有线程共享的部分，在虚拟机启动的时候就已经创建。所有的对象和数组都在堆上进行分配。这部分空间可通过 GC 进行回收。当申请不到空间时会抛出 OutOfMemoryError。下面我们简单的模拟一个堆内存溢出的情况：

```
package` `com.paddx.test.memory;` `import` `java.util.ArrayList;``import` `java.util.List;` `public` `class` `HeapOomMock {``  ``public` `static` `void` `main(String[] args) {``    ``List<``byte``[]> list = ``new` `ArrayList<``byte``[]>();``    ``int` `i = ``0``;``    ``boolean` `flag = ``true``;``    ``while` `(flag){``      ``try` `{``        ``i++;``        ``list.add(``new` `byte``[``1024` `* ``1024``]);``//每次增加一个1M大小的数组对象``      ``}``catch` `(Throwable e){``        ``e.printStackTrace();``        ``flag = ``false``;``        ``System.out.println(``"count="``+i);``//记录运行的次数``      ``}``    ``}``  ``}``}
```

代码段 2

运行上述代码，输出结果如下：　　

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160326193901979-647552717.png)　　　

注意，这里我指定了堆内存的大小为16M，所以这个地方显示的count=14（这个数字不是固定的），至于为什么会是14或其他数字，需要根据 GC 日志来判断，具体原因会在下篇文章中给大家解释。

　　5、方法区：

　　方法区也是所有线程共享。主要用于存储类的信息、常量池、方法数据、方法代码等。方法区逻辑上属于堆的一部分，但是为了与堆进行区分，通常又叫“非堆”。 关于方法区内存溢出的问题会在下文中详细探讨。

**二、PermGen（永久代）**

　　绝大部分 Java 程序员应该都见过 "java.lang.OutOfMemoryError: PermGen space "这个异常。这里的 “PermGen space”其实指的就是方法区。不过方法区和“PermGen space”又有着本质的区别。前者是 JVM 的规范，而后者则是 JVM 规范的一种实现，并且只有 HotSpot 才有 “PermGen space”，而对于其他类型的虚拟机，如 JRockit（Oracle）、J9（IBM） 并没有“PermGen space”。由于方法区主要存储类的相关信息，所以对于动态生成类的情况比较容易出现永久代的内存溢出。最典型的场景就是，在 jsp 页面比较多的情况，容易出现永久代内存溢出。我们现在通过动态生成类来模拟 “PermGen space”的内存溢出：

```
package` `com.paddx.test.memory;` `public` `class` `Test {``}
```

 代码段 3

```
package` `com.paddx.test.memory;` `import` `java.io.File;``import` `java.net.URL;``import` `java.net.URLClassLoader;``import` `java.util.ArrayList;``import` `java.util.List;` `public` `class` `PermGenOomMock{``  ``public` `static` `void` `main(String[] args) {``    ``URL url = ``null``;``    ``List<ClassLoader> classLoaderList = ``new` `ArrayList<ClassLoader>();``    ``try` `{``      ``url = ``new` `File(``"/tmp"``).toURI().toURL();``      ``URL[] urls = {url};``      ``while` `(``true``){``        ``ClassLoader loader = ``new` `URLClassLoader(urls);``        ``classLoaderList.add(loader);``        ``loader.loadClass(``"com.paddx.test.memory.Test"``);``      ``}``    ``} ``catch` `(Exception e) {``      ``e.printStackTrace();``    ``}``  ``}``}
```

代码段 4

运行结果如下：

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160327005846979-1124627174.png)

　　本例中使用的 JDK 版本是 1.7，指定的 PermGen 区的大小为 8M。通过每次生成不同URLClassLoader对象来加载Test类，从而生成不同的类对象，这样就能看到我们熟悉的 "java.lang.OutOfMemoryError: PermGen space " 异常了。这里之所以采用 JDK 1.7，是因为在 JDK 1.8 中， HotSpot 已经没有 “PermGen space”这个区间了，取而代之是一个叫做 Metaspace（元空间） 的东西。下面我们就来看看 Metaspace 与 PermGen space 的区别。

**三、Metaspace（元空间）**

　　其实，移除永久代的工作从JDK1.7就开始了。JDK1.7中，存储在永久代的部分数据就已经转移到了Java Heap或者是 Native Heap。但永久代仍存在于JDK1.7中，并没完全移除，譬如符号引用(Symbols)转移到了native heap；字面量(interned strings)转移到了java heap；类的静态变量(class statics)转移到了java heap。我们可以通过一段程序来比较 JDK 1.6 与 JDK 1.7及 JDK 1.8 的区别，以字符串常量为例：

```
package` `com.paddx.test.memory;` `import` `java.util.ArrayList;``import` `java.util.List;` `public` `class` `StringOomMock {``  ``static` `String base = ``"string"``;``  ``public` `static` `void` `main(String[] args) {``    ``List<String> list = ``new` `ArrayList<String>();``    ``for` `(``int` `i=``0``;i< Integer.MAX_VALUE;i++){``      ``String str = base + base;``      ``base = str;``      ``list.add(str.intern());``    ``}``  ``}``}
```

这段程序以2的指数级不断的生成新的字符串，这样可以比较快速的消耗内存。我们通过 JDK 1.6、JDK 1.7 和 JDK 1.8 分别运行：

JDK 1.6 的运行结果：

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160327005929386-409283462.png)

JDK 1.7的运行结果：

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160327010033823-1341228280.png)

JDK 1.8的运行结果：

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160327010143776-1612977566.png)

　　从上述结果可以看出，JDK 1.6下，会出现“PermGen Space”的内存溢出，而在 JDK 1.7和 JDK 1.8 中，会出现堆内存溢出，并且 JDK 1.8中 PermSize 和 MaxPermGen 已经无效。因此，可以大致验证 JDK 1.7 和 1.8 将字符串常量由永久代转移到堆中，并且 JDK 1.8 中已经不存在永久代的结论。现在我们看看元空间到底是一个什么东西？

　　元空间的本质和永久代类似，都是对JVM规范中方法区的实现。不过元空间与永久代之间最大的区别在于：元空间并不在虚拟机中，而是使用本地内存。因此，默认情况下，元空间的大小仅受本地内存限制，但可以通过以下参数来指定元空间的大小：

　　-XX:MetaspaceSize，初始空间大小，达到该值就会触发垃圾收集进行类型卸载，同时GC会对该值进行调整：如果释放了大量的空间，就适当降低该值；如果释放了很少的空间，那么在不超过MaxMetaspaceSize时，适当提高该值。
　　-XX:MaxMetaspaceSize，最大空间，默认是没有限制的。

　　除了上面两个指定大小的选项以外，还有两个与 GC 相关的属性：
　　-XX:MinMetaspaceFreeRatio，在GC之后，最小的Metaspace剩余空间容量的百分比，减少为分配空间所导致的垃圾收集
　　-XX:MaxMetaspaceFreeRatio，在GC之后，最大的Metaspace剩余空间容量的百分比，减少为释放空间所导致的垃圾收集

现在我们在 JDK 8下重新运行一下代码段 4，不过这次不再指定 PermSize 和 MaxPermSize。而是指定 MetaSpaceSize 和 MaxMetaSpaceSize的大小。输出结果如下：

![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/820406-20160327010233933-699106123.png)

从输出结果，我们可以看出，这次不再出现永久代溢出，而是出现了元空间的溢出。

**四、总结**

　　通过上面分析，大家应该大致了解了 JVM 的内存划分，也清楚了 JDK 8 中永久代向元空间的转换。不过大家应该都有一个疑问，就是为什么要做这个转换？所以，最后给大家总结以下几点原因：

　　1、字符串存在永久代中，容易出现性能问题和内存溢出。

　　2、类及方法的信息等比较难确定其大小，因此对于永久代的大小指定比较困难，太小容易出现永久代溢出，太大则容易导致老年代溢出。

　　3、永久代会为 GC 带来不必要的复杂度，并且回收效率偏低。

　　4、Oracle 可能会将HotSpot 与 JRockit 合二为一。

 作者：[liuxiaopeng](http://www.cnblogs.com/paddix)

 博客地址：[http://www.cnblogs.com/paddix/](http://www.cnblogs.com/paddix)

 声明：转载请在文章页面明显位置给出原文连接。 

标签: [JVM](https://www.cnblogs.com/paddix/tag/JVM/), [内存模型](https://www.cnblogs.com/paddix/tag/内存模型/)

[好文要顶](javascript:void(0);) [关注我](javascript:void(0);) [收藏该文](javascript:void(0);) [![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/icon_weibo_24.png)](javascript:void(0);) [![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/wechat.png)](javascript:void(0);)

[![img](Java8内存模型—永久代(PermGen)和元空间(Metaspace) - liuxiaopeng - 博客园.assets/20160405085105.png)](https://home.cnblogs.com/u/paddix/)

[liuxiaopeng](https://home.cnblogs.com/u/paddix/)
[关注 - 2](https://home.cnblogs.com/u/paddix/followees/)
[粉丝 - 519](https://home.cnblogs.com/u/paddix/followers/)

[+加关注](javascript:void(0);)

73

0

[« ](https://www.cnblogs.com/paddix/p/5282004.html)上一篇： [从字节码层面看“HelloWorld”](https://www.cnblogs.com/paddix/p/5282004.html)
[» ](https://www.cnblogs.com/paddix/p/5326863.html)下一篇： [通过反编译深入理解Java String及intern](https://www.cnblogs.com/paddix/p/5326863.html)

posted @ 2016-03-27 01:04 [liuxiaopeng](https://www.cnblogs.com/paddix/) 阅读(157439) 评论(29) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=5309550) [收藏](javascript:void(0))





评论列表

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#1楼](https://www.cnblogs.com/paddix/p/5309550.html#3430578) 2016-05-13 15:11 [郑斌blog](https://www.cnblogs.com/zhengbin/)

博主写的都挺好的，关注~

[支持(1) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#2楼](https://www.cnblogs.com/paddix/p/5309550.html#3618762) 2017-02-15 09:49 [堕落门徒](https://home.cnblogs.com/u/564309/)

"　元空间的本质和永久代类似，都是对JVM规范中方法区的实现。不过元空间与永久代之间最大的区别在于：元空间并不在虚拟机中，而是使用本地内存。"
博主写的很突出重点，赞。

[支持(7) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#3楼](https://www.cnblogs.com/paddix/p/5309550.html#3638273) 2017-03-12 10:21 [zzhi.wang](https://www.cnblogs.com/zhangzhi19861216/)

讲的很好

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#4楼](https://www.cnblogs.com/paddix/p/5309550.html#3657140) 2017-04-01 11:44 [zhglance](https://www.cnblogs.com/zhglance/)

文章很好，大赞！

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#5楼](https://www.cnblogs.com/paddix/p/5309550.html#3660463) 2017-04-06 14:09 [awkejiang](https://home.cnblogs.com/u/1133533/)

赞！

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#6楼](https://www.cnblogs.com/paddix/p/5309550.html#3674428) 2017-04-22 19:27 [向马湾](https://www.cnblogs.com/xiang-ma/)

讲的条理清晰，有一个问题请教博主：总结中的第二点，“”对于永久代的大小指定比较困难，太小容易出现永久代溢出，“---这个比较容易理解，但下一句---”太大则容易导致老年代溢出。“，为啥永久代太大会容易导致老年代溢出？啥时候永久代和老年代联系上了？

[支持(4) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#7楼](https://www.cnblogs.com/paddix/p/5309550.html#3714486) 2017-06-14 17:46 [UncleMing](https://home.cnblogs.com/u/1182968/)

首先赞一下楼主的文章。
需要指正一下：
去除永久代的原因：（1）为了HotSpot与JRockit的融合；（2）永久代大小不容易确定，PermSize指定太小容易造成永久代OOM，与老年代没关系。

[支持(8) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#8楼](https://www.cnblogs.com/paddix/p/5309550.html#3742949) 2017-07-25 14:43 [非余之鱼](https://www.cnblogs.com/yidongdematong/)

zan

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#9楼](https://www.cnblogs.com/paddix/p/5309550.html#3744011) 2017-07-26 17:09 [想个名字真难](https://home.cnblogs.com/u/1207451/)

文章写的很清晰，但是总结有两点问题：
1、永久代大小并不会影响老年代溢出。
永久代只不过是HotSpot JVM将GC分代收集扩展到方法区，从而出现的一种对方法区的叫法，但是本质上与Heap依然是不同的JVM数据区。如果非要提出方法区把内存占满影响Heap自动扩展的话，那么JDK8中Metaspace一样无法解决。
2、去除永久代后分代GC确实可以减少复杂性，但是还是需要设计额外的方法区GC（老实说HotSpot JVM扩展永久代就是想省事），且方法区功能也决定了它回收效率就是偏低，这与永久代并没有关系。

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#10楼](https://www.cnblogs.com/paddix/p/5309550.html#3753976) 2017-08-09 17:01 [poyi2008](https://home.cnblogs.com/u/446404/)

不错,zan

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#11楼](https://www.cnblogs.com/paddix/p/5309550.html#3782617) 2017-09-12 22:21 [xiaoyon](https://www.cnblogs.com/hackerxiaoyon/)

[@](https://www.cnblogs.com/paddix/p/5309550.html#3674428) 向马湾
我的觉得因为永久代太大，老年代就会变小了，从而导致容易溢出问题。不知道是否解释正确。

[支持(0) ](javascript:void(0);)[反对(6)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#12楼](https://www.cnblogs.com/paddix/p/5309550.html#3884795) 2018-01-09 00:23 [bambi2018](https://home.cnblogs.com/u/1314513/)

请问那些参数信息怎么查看的？

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#13楼](https://www.cnblogs.com/paddix/p/5309550.html#3928951) 2018-03-21 10:48 [不将就！](https://www.cnblogs.com/byron0918/)

感谢分享，写的很好！

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#14楼](https://www.cnblogs.com/paddix/p/5309550.html#4055921) 2018-09-01 22:39 [DFZ](https://home.cnblogs.com/u/436899/)

点赞，唯一不好的一点是，文章标题，其实文章开头的图片不是JVM的内存模型，而是JVM运行时数据区，JVM的内存模型是另一个概念

[支持(2) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#15楼](https://www.cnblogs.com/paddix/p/5309550.html#4097937) 2018-10-24 19:18 [南风99](https://home.cnblogs.com/u/1474204/)

文章标题提到了元空间，元空间就是直接内存吧，这篇文章提到了直接内存[《java8的新特性：内存结构、直接内存的介绍》](http://swiftlet.net/archives/2759)

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#16楼](https://www.cnblogs.com/paddix/p/5309550.html#4204203) 2019-03-16 14:56 [itaha](https://www.cnblogs.com/itaha/)

你好，请问元空间不在虚拟机了，那么垃圾回收如何操作元空间的

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#17楼](https://www.cnblogs.com/paddix/p/5309550.html#4213501) 2019-03-26 10:12 [我是来学习的JMY](https://www.cnblogs.com/loveJMY/)

String str = base + base;
对这个有疑问，我认为这个分配到的是heap区，不是方法区，不管是jdk几的版本，因为这个和new String是一样的~~

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#18楼](https://www.cnblogs.com/paddix/p/5309550.html#4238454) 2019-04-23 17:23 [9dragon](https://home.cnblogs.com/u/1247649/)

对于最后一个实验，java8字符串常量在不在Metaspace，在Heap

java -version
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)

最终异常还是：
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space

[支持(3) ](javascript:void(0);)[反对(1)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#19楼](https://www.cnblogs.com/paddix/p/5309550.html#4240898) 2019-04-25 20:55 [小永coding](https://www.cnblogs.com/my12/)

大佬的第一个标题 不太准确， 应该改成 JVM内存结构

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#20楼](https://www.cnblogs.com/paddix/p/5309550.html#4461230) 2019-12-17 09:48 [元宝爸爸](https://www.cnblogs.com/xinrong2019/)

非常棒！讲的很清晰！对我理解这块很有帮助！

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#21楼](https://www.cnblogs.com/paddix/p/5309550.html#4540455) 2020-04-02 23:15 [灰可爱](https://www.cnblogs.com/jundima/)

[@](https://www.cnblogs.com/paddix/p/5309550.html#4238454)9dragon
String.intern方法不是会把他加入常量池吗

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#22楼](https://www.cnblogs.com/paddix/p/5309550.html#4553270) 2020-04-17 14:56 [aqu415](https://www.cnblogs.com/aqu415/)

首先写的很清晰
嗯，标题感觉有误；
内存模型可不是这样的，改为“运行时数据区”还差不多
内存模型主要讲的是java如何保证各个工作线程与主内存间的数据访问，更新和同步的问题

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#23楼](https://www.cnblogs.com/paddix/p/5309550.html#4574670) 2020-05-12 14:17 [supermary](https://home.cnblogs.com/u/1548503/)

我想问一下这个元空间的本地内存和那个直接内存有什么区别啊

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#24楼](https://www.cnblogs.com/paddix/p/5309550.html#4606204) 2020-06-15 17:04 [Jack_vk](https://www.cnblogs.com/happyMelon/)

```
java version "1.7.0_80" Java(TM) SE Runtime Environment (build 1.7.0_80-b15) Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)
```

运行代码后的输出为：

```java
[GC[DefNew: 8192K->1023K(9216K), 0.0159510 secs] 8192K->6947K(19456K), 0.0159840 secs] [Times: user=0.01 sys=0.00, real=0.02 secs] 
[GC[DefNew: 9215K->9215K(9216K), 0.0000150 secs][Tenured: 5923K->10239K(10240K), 0.0343190 secs] 15139K->14088K(19456K), [Perm : 2664K->2664K(21248K)], 0.0343870 secs] [Times: user=0.03 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0403580 secs] 19455K->18836K(19456K), [Perm : 2665K->2665K(21248K)], 0.0404000 secs] [Times: user=0.04 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0373340 secs] 19455K->19383K(19456K), [Perm : 2665K->2665K(21248K)], 0.0373630 secs] [Times: user=0.05 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0393410 secs] 19455K->19409K(19456K), [Perm : 2665K->2664K(21248K)], 0.0393760 secs] [Times: user=0.04 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0348370 secs] 19455K->19450K(19456K), [Perm : 2664K->2664K(21248K)], 0.0348630 secs] [Times: user=0.03 sys=0.00, real=0.03 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0348470 secs] 19455K->19455K(19456K), [Perm : 2664K->2664K(21248K)], 0.0348760 secs] [Times: user=0.04 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0361920 secs] 19455K->19455K(19456K), [Perm : 2664K->2664K(21248K)], 0.0362190 secs] [Times: user=0.03 sys=0.00, real=0.03 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0395020 secs] 19455K->19455K(19456K), [Perm : 2664K->2664K(21248K)], 0.0395390 secs] [Times: user=0.04 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0417670 secs] 19455K->19444K(19456K), [Perm : 2664K->2664K(21248K)], 0.0417920 secs] [Times: user=0.04 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0371640 secs] 19455K->19454K(19456K), [Perm : 2664K->2664K(21248K)], 0.0371910 secs] [Times: user=0.04 sys=0.01, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0364680 secs] 19455K->19455K(19456K), [Perm : 2664K->2664K(21248K)], 0.0364920 secs] [Times: user=0.04 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->10239K(10240K), 0.0368060 secs] 19455K->19455K(19456K), [Perm : 2664K->2664K(21248K)], 0.0368290 secs] [Times: user=0.03 sys=0.00, real=0.04 secs] 
[Full GC[Tenured: 10239K->228K(10240K), 0.0065980 secs] 19455K->228K(19456K), [Perm : 2664K->2664K(21248K)], 0.0066330 secs] [Times: user=0.01 sys=0.00, real=0.00 secs] 
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.lang.ClassLoader.findLoadedClass0(Native Method)
	at java.lang.ClassLoader.findLoadedClass(ClassLoader.java:1093)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:407)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:358)
	at com.hua.jvm.PermGenOomMock.main(PermGenOomMock.java:24)
Heap
 def new generation   total 9216K, used 300K [0x00000007f9a00000, 0x00000007fa400000, 0x00000007fa400000)
  eden space 8192K,   3% used [0x00000007f9a00000, 0x00000007f9a4b058, 0x00000007fa200000)
  from space 1024K,   0% used [0x00000007fa300000, 0x00000007fa300000, 0x00000007fa400000)
  to   space 1024K,   0% used [0x00000007fa200000, 0x00000007fa200000, 0x00000007fa300000)
 tenured generation   total 10240K, used 228K [0x00000007fa400000, 0x00000007fae00000, 0x00000007fae00000)
   the space 10240K,   2% used [0x00000007fa400000, 0x00000007fa4392d0, 0x00000007fa439400, 0x00000007fae00000)
 compacting perm gen  total 21248K, used 2695K [0x00000007fae00000, 0x00000007fc2c0000, 0x0000000800000000)
   the space 21248K,  12% used [0x00000007fae00000, 0x00000007fb0a1ee8, 0x00000007fb0a2000, 0x00000007fc2c0000)
No shared spaces configured.
```

没有出现`java.lang.OutOfMemoryError: PermGen Space`。是不是和jdk版本有关？

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#25楼](https://www.cnblogs.com/paddix/p/5309550.html#4606209) 2020-06-15 17:05 [Jack_vk](https://www.cnblogs.com/happyMelon/)

[@](https://www.cnblogs.com/paddix/p/5309550.html#4204203)itaha
在本地内存中，是可以进行垃圾回收的

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#26楼](https://www.cnblogs.com/paddix/p/5309550.html#4671272) 2020-08-31 02:37 [阿著](https://home.cnblogs.com/u/1675089/)

[@](https://www.cnblogs.com/paddix/p/5309550.html#3618762)堕落门徒
确实很赞

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#27楼](https://www.cnblogs.com/paddix/p/5309550.html#4674733) 2020-09-03 17:27 [zoyua](https://home.cnblogs.com/u/1975609/)

清晰

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#28楼](https://www.cnblogs.com/paddix/p/5309550.html#4728329) 2020-11-04 14:09 [孤独的人是可耻的](https://www.cnblogs.com/aloney/)

两点疑问：
1.最后一个例子，没有设置metaspace大小之前报内存溢出的位置的heap,设置了元空间大小后，报的内存溢出的位置就是metaspace，为什么？
2.文中说明jdk1.8 将字符串常量由永久代转移到堆中，意识元空间移到堆中去了？后面又说元空间使用的不是虚拟机内存，而是直接内存，那么元空间移到堆中到底是什么意思呢，没有使用堆中的内存，又移到了堆中去了，只是概念上的移到了堆中去了吗？

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)

  [回复 ](javascript:void(0);)[引用](javascript:void(0);)

[#29楼](https://www.cnblogs.com/paddix/p/5309550.html#4785473) 2020-12-25 14:42 [沧海一滴](https://www.cnblogs.com/softidea/)

[@](https://www.cnblogs.com/paddix/p/5309550.html#3674428)向马湾
太大，放的类多了，如果类的实例也多，永久代是不是就放不下了

[支持(0) ](javascript:void(0);)[反对(0)](javascript:void(0);)