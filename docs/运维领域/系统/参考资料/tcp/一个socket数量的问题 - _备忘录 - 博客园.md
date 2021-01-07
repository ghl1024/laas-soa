## [一个socket数量的问题](https://www.cnblogs.com/10087622blog/p/10723265.html)

最近遇到一个问题，从业务上出现ftp异常：

```
ftp 172.**.**.**
ftp: connect: Cannot assign requested address
```

这台服务器上的socket统计如下：

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
ss -s
Total: 42724 (kernel 42982)
TCP:   41047 (estab 74, closed 40940, orphaned 0, synrecv 0, timewait 3/0), ports 12036-----这个是cat /proc/slabinfo |grep -i tcp_bind_bucket 的inuse那列

Transport Total     IP        IPv6
*         42982     -         -
RAW       2         2         0
UDP       389       387       2
TCP       107       105       2
INET      498       494       4
FRAG      0         0         0
```

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

可以看到，closed的值很高，ports也很高，占用了12036个端口，

ss -s执行的源代码是：

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
int print_summary(void)
{
    struct sockstat s;
    struct snmpstat sn;

    if (get_sockstat(&s) < 0)---------------读取/proc/net/sockstat
        perror("ss: get_sockstat");
    if (get_snmp_int("Tcp:", "CurrEstab", &sn.tcp_estab) < 0)
        perror("ss: get_snmpstat");

    printf("Total: %d (kernel %d)\n", s.socks, slabstat.socks);

    printf("TCP:   %d (estab %d, closed %d, orphaned %d, synrecv %d, timewait %d/%d), ports %d\n",
           s.tcp_total + slabstat.tcp_syns + s.tcp_tws,
           sn.tcp_estab,
           s.tcp_total - (s.tcp4_hashed+s.tcp6_hashed-s.tcp_tws),
           s.tcp_orphans,
           slabstat.tcp_syns,
           s.tcp_tws, slabstat.tcp_tws,
           slabstat.tcp_ports-----------这个就是slabinfo中的tcp_bind_bucket 的activeobj 
           );

    printf("\n");
    printf("Transport Total     IP        IPv6\n");
    printf("*      %-9d %-9s %-9s\n", slabstat.socks, "-", "-");
    printf("RAW      %-9d %-9d %-9d\n", s.raw4+s.raw6, s.raw4, s.raw6);
    printf("UDP      %-9d %-9d %-9d\n", s.udp4+s.udp6, s.udp4, s.udp6);
    printf("TCP      %-9d %-9d %-9d\n", s.tcp4_hashed+s.tcp6_hashed, s.tcp4_hashed, s.tcp6_hashed);
    printf("INET      %-9d %-9d %-9d\n",
           s.raw4+s.udp4+s.tcp4_hashed+
           s.raw6+s.udp6+s.tcp6_hashed,
           s.raw4+s.udp4+s.tcp4_hashed,
           s.raw6+s.udp6+s.tcp6_hashed);
    printf("FRAG      %-9d %-9d %-9d\n", s.frag4+s.frag6, s.frag4, s.frag6);

    printf("\n");

    return 0;
}
```

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

可以看到，ss -s 关于ipv4的输出是通过读取/proc/net/sockstat 的内容，

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
cat /proc/net/sockstat
sockets: used 42639
TCP: inuse 81 orphan 0 tw 6 alloc 41019 mem 286
UDP: inuse 333 mem 63
UDPLITE: inuse 0
RAW: inuse 2
FRAG: inuse 0 memory 0
```

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

和前面数据有些相差是因为不是严格一个时间点取的，同时，alloc是比较接近closed的，（注意ss中关于closed的算法，要获取精确值，应该关注 /proc/net/sockstat

中的alloc的值）

而正常的设备大概是：

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
cat /proc/net/sockstat
sockets: used 6772
TCP: inuse 1813 orphan 3 tw 34 alloc 1815 mem 32
UDP: inuse 3893 mem 1895
UDPLITE: inuse 0
RAW: inuse 1
FRAG: inuse 0 memory 0
```

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

可以明显看到alloc的数量相比正常设备很高，而且不是属于inuse状态。

```
ss -t -a |wc -l 
63
```

所以这个被ss列入到close状态的大多数就是alloc状态，closed被展示为： s.tcp_total - (s.tcp4_hashed+s.tcp6_hashed-s.tcp_tws),

而s.tcp_total格式化为：

```
    else if (strcmp(id, "TCP:") == 0)
        sscanf(rem, "%*s%d%*s%d%*s%d%*s%d%*s%d",
         &s->tcp4_hashed,---------这个就是inuse那列
         &s->tcp_orphans, &s->tcp_tws, &s->tcp_total, &s->tcp_mem);-------tcp_mem就是tcp申请的内存，内核中的tcp_memory_allocated变量
```

其实就是：

```
TCP: inuse 81 orphan 0 tw 6 alloc 41019 mem 286

中的alloc那列，tcp_total里面就是alloc的tcp socket总数，但是inuse的又远远低于alloc状态，这个是为啥？
```

而对应的closed这项为：

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
    printf("TCP:   %d (estab %d, closed %d, orphaned %d, synrecv %d, timewait %d/%d), ports %d\n",
           s.tcp_total + slabstat.tcp_syns + s.tcp_tws,
           sn.tcp_estab,
           s.tcp_total - (s.tcp4_hashed+s.tcp6_hashed-s.tcp_tws),---------这项closed就是alloc的tcp socket加上timewait 然后减去inused
           s.tcp_orphans,
           slabstat.tcp_syns,
           s.tcp_tws, slabstat.tcp_tws,
           slabstat.tcp_ports
           );
```

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

 

按照内核代码，alloc的数量也就是：

```
sockets = percpu_counter_sum_positive(&tcp_sockets_allocated);
```

这个值在 tcp_v4_init_sock和tcp sock的 sk_clone函数 中增加，并在销毁tcp socket的 tcp_v4_destroy_sock函数中减少，两者处于配对的关系。

写了一个测试程序，才确认，ss -s显示closed的状态的socket，其实就是socket系统调用之后，还没有使用的socket，没有建联，也没侦听，也没关闭。想起tcp的状态变迁图，确实一开始的状态是closed，走了弯路，因为一开始排查，以为是跟close-wait相关，结果使用 ss -o state close-wait 看了发现数量也不对，才知道查错了方向。

回到一开始的业务本身，Cannot assign requested address 确定是绑定端口失败，端口不够用了。

而该设备上配置的ip端口范围是：

```
sysctl -a |grep port_range
net.ipv4.ip_local_port_range = 50000    62000
```

也就是12000个，当ports占用之后，端口就不够了，而这些端口占用，并没有实际链接，也就是closed状态的4万多个socket中，有接近12000个端口被占用且不提供服务（业务代码bug）。

其实它想占那么多端口的，4万多个tcp的socket，有30000多bind 端口失败。所以才出现了closed 4万多，而ports为12036的状态，当然，多出来的36个，我还没来得及分析，业务进程就重启了，所以看不到具体占用的了。

最近再次遇到了这个问题：

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
cat /proc/net/sockstat
sockets: used 2649
TCP: inuse 1800 orphan 171 tw 4667 alloc 64572 mem 419992
UDP: inuse 34 mem 33
UDPLITE: inuse 0
RAW: inuse 0
FRAG: inuse 0 memory 0
ss -s
Total: 2641 (kernel 3246)
TCP:   69562 (estab 1294, closed 67758, orphaned 168, synrecv 0, timewait 5000/0), ports 4988

Transport Total     IP        IPv6
*         3246      -         -
RAW       0         0         0
UDP       34        34        0
TCP       1804      1789      15
INET      1838      1823      15
FRAG      0         0         0
```

[![复制代码](一个socket数量的问题 - _备忘录 - 博客园.assets/copycode.gif)](javascript:void(0);)

 

为了避免后来人犯同样的错，简单记录之。

 

水平有限，如果有错误，请帮忙提醒我。如果您觉得本文对您有帮助，可以点击下面的 推荐 支持一下我。版权所有，需要转发请带上本文源地址，博客一直在更新，欢迎 关注 。

分类: [网络相关](https://www.cnblogs.com/10087622blog/category/1088613.html)