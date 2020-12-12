# Spring Boot 内嵌容器Undertow参数设置

![img](Spring Boot 内嵌容器Undertow参数设置_Lovnx-CSDN博客_undertow配置详解.assets/original.png)

[Lovnx](https://lovnx.blog.csdn.net/) 2017-12-26 20:50:15 ![img](Spring Boot 内嵌容器Undertow参数设置_Lovnx-CSDN博客_undertow配置详解.assets/articleReadEyes.png) 27483 ![img](Spring Boot 内嵌容器Undertow参数设置_Lovnx-CSDN博客_undertow配置详解.assets/tobarCollect.png) 收藏 8

分类专栏： [Spring Boot](https://blog.csdn.net/rickiyeat/category_6788109.html) [Spring Cloud](https://blog.csdn.net/rickiyeat/category_6751201.html) 文章标签： [undertow](https://www.csdn.net/tags/MtjaMg4sMjYxNzItYmxvZwO0O0OO0O0O.html)

版权

**配置项：**

```
# 设置IO线程数, 它主要执行非阻塞的任务,它们会负责多个连接, 默认设置每个CPU核心一个线程
# 不要设置过大，如果过大，启动项目会报错：打开文件数过多

server.undertow.io-threads=16

# 阻塞任务线程池, 当执行类似servlet请求阻塞IO操作, undertow会从这个线程池中取得线程
# 它的值设置取决于系统线程执行任务的阻塞系数，默认值是IO线程数*8

server.undertow.worker-threads=256

# 以下的配置会影响buffer,这些buffer会用于服务器连接的IO操作,有点类似netty的池化内存管理
# 每块buffer的空间大小,越小的空间被利用越充分，不要设置太大，以免影响其他应用，合适即可

server.undertow.buffer-size=1024

# 每个区分配的buffer数量 , 所以pool的大小是buffer-size * buffers-per-region

server.undertow.buffers-per-region=1024

# 是否分配的直接内存(NIO直接分配的堆外内存)

server.undertow.direct-buffers=true12345678910111213141516171819202122
```

**来看看源代码：**

https://github.com/undertow-io/undertow/blob/master/core/src/main/java/io/undertow/Undertow.java

```
ioThreads = Math.max(Runtime.getRuntime().availableProcessors(), 2);

workerThreads = ioThreads * 8;

//smaller than 64mb of ram we use 512b buffers
if (maxMemory < 64 * 1024 * 1024) {
    //use 512b buffers
    directBuffers = false;
    bufferSize = 512;
} else if (maxMemory < 128 * 1024 * 1024) {
    //use 1k buffers
    directBuffers = true;
    bufferSize = 1024;
} else {
    //use 16k buffers for best performance
    //as 16k is generally the max amount of data that can be sent in a single write() call
    directBuffers = true;
    bufferSize = 1024 * 16 - 20; //the 20 is to allow some space for protocol headers, see UNDERTOW-1209
}12345678910111213141516171819
```

很显然，Undertow认为它的运用场景是在IO密集型的系统应用中，并且认为多核机器是一个比较容易满足的点，Undertow初始化假想应用的阻塞系数在0.8~0.9之间，所以阻塞线程数直接乘了个8，当然，如果对应用较精确的估测阻塞系数，可以配置上去，