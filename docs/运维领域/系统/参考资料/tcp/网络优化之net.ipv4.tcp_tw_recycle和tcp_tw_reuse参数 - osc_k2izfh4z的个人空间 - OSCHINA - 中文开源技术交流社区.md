# [网络优化之net.ipv4.tcp_tw_recycle和tcp_tw_reuse参数](https://my.oschina.net/u/4302617/blog/3543377)

[osc_k2izfh4z](https://my.oschina.net/u/4302617)

2019/05/10 00:29

阅读数 4.5K

[Linux基金会Kubernetes安全专家认证上线，预约享早鸟折扣，最后三天！>>>![img](网络优化之net.ipv4.tcp_tw_recycle和tcp_tw_reuse参数 - osc_k2izfh4z的个人空间 - OSCHINA - 中文开源技术交流社区.assets/hot3.png)](https://training.linuxfoundation.cn/activities/22?from=oschina)

 

linux TIME_WAIT 相关参数:

```
net.ipv4.tcp_tw_reuse = 0    表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭
net.ipv4.tcp_tw_recycle = 0  表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭
net.ipv4.tcp_fin_timeout = 60  表示如果套接字由本端要求关闭，这个参数决定了它保持在FIN-WAIT-2状态的时间（可改为30，一般来说FIN-WAIT-2的连接也极少）
```

注意：

\- 不像Windows 可以修改注册表修改2MSL 的值，linux 是没有办法修改MSL的，tcp_fin_timeout 不是2MSL 而是Fin-WAIT-2状态.

\- tcp_tw_reuse 和SO_REUSEADDR 是两个完全不同的东西

 

查看参数：

cat/proc/sys/net/ipv4/tcp_tw_recycle （表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭）

*cat /proc/sys/net/ipv4/tcp_tw_reuse

修改参数：
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/tcp_tw_reuse'
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/tcp_tw_recycle'*

\1. tw_reuse，tw_recycle 必须在客户端和服务端timestamps 开启时才管用（默认打开）

\2. tw_reuse 只对客户端起作用，开启后客户端在1s内回收

\3. tw_recycle 对客户端和服务器同时起作用，开启后在 3.5*RTO 内回收，RTO 200ms~ 120s 具体时间视网络状况。

　　内网状况比tw_reuse 稍快，公网尤其移动网络大多要比tw_reuse 慢，优点就是能够回收服务端的TIME_WAIT数量

 



## 对于客户端

\1. 作为客户端因为有端口65535问题，TIME_OUT过多直接影响处理能力，打开tw_reuse 即可解决，不建议同时打开tw_recycle，帮助不大。

\2. tw_reuse 帮助客户端1s完成连接回收，基本可实现单机6w/s请求，需要再高就增加IP数量吧。

\3. 如果内网压测场景，且客户端不需要接收连接，同时tw_recycle 会有一点点好处。

\4. 业务上也可以设计由服务端主动关闭连接

 



## 对于服务端

\1. 打开tw_reuse无效

\2. 线上环境 tw_recycle 不要打开

  服务器处于NAT 负载后，或者客户端处于NAT后（这是一定的事情，基本公司家庭网络都走NAT）；

　公网服务打开就可能造成部分连接失败，内网的话到时可以视情况打开；

  像我所在公司对外服务都放在负载后面，负载会把timestamp 都给清空，好吧，就算你打开也不起作用。

\3. 服务器TIME_WAIT 高怎么办

  不像客户端有端口限制，处理大量TIME_WAIT Linux已经优化很好了，每个处于TIME_WAIT 状态下连接内存消耗很少，

而且也能通过tcp_max_tw_buckets = *262144* 配置最大上限，现代机器一般也不缺这点内存。

  下面像我们一台每秒峰值1w请求的http 短连接服务，长期处于tw_buckets 溢出状态，

tw_socket_TCP 占用70M, 因为业务简单服务占用CPU 200% 运行很稳定。

![复制代码](网络优化之net.ipv4.tcp_tw_recycle和tcp_tw_reuse参数 - osc_k2izfh4z的个人空间 - OSCHINA - 中文开源技术交流社区.assets/2ea8d51f10fae8dc016594e3fc8b48e7817.gif)

![复制代码](网络优化之net.ipv4.tcp_tw_recycle和tcp_tw_reuse参数 - osc_k2izfh4z的个人空间 - OSCHINA - 中文开源技术交流社区.assets/3d792692a3757517b4f023d6a3a9271bbf2.gif)

slabtop

262230 251461  95%   0.25K  17482    15   69928K tw_sock_TCP

```
ss -s
Total: 259 (kernel 494)
TCP:   262419 (estab 113, closed 262143, orphaned 156, synrecv 0, timewait 262143/0), ports 80

Transport Total     IP        IPv6
*         494       -         -        
RAW       1         1         0        
UDP       0         0         0        
TCP       276       276       0        
INET      277       277       0        
FRAG      0         0         0
```

![复制代码](网络优化之net.ipv4.tcp_tw_recycle和tcp_tw_reuse参数 - osc_k2izfh4z的个人空间 - OSCHINA - 中文开源技术交流社区.assets/e7381d2bd4b58ac3dc0cda5cf756367d502.gif)

![复制代码](网络优化之net.ipv4.tcp_tw_recycle和tcp_tw_reuse参数 - osc_k2izfh4z的个人空间 - OSCHINA - 中文开源技术交流社区.assets/674b84bde17af7401f5a84c00be1b959dc0.gif)

唯一不爽的就是：

系统日志中overflow 错误一直再刷屏，也许该buckets 调大一下了

TCP: time wait bucket table overflow
TCP: time wait bucket table overflow
TCP: time wait bucket table overflow
TCP: time wait bucket table overflow
TCP: time wait bucket table overflow

 

\5. 业务上也可以设计由客户端主动关闭连接

 



## 原理分析

 \1. MSL 由来

　　发起连接关闭方回复最后一个fin 的ack，为避免对方ack 收不到、重发的或还在中间路由上的fin 把新连接给干掉了，等个2MSL，4min。

　　也就是连接有谁关闭的那一方有time_wait问题，被关那方无此问题。

\2. reuse、recycle

   通过timestamp的递增性来区分是否新连接，新连接的timestamp更大，那么小的timestamp的fin 就不会fin掉新连接。

\3. reuse

   通过timestamp 递增性，客户端、服务器能够处理outofbind fin包

\4. recycle

  对于服务端，同一个src ip，可能会是NAT后很多机器，这些机器timestamp递增性无可保证，服务器会拒绝非递增请求连接。

 

 细节之处还得好好阅读tcp 协议栈源码了

【案例分析1】

最近发现几个监控用的脚本在连接监控数据库的时候偶尔会连不上，报错：
 Couldn't connect to host:3306/tcp: IO::Socket::INET: connect: Cannot assign requested address
查看了一下发现系统中存在大量处于TIME_WAIT状态的tcp端口
$netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'
TIME_WAIT 50013
ESTABLISHED 27
SYN_RECV 1
由于要监控的主机太多，监控的agent可能在短时间内创建大量连接到监控数据库(MySQL)并释放造成的。在网上查阅了一些tcp参数的相关资料，最后通过修改了几个系统内核的tcp参数缓解了该问题：
\#vi /etc/sysctl.conf

net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1

\#sysctl -p
其中：
net.ipv4.tcp_tw_reuse = 1 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
net.ipv4.tcp_tw_recycle = 1 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭。
修改完成并生效后，系统中处于TIME_WAIT状态的tcp端口数量迅速下降到100左右：
$netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'
TIME_WAIT 82
ESTABLISHED 36
简单记录于此，备忘。

 

【案例分析2】

网上的帖子，大多都写开启net.ipv4.tcp_tw_recycle这个开关，可以快速回收处于TIME_WAIT状态的socket（针对Server端而言）。


而实际上，这个开关，需要net.ipv4.tcp_timestamps（默认开启的）这个开关开启才有效果。
更不为提到却很重要的一个信息是：当tcp_tw_recycle开启时（tcp_timestamps同时开启，快速回收socket的效果达到），对于位于NAT设备后面的Client来说，是一场灾难——会导到NAT设备后面的Client连接Server不稳定（有的Client能连接server，有的Client不能连接server）。也就是说，tcp_tw_recycle这个功能，是为“内部网络”（网络环境自己可控——不存在NAT的情况）设计的，对于公网，不宜使用。

通常，“回收”TIME_WAIT状态的socket是因为“无法主动连接远端”，因为无可用的端口，而不应该是要回收内存（没有必要）。即，需求是“Client”的需求，Server会有“端口不够用”的问题吗？除非是前端机，需要大量的连接后端服务——即充当着Client的角色。
正确的解决这个总是办法应该是：
net.ipv4.ip_local_port_range = 9000 6553 #默认值范围较小
net.ipv4.tcp_max_tw_buckets = 10000 #默认值较小，还可适当调小
net.ipv4.tcp_tw_reuse = 1 #
net.ipv4.tcp_fin_timeout = 10 #
\---------------------
作者：天府云创
来源：CSDN
原文：https://blog.csdn.net/enweitech/article/details/79261439
版权声明：本文为博主原创文章，转载请附上博文链接！

[buckets](https://www.oschina.net/p/buckets)[linux](https://www.oschina.net/p/linux)[inet](https://www.oschina.net/p/inet)[bash](https://www.oschina.net/p/bash)

本文转载自：https://www.cnblogs.com/ppp1314520818/p/10842037.html