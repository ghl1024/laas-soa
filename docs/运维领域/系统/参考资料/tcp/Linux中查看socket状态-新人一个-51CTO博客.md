# Linux中查看socket状态

[![img](Linux中查看socket状态-新人一个-51CTO博客.assets/wKioL1YI-anBR2mtAABNsyjgyyY514_middle.jpg)](https://blog.51cto.com/welcomeweb)

[憬薇](https://blog.51cto.com/welcomeweb)关注0人评论[5402人阅读](javascript:;)[2017-10-23 21:03:44](javascript:;)

Linux中查看socket状态：
cat /proc/net/sockstat #（这个是ipv4的）

sockets: used 137 TCP: inuse 49 orphan 0 tw 3272 alloc 52 mem 46UDP: inuse 1 mem 0RAW: inuse 0 FRAG: inuse 0 memory 0

说明：
sockets: used：已使用的所有协议套接字总量
TCP: inuse：正在使用（正在侦听）的TCP套接字数量。其值≤ netstat –lnt | grep ^tcp | wc –l
TCP: orphan：无主（不属于任何进程）的TCP连接数（无用、待销毁的TCP socket数）
TCP: tw：等待关闭的TCP连接数。其值等于netstat –ant | grep TIME_WAIT | wc –l
TCP：alloc(allocated)：已分配（已建立、已申请到sk_buff）的TCP套接字数量。其值等于netstat –ant | grep ^tcp | wc –l
TCP：mem：套接字缓冲区使用量（单位不详。用scp实测，速度在4803.9kB/s时：其值=11，netstat –ant 中相应的22端口的Recv-Q＝0，Send-Q≈400）
UDP：inuse：正在使用的UDP套接字数量
RAW：
FRAG：使用的IP段数量

IPv6请看：cat /proc/net/sockstat6

TCP6: inuse 3UDP6: inuse 0RAW6: inuse 0 FRAG6: inuse 0 memory 0

通过这些值，可以很容易计算出当前的tcp请求数，然后做相关的监控。



©著作权归作者所有：来自51CTO博客作者憬薇的原创作品，如需转载，请与作者联系，否则将追究法律责任

[监控](https://blog.51cto.com/search/result?q=+监控)[sockt](https://blog.51cto.com/search/result?q=sockt)[状态查看](https://blog.51cto.com/search/result?q=状态查看)