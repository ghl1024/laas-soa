# [Pod中进程内存缓存问题](https://www.cnblogs.com/orchidzjl/p/11806718.html)

### 背景

环境：openshift3.11

开发反映部署在容器中的java应用内存持续增长，只升不降，具体为：

java应用部署在容器中，配置的jvm参数为-Xms1024m -Xmx1024m，容器memory request为1G， memory limit为4G，通过openshift的Pod metrics监控发现，应用消耗内存达到99%（只剩下3M），但是Pod处于Running状态，没有发生OOM，Pod容器java进程正常接收出了请求。增加容器memory limit至8G，内存依然消耗至99%。

 

### 排查过程

容器为单进程模型，其中只运行了一个java进程。通过docker stats containerId查看容器消耗的内存为1.735g，通过top命令查看到得java进程的res值为1.7g

查看容器的内存使用信息：

```
#进入cgroup工作目录``cd` `/sys/fs/cgroup/memory/` `#查找容器id``docker ``ps` `| ``grep` `{name}` `#通过容器id查找Pod slice目录，如下``systemd-cgls | ``grep` `-C3 contianerId``│  └─kubepods-burstable-pod2df5422b_fed3_11e9_be3c_5254008ade6c.slice``│   ├─docker-b9f2ce762cdc8435167bff21eb2cd31d9e1214ad75f2326bffba5e2f1d46422d.scope ``#业务容器``│   │ ├─32014 tini -- ``/run``.sh``│   │ └─32584 java -jar ``/deployments/test``.jar``│   └─docker-77fde00b840ba03d4d2d52dd0e08ff2a2db7c85e0233bf2847aaa8fa2250b657.scope ``#根容器``│    └─28520 ``/usr/bin/pod` `#查看内存信息相关目录如下``cat` `/sys/fs/cgroup/memory/kubepods``.slice``/kubepods-burstable``.slice``/kubepods-burstable-pod2df5422b_fed3_11e9_be3c_5254008ade6c``.slice``/docker-b9f2ce762cdc8435167bff21eb2cd31d9e1214ad75f2326bffba5e2f1d46422d``.scope``/memory``.usage_in_bytes` `cat` `/sys/fs/cgroup/memory/kubepods``.slice``/kubepods-burstable``.slice``/kubepods-burstable-pod2df5422b_fed3_11e9_be3c_5254008ade6c``.slice``/docker-b9f2ce762cdc8435167bff21eb2cd31d9e1214ad75f2326bffba5e2f1d46422d``.scope``/memory``.stat
memory.usage_in_bytes文件中的值即为metrics监控中的值
memory.stat文件中cahce字段的值就是这个容器用于cache的内存
```

 

看来metrics监控中的值就是取自memory.usage_in_bytes，而这个值是包含memory.stat中的cache的

那应用为什么会消耗大量cache？

```
#查看java应用的log4j2配置，发现其中配置了最大保留两个归档文件，每个归档文件大小为2GB，也就是说日志量最大为6GB左右，查看pod中的日志也确实达到了最大的量。做以下步骤验证``1.取消日志输出到文件，metrics监控到得值与dokcer stats或``top``中的值相近``2.配置最大保留两个归档文件，每个归档文件大小为100M，查看memory.stat中的cache值为350M左右` `也就是说log42配置的日志输出到文件会缓存到内存
```

 

这个缓存对容器有什么影响吗？

```
#是没有任何影响的，java进程只消耗内存1.7G左右，剩余的内存是被log4j用于缓存以充分利用内存提高读写效率，当java进程实例消耗内存增加，cache也会相应的释放，这应该是linux的内存机制决定的Linux has this basic rule: a page of free RAM is wasted RAM. RAM is used for a lot more than just user application data. It also stores data for the kernel itself and, most importantly, can mirror data stored on the disk for super-fast access, this is reported usually as “buffers/cache”, “disk cache” or “cached” by top. Cached memory is essentially free, in that it can be replaced quickly if a running (or newly starting) program needs the memory.
```

 

所以在prometheus监控告警中也应该去掉cache这一部分

 

参考：

http://trustmeiamadeveloper.com/2016/03/18/where-is-my-memory-java/