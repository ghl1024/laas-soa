[![img](聊聊jvm的Code Cache.assets/6619c4d0978378785a89c945d78266a4~300x300.image)](https://juejin.cn/user/2313028193225319)

[go4it ](https://juejin.cn/user/2313028193225319)[![lv-4](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMyIgaGVpZ2h0PSIxNCIgdmlld0JveD0iMCAwIDIzIDE0Ij4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZmlsbD0iIzM0RDE5QiIgZD0iTTMgMWgxN2EyIDIgMCAwIDEgMiAydjhhMiAyIDAgMCAxLTIgMkgzYTIgMiAwIDAgMS0yLTJWM2EyIDIgMCAwIDEgMi0yeiIvPgogICAgICAgIDxwYXRoIGZpbGw9IiNGRkYiIGQ9Ik0zIDRoMnY3SDN6TTggNmgybDIgNWgtMnoiLz4KICAgICAgICA8cGF0aCBmaWxsPSIjRkZGIiBkPSJNMTQgNmgtMmwtMiA1aDJ6TTMgOWg1djJIM3pNMTYuMzMzIDRMMTcgM3YzaC0yek0xNSA2aDJ2NGgtMnpNMTcgOGgxdjJoLTF6TTE3IDNoMXYyaC0xek0xOCAzaDJ2OGgtMnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==)](https://juejin.cn/book/5c90640c5188252d7941f5bb/section/5c9065385188252da6320022)

2019年03月30日 阅读 2780

关注

# 聊聊jvm的Code Cache

## 序

本文主要研究一下jvm的Code Cache

## Code Cache

JVM生成的native code存放的内存空间称之为Code Cache；JIT编译、JNI等都会编译代码到native code，其中JIT生成的native code占用了Code Cache的绝大部分空间

## 相关参数

### Codecache Size Options

- -XX:InitialCodeCacheSize

> 用于设置初始CodeCache大小

- -XX:ReservedCodeCacheSize

> 用于设置Reserved code cache的最大大小，通常默认是240M

- -XX:CodeCacheExpansionSize

> 用于设置code cache的expansion size，通常默认是64K

### Codecache Flush Options

- -XX:+UseCodeCacheFlushing

> 是否在code cache满的时候先尝试清理一下，如果还是不够用再关闭编译，默认开启

### Compilation Policy Options

- -XX:CompileThreshold

> 方法触发编译时的调用次数，默认是10000

- -XX:OnStackReplacePercentage

> 方法中循环执行部分代码的执行次数触发OSR编译时的阈值，默认是140

### Compilation Limit Options

- -XX:MaxInlineLevel

> 针对嵌套调用的最大内联深度，默认为9

- -XX:MaxInlineSize

> 方法可以被内联的最大bytecode大小，默认为35

- -XX:MinInliningThreshold

> 方法可以被内联的最小调用次数，默认为250

- -XX:+InlineSynchronizedMethods

> 是否允许内联synchronized methods，默认为true

### Diagnostic Options

- -XX:+PrintFlagsFinal(`默认没有启用`)

> 用于查看所有可设置的参数及最终值(`JDK 6 update 21开始才可以用`），默认是不包括diagnostic或experimental系的。如果要在-XX:+PrintFlagsFinal的输出里看到这两种参数的信息，分别需要显式指定-XX:+UnlockDiagnosticVMOptions / -XX:+UnlockExperimentalVMOptions(`-XX:+PrintCommandLineFlags 这个参数的作用是显示出VM初始化完毕后所有跟最初的默认值不同的参数及它们的值`)

- -XX:+PrintCodeCache(`默认没有启用`)

> -XX:+PrintCodeCache用于jvm关闭时输出code cache的使用情况

- -XX:+PrintCodeCacheOnCompilation(`默认没有启用`)

> 用于在方法每次被编译时输出code cache的使用情况

## 查看Code Cache的使用情况

### -XX:+PrintCodeCache

```
CodeHeap 'non-profiled nmethods': size=120032Kb used=2154Kb max_used=2160Kb free=117877Kb
 bounds [0x00000001178ea000, 0x0000000117b5a000, 0x000000011ee22000]
CodeHeap 'profiled nmethods': size=120028Kb used=10849Kb max_used=11005Kb free=109178Kb
 bounds [0x00000001103b3000, 0x0000000110e73000, 0x00000001178ea000]
CodeHeap 'non-nmethods': size=5700Kb used=1177Kb max_used=1239Kb free=4522Kb
 bounds [0x000000010fe22000, 0x0000000110092000, 0x00000001103b3000]
 total_blobs=5638 nmethods=4183 adapters=435
 compilation: enabled
              stopped_count=0, restarted_count=0
 full_count=0
复制代码
```

- jvm启动参数加上-XX:+PrintCodeCache，可以在jvm关闭时输出code cache的使用情况
- 这里分了non-profiled nmethods、profiled nmethods、non-nmethods三部分来展示
- 其中size就是限制的最大大小，used表示实际使用量，max_used就是使用大小的high water mark，free由size-used得来

### jcmd pid Compiler.codecache

```
/ # jcmd 1 Compiler.codecache
1:
CodeHeap 'non-profiled nmethods': size=120036Kb used=1582Kb max_used=1582Kb free=118453Kb
 bounds [0x00007f1e42226000, 0x00007f1e42496000, 0x00007f1e4975f000]
CodeHeap 'profiled nmethods': size=120032Kb used=9621Kb max_used=9621Kb free=110410Kb
 bounds [0x00007f1e3acee000, 0x00007f1e3b65e000, 0x00007f1e42226000]
CodeHeap 'non-nmethods': size=5692Kb used=1150Kb max_used=1198Kb free=4541Kb
 bounds [0x00007f1e3a75f000, 0x00007f1e3a9cf000, 0x00007f1e3acee000]
 total_blobs=5610 nmethods=4369 adapters=412
 compilation: enabled
              stopped_count=0, restarted_count=0
 full_count=0
复制代码
```

> 使用jcmd的Compiler.codecache也可以查看code cache的使用情况，输出跟-XX:+PrintCodeCache相同

### jcmd pid VM.native_memory

```
/ # jcmd 1 VM.native_memory
1:

Native Memory Tracking:

Total: reserved=1928023KB, committed=231182KB
-                 Java Heap (reserved=511488KB, committed=140288KB)
                            (mmap: reserved=511488KB, committed=140288KB)

-                     Class (reserved=1090832KB, committed=46608KB)
                            (classes #8218)
                            (  instance classes #7678, array classes #540)
                            (malloc=1296KB #19778)
                            (mmap: reserved=1089536KB, committed=45312KB)
                            (  Metadata:   )
                            (    reserved=40960KB, committed=39680KB)
                            (    used=38821KB)
                            (    free=859KB)
                            (    waste=0KB =0.00%)
                            (  Class space:)
                            (    reserved=1048576KB, committed=5632KB)
                            (    used=5190KB)
                            (    free=442KB)
                            (    waste=0KB =0.00%)

-                    Thread (reserved=37130KB, committed=2806KB)
                            (thread #36)
                            (stack: reserved=36961KB, committed=2636KB)
                            (malloc=127KB #189)
                            (arena=42KB #70)

-                      Code (reserved=248651KB, committed=15351KB)
                            (malloc=963KB #4600)
                            (mmap: reserved=247688KB, committed=14388KB)

-                        GC (reserved=21403KB, committed=7611KB)
                            (malloc=5419KB #9458)
                            (mmap: reserved=15984KB, committed=2192KB)

-                  Compiler (reserved=150KB, committed=150KB)
                            (malloc=20KB #447)
                            (arena=131KB #5)

-                  Internal (reserved=3744KB, committed=3744KB)
                            (malloc=1696KB #6416)
                            (mmap: reserved=2048KB, committed=2048KB)

-                     Other (reserved=24KB, committed=24KB)
                            (malloc=24KB #2)

-                    Symbol (reserved=10094KB, committed=10094KB)
                            (malloc=7305KB #219914)
                            (arena=2789KB #1)

-    Native Memory Tracking (reserved=4130KB, committed=4130KB)
                            (malloc=12KB #158)
                            (tracking overhead=4119KB)

-               Arena Chunk (reserved=177KB, committed=177KB)
                            (malloc=177KB)

-                   Logging (reserved=7KB, committed=7KB)
                            (malloc=7KB #264)

-                 Arguments (reserved=18KB, committed=18KB)
                            (malloc=18KB #500)

-                    Module (reserved=165KB, committed=165KB)
                            (malloc=165KB #1699)

-                 Safepoint (reserved=4KB, committed=4KB)
                            (mmap: reserved=4KB, committed=4KB)

-                   Unknown (reserved=4KB, committed=4KB)
                            (mmap: reserved=4KB, committed=4KB)
复制代码
```

> 使用jcmd的VM.native_memory也可以查看code cache的使用情况(`Code部分`)，Compiler部分为Memory tracking used by the compiler when generating code

### 使用MemoryPoolMXBean查看

```
    @Test
    public void testGetCodeCacheUsage(){
        ManagementFactory.getPlatformMXBeans(MemoryPoolMXBean.class)
                .stream()
                .filter(e -> MemoryType.NON_HEAP == e.getType())
                .filter(e -> e.getName().startsWith("CodeHeap"))
                .forEach(e -> {
                    LOGGER.info("name:{},info:{}",e.getName(),e.getUsage());
                });
    }
复制代码
```

> MemoryPoolMXBean包含了HEAP及NON_HEAP，其中code cache属于NON_HEAP，其输出如下：

```
12:21:10.728 [main] INFO com.example.CodeCacheTest - name:CodeHeap 'non-nmethods',info:init = 2555904(2496K) used = 1117696(1091K) committed = 2555904(2496K) max = 5836800(5700K)
12:21:10.743 [main] INFO com.example.CodeCacheTest - name:CodeHeap 'profiled nmethods',info:init = 2555904(2496K) used = 1543808(1507K) committed = 2555904(2496K) max = 122908672(120028K)
12:21:10.743 [main] INFO com.example.CodeCacheTest - name:CodeHeap 'non-profiled nmethods',info:init = 2555904(2496K) used = 319616(312K) committed = 2555904(2496K) max = 122912768(120032K)
复制代码
```

### spring boot应用查看

```
/ # curl -i "http://localhost:8080/actuator/metrics/jvm.memory.used?tag=area:nonheap"
HTTP/1.1 200
Content-Disposition: inline;filename=f.txt
Content-Type: application/vnd.spring-boot.actuator.v2+json;charset=UTF-8
Transfer-Encoding: chunked
Date: Sat, 30 Mar 2019 04:26:39 GMT

{"name":"jvm.memory.used","description":"The amount of used memory","baseUnit":"bytes","measurements":[{"statistic":"VALUE","value":6.5295408E7}],"availableTags":[{"tag":"id","values":["CodeHeap 'non-profiled nmethods'","CodeHeap 'profiled nmethods'","Compressed Class Space","Metaspace","CodeHeap 'non-nmethods'"]}]}

/ # curl -i "http://localhost:8080/actuator/metrics/jvm.memory.used?tag=area:nonheap&tag=id:CodeHeap%20%27non-profiled
%20nmethods%27"
HTTP/1.1 200
Content-Disposition: inline;filename=f.txt
Content-Type: application/vnd.spring-boot.actuator.v2+json;charset=UTF-8
Transfer-Encoding: chunked
Date: Sat, 30 Mar 2019 04:24:58 GMT

{"name":"jvm.memory.used","description":"The amount of used memory","baseUnit":"bytes","measurements":[{"statistic":"VALUE","value":1592448.0}],"availableTags":[]}
复制代码
```

> springboot使用micrometer，通过/actuator/metrics接口提供相关指标查询功能，其中code cache在jvm.memory.used这个metric中 它是基于MemoryPoolMXBean来实现的，具体详见micrometer-core-1.1.3-sources.jar!/io/micrometer/core/instrument/binder/jvm/JvmMemoryMetrics.java

## 小结

- JVM生成的native code存放的内存空间称之为Code Cache；JIT编译、JNI等都会编译代码到native code，其中JIT生成的native code占用了Code Cache的绝大部分空间
- -XX:ReservedCodeCacheSize用于设置Reserved code cache的最大大小，通常默认是240M；对于有些应用来说240M可能太大，code cache可能都填不满，相当于unconstrained，此时JIT就会继续编译任何它认为可以编译的code
- 查看Code Cache的内存使用情况有好几种方法：
  - jvm启动参数加上-XX:+PrintCodeCache，可以在jvm关闭时输出code cache的使用情况
  - 使用jcmd的Compiler.codecache，其输出跟-XX:+PrintCodeCache相同；
  - 使用jcmd的VM.native_memory也可以查看code cache的使用情况(`Code部分`)
  - 使用JMX来获取NON_HEAP类型中的name为CodeHeap开头的MemoryPoolMXBean可以得到code cache的使用情况
  - 如果是springboot应用，它使用micrometer，通过/actuator/metrics接口提供相关指标查询功能，其中code cache在jvm.memory.used这个metric中

## doc

- [15 Codecache Tuning](https://docs.oracle.com/javase/8/embedded/develop-apps-platforms/codecache.htm)
- [JVM的编译策略](https://segmentfault.com/a/1190000004649033)
- [What are ReservedCodeCacheSize and InitialCodeCacheSize?](https://stackoverflow.com/questions/7513185/what-are-reservedcodecachesize-and-initialcodecachesize)
- [Why does the JVM have a maximum inline depth?](https://stackoverflow.com/questions/32503669/why-does-the-jvm-have-a-maximum-inline-depth/)
- [Code Cache满导致应用性能降低](https://juejin.im/post/6844903601786060808)