# JVM系列六(JVM-codecache内存区域介绍)

[2016-05-05](https://thinkhejie.github.io/2016/05/05/JVM系列_06/)

JVM-codecache内存区域介绍



## JVM-codecache内存区域介绍

大家都知道JVM在运行时会将频繁调用方法的字节码编译为本地机器码。这部分代码所占用的内存空间成为CodeCache区域。一般情况下我们是不会关心这部分区域的且大部分开发人员对这块区域也不熟悉。偶然的机会我们线上服务器Down了，在日志里面看到java.lang.OutOfMemoryError code cache。通过查找资料来详细了解一下该快内存区域的使用。

Java进行JIT的时候，会将编译的本地代码放在codecache中，因此可能出现codecache失效的情况。等到codecache失效了，就会需要重新flush的情况，这就会导致gc很慢的情况，因此，一定要保证codecache在不能溢出（注意采用-XX:+TieredCompilation java8 server模式的默认编译方式，是分层编译的。要取消分层编译，要-XX:-TieredCompilation）。分层编译的情况下，编译的阈值更低，更容易达到编译标准，所以很容易好近codecache，这点要注意，所以很容易的产生codecache溢出的。

Java8可以加入参数-XX:+PrintCodeCache，加入后，在jvm退出的时候，就会打印出codecache的使用量，最大使用量，这样我们就可以看出是否有超出的情况。

## Codecache大小控制选项

| 选项                   | 默认值    | 描述                                |
| ---------------------- | --------- | ----------------------------------- |
| InitialCodeCacheSize   | 2555904   | 默认的CodeCache区域大小，单位为字节 |
| ReservedCodeCacheSize  | 251658240 | CodeCache区域的最大值，单位为字节   |
| CodeCacheExpansionSize | 65536     | CodeCache每次扩展大小，单位为字节   |

## Codecache刷新选项

| 选项                         | 默认值                                                       | 描述 |
| ---------------------------- | ------------------------------------------------------------ | ---- |
| ExitOnFullCodeCache          | false 当CodeCache区域满了的时候是否退出JVM                   |      |
| UseCodeCacheFlushing         | false 是否在关闭JIT编译前清除CodeCache                       |      |
| MinCodeCacheFlushingInterval | 30 刷新CodeCache的最小时间间隔 ，单位为秒                    |      |
| CodeCacheMinimumFreeSpace    | 512000 当CodeCache区域的剩余空间小于参数指定的值时停止JIT编译。剩余的空间不会再用来存放方法的本地代码, 可以存放本地方法适配器代 |      |

## 编译策略选项

| 选项                     | 默认值                                                    | 描述 |
| ------------------------ | --------------------------------------------------------- | ---- |
| CompileThreshold         | 10000 指定方法在在被JIT编译前被调用的次数                 |      |
| OnStackReplacePercentage | 140 该值为用于计算是否触发OSR（OnStackReplace）编译的阈值 |      |

## OSR编译的阈值计算

在client模式时，计算规则为CompileThreshold *(OnStackReplacePercentage/100)，在server模式时，计算规则为(CompileThreshold* (OnStackReplacePercentage - InterpreterProfilePercentage))/100。InterpreterProfilePercentage的默认值为33，当方法上的回边计数器到达这个值时，即触发后台的OSR编译，并将方法上累积的调用计数器设置为CompileThreshold的值，同时将回边计数器设置为CompileThreshold/2的值，一方面是为了避免OSR编译频繁触发；另一方面是以便当方法被再次调用时即触发正常的编译，当累积的回边计数器的值再次达到该值时，先检查OSR编译是否完成。如果OSR编译完成，则在执行循环体的代码时进入编译后的代码；如果OSR编译未完成，则继续把当前回边计数器的累积值再减掉一些，从这些描述可看出，默认情况下对于回边的情况，server模式下只要回边次数达到10 700次，就会触发OSR编译。

用以下一段示例代码来模拟编译的触发：

```
public class Foo{  
    public static void main(String[] args){  
    Foo foo=new Foo();  
        for(int i=0;i<10;i++){  
            foo.bar();  
        }  
    }  
    public void bar(){  
        // some bar code  
        for(int i=0;i<10700;i++){  
        bar2();  
        }  
    }  
    private void bar2(){  
        // bar2 method  
    }  
}
```



以上代码采用java -server方式执行，当main中第一次调用foo.bar时，bar方法上的调用计数器为1，回边计数器为0；当bar方法中的循环执行完毕时，bar方法的调用计数器仍然为1，回边计数器则为10 700，达到触发OSR编译的条件，于是触发OSR编译，并将bar方法的调用计数器设置为10 000，回边计数器设置为5 000。

当main中第二次调用foo.bar时，jdk发现bar方法的调用次数已超过compileThreshold，于是在后台执行JIT编译，并继续解释执行// some bar code，进入循环时，先检查OSR编译是否完成。如果完成，则执行编译后的代码，如果未编译完成，则继续解释执行。

当main中第三次调用foo.bar时，如果此时JIT编译已完成，则进入编译后的代码；如果编译未完成，则继续按照上面所说的方式执行。

由于Sun JDK的这个特性，在对Java代码进行性能测试时，要尤其注意是否事先做了足够次数的调用，以保证测试是公平的；对于高性能的程序而言，也应考虑在程序提供给用户访问前，自行进行一定的调用，以保证关键功能的性能。

## JIT编译限制选项

| 选项                      | 默认值 | 描述                                     |
| ------------------------- | ------ | ---------------------------------------- |
| MaxInlineLevel            | 9      | 在进行方法内联前，方法的最多嵌套调用次数 |
| MaxInlineSize             | 35     | 被内联方法的字节码最大值                 |
| MinInliningThreshold      | 9      | 方法被内联的最小调用次数                 |
| InlineSynchronizedMethods | true   | 是否对同步方法进行内联                   |

## JIT诊断选项

| 选项                        | 默认值 | 描述                                                 |
| --------------------------- | ------ | ---------------------------------------------------- |
| PrintFlagsFinal             | false  | 是否打印所有的JVM参数                                |
| PrintCodeCache              | false  | 是否在JVM退出前打印CodeCache的使用情况               |
| PrintCodeCacheOnCompilation | false  | 是否在每个方法被JIT编译后打印CodeCache区域的使用情况 |

## 其它

在tomcat的脚本中，加入-XX:+PrintCodeCache参数，在启动后，直接 sh shutdown.sh 可以看出打出命令后，立马出现了CodeCache: size=245760Kb used=1585Kb max_used=1597Kb free=244174Kb

bounds [0x00007f2b25000000, 0x00007f2b25270000, 0x00007f2b34000000]
total_blobs=490 nmethods=229 adapters=177
compilation: enabled

一段话，之后tomcat就关闭了。

同时，这段话在catalina。out文件中也有。

这样我们就可以通过这种方式，来确定codecache的大小了。

需要注意的是：

只有在catalina.out文件中才有这个内容，而在日志中是没有这个内容的，即是将日志级别调成info亦是如此

```
#是无法打印出codecache使用情况的
kill -3
kill -9
#是可以打印出codecache使用情况的
kill -15
```

Java代码在执行时一旦被编译器编译为机器码，下一次执行的时候就会直接执行编译后的代码，也就是说，编译后的代码被缓存了起来。缓存编译后的机器码的内存区域就是codeCache。这是一块独立于java堆之外的内存区域。除了jit编译的代码之外，java所使用的本地方法代码（JNI）也会存在codeCache中。不同版本的jvm、不同的启动方式codeCache的默认大小也不同。
JVM一个有趣的，但往往被忽视的内存区域是“代码缓存”，它是用来存储已编译方法生成的本地代码。代码缓存确实很少引起性能问题，但是一旦发生其影响可能是毁灭性的。如果代码缓存被占满，JVM会打印出一条警告消息，并切换到interpreted-only 模式：JIT编译器被停用，字节码将不再会被编译成机器码。因此，应用程序将继续运行，但运行速度会降低一个数量级，直到有人注意到这个问题。就像其他内存区域一样，我们可以自定义代码缓存的大小。相关的参数是-XX:InitialCodeCacheSize 和-XX:ReservedCodeCacheSize，它们的参数和上面介绍的参数一样，都是字节值。

### UseCodeCacheFlushing

如果代码缓存不断增长，例如，因为热部署引起的内存泄漏，那么提高代码的缓存大小只会延缓其发生溢出。为了避免这种情况的发生，我们可以尝试一个有趣的新参数：当代码缓存被填满时让JVM放弃一些编译代码。通过使用-XX:+UseCodeCacheFlushing 这个参数，我们至少可以避免当代码缓存被填满的时候JVM切换到interpreted-only 模式。不过，我仍建议尽快解决代码缓存问题发生的根本原因，如找出内存泄漏并修复它。

### CodeCache清理

```
#默认为4,清理方法sweep_code_cache()的调用次数
-XX:NmethodSweepFraction
#（默认500K）停止JIT的阈值
-XX:CodeCacheMinimumFreeSpace=[g|m|k]
#（默认1500K）开始code cache清理的阈值
-XX:CodeCacheFlushingMinimumFreeSpace=1500K
# 指定两次CodeCache清理的最小时间间隔，默认30秒。
-XX:MinCodeCacheFlushingInterval
```

在CodeCache被清理的过程中，JIT的方法标记有2种，一种是not entrant，另外一种是zombie，在not entrant的时候，只是清除工作准备开始，可能还有执行栈会指向这个方法，还不能清除，一旦执行完成，没有人引用这个方法了，就标记为zombie。这个时候，就可以清除这个方法了。

```
-XX:InitialCodeCacheSize=32m
-XX:ReservedCodeCacheSize=256M
#sets this option to true.jdk8中，在jvm停止的时候打印出codeCache的使用情况。
#其中max_used就是在整个运行过程中codeCache的最大使用量。可以通过这个值来设置一个合理的codeCache大小，在保证应用正常运行的情况下减少内存使用。
-XX:+PrintCodeCache 
-XX:ReservedCodeCacheSize
-XX:+UseCodeCacheFlushing
-XX:NmethodSweepFraction
-XX:CodeCacheFlushingMinimumFreeSpace=1500k
-XX:MinCodeCacheFlushingInterval
#可以通过以下jvm参数开启分层编译模式：
-XX:+TieredCompilation
#jdk8中server模式默认采用分层编译方式，如果需要关闭分层编译，需要加上参数
-XX:-TieredCompilation
```

VM 版本和启动方式 默认 codeCache大小
32-bit client, Java 8 32 MB
32-bit server, java 8 *48M
32-bit server with Tiered Compilation, Java 8 240 MB
32-bit client, Java 7 32 MB
32-bit server, Java 7 48 MB
32-bit server with Tiered Compilation, Java 7 96 MB
64-bit server, Java 7 48 MB
64-bit server with Tiered Compilation, Java 7 96 MB
64-bit server, Java 8* 48M
64-bit server with Tiered Compilation, Java 8 240 MB

相关文献：

http://docs.oracle.com/javase/8/embedded/develop-apps-platforms/codecache.htm#A1099598
http://blog.csdn.net/dm_vincent/article/details/39529941
http://blog.csdn.net/yandaonan/article/details/50844806
http://wen-owen.iteye.com/blog/1473550
https://docs.oracle.com/javase/8/embedded/develop-apps-platforms/codecache.htm
[http://blog.leanote.com/post/zenglingshu/%E4%B8%80%E4%B8%AART%E4%B8%8B%E9%99%8D%E7%9A%84%E5%A5%87%E6%80%AACase%5B%E8%BD%AC%5D](http://blog.leanote.com/post/zenglingshu/一个RT下降的奇怪Case[转])
https://docs.oracle.com/javase/8/embedded/develop-apps-platforms/codecache.htm