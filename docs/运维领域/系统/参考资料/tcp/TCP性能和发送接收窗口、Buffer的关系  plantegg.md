## TCP性能和发送接收窗口、Buffer的关系

 发表于 2019-09-28 | 分类于 [TCP ](https://plantegg.github.io/categories/TCP/)| | 次

# 前言

本文希望解析清楚，当我们在代码中写下 socket.setSendBufferSize 和 sysctl 看到的rmem/wmem系统参数以及最终我们在TCP常常谈到的接收发送窗口的关系，以及他们怎样影响TCP传输的性能，同时如何通过图形来展示哪里是传输瓶颈。

拥塞窗口相关文章比较多，他们跟带宽紧密相关，所以大家比较好判断，反而是接收、发送窗口一旦出现瓶颈，就没这么好判断了。

先明确一下：**文章标题中所说的Buffer指的是sysctl中的 rmem或者wmem，如果是代码中指定的话对应着SO_SNDBUF或者SO_RCVBUF，从TCP的概念来看对应着发送窗口或者接收窗口**

# TCP性能和发送接收Buffer的关系

先从碰到的一个实际问题看起：

> 应用通过专线跨网络访问云上的服务，专线100M，时延20ms，一个SQL查询了22M数据，结果花了大概25秒，这太慢了，不正常。
>
> 如果通过云上client访问云上服务那么1-2秒就返回了（说明不跨网络服务是正常的）。
>
> 如果通过http或者scp从公司向云上传输这22M的数据大概两秒钟也传送完毕了（说明网络带宽不是瓶颈），
>
> 所以这里问题的原因基本上是我们的服务在这种网络条件下有性能问题，需要找出为什么。

## 抓包分析 tcpdump+wireshark

抓包分析这22M的数据传输，如下图（wireshark 时序图），横轴是时间，纵轴是sequence number：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d188530df31712e8341f5687a960743a.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/d188530df31712e8341f5687a960743a.png)

粗一看没啥问题，因为时间太长掩盖了问题。把这个图形放大，只看中间50ms内的传输情况（横轴是时间，纵轴是sequence number，一个点代表一个包）

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/e177d59ecb886daef5905ed80a84dfd2.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/e177d59ecb886daef5905ed80a84dfd2.png)

换个角度，看看窗口尺寸图形：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/7ae26e844629258de173a05d5ad595f9.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/7ae26e844629258de173a05d5ad595f9.png)

从bytes in flight也大致能算出来总的传输速度 16K*1000/20=800Kb/秒

我们的应用代码中会默认设置 socketSendBuffer 为16K:

> socket.setSendBufferSize(16*1024) //16K send buffer

来看一下tcp包发送流程：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d385a7dad76ec4031dfb6c096bca434b.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/d385a7dad76ec4031dfb6c096bca434b.png)

（图片[来自](https://www.atatech.org/articles/9032)）

## 原理解析

如果tcp发送buffer也就是SO_SNDBUF只有16K的话，这些包很快都发出去了，但是这16K的buffer不能立即释放出来填新的内容进去，因为tcp要保证可靠，万一中间丢包了呢。只有等到这16K中的某些包ack了，才会填充一些新包进来然后继续发出去。由于这里rt基本是20ms，也就是16K发送完毕后，等了20ms才收到一些ack，这20ms应用、内核什么都不能做，所以就是如前面第二个图中的大概20ms的等待平台。这块请参考[这篇文章](https://www.atatech.org/articles/79660)

比如下图，wmem大小是8，发出1-8后，buffer不能释放，等到收到ack1-4后，释放1-4，buffer也就是释放了一半，这一半可以填充新的发送数据进来了。 上面的问题在于ack花了很久，导致buffer一直不能释放。

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/3d9e77f8c9b0cab1484c870d2c0d2473.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/3d9e77f8c9b0cab1484c870d2c0d2473.png)

**sendbuffer相当于发送仓库的大小，仓库的货物都发走后，不能立即腾出来发新的货物，而是要等对方确认收到了(ack)才能腾出来发新的货物。 传输速度取决于发送仓库（sendbuffer）、接收仓库（recvbuffer）、路宽（带宽）的大小，如果发送仓库（sendbuffer）足够大了之后接下来的瓶颈就会是高速公路了（带宽、拥塞窗口）。而实际上这个案例中带宽够、接收仓库也够，但是发送仓库太小了，导致发送过程断断续续，所以非常慢。**

如果是UDP，就没有可靠的概念，有数据统统发出去，根本不关心对方是否收到，也就不需要ack和这个发送buffer了。

## 几个发送buffer相关的内核参数

```
$sudo sysctl -a | egrep "rmem|wmem|tcp_mem|adv_win|moderate"
net.core.rmem_default = 212992
net.core.rmem_max = 212992
net.core.wmem_default = 212992 //core是给所有的协议使用的,
net.core.wmem_max = 212992
net.ipv4.tcp_adv_win_scale = 1
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_rmem = 4096    87380    6291456  //最小值  默认值  最大值】
net.ipv4.tcp_wmem = 4096    16384    4194304 //tcp这种就自己的专用选项就不用 core 里面的值了
net.ipv4.udp_rmem_min = 4096
net.ipv4.udp_wmem_min = 4096
vm.lowmem_reserve_ratio = 256    256    32
net.ipv4.tcp_mem = 88560        118080  177120
vm.lowmem_reserve_ratio = 256   256     32
```

net.ipv4.tcp_wmem 默认就是16K，而且内核是能够动态调整的，只不过我们代码中这块的参数是很多年前从Cobra中继承过来的，初始指定了sendbuffer的大小。代码中设置了这个参数后就关闭了内核的动态调整功能，这就是为什么http或者scp都很快，因为他们的send buffer是动态调整的。

接收buffer是有开关可以动态控制的，发送buffer没有开关默认就是开启，关闭只能在代码层面来控制

> net.ipv4.tcp_moderate_rcvbuf

## 优化

调整 socketSendBuffer 到256K，查询时间从25秒下降到了4秒多，但是比理论带宽所需要的时间略高

继续查看系统 net.core.wmem_max 参数默认最大是130K，所以即使我们代码中设置256K实际使用的也是130K，继续调大这个系统参数后整个网络传输时间大概2秒(跟100M带宽匹配了，scp传输22M数据也要2秒），整体查询时间2.8秒。测试用的mysql client短连接，如果代码中的是长连接的话会块300-400ms（消掉了握手和慢启动阶段），这基本上是理论上最快速度了

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/3dcfd469fe1e2f7e1d938a5289b83826.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/3dcfd469fe1e2f7e1d938a5289b83826.png)

如果调用setsockopt()设置了socket选项SO_SNDBUF，将关闭发送端缓冲的自动调节机制，tcp_wmem将被忽略，SO_SNDBUF的最大值由net.core.wmem_max限制。

## BDP 带宽时延积

BDP=rtt*(带宽/8)

这个 buffer 调到1M测试没有帮助，从理论计算BDP（带宽时延积） 0.02秒*(100MB/8)=250Kb 所以 ***SO_SNDBUF为256Kb的时候基本能跑满带宽了，再大也没有什么实际意义了** 。也就是前面所说的仓库足够后瓶颈在带宽上了。

因为这里根据带宽、rtt计算得到的BDP是250K，BDP跑满后拥塞窗口（带宽、接收窗口和rt决定的）即将成为新的瓶颈，所以调大buffer没意义了。

## 用tc构造延时和带宽限制的模拟重现环境

```
sudo tc qdisc del dev eth0 root netem delay 20ms
sudo tc qdisc add dev eth0 root tbf rate 500kbit latency 50ms burst 15kb
```

## 这个案例关于wmem的结论

默认情况下Linux系统会自动调整这个buffer（net.ipv4.tcp_wmem）, 也就是不推荐程序中主动去设置SO_SNDBUF，除非明确知道设置的值是最优的。

从这里我们可以看到，有些理论知识点虽然我们知道，但是在实践中很难联系起来，也就是常说的无法学以致用，最开始看到抓包结果的时候比较怀疑发送、接收窗口之类的，没有直接想到send buffer上，理论跟实践没联系上。

## 接下来看看接收buffer(rmem)和接收窗口的关系

用这样一个案例下来验证接收窗口的作用：

> 有一个batch insert语句，整个一次要插入5532条记录，所有记录大小总共是376K，也就是这个sql语句本身是376K。

## SO_RCVBUF很小的时候并且rtt很大对性能的影响

如果rtt是40ms，总共需要5-6秒钟：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/4af4765c045e9eed2e36d9760d4a2aba.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/4af4765c045e9eed2e36d9760d4a2aba.png)

基本可以看到server一旦空出来点窗口，client马上就发送数据，由于这点窗口太小，rtt是40ms，也就是一个rtt才能传3456字节的数据，整个带宽才用到80-90K，完全没跑满。

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/1984258c0300921799476777f5f0a38a.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/1984258c0300921799476777f5f0a38a.png)

比较明显间隔 40ms 一个等待台阶，台阶之间两个包大概3K数据，总的传输效率如下：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/5ec50ecf25444e96d81fab975b5a79e6.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/5ec50ecf25444e96d81fab975b5a79e6.png)

**斜线越陡表示速度越快，从上图看整体SQL上传花了5.5秒，执行0.5秒。**

此时对应的窗口尺寸：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/05d6357ed53c1c16f0dd0454251916ef.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/05d6357ed53c1c16f0dd0454251916ef.png)

窗口由最开始28K(20个1448）很快降到了不到4K的样子，然后基本游走在即将满的边缘，虽然读取慢，幸好rtt也大，导致最终也没有满。（这个是3.1的Linux，应用SO_RCVBUF设置的是8K，用一半来做接收窗口）

## SO_RCVBUF很小的时候并且rtt很小对性能的影响

如果同样的语句在 rtt 是0.1ms的话

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/67f280a1cf499ae388fc44d6418869a7.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/67f280a1cf499ae388fc44d6418869a7.png)

虽然明显看到接收窗口经常跑满，但是因为rtt很小，一旦窗口空出来很快就通知到对方了，所以整个过小的接收窗口也没怎么影响到整体性能

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/15b7d6852e44fc179d60d76f322695c7.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/15b7d6852e44fc179d60d76f322695c7.png)

如上图11.4秒整个SQL开始，到11.41秒SQL上传完毕，11.89秒执行完毕（执行花了0.5秒），上传只花了0.01秒

接收窗口情况：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/0f3050cd98db40a352410a11a521e8b2.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/0f3050cd98db40a352410a11a521e8b2.png)

如图，接收窗口由最开始的28K降下来，然后一直在5880和满了之间跳动

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/0db5c3684a9314907f9158ac15b6ac71.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/0db5c3684a9314907f9158ac15b6ac71.png)

从这里可以得出结论，接收窗口的大小对性能的影响，rtt越大影响越明显，当然这里还需要应用程序配合，如果应用程序一直不读走数据即使接收窗口再大也会堆满的。

## SO_RCVBUF和tcp window full的坏case

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/55cf9875d24d76a077c442327d54fa34.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/55cf9875d24d76a077c442327d54fa34.png)

上图中红色平台部分，停顿了大概6秒钟没有发任何有内容的数据包，这6秒钟具体在做什么如下图所示，可以看到这个时候接收方的TCP Window Full，同时也能看到接收方（3306端口）的TCP Window Size是8192（8K），发送方（27545端口）是20480.

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/da48878ce0c01bcdedb1e6d6a6cc6d1c.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/da48878ce0c01bcdedb1e6d6a6cc6d1c.png)

这个状况跟前面描述的recv buffer太小不一样，8K是很小，但是因为rtt也很小，所以server总是能很快就ack收到了，接收窗口也一直不容易达到full状态，但是一旦接收窗口达到了full状态，居然需要惊人的6秒钟才能恢复，这等待的时间有点太长了。这里应该是应用读取数据太慢导致了耗时6秒才恢复，所以最终这个请求执行会非常非常慢（时间主要耗在了上传SQL而不是执行SQL）.

实际原因不知道，从读取TCP数据的逻辑来看这里没有明显的block，可能的原因：

- request的SQL太大，Server（3306端口上的服务）从TCP读取SQL需要放到一块分配好的内存，内存不够的时候需要扩容，扩容有可能触发fgc，从图形来看，第一次满就卡顿了，而且每次满都卡顿，不像是这个原因
- request请求一次发过来的是多个SQL，应用读取SQL后，将SQL分成多个，然后先执行第一个，第一个执行完后返回response，再读取第二个。图形中卡顿前没有response返回，所以也不是这个原因
- ……其它未知原因

## 接收方不读取数据导致的接收窗口满同时有丢包发生

服务端返回数据到client端，TCP协议栈ack这些包，但是应用层没读走包，这个时候 SO_RCVBUF 堆积满，client的TCP协议栈发送 ZeroWindow 标志给服务端。也就是接收端的 buffer 堆满了（但是服务端这个时候看到的bytes in fly是0，因为都ack了），这时服务端不能继续发数据，要等 ZeroWindow 恢复。

那么接收端上层应用不读走包可能的原因：

- 应用代码卡顿、GC等等
- 应用代码逻辑上在做其它事情（比如Server将SQL分片到多个DB上，Server先读取第一个分片，如果第一个分片数据很大很大，处理也慢，那么即使第二个分片数据都返回到了TCP 的recv buffer，应用也没去读取其它分片的结果集，直到第一个分片读取完毕。如果SQL带排序，那么Server会轮询读取多个分片，造成这种卡顿的概率小了很多）

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/49e2635a7c4025d44b915a1f17dd272a.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/49e2635a7c4025d44b915a1f17dd272a.png)

上图这个流因为应用层不读取TCP数据，导致TCP接收Buffer满，进而接收窗口为0，server端不能再发送数据而卡住，但是ZeroWindow的探测包，client都有正常回复，所以1903秒之后接收方窗口不为0后（window update）传输恢复。

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/2e493d8dc32bb63f2126375de6675351.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/2e493d8dc32bb63f2126375de6675351.png)

这个截图和前一个类似，是在Server上(3003端口)抓到的包，不同的是接收窗口为0后，server端多次探测（Server上抓包能看到），但是client端没有回复 ZeroWindow（也有可能是回复了，但是中间环节把ack包丢了,或者这个探测包client没收到），造成server端认为client死了、不可达之类，进而反复重传，重传超过15次之后，server端认为这个连接死了，粗暴单方面断开（没有reset和fin,因为没必要，server认为网络连通性出了问题）。

等到1800秒后，client的接收窗口恢复了，发个window update给server，这个时候server认为这个连接已经断开了，只能回复reset

网络不通，重传超过一定的时间（tcp_retries2)然后断开这个连接是正常的，这里的问题是：

1. 为什么这种场景下丢包了，而且是针对某个stream一直丢包

可能是因为这种场景下触发了中间环节的流量管控，故意丢包了（比如proxy、slb、交换机都有可能做这种选择性的丢包）

这里server认为连接断开，没有发reset和fin,因为没必要，server认为网络连通性出了问题。client还不知道server上这个连接清理掉了，等client回复了一个window update，server早就认为这个连接早断了，突然收到一个update，莫名其妙，只能reset

## 接收窗口和SO_RCVBUF的关系

### ss 查看socket buffer大小

初始接收窗口一般是 **mss乘以初始cwnd（为了和慢启动逻辑兼容，不想一下子冲击到网络）**，如果没有设置SO_RCVBUF，那么会根据 net.ipv4.tcp_rmem 动态变化，如果设置了SO_RCVBUF，那么接收窗口要向下面描述的值靠拢。

[初始cwnd可以大致通过查看到](https://access.redhat.com/discussions/3624151)：

```
ss -itmpn dst "10.81.212.8"
State      Recv-Q Send-Q Local Address:Port  Peer Address:Port
ESTAB      0      0      10.xx.xx.xxx:22     10.yy.yy.yyy:12345  users:(("sshd",pid=1442,fd=3))
         skmem:(r0,rb369280,t0,tb87040,f4096,w0,o0,bl0,d92)

Here we can see this socket has Receive Buffer 369280 bytes, and Transmit Buffer 87040 bytes.
Keep in mind the kernel will double any socket buffer allocation for overhead. 
So a process asks for 256 KiB buffer with setsockopt(SO_RCVBUF) then it will get 512 KiB buffer space. This is described on man 7 tcp. 
```

初始窗口计算的代码逻辑，重点在17行：

```
    /* TCP initial congestion window as per rfc6928 */
    #define TCP_INIT_CWND           10
    /* 3. Try to fixup all. It is made immediately after connection enters

       established state.
             */
            void tcp_init_buffer_space(struct sock *sk)
            {
          int tcp_app_win = sock_net(sk)->ipv4.sysctl_tcp_app_win;
          struct tcp_sock *tp = tcp_sk(sk);
          int maxwin;

        if (!(sk->sk_userlocks & SOCK_SNDBUF_LOCK))
                tcp_sndbuf_expand(sk);

        //初始最大接收窗口计算过程
        tp->rcvq_space.space = min_t(u32, tp->rcv_wnd, TCP_INIT_CWND * tp->advmss);
        tcp_mstamp_refresh(tp);
        tp->rcvq_space.time = tp->tcp_mstamp;
        tp->rcvq_space.seq = tp->copied_seq;

        maxwin = tcp_full_space(sk);

        if (tp->window_clamp >= maxwin) {
                tp->window_clamp = maxwin;

                if (tcp_app_win && maxwin > 4 * tp->advmss)
                        tp->window_clamp = max(maxwin -
                                               (maxwin >> tcp_app_win),
                                               4 * tp->advmss);
        }

        /* Force reservation of one segment. */
        if (tcp_app_win &&
            tp->window_clamp > 2 * tp->advmss &&
            tp->window_clamp + tp->advmss > maxwin)
                tp->window_clamp = max(2 * tp->advmss, maxwin - tp->advmss);

        tp->rcv_ssthresh = min(tp->rcv_ssthresh, tp->window_clamp);
        tp->snd_cwnd_stamp = tcp_jiffies32;
}
```

传输过程中，最大接收窗口会动态调整，当指定了SO_RCVBUF后，实际buffer是两倍SO_RCVBUF，但是要分出一部分（2^net.ipv4.tcp_adv_win_scale)来作为乱序报文缓存。

> 1. net.ipv4.tcp_adv_win_scale = 2 //2.6内核，3.1中这个值默认是1

如果SO_RCVBUF是8K，总共就是16K，然后分出2^2分之一，也就是4分之一，还剩12K当做接收窗口；如果设置的32K，那么接收窗口是48K
static inline int tcp_win_from_space(const struct sock *sk, int space)
{//space 传入的时候就已经是 2*SO_RCVBUF了
int tcp_adv_win_scale = sock_net(sk)->ipv4.sysctl_tcp_adv_win_scale;

```
        return tcp_adv_win_scale <= 0 ?
                (space>>(-tcp_adv_win_scale)) :
                space - (space>>tcp_adv_win_scale); //sysctl参数tcp_adv_win_scale 
}
```

接收窗口有最大接收窗口和当前可用接收窗口。

一般来说一次中断基本都会将 buffer 中的包都取走。

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d7d3af2c03653e6cf8ae2befa0022832.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/d7d3af2c03653e6cf8ae2befa0022832.png)

绿线是最大接收窗口动态调整的过程，最开始是1460*10，握手完毕后略微调整到1472*10（可利用body增加了12），随着数据的传输开始跳涨

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d0e12e8bad8764385549f9b391c62ab0.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/d0e12e8bad8764385549f9b391c62ab0.png)

上图是四个batch insert语句，可以看到绿色接收窗口随着数据的传输越来越大，图中蓝色竖直部分基本表示SQL上传，两个蓝色竖直条的间隔代表这个insert在服务器上真正的执行时间。这图非常陡峭，表示上传没有任何瓶颈.

### 设置 SO_RCVBUF 后通过wireshark观察到的接收窗口基本

下图是设置了 SO_RCVBUF 为8192的实际情况：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d0e12e8bad8764385549f9b391c62ab0.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/d0e12e8bad8764385549f9b391c62ab0.png)

从最开始的14720，执行第一个create table语句后降到14330，到真正执行batch insert就降到了8192*1.5. 然后一直保持在这个值

### If you set a “receive buffer size” on a TCP socket, what does it actually mean?

[The naive answer would go something along the lines of: the TCP receive buffer setting indicates the maximum number of bytes a ](https://blog.cloudflare.com/the-story-of-one-latency-spike/)[`read()`](https://blog.cloudflare.com/the-story-of-one-latency-spike/)[ syscall could retrieve without blocking.](https://blog.cloudflare.com/the-story-of-one-latency-spike/)

Note that if the buffer size is set with `setsockopt()`, the value returned with `getsockopt()` is always *double* the size requested to allow for overhead. This is described in `man 7 socket`.

## 长肥网络（rt很高、带宽也高）下接收窗口对传输性能的影响

最后通过一个实际碰到的案例，涉及到了接收窗口、发送Buffer以及高延时情况下的性能问题

案例描述：从中国访问美国的服务器下载图片，只能跑到220K，远远没有达到带宽能力，其中中美之间的网络延时时150ms，这个150ms已经不能再优化了。业务结构是：

client ——150ms—–>>>LVS—1ms–>>>美国的统一接入server—–1ms—–>>>nginx

通过下载一个4M的文件大概需要20秒，分别在client和nginx上抓包来分析这个问题（统一接入server没权限上去）

### Nginx上抓包

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/259767fb17f7dbffe7f77ab059c47dbd.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/259767fb17f7dbffe7f77ab059c47dbd.png)

从这里可以看到Nginx大概在60ms内就将4M的数据都发完了

### client上抓包

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/466fba92829f6a922ccd2d57a7e3fdac.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/466fba92829f6a922ccd2d57a7e3fdac.png)

从这个图上可以清楚看到大概每传输大概30K数据就有一个150ms的等待平台，这个150ms基本是client到美国的rt。

从我们前面的阐述可以清楚了解到因为rt比较高，统一接入server每发送30K数据后要等150ms才能收到client的ack，然后继续发送，猜是因为上面设置的发送buffer大概是30K。

检查统一接入server的配置，可以看到接入server的配置里面果然有个32K buffer设置

### 将buffer改大

速度可以到420K，但是还没有跑满带宽：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/93e254c5154ce2e065bec9fb34f3db2b.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/93e254c5154ce2e065bec9fb34f3db2b.png)

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/0a8c68a58da6f169573b57cde0ffba93.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/0a8c68a58da6f169573b57cde0ffba93.png)

接着看一下client上的抓包

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/822737a4ed6ffe6b920d4b225a1be5bf.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/822737a4ed6ffe6b920d4b225a1be5bf.png)

可以清楚看到 client的接收窗口是64K， 64K*1000/150=426K 这个64K很明显是16位的最大值，应该是TCP握手有一方不支持window scaling factor

那么继续分析一下握手包，syn：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/004886698ddbaa1cbc8342a9cd667c76.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/004886698ddbaa1cbc8342a9cd667c76.png)

说明client是支持的，再看 syn+ack：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/70155e021390cb1ee07091c306c375f4.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/70155e021390cb1ee07091c306c375f4.png)

可以看到服务端不支持，那就最大只能用到64K。需要修改服务端代理程序，这主要是LVS或者代理的锅。

如果内网之间rt很小这个锅不会爆发，一旦网络慢一点就把问题恶化了

比如这是这个应用的开发人员的反馈：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/a08a204ec7ad4bba7867dacea1668322.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/a08a204ec7ad4bba7867dacea1668322.png)

长肥网络就像是很长很宽的高速公路，上面可以同时跑很多车，而如果发车能力不够，就容易跑不满高速公路。
在rt很短的时候可以理解为高速公路很短，所以即使发车慢也还好，因为车很快就到了，到了后就又能发新车了。rt很长的话就要求更大的仓库了。

整个这个问题，我最初拿到的问题描述结构是这样的（不要笑用户连自己的业务结构都描述不清）：

client ——150ms—–>>>nginx

实际开发人员也不能完全描述清楚结构，从抓包中慢慢分析反推他们的结构，到最后问题的解决。

这个案例综合了发送窗口（32K）、接收窗口（64K，因为握手LVS不支持window scale）、rt很大将问题暴露出来（跨国网络，rt没法优化）。

## delay ack拉高实际rt的case

如下业务监控图：实际处理时间（逻辑服务时间1ms，rtt2.4ms，加起来3.5ms），但是系统监控到的rt（蓝线）是6ms，如果一个请求分很多响应包串行发给client，这个6ms是正常的（1+2.4*N），但实际上如果send buffer足够的话，按我们前面的理解多个响应包会并发发出去，所以如果整个rt是3.5ms才是正常的。

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d56f87a19a10b0ac9a3b7009641247a0.png)](https://ata2-img.oss-cn-zhangjiakou.aliyuncs.com/d56f87a19a10b0ac9a3b7009641247a0.png)

抓包来分析原因：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/d5e2e358dd1a24e104f54815c84875c9.png)](https://ata2-img.oss-cn-zhangjiakou.aliyuncs.com/d5e2e358dd1a24e104f54815c84875c9.png)

实际看到大量的response都是3.5ms左右，符合我们的预期，但是有少量rt被delay ack严重影响了

从下图也可以看到有很多rtt超过3ms的，这些超长时间的rtt会最终影响到整个服务rt

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/48eae3dcd7c78a68b0afd5c66f783f23.png)](https://ata2-img.oss-cn-zhangjiakou.aliyuncs.com/48eae3dcd7c78a68b0afd5c66f783f23.png)

## OS层面相关参数：

```
$sudo sysctl -a | egrep "rmem|wmem|tcp_mem|adv_win|moderate"
net.core.rmem_default = 212992
net.core.rmem_max = 212992
net.core.wmem_default = 212992 //core是给所有的协议使用的,
net.core.wmem_max = 212992
net.ipv4.tcp_adv_win_scale = 1
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_rmem = 4096    87380    6291456
net.ipv4.tcp_wmem = 4096    16384    4194304 //tcp这种就自己的专用选项就不用 core 里面的值了
net.ipv4.udp_rmem_min = 4096
net.ipv4.udp_wmem_min = 4096
vm.lowmem_reserve_ratio = 256    256    32
net.ipv4.tcp_mem = 88560        118080  177120
```

发送buffer系统比较好自动调节，依靠发送数据大小和rt延时大小，可以相应地进行调整；但是接受buffer就不一定了，接受buffer的使用取决于收到的数据快慢和应用读走数据的速度，只能是OS根据系统内存的压力来调整接受buffer。系统内存的压力取决于 net.ipv4.tcp_mem.

需要特别注意：**tcp_wmem 和 tcp_rmem 的单位是字节，而 tcp_mem 的单位的页面**

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/ea04e40acda986675bf0ad0ea7b9b8ff.png)](https://ata2-img.oss-cn-zhangjiakou.aliyuncs.com/ea04e40acda986675bf0ad0ea7b9b8ff.png)

## 内核观测tcp_mem是否不足

因 tcp_mem 达到限制而无法发包或者产生抖动的问题，我们也是可以观测到的。为了方便地观测这类问题，Linux 内核里面预置了静态观测点：sock_exceed_buf_limit（需要 4.16+ 的内核版本）。

> $ echo 1 > /sys/kernel/debug/tracing/events/sock/sock_exceed_buf_limit/enable

然后去看是否有该事件发生：

> $ cat /sys/kernel/debug/tracing/trace_pipe

如果有日志输出（即发生了该事件），就意味着你需要调大 tcp_mem 了，或者是需要断开一些 TCP 连接了。

### 或者通过systemtap来观察

如下是tcp_sendmsg流程，sk_stream_wait_memory就是tcp_wmem不够的时候触发等待：

[![image.png](TCP性能和发送接收窗口、Buffer的关系  plantegg.assets/ff025f076a4a2bc2b1b13d11f32a97d3.png)](https://ata2-img.cn-hangzhou.oss-pub.aliyun-inc.com/ff025f076a4a2bc2b1b13d11f32a97d3.png)

如果sendbuffer不够就会卡在上图中的第一步 sk_stream_wait_memory, 通过systemtap脚本可以验证：

```
 #!/usr/bin/stap
    # Simple probe to detect when a process is waiting for more socket send
    # buffer memory. Usually means the process is doing writes larger than the
    # socket send buffer size or there is a slow receiver at the other side.
    # Increasing the socket's send buffer size might help decrease application
    # latencies, but it might also make it worse, so buyer beware.

probe kernel.function("sk_stream_wait_memory")
{
    printf("%u: %s(%d) blocked on full send buffern",
        gettimeofday_us(), execname(), pid())
}

probe kernel.function("sk_stream_wait_memory").return
{
    printf("%u: %s(%d) recovered from full send buffern",
        gettimeofday_us(), execname(), pid())
}

# Typical output: timestamp in microseconds: procname(pid) event
#
# 1218230114875167: python(17631) blocked on full send buffer
# 1218230114876196: python(17631) recovered from full send buffer
# 1218230114876271: python(17631) blocked on full send buffer
# 1218230114876479: python(17631) recovered from full send buffer
```

## 总结

- 一般来说绝对不要在程序中手工设置SO_SNDBUF和SO_RCVBUF，内核自动调整比你做的要好；
- SO_SNDBUF一般会比发送滑动窗口要大，因为发送出去并且ack了的才能从SO_SNDBUF中释放；
- TCP接收窗口跟SO_RCVBUF关系很复杂；
- SO_RCVBUF太小并且rtt很大的时候会严重影响性能；
- 接收窗口比发送窗口复杂多了；
- 发送窗口/SO_SNDBUF–发送仓库，带宽/拥塞窗口–马路通畅程度，接收窗口/SO_RCVBUF–接收仓库；
- 发送仓库、马路宽度、长度（rt）、接收仓库一起决定了传输速度–类比一下快递过程。

**总之记住一句话：不要设置socket的SO_SNDBUF和SO_RCVBUF**

# 相关和参考文章

[经典的 nagle 和 dalay ack对性能的影响 就是要你懂 TCP– 最经典的TCP性能问题](https://www.atatech.org/articles/80292)

[关于TCP 半连接队列和全连接队列](https://www.atatech.org/articles/78858)

[MSS和MTU导致的悲剧](https://www.atatech.org/articles/60633)

[双11通过网络优化提升10倍性能](https://www.atatech.org/articles/73174)

[就是要你懂TCP的握手和挥手](https://www.atatech.org/articles/79660)

[高性能网络编程7–tcp连接的内存使用](https://www.atatech.org/articles/13203)

[The story of one latency spike](https://blog.cloudflare.com/the-story-of-one-latency-spike/)

[What is rcv_space in the ‘ss –info’ output, and why it’s value is larger than net.core.rmem_max](https://access.redhat.com/discussions/782343)

[# performance](https://plantegg.github.io/tags/performance/) [# Linux](https://plantegg.github.io/tags/Linux/) [# TCP](https://plantegg.github.io/tags/TCP/) [# sendBuffer](https://plantegg.github.io/tags/sendBuffer/) [# rmem](https://plantegg.github.io/tags/rmem/) [# wmem](https://plantegg.github.io/tags/wmem/) [# recvBuffer](https://plantegg.github.io/tags/recvBuffer/) [# 接收窗口](https://plantegg.github.io/tags/接收窗口/) [# 发送窗口](https://plantegg.github.io/tags/发送窗口/)