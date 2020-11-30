一、对用户使用有直接影响的功能

- ACL用户权限控制功能
- RESP3：新的 Redis 通信协议
- Cluster 管理工具
- SSL 支持

二、Redis 内部的优化

- IO多线程支持
- 新的Module API
- 新的 Expire 算法

三、外部工具

- Redis Cluster Proxy
- Disque

### ACL

目前的 Redis（5及以下版本），没有用户权限管理这个概念，只有一个AUTH密码验证功能，基本上能够接入的用户就是root用户。
 ACL 就是为了避免接入的用户进行危险命令的操作开发的功能，这类命令如 FLUSHALL，DEBUG等。
 多年来 Redis 管理员通过RENAME命令来进行限制。另一方面，开发人员有时候不清楚一些Redis 驱动的内部实现，可能无意中触发一些危险命令，所以也需要进行限制。
 Redis 6 中加入ACL的功能，能够对接入的用户进行三个层面的权限控制：
 （1）接入权限：用户名和密码；
 （2）可以执行的命令；
 （3）可以操作的 KEY。
 下面我们实际代码中看看效果，下面展示我创建一个用户aaron，设置他的密码，允许执行所有命令，针对所有KEY。



```ruby
127.0.0.1:6380> ACL WHOAMI
"default"
127.0.0.1:6380> ACL setuser aaron on >mypasswd +@all ~*
OK
127.0.0.1:6380> AUTH aaron mypasswd
OK
127.0.0.1:6380> ACL WHOAMI
"aaron"
127.0.0.1:6380> GET foo
(nil)
127.0.0.1:6380> SET foo bar
OK
```

然后我尝试将 aaron 这个用户去掉SET命令的权限。



```ruby
127.0.0.1:6380> ACL setuser aaron -SET
OK
127.0.0.1:6380> SET foo 123
(error) NOPERM this user has no permissions to run the 'set' command or its subcommand
```

我们也可以控制用户可以对哪些 KEY 进行操作，比如下面演示一个叫做 Ben 的用户，他只能创建以 ben 为前缀的 KEY。



```ruby
127.0.0.1:6380> ACL setuser ben on >mypasswd +@all ~ben*
OK
127.0.0.1:6380> set foo bar
(error) NOPERM this user has no permissions to access one of the keys used as arguments
127.0.0.1:6380> set benfoo bar
OK
```

"default" 用户是我们默认连接入 Redis 时的用户，默认情况下这个用户有所有的权限，当然了，我们也可以像以前那样给默认用户设置权限。通过ACL list可以查看当前有哪些用户和他们的权限和密码（前提是该用户有ACL命令的权限）。



```ruby
127.0.0.1:6380> ACL list
1) "user aaron on >mypasswd ~* +@all -set"
2) "user default on nopass ~* +@all"
```

作者提到ACL功能是基于 bitmap 实现的，对性能几乎没有影响。
 关于ACL功能就介绍到这里，有兴趣的作者可以看官方文档：
 [https://redis.io/topics/acl](https://links.jianshu.com/go?to=https%3A%2F%2Fredis.io%2Ftopics%2Facl)

### RESP3

RESP 全称 REdis Serialization Protocol，是 Redis 服务端与客户端之间通信的协议。Redis 5 使用的是 RESP2，而 Redis 6 开始在兼容 RESP2 的基础上，开始支持 RESP3。其实一开始作者是打算完全放弃 RESP2的，后来被劝退了。详情见链接（[http://antirez.com/news/125](https://links.jianshu.com/go?to=http%3A%2F%2Fantirez.com%2Fnews%2F125)）。
 那么 RESP3 有哪些改进的地方呢？

**在 RESP2 中，所有的返回内容，都是一个字符串数组的形式，不管是 list 还是 sorted set。因此客户端需要自行去根据类型进行解读，增加了客户端实现的复杂性。**
 下面以具体的命令展示 RESP3 中的具体变化。



```objectivec
127.0.0.1:6379> HSET myhash a 1 b 2 c 3
(integer) 3
127.0.0.1:6379> HSET myhash a 1 b 2 c 3
(integer) 0
127.0.0.1:6379> HGETALL myhash
1) "a"
2) "1"
3) "b"
4) "2"
5) "c"
6) "3"
127.0.0.1:6379> HELLO 3 #转换成RESP3的命令
1# "server" => "redis"
2# "version" => "6.0.3"
3# "proto" => (integer) 3
4# "id" => (integer) 4
5# "mode" => "standalone"
6# "role" => "master"
7# "modules" => (empty array)
127.0.0.1:6379> HGETALL myhash
1# "a" => "1"
2# "b" => "2"
3# "c" => "3"
```

其实可以看到协议版本切换后返回结果直观上是key-value，还可以通过telnet之后进行操作看返回结果：



```bash
 telnet 127.0.0.1 6379
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
HGETALL myhash
*6
$1
a
$1
1
$1
b
$1
2
$1
c
$1
3
HELLO 3 #转换成RESP3的命令
HGETALL myhash
%3
$1
a
$1
1
$1
b
$1
2
$1
c
$1
3
```

可以看到，以前返回两个field的hash，就是直接无差别地返回6个值，而新的RESP3就会告诉客户端返回3个key-value，通过%表示键值对（也成为map类型）的个数。

其他新的定义还有不少，比如支持 Boolean 类型，set集合类型等等，有兴趣的读者，也是可以去详细看看 RESP3 的设计稿：
 [https://github.com/antirez/RE](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fantirez%2FRE)...

除了具体的数据类型，RESP3 开始支持KEY属性类型（Attribute type），使服务器和客户端之间可以实现更复杂的功能，比如返回信息里带上一个Key的访问频率，使客户端能实现更智能的缓存功能（[http://antirez.com/news/130](https://links.jianshu.com/go?to=http%3A%2F%2Fantirez.com%2Fnews%2F130)）。
 话说，客户端缓存功能，可以说是在提升 Redis 作为缓存的读写能力有了质的飞跃，值得期待。

### Cluster 管理工具

作者分享说redis-trib.rb的功能集成到redis-cli，但这个不是 Redis 5 就已经做了的事情吗？看了一圈，也并没有太大的变化，就增加了一个backup命令。

除了redis-cli，其实另一个工具的优化更让人喜闻乐见，就是redis-benchmark。官方benchmark工具总算支持cluster了，通过多线程的方式对多个分片进行压测。

### 支持 SSL 连接

Amazon 提供的一个功能，在 Redis 6 中 merge 进来。没有提及细节，不清楚对性能有多大影响。

### IO多线程

可能看到这里大家很开心，终于TM支持多线程，不过你可能高兴的有点早了，这里不是你想的多线程。

众所周知，Redis是单线程的。Redis在处理客户端的请求时，包括获取 (socket 读)、解析、执行、内容返回 (socket 写) 等都由一个顺序串行的主线程处理，这就是所谓的“单线程”。

但如果严格来讲从Redis4.0之后并不是单线程，除了主线程外，它也有后台线程在处理一些较为缓慢的操作，例如清理脏数据、无用连接的释放、大key的删除等等。

##### 为什么一直是单线程

官方曾做过类似问题的回复：使用Redis时，几乎不存在CPU成为瓶颈的情况， Redis主要受限于内存和网络。

例如在一个普通的Linux系统上，Redis通过使用pipelining每秒可以处理100万个请求，所以如果应用程序主要使用O(N)或O(log(N))的命令，它几乎不会占用太多CPU。

使用了单线程后，可维护性高。多线程模型虽然在某些方面表现优异，但是它却引入了程序执行顺序的不确定性，带来了并发读写的一系列问题，增加了系统复杂度、同时可能存在线程切换、甚至加锁解锁、死锁造成的性能损耗。

Redis通过AE事件模型以及IO多路复用等技术，处理性能非常高，因此没有必要使用多线程。单线程机制使得 Redis 内部实现的复杂度大大降低，Hash 的惰性 Rehash、Lpush 等等 “线程不安全” 的命令都可以无锁进行。

##### 为什么改进成多线程

Redis将所有数据放在内存中，内存的响应时长大约为100纳秒，对于小数据包，Redis服务器可以处理80,000到100,000 QPS，这也是Redis处理的极限了，对于80%的公司来说，单线程的Redis已经足够使用了。

但随着越来越复杂的业务场景，有些公司动不动就上亿的交易量，因此需要更大的QPS。

常见的解决方案是在分布式架构中对数据进行分区并采用多个服务器，但该方案有非常大的缺点，例如要管理的Redis服务器太多，维护代价大；某些适用于单个Redis服务器的命令不适用于数据分区；数据分区无法解决热点读/写问题；数据偏斜，重新分配和放大/缩小变得更加复杂等等。

从Redis自身角度来说，因为读写网络的read/write系统调用占用了Redis执行期间大部分CPU时间，瓶颈主要在于网络的 IO 消耗, 优化主要有两个方向:

- 提高网络 IO 性能，典型的实现比如使用 DPDK 来替代内核网络栈的方式
- 使用多线程充分利用多核，典型的实现比如 Memcached。

协议栈优化的这种方式跟 Redis 关系不大，支持多线程是一种最有效最便捷的操作方式。所以总结起来，redis支持多线程主要就是两个原因：

- 可以充分利用服务器 CPU 资源，目前主线程只能利用一个核
- 多线程任务可以分摊 Redis 同步 IO 读写负荷

##### Redis6.0 采用多线程后，性能的提升效果如何

Redis 作者 antirez 在 RedisConf 2019分享时曾提到：Redis 6 引入的多线程 IO 特性对性能提升至少是一倍以上。国内也有大牛曾使用unstable版本在阿里云esc进行过测试，GET/SET 命令在4线程 IO时性能相比单线程是几乎是翻倍了，详情见[https://zhuanlan.zhihu.com/p/76788470](https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F76788470)

##### Redis6.0 多线程实现机制

![img](https:////upload-images.jianshu.io/upload_images/11313361-4e8a710353fe4377.png?imageMogr2/auto-orient/strip|imageView2/2/w/623/format/webp)

多线程处理流程



1、主线程负责接收建立连接请求，获取 socket 放入全局等待读处理队列
 2、主线程处理完读事件之后，通过 RR(Round Robin) 将这些连接分配给这些 IO 线程
 3、主线程阻塞等待 IO 线程读取 socket 完毕
 4、主线程通过单线程的方式执行请求命令，请求数据读取并解析完成，但并不回写
 5、主线程阻塞等待 IO 线程将数据回写 socket 完毕
 6、解除绑定，清空等待队列

该设计有如下特点：

- IO 线程要么同时在读 socket，要么同时在写，不会同时读或写
- IO 线程只负责读写 socket 解析命令，不负责命令处理

### Proxy

针对 Cluster 的代理，这么多年了，仍然有不少人在Cluster的接入方式上挣扎，因为缺少合适的驱动而无法使用Cluster。所以开发了这个Proxy功能。作者也强调，虽然这个Proxy 让 Cluster 拥有了像单实例一样的接入方式，但是本质上还是 Cluster，不支持的命令还是不会支持，比如跨 slot 的多Key操作。
 其实社区早已有过不少 Proxy 方面的尝试，而且有些做的还不错。那么这个官方的 Proxy 究竟会给我们带来什么惊喜呢？还是让我们拭目以待吧。

### Disque

这个本来是作者几年前开发的一个基于 Redis 的消息队列工具，但多年来作者发现 Redis 在持续开发时，他也要持续把新的功能合并到这个Disque 项目里面，这里有大量无用的工作。因此这次他在 Redis 的基础上通过 Modules 功能实现 Disque。

如果业务并不需要保持严格消息的顺序，这个 Disque 能提供足够简单和快速的消息队列功能。