主动关闭的一方在发送最后一个ACK后就会进入TIME_WAIT状态，并停留2MSL（Max Segment LifeTime）时间，这个是TCP/IP必不可少的。

TCP/IP的设计者如此设计，主要原因有两个：

1 防止上一次连接中的包迷路后重新出现，影响新的连接（经过2MSL时间后，上一次连接中所有重复的包都会消失）。

2 为了可靠地关闭TCP连接。主动关闭方发送的最后一个ACK（FIN）有可能会丢失，如果丢失，被动方会重新发FIN，这时如果主动方处于CLOSED状态，就会响应RST而不是ACK。所以主动方要处于TIME_WAIT状态，而不能是CLOSED状态。另外，TIME_WAIT并不会占用很大的资源，除非受到攻击

查看当前连接统计数：

```
netstat -n| awk '/^tcp/ {++S［$NF］} END {for(a in S) print a, S［a］}' 
```

CLOSED：无连接是活动的或正在进行中的。
LISTEN：服务器在等待进入呼叫。
SYN_RECV：一个连接请求已经到达，等待确认。
SYN_SENT：应用已经开始，打开一个连接。
ESTABLISHED：正常数据传输状态。
FIN_WAIT1：应用说它已经完成。
FIN_WAIT2：另一边已同意释放。
CLOSING：两边同时尝试关闭。
TIME_WAIT：另一边已初始化一个释放。
LAST_ACK：等待所有分组死掉。

修改Linux内核参数来减少Squid服务器的TIME_WAIT套接字数量

```
vim /etc/sysctl.conf
```

添加参数：

net.ipv4.tcp_syncookies=1 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookie来处理，可防范少量的SYN攻击。默认为0，表示关闭。

net.ipv4.tcp_tw_reuse=1 表示开启重用。允许将TIME-WAIT套接字重新用于新的TCP连接。默认为0，表示关闭。

net.ipv4.tcp_tw_recycle=1 表示开启TCP连接中TIME-WAIT套接字的快速回收。默认为0，表示关闭。

net.ipv4.tcp_fin_timeout=30 表示如果套接字由本端要求关闭，这个参数决定了它保持在FIN-WAIT-2状态的时间。

net.ipv4.tcp_keepalive_time=1200 表示当keepalive启用时，TCP发送keepalive消息的频度。默认是2小时，这里改为20分钟。

net.ipv4.ip_local_port_range=1024 65000 表示向外连接的端口范围。默认值很小：32768～61000，改为1024～65000。

net.ipv4.tcp_max_syn_backlog=8192 表示SYN队列的长度，默认为1024，加大队列长度为8192，可以容纳更多等待连接的网络连接数。

net.ipv4.tcp_max_tw_buckets=5000 表示系统同时保持TIME_WAIT套接字的最大数量，如果超过这个数 字，TIME_WAIT套接字将立刻被清除并打印警告信息。默认为180000，改为5000。

```
vim /etc/sysctl.conf

net.ipv4.tcp_syncookies=1
net.ipv4.tcp_tw_reuse=1
net.ipv4.tcp_tw_recycle=1
net.ipv4.tcp_fin_timeout=30
net.ipv4.tcp_keepalive_time=1200
net.ipv4.ip_local_port_range=1024 65000
net.ipv4.tcp_max_syn_backlog=8192
net.ipv4.tcp_max_tw_buckets=5000
```

对于Apache、Nginx等服务器，前面介绍的几个参 数已经可以很好地减少TIME_WAIT套接字数量，但是对于Squid来说，效果却不大。有了此参数就可以控制TIME_WAIT套接字的最大数量，避 免Squid服务器被大量的TIME_WAIT套接字拖死。

- 执行以下命令使内核配置立即生效：

```
/sbin/sysctl -p
```

Apache或Nginx等的Web服务器，或Nginx的反向代理，则只需要更改以下几项即可：

```
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.ip_local_port_range = 1024 65000
```

邮件服务器，则建议内核方案如下：

```
net.ipv4.tcp_fin_timeout = 30 
net.ipv4.tcp_keepalive_time = 300 
net.ipv4.tcp_tw_reuse = 1 
net.ipv4.tcp_tw_recycle = 1 
net.ipv4.ip_local_port_range = 5000 65000
kernel.shmmax = 134217728
```

行以下命令使内核配置立即生效：

```
/sbin/sysctl -p
```

-- 衣带渐宽终不悔，为伊消得人憔悴。---

分类: [linux](https://www.cnblogs.com/xkus/category/1096747.html)

标签: [CentOS TCP 连接内核参数优化](https://www.cnblogs.com/xkus/tag/CentOS TCP 连接内核参数优化/)