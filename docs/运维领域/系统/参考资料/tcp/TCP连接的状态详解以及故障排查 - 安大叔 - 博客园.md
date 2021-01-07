# [TCP连接的状态详解以及故障排查](https://www.cnblogs.com/andashu/p/6274096.html)


WEB产品的性能测试，有很多tcp连接方面的问题，也因为这方面的问题，导致性能出现不稳定等情况，客户端和服务器之间数据传输，以及之间连接状态的转变，哪些状态是正常的状态，哪些状态是异常的状态，怎样去定位这些问题，以及常用的工具，今天针对这些问题简单的总结了一下；

 

> 1
>
> TCP状态获取

  1）netstat -nat  查看TCP各个状态的数量

  2）lsof  -i:port  可以检测到打开套接字的状况

  3)  sar -n SOCK 查看tcp创建的连接数

  4)  tcpdump -iany tcp port 9000 对tcp端口为9000的进行抓包

 

 

 

> 2
>
> TCP状态迁移路线图

![img](TCP连接的状态详解以及故障排查 - 安大叔 - 博客园.assets/0)

CLOSED：没有任何连接状态；

LISTENING：侦听来自远方的TCP端口的连接请求；

 首先服务端需要打开一个socket进行监听，状态为LISTEN。

 有提供某种服务才会处于LISTENING状态，TCP状态变化就是某个端口的状态变化，提供一个服务就打开一个端口，例如：提供www服务默认开的是80端口，提供ftp服务默认的端口为21，当提供的服务没有被连接时就处于LISTENING状态。FTP服务启动后首先处于侦听（LISTENING）状态。处于侦听LISTENING状态时，该端口是开放的，等待连接，但还没有被连接。就像你房子的门已经敞开的，但还没有人进来。

  看LISTENING状态最主要的是看本机开了哪些端口，这些端口都是哪个程序开的，关闭不必要的端口是保证安全的一个非常重要的方面，服务端口都对应一个服务（应用程序），停止该服务就关闭了该端口，例如要关闭21端口只要停止IIS服务中的FTP服务即可。关于这方面的知识请参阅其它文章。

  如果你不幸中了服务端口的木马，木马也开个端口处于LISTENING状态。

SYN-SENT：客户端SYN_SENT状态：

 再发送连接请求后等待匹配的连接请求:客户端通过应用程序调用connect进行active open.于是客户端tcp发送一个SYN以请求建立一个连接.之后状态置为SYN_SENT. 在发送连接请求后等待匹配的连接请求

 当请求连接时客户端首先要发送同步信号给要访问的机器，此时状态为SYN_SENT，如果连接成功了就变为ESTABLISHED，正常情况下SYN_SENT状态非常短暂。例如要访问网站http://www.baidu.com,如果是正常连接的话，用TCPView观察IE建立的连接会发现很快从SYN_SENT变为ESTABLISHED，表示连接成功。SYN_SENT状态快的也许看不到。

 如果发现有很多SYN_SENT出现，那一般有这么几种情况，一是你要访问的网站不存在或线路不好，二是用扫描软件扫描一个网段的机器，也会出出现很多SYN_SENT，另外就是可能中了病毒了，例如中了"冲击波"，病毒发作时会扫描其它机器，这样会有很多SYN_SENT出现。

SYN-RECEIVED：服务器端状态SYN_RCVD

​    再收到和发送一个连接请求后等待对方对连接请求的确认

 当服务器收到客户端发送的同步信号时，将标志位ACK和SYN置1发送给客户端，此时服务器端处于SYN_RCVD状态，如果连接成功了就变为ESTABLISHED，正常情况下SYN_RCVD状态非常短暂。

 如果发现有很多SYN_RCVD状态，那你的机器有可能被SYN Flood的DoS(拒绝服务攻击)攻击了。

 

ESTABLISHED：代表一个打开的连接。

 ESTABLISHED状态是表示两台机器正在传输数据，观察这个状态最主要的就是看哪个程序正在处于ESTABLISHED状态。

 服务器出现很多ESTABLISHED状态： netstat -nat |grep 9502或者使用lsof  -i:9502可以检测到。

 当客户端未主动close的时候就断开连接：即客户端发送的FIN丢失或未发送。

 这时候若客户端断开的时候发送了FIN包，则服务端将会处于CLOSE_WAIT状态；

 这时候若客户端断开的时候未发送FIN包，则服务端处还是显示ESTABLISHED状态；

 结果客户端重新连接服务器。

 而新连接上来的客户端（也就是刚才断掉的重新连上来了）在服务端肯定是ESTABLISHED; 如果客户端重复的上演这种情况，那么服务端将会出现大量的假的ESTABLISHED连接和CLOSE_WAIT连接。

 最终结果就是新的其他客户端无法连接上来，但是利用netstat还是能看到一条连接已经建立，并显示ESTABLISHED，但始终无法进入程序代码

FIN-WAIT-1：等待远程TCP连接中断请求，或先前的连接中断请求的确认

 主动关闭(active close)端应用程序调用close，于是其TCP发出FIN请求主动关闭连接，之后进入FIN_WAIT1状态./* The socket is closed, and the connection is shutting down. 等待远程TCP的连接中断请求，或先前的连接中断请求的确认 */

 如果服务器出现shutdown再重启，使用netstat -nat查看，就会看到很多FIN-WAIT-1的状态。就是因为服务器当前有很多客户端连接，直接关闭服务器后，无法接收到客户端的ACK。

FIN-WAIT-2：从远程TCP等待连接中断请求

 主动关闭端接到ACK后，就进入了FIN-WAIT-2，从远程TCP等待连接中断请求

 这就是著名的半关闭的状态了，这是在关闭连接时，客户端和服务器两次握手之后的状态。在这个状态下，应用程序还有接受数据的能力，但是已经无法发送数据，但是也有一种可能是，客户端一直处于FIN_WAIT_2状态，而服务器则一直处于WAIT_CLOSE状态，而直到应用层来决定关闭这个状态。

CLOSE-WAIT：等待从本地用户发来的连接中断请求

 被动关闭(passive close)端TCP接到FIN后，就发出ACK以回应FIN请求(它的接收也作为文件结束符传递给上层应用程序),并进入CLOSE_WAIT.等待从本地用户发来的连接中断请求

   

CLOSING：等待远程TCP对连接中断的确认

等待远程TCP对连接中断的确认

LAST-ACK：等待原来的发向远程TCP的连接中断请求的确认

被动关闭端一段时间后，接收到文件结束符的应用程序将调用CLOSE关闭连接。这导致它的TCP也发送一个 FIN,等待对方的ACK.就进入了LAST-ACK 等待原来发向远程TCP的连接中断请求的确认

使用并发压力测试的时候，突然断开压力测试客户端，服务器会看到很多LAST-ACK。

TIME-WAIT：等待足够的时间以确保远程TCP接收到连接中断请求的确认

在主动关闭端接收到FIN后，TCP就发送ACK包，并进入TIME-WAIT状态，等待足够的时间以确保远程TCP接收到连接中断请求的确认 */

   TIME_WAIT等待状态，这个状态又叫做2MSL状态，说的是在TIME_WAIT2发送了最后一个ACK数据报以后，要进入TIME_WAIT状态，这个状态是防止最后一次握手的数据报没有传送到对方那里而准备的（注意这不是四次握手，这是第四次握手的保险状态）。这个状态在很大程度上保证了双方都可以正常结束，但是，问题也来了。由于插口的2MSL状态（插口是IP和端口对的意思，socket），使得应用程序在2MSL时间内是无法再次使用同一个插口的，对于客户程序还好一些，但是对于服务程序，例如httpd，它总是要使用同一个端口来进行服务，而在2MSL时间内，启动httpd就会出现错误（插口被使用）。为了避免这个错误，服务器给出了一个平静时间的概念，这是说在2MSL时间内，虽然可以重新启动服务器，但是这个服务器还是要平静的等待2MSL时间的过去才能进行下一次连接。

TCP的状态迁移图看似复杂，但是仔细观察，是有两条线路的；

客户端应用程序的状态迁移图

客户端的状态可以用如下的流程来表示：

​    CLOSED->SYN_SENT->ESTABLISHED->FIN_WAIT_1->FIN_WAIT_2->TIME_WAIT->CLOSED

以上流程是在程序正常的情况下应该有的流程，从书中的图中可以看到，在建立连接时，当客户端收到SYN报文的ACK以后，客户端就打开了数据交互地连接。而结束连接则通常是客户端主动结束的，客户端结束应用程序以后，需要经历FIN_WAIT_1，FIN_WAIT_2等状态，这些状态的迁移就是前面提到的结束连接的四次握手。

服务器的状态迁移图

服务器的状态可以用如下的流程来表示：

​    CLOSED->LISTEN->SYN收到->ESTABLISHED->CLOSE_WAIT->LAST_ACK->CLOSED

在建立连接的时候，服务器端是在第三次握手之后才进入数据交互状态，而关闭连接则是在关闭连接的第二次握手以后（注意不是第四次）。而关闭以后还要等待客户端给出最后的ACK包才能进入初始的状态。

其他状态迁移

还有一些其他的状态迁移，这些状态迁移针对服务器和客户端两方面的总结如下

LISTEN->SYN_SENT，对于这个解释就很简单了，服务器有时候也要打开连接的嘛。

SYN_SENT->SYN收到，服务器和客户端在SYN_SENT状态下如果收到SYN数据报，则都需要发送SYN的ACK数据报并把自己的状态调整到SYN收到状态，准备进入ESTABLISHED

SYN_SENT->CLOSED，在发送超时的情况下，会返回到CLOSED状态。

SYN_收到->LISTEN，如果受到RST包，会返回到LISTEN状态。

SYN_收到->FIN_WAIT_1，这个迁移是说，可以不用到ESTABLISHED状态，而可以直接跳转到FIN_WAIT_1状态并等待关闭。

![img](TCP连接的状态详解以及故障排查 - 安大叔 - 博客园.assets/0)

 

 

 

 

> 3
>
> TCP连接建立三次握手

> Client连接Server：
>
> 当Client端调用socket函数调用时，相当于Client端产生了一个处于Closed状态的套接字。
>
>  1）第一次握手：Client端又调用connect函数调用，系统为Client随机分配一个端口，连同传入connect中的参数(Server的IP和端口)，这就形成了一个连接四元组，客户端发送一个带SYN标志的TCP报文到服务器。这是三次握手过程中的报文1。connect调用让Client端的socket处于SYN_SENT状态，等待服务器确认；SYN：同步序列编号(Synchronize Sequence Numbers)。
>
>  2)第二次握手： 服务器收到syn包，必须确认客户的SYN（ack=j+1），同时自己也发送一个SYN包（syn=k），即SYN+ACK包，此时服务器进入SYN_RECV状态；
>
>  3)第三次握手：客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=k+1)，此包发送完毕，客户器和客务器进入ESTABLISHED状态，完成三次握手。连接已经可以进行读写操作。
>
> 一个完整的三次握手也就是： 请求---应答---再次确认。
>
> TCP协议通过三个报文段完成连接的建立，这个过程称为三次握手(three-way handshake)，过程如下图所示。
>
> 对应的函数接口：
>
> ![img](TCP连接的状态详解以及故障排查 - 安大叔 - 博客园.assets/0)
>
> Server：
>
>  当Server端调用socket函数调用时，相当于Server端产生了一个处于Closed状态的监听套接字
>
>  Server端调用bind操作，将监听套接字与指定的地址和端口关联，然后又调用listen函数，系统会为其分配未完成队列和完成队列，此时的监听套接字可以接受Client的连接，监听套接字状态处于LISTEN状态。
>
>  当Server端调用accept操作时，会从完成队列中取出一个已经完成的client连接，同时在server这段会产生一个会话套接字，用于和client端套接字的通信，这个会话套接字的状态是ESTABLISH。
>
> 从图中可以看出，当客户端调用connect时，触发了连接请求，向服务器发送了SYN J包，这时connect进入阻塞状态；服务器监听到连接请求，即收到SYN J包，调用accept函数接收请求向客户端发送SYN K ，ACK J+1，这时accept进入阻塞状态；客户端收到服务器的SYN K ，ACK J+1之后，这时connect返回，并对SYN K进行确认；服务器收到ACK K+1时，accept返回，至此三次握手完毕，连接建立。
>
> 我们可以通过网络抓包的查看具体的流程：
>
> 比如我们服务器开启9502的端口。使用tcpdump来抓包：
>
> tcpdump -iany tcp port 9502
>
> 然后我们使用telnet 127.0.0.1 9502开连接.:
>
> telnet 127.0.0.1 9502
>
> 14:12:45.104687 IP localhost.39870 > localhost.9502: Flags [S], seq 2927179378, win 32792, options [mss 16396,sackOK,TS val 255474104 ecr 0,nop,wscale 3], length 0（1）
>
> 14:12:45.104701 IP localhost.9502 > localhost.39870: Flags [S.], seq 1721825043, ack 2927179379, win 32768, options [mss 16396,sackOK,TS val 255474104 ecr 255474104,nop,wscale 3], length 0  （2）
>
> 14:12:45.104711 IP localhost.39870 > localhost.9502: Flags [.], ack 1, win 4099, options [nop,nop,TS val 255474104 ecr 255474104], length 0  （3）
>
> 14:13:01.415407 IP localhost.39870 > localhost.9502: Flags [P.], seq 1:8, ack 1, win 4099, options [nop,nop,TS val 255478182 ecr 255474104], length 7
>
> 14:13:01.415432 IP localhost.9502 > localhost.39870: Flags [.], ack 8, win 4096, options [nop,nop,TS val 255478182 ecr 255478182], length 0
>
> 14:13:01.415747 IP localhost.9502 > localhost.39870: Flags [P.], seq 1:19, ack 8, win 4096, options [nop,nop,TS val 255478182 ecr 255478182], length 18
>
> 14:13:01.415757 IP localhost.39870 > localhost.9502: Flags [.], ack 19, win 4097, options [nop,nop,TS val 255478182 ecr 255478182], length 0
>
> 我们看到 （1）（2）（3）三步是建立tcp：
>
> 第一次握手：
>
> 14:12:45.104687 IP localhost.39870 > localhost.9502: Flags [S], seq 2927179378
>
> 客户端IP localhost.39870 (客户端的端口一般是自动分配的) 向服务器localhost.9502 发送syn包(syn=j)到服务器》
>
> syn的seq= 2927179378
>
> 第二次握手：
>
> 14:12:45.104701 IP localhost.9502 > localhost.39870: Flags [S.], seq 1721825043, ack 2927179379,
>
> 服务器收到syn包，必须确认客户的SYN（ack=j+1），同时自己也发送一个SYN包（syn=k），即SYN+ACK包
>
> SYN（ack=j+1）=ack 2927179379   服务器主机SYN包（syn=seq 1721825043）
>
> 第三次握手：
>
> 14:12:45.104711 IP localhost.39870 > localhost.9502: Flags [.], ack 1,
>
> 客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=k+1)
>
> 客户端和服务器进入ESTABLISHED状态后，可以进行通信数据交互。此时和accept接口没有关系，即使没有accepte，也进行3次握手完成。
>
> 连接出现连接不上的问题，一般是网路出现问题或者网卡超负荷或者是连接数已经满啦。
>
> 紫色背景的部分：
>
> IP localhost.39870 > localhost.9502: Flags [P.], seq 1:8, ack 1, win 4099, options [nop,nop,TS val 255478182 ecr 255474104], length 7
>
> 客户端向服务器发送长度为7个字节的数据，
>
> IP localhost.9502 > localhost.39870: Flags [.], ack 8, win 4096, options [nop,nop,TS val 255478182 ecr 255478182], length 0
>
> 服务器向客户确认已经收到数据
>
> IP localhost.9502 > localhost.39870: Flags [P.], seq 1:19, ack 8, win 4096, options [nop,nop,TS val 255478182 ecr 255478182], length 18
>
> 然后服务器同时向客户端写入数据。
>
> IP localhost.39870 > localhost.9502: Flags [.], ack 19, win 4097, options [nop,nop,TS val 255478182 ecr 255478182], length 0
>
> 客户端向服务器确认已经收到数据
>
> 这个就是tcp可靠的连接，每次通信都需要对方来确认。
>
>  
>
>  

 

> 4
>
> 
>
> TCP连接终止（四次握手）

 

> 由于TCP连接是全双工的，因此每个方向都必须单独进行关闭。这原则是当一方完成它的数据发送任务后就能发送一个FIN来终止这个方向的连接。收到一个 FIN只意味着这一方向上没有数据流动，一个TCP连接在收到一个FIN后仍能发送数据。首先进行关闭的一方将执行主动关闭，而另一方执行被动关闭。
>
>    建立一个连接需要三次握手，而终止一个连接要经过四次握手，这是由TCP的半关闭(half-close)造成的，如图：
>
> ![img](TCP连接的状态详解以及故障排查 - 安大叔 - 博客园.assets/0)
>
> （1）客户端A发送一个FIN，用来关闭客户A到服务器B的数据传送（报文段4）。
>
> （2）服务器B收到这个FIN，它发回一个ACK，确认序号为收到的序号加1（报文段5）。和SYN一样，一个FIN将占用一个序号。
>
> （3）服务器B关闭与客户端A的连接，发送一个FIN给客户端A（报文段6）。
>
> （4）客户端A发回ACK报文确认，并将确认序号设置为收到序号加1（报文段7）。
>
> 对应函数接口如图：
>
> ![img](TCP连接的状态详解以及故障排查 - 安大叔 - 博客园.assets/0)
>
> 调用过程如下：
>
> - 1) 当client想要关闭它与server之间的连接。client（某个应用进程）首先调用close主动关闭连接，这时TCP发送一个FIN M；client端处于FIN_WAIT1状态。
> - 2) 当server端接收到FIN M之后，执行被动关闭。对这个FIN进行确认，返回给client ACK。当server端返回给client ACK后，client处于FIN_WAIT2状态，server处于CLOSE_WAIT状态。它的接收也作为文件结束符传递给应用进程，因为FIN的接收 意味着应用进程在相应的连接上再也接收不到额外数据；
> - 3) 一段时间之后，当server端检测到client端的关闭操作(read返回为0)。接收到文件结束符的server端调用close关闭它的socket。这导致server端的TCP也发送一个FIN N；此时server的状态为LAST_ACK。
> - 4) 当client收到来自server的FIN后 。 client端的套接字处于TIME_WAIT状态，它会向server端再发送一个ack确认，此时server端收到ack确认后，此套接字处于CLOSED状态。
>
>  

 

 

***\*安大叔说\****

人只有保持不甘心的心态才能激励自己不断努力前进，所以永远保持自己的不甘吧，去学习去让自己进步，而不是认命和抱怨