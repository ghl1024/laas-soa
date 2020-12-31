# [docker容器内存占用 之 系统cache,docker下java的内存该如何配置--temp](https://www.cnblogs.com/duanxz/p/10247494.html)

缘起： 
监控（docker stats）显示容器内存被用完了，进入容器瞅了瞅，没有发现使用内存多的进程，使用awk等工具把容器所有进程使用的内存加起来看看，距离用完还远了去了，何故？

分析：

该不会docker stats计算错误？

进入/sys/fs/cgroup/memory/docker/xxxxx/ 查看memory.usage ，确认计算没有错误

我们知道，系统内存会有一部分被buffer、cache之类占用，linux也会把这部分内存算到已使用，对于容器来讲，也应该存在此“问题”，而且非常有可能linux会把某容器引发的cache占用算到容器占用的内存上；验证很简单，进容器dd一个大文件就知道了：

dd 大文件后，docker stat显示已用内存变多

宿主机上： echo 3 > /proc/sys/vm/drop_caches 后，docker stat显示已用内存变少

至此，原因查明

问题：

对于宿主机来讲，计算内存占用时，可以拿已用内存减去cache/buffer ，那么对于容器来讲，如果减去容器部分的cache/buffer 呢？如果不减去，也会造成误报警

测试发现： dd 产生的文件cache占用的内存会计算到 inactive_file 的头上

源地址：https://phpor.net/blog/post/4854

# 在docker中使用java的内存情况

# 前言

微服务和docker的结合应该是现在服务端的主流技术，随着springboot的出现，有很多公司已经把微服务迁移到了docker容器中，我们也不甘寂寞，也尝试了一把新技术，把以前的整体服务进行拆分以后，也全部上到了docker容器中。

# 问题

很久之前，业务部门利用springboot开发好一个app以后，就可以通过`java -jar` 的命令把程序丢给docker，然后在容器中启动起来，也不管到底系统给这个应用分配了多少内存。

后来由于java默认使用的内存是docker实体机器1/4的内存，导致部署了很多应用以后，经常出现内存不足的情况，然后公司要求应用在启动的时候通过jvm的启动参数来限制java使用的内存来缓解内存消耗过快的问题。

再后来，我们的docker平台进行了升级， 有了可以让应用限制cpu个数和mem大小的参数设置，后面应用方把app的 `-Xmx`和docker的内存大小设置成同样大小， 比如2g。后面发现跑了一段时间以后，应用经常出现oom的情况，而被杀掉。

因为java使用的内存不仅仅是 `-Xmx`设置的大小， `-Xmx`设置的大小只是java进程堆的最大占用内存，

# 原因

为什么会出现上面这个问题呢？通过监控系统可以知道，docker获得的mem_usage的大小是从外部得到的java进程的内存大小，不仅仅是 `-Xmx`设置的大小，如果 `-Xmx`和docker分配的内存一致的话，由于java应用其他的地方还要占用不少的内存，导致还没有到达 `-Xmx`的时候就没有可以用的内存了，所以被docker容器给干掉了，从而出现了oom的情况。

那么java程序启动的时候需要哪些方面的内存呢？

1. java程序的堆内存，最大就是 `-Xmx`设置的这个值
2. Garbage collection在垃圾回收的时候使用的内存
3. JIT optimization使用的内存
4. java程序的Off-heap所使用的内存
5. java程序的Metaspace所使用的内存
6. JNI Code所占用的内存
7. jvm启动的时候所占用的内存。

如何大体估算java进程使用的内存呢?

```
Max memory = [-Xmx] + [-XX:MaxPermSize] + number_of_threads * [-Xss]
```

上面的公式大体得到了内存的占用，但是不是全部占用，网上有一些人做了一些试验，有两篇比较好的介绍文章:
[https://plumbr.eu/blog/memory-leaks/why-does-my-java-process-consume-more-memory-than-xmx](https://plumbr.eu/blog/memory-leaks/why-does-my-java-process-consume-more-memory-than-xmx)
和
[http://trustmeiamadeveloper.com/2016/03/18/where-is-my-memory-java/](https://link.jianshu.com/?t=http://trustmeiamadeveloper.com/2016/03/18/where-is-my-memory-java/)

所以猜测在设置jvm启动参数的时候 `-Xmx`的这个值一般要小于docker限制内存数，个人觉得 `-Xmx`:`docker`的比例为 `4/5 - 3/4`，

目前正在试验和观察，这里仅仅保存一下记录，以免忘记。