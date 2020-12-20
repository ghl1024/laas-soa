# ZooKeeper管理员指南

## 部署

这部分包含了部署ZooKeeper的信息和覆盖这些话题

- 系统要求
- 集群(多服务)安装
- 单服务和开发者安装

前两部分假定你对在例如数据中心的生产环境安装ZooKeeper有兴趣。最后一部分包含你在一个有限的基础上安装ZooKeeper的情况 - 为了评估，测试，或者开发 - 但是不在生产环境 。

## 系统要求

支持的平台

ZooKeeper由多个组件组成。 一些组件被广泛支持，其他组件仅在较小的一组平台上受支持。

- 客户端是Java客户端库，由应用程序用于连接到ZooKeeper集合。
- 服务器是在ZooKeeper集合节点上运行的Java服务器。
- Native Client是C中实现的客户端，类似于Java客户端，由应用程序用于连接到ZooKeeper系统。
- Contrib是指多个可选的附加组件。

以下矩阵描述了在不同操作系统平台上运行每个组件的承诺级别。

| 操作系统  | 客户端     | 服务器     | 原生客户端 | 控制       |
| :-------- | :--------- | :--------- | :--------- | :--------- |
| GNU/Linux | 开发与生产 | 开发与生产 | 开发与生产 | 开发与生产 |
| Solaris   | 开发与生产 | 开发与生产 | 不支持     | 不支持     |
| FreeBSD   | 开发与生产 | 开发与生产 | 不支持     | 不支持     |
| Windows   | 开发与生产 | 开发与生产 | 不支持     | 不支持     |
| Mac OS X  | 仅开发     | 仅开发     | 不支持     | 不支持     |

对于未明确提到的矩阵中支持的任何操作系统，组件可能会也可能不起作用。 ZooKeeper社区将修复为其他平台报告的明显错误，但没有完全支持。

软件要求

ZooKeepr运行在java 发行版本1.6或更高(JDK 6 或更高，FreeBSD支持需要openjdk7)。它作为一个ZooKeeper服务器集成运行。三个ZooKeeper服务端是建议的集群最小了数量，我们也建议他们运行在不同的机器上。在Yahoo!，ZooKeeper通常被布置在专用的RHEL上面。一个双核的处理器，2GM的内在，和80G的硬盘。

## 集群(多个服务端)安装

为了ZooKeeper服务更可靠，你应该在集群中部署ZooKeeper,只要集群中的大多数运行起来，服务就是可用的。因为ZooKeeper需要一个大多数，最好用一个奇数的机器。例如，用四台机器ZooKeeeperk只能处理一个机器故障。如果两台机器失效，剩下的两台不能组成大多数。然而，用五台机器ZooKeeper可能处理2台机器失效。

|      | 就像在入门指南中提到的，最少需要三个服务端对于一个容错集群安装，并且强烈建议你有奇数个服务端。通常三台服务端对生产环境安装是够的，但是在维护期间为了最大化的可靠性，你可能想要安装五台服务端。对于三台服务端，如果你在其中一台上执行维修，在维修期间其中一台将会是容易失效的。如果你有五台运行的服务，你可以让一台停掉来维修。并且知道如果其它四台中和一台突然失效也是ok的。你的冗余考虑应该包含你的环境的所有方面。如果你有三个ZooKeeper服务端，但是他们的网线都插入到同一个网络交换机上面，那么交换机的失败将挂掉你整个集群。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

这里是安装集群中一个服务端的步骤。这些步骤应该在集群中的每一个主机上执行:

1. 安装Java JDK。你可以使用本地的系统包，或从http://java.sun.com/javase/downloads/index.jsp下载

2. 设置Java 堆大小。这对于避免交换很重要。交换将严重降低ZooKeeper的性能。为了决定正确的。使用压力测试，并且确保引起交换的限制的下面。保守起见 - 对于4G内在的机器，使用最多3G的堆内存。

3. 安装ZooKeeper服务端安装包。它可以从http://ZooKeeper.apache.org/releases.html 下载。

4. 创建配置文件。这个文件可以是任何名字。使用下面的设置作为开始:

   ```Properties
   tickTime=2000
   dataDir=/var/lib/ZooKeeper/
   clientPort=2181
   initLimit=5
   syncLimit=2
   server.1=zoo1:2888:3888
   server.2=zoo2:2888:3888
   server.3=zoo3:2888:3888
   ```

   你可以找到这些和其它设置的含义在Configuration Parameters部分。

   每一个机器是ZooKeeper集群的一部分。他们应该知道集群中的其它机器。你使用server.id=host:port:port这样的形式来达到这样的目的。参数host和port是直观的。你通过创建一个名字为myid的文件来区分每一台机器的服务id,每一服务端一个，它放在服务端的配置文件指定的dataDir的参数的数据目录下。

5. myid文件包含一个单行文本，它的值是机器的id。所以服务端1的myid将包含文本"1"而没有其它。这个id必须在集群中是唯一的并且是一个1到255之间的值。

6. 如果您的配置文件已设置，您可以启动ZooKeeper服务器：

   ```SH
   $ java -cp ZooKeeper.jar：lib / slf4j-api-1.7.5.jar：lib / slf4j-log4j12-1.7.5.jar：lib / log4j-1.2.17.jar：conf \ org.apache.ZooKeeper。 server.quorum.QuorumPeerMain zoo.cfg
   ```

   QuorumPeerMain启动ZooKeeper服务器，JMX管理bean也被注册，允许通过JMX管理控制台进行管理。 ZooKeeper JMX文档包含有关使用JMX管理ZooKeeper的详细信息。

   有关启动服务器实例的示例，请参阅发行版中包含的脚本bin / ZooKeeperServer.sh。

7. 通过连接到主机来测试您的部署：

   在Java中，您可以运行以下命令来执行简单的操作：

   ```SH
   $ bin / zkCli.sh -server 127.0.0.1:2181
   ```

## 单一服务器和开发者安装

如果你为了开发目的安装ZooKeeper。你将可能想安装一个ZooKeeper的服务实例，然后安装Java或c的客户端库在你的开发机器上。

安装一个服务实例的步骤和上面的相似，除了配置文件更简单。你可以找到完整的操作指南在ZooKeeper Getting Started Guide的 Installing and Running ZooKeeper in Single Server Mode部分。

更多关于安装客户端库的信息，参考 ZooKeeper Programmer’s Guide的 Bindings部分

## 管理

这部分包含关于运行和维护ZooKeeper的信息并且包含这些主题：

- 设计一个ZooKeeper部署
- 准备
- 考虑的事：ZooKeeper的长处和局限性
- 管理
- 维护
- 监督
- 监测
- 日志
- 故障排除
- 配置参数
- ZooKeeper命令
- 数据文件管理
- 避免的事
- 最佳实践

### 设计一个ZooKeeper部署

ZooKeeper的可靠性基于两个假设。

1. 只有部署中的一小部分将失效。在这里失效是指机器崩溃，或网络的一些问题使一个服务端和其它的隔离开来。
2. 正确地部署机器。正确操作是正确地执行代码，使时间正常地工作，并且使存储和网络组件执行一致。

下面包含的部分对于ZooKeeper管理员来说是最大限度地认为这些假设是成立的。一些是跨机器的考虑，其它是一些你应该为每一台机器考虑的事情。

跨机器的要求

为了做ZooKeeper服务活跃，必须有大多数的机器可以彼此通信。为了构建一个可以容忍F台机器失效的部署，你应该部署2×F+1台机器。因此，一个包含三台机器的部署可以处理一个失效，一外包含5台机器的部署可以处理2台失效。注意一个6台机器的部署只能处理2个失效因为3台机器不是大多数。因为这个原因，ZooKeeper部署通常由奇数个机器组成。

为了达到最大可能地容忍失效，你应该试着使机器失效独立地。例如，如果大部分机器用相同的交换机，交换机的失效将引起相互关联的失效并且使服务挂掉。对于使用相同的电源，空调系统也一样。

单机要求

如果ZooKeeper不得不和其它应用竞争像存储设置，CPU,网络或内在的资源，它的性能将受到显著影响。ZooKeeper具有很强的持久性保证，这意为它使用存储设置来记录改变在负责改变的操作完成之前。你应该意识到这个依赖，并且照顾好它，如果你想保证ZooKeeper的操作不被你的存在设置挂起。这里有一些你可以做的事情来减小这种下降。

- ZooKeeper的事务日志必须在一个专门的设备上(一个专门的分区是不够的)ZooKeeper顺序地写日志，没有寻找，共享你的日志设备和其它进程可能引起寻找和竞争，这可能导致几秒的延迟。
- 不要把ZooKeeepr放到一个引起交换的位置。为了使ZooKeeper运行的及时性，简单地不能允许它交换。因些，确保给ZooKeeper分配最大堆的大小不比真实的内存大。关于这点的更多内容，参考下面的 Things to Avoid。

## 供应

## 需要考虑的事项：ZooKeeper的优点和局限性

## 管理

## 维护

对于ZooKeeper的集群的长时间的维护是必要的，然而你必须注意以下事情：

正在进行的数据目录清理

ZooKeeper的数据目录包含的文件是存储在特定服务集群中的znode的持久化副本。他们是快照和事务日志文件。当对znode做了改变，这些改变被附加到一个事务日志里，有时候，当一个日志增大，当前所有 znode的状态的快照将被 写到文件系统中。这个快照取代所有先前的日志。

ZooKeeper服务端将**不会删除老的快照和日志文件**。当使用默认的配置时(参考下面的自动清除)，这是操作者的责任。每一个服务端环境是不同的因此管理这些文件的要求也不尽相同(例如备份)。

PurgeTxnLo工具实现了一个管理者可以使用的简单的保留策略。API文档包含了调用规则的详细信息(参数，等等)。

在下面的例子最后几个快照和他们相应的日志被保留并且其它的被删除。<count>的值通常应该大于3(尽管不是很必要,这提供了三个备份,在不可能的情况下，最近一个已经被破坏)。这可以在ZooKeeper服务端的机器上运行一个定时任务来每天清除日志。

```SH
java -cp ZooKeeper.jar:lib/slf4j-api-1.7.5.jar:lib/slf4j-log4j12-1.7.5.jar:lib/log4j-1.2.16.jar:conf org.apache.ZooKeeper.server.PurgeTxnLog <dataDir> <snapDir> -n <count>
```

自动清除快照和它对应的日志文件在ZooKeeper3.4中被引入并且可以通过下面的参数开启。**autopurge.snapRetainCount** 和**autopurge.purgeInterval**，关于这方面更多信息，请参考下面的Advanced Configuration。

调试日志清除(log4j)

参考这个文档关于logging的部分。它假设你使用log4j内置的特性设置一个滚动文件附加器。。conf/log4j.properties里的配置例子提供了这样的一个例子。

## 监督

你将想要一个监督进程来管理你所有的ZooKeeper服务端进程，ZooKeeper服务端被设计成快速失败的。意为着它将关闭(进程退出)如果它遇到一个不能恢复的错误。一个ZooKeeper服务集群是高度可靠的，意为着它当一个服务挂掉的时候，集群作为一个整体还是可以活跃和处理请求。另外，因为集群是"自治愈的"，失效的服务端启动后将自动地加入集群而不任何人为干预。

管理进程如daemontools或SMF（其他监控过程的选项也可以使用，由您自己决定使用哪一个，这仅仅是两个示例），管理您的ZooKeeper服务器可确保如果进程异常退出，将自动重新启动，并将快速重新加入群集。

如果发生OutOfMemoryError，还建议将ZooKeeper服务器进程配置为终止并转储其堆。这通过在Linux和Windows上分别启动具有以下参数的JVM来实现。 ZooKeeper随附的ZooKeeperServer.sh和ZooKeeperServer.cmd脚本设置了这些选项。

```SH
-XX:+HeapDumpOnOutOfMemoryError -XX:OnOutOfMemoryError='kill -9 %p'
"-XX:+HeapDumpOnOutOfMemoryError" "-XX:OnOutOfMemoryError=cmd /c taskkill /pid %%%%p /t /f"
```

## 检测

ZooKeeper服务可以被检测用两种主要的方式；1)通过使用4字母单词的命令 2)JMX参考适当的部分为你的需求。

## 日志

ZooKeeper使用SLF4J版本1.7.5作为其日志记录基础设施。 为了向后兼容，它绑定到LOG4J，但您可以使用LOGBack或您选择的任何其他支持的日志记录框架。

ZooKeeper默认log4j.properties文件驻留在conf目录中。 Log4j要求log4j.properties位于工作目录（运行ZooKeeper的目录）或可从类路径访问。

有关SLF4J的更多信息，请参阅其手册。

有关LOG4J的更多信息，请参阅log4j手册的Log4j默认初始化过程。

## 故障排除

服务没有起来因为文件损坏

```
一个服务可能不能读它的数据库并且不能启动因为一些ZooKeeper服务的事务日志文件损坏。你将看到一些IOException在载入ZooKeeper数据库的时候。在这样的情况下，确保你集群中所有其它服务端启动起来并且工作。在命令端口使用“stat”命令查看是否他们处于健康状态。在你检测所有其它服务端都起来后，你可以继续并且清理坏掉的服务端的数据库。删除datadir/version-2目录下的所有文件和datalogdir/version-2/。重启服务。
```

## 配置参数

ZooKeeper的行为由ZooKeeper的配置文件支配。这个文件被设计，所以完全相同的文件可以被ZooKeeper集群中的所有服务端使用，假设他们的硬盘分布是一样的。如果服务端使用不同的配置文件，必须特别小心确保所有的服务端和他们的配置文件想匹配。

|      | 在3.5和最新的,其中一些参数应该被放在动态配置文件中，如果他们放在静态的配置文件中，ZooKeeper将自动地把他们移动到动态配置文件中。参考Dynamic Reconfiguration来获取更多的信息。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

最小配置

这里是在配置文件中必须被定义的最小的配置关键字：

- clientPort

  监听客户端连接的端口;也就是说，客户端试图连接的端口

- secureClientPort

  使用SSL侦听安全客户端连接的端口。 **clientPort**指定明文连接的端口，而**secureClientPort**指定SSL连接的端口。 指定两者都启用混合模式，同时省略或者将禁用该模式。请注意，当用户插入ZooKeeper.serverCnxnFactory，ZooKeeper.clientCnxnSocket作为Netty时，将启用SSL功能。

- dataDir

  ZooKeeper将存储内在数据库快照的地方，除非另外指定，也是数据库更新的事务日志的地方。小心你在那里放你的事务日志。一个专门的事务日志存储设备是一致好性能的关键。把日志放到忙的设置上将严重影响性能。

- tickTime

  一个tick的长度，ZooKeeper使用的最基本的时间单位，以毫秒为单位。它被用来管理心跳，超时。例如，最小的会话超时是两个tick.

高级配置

这部分的配置是可选的。你可以使用他们进一步地调试ZooKeeper服务端的行为。其中一些可以使用Java系统参数来设置，通常以ZooKeeper.keyword的格式。对于系统参数，当可用时，被标注出来在下面。

- dataLogDir

  (不是Java系统参数)这个选项将指导机器写事务日志到**dataLogDir**而不是**dataDir**。这允许一个专门的日志设备被使用，并且帮助避免在日志和快照之间的冲突。有一个专门的日志设备对吞吐量和延迟有一个大的影响。强烈建议指定一个日志设备并且设置dataLogDir来指到这个设备的目录，并且确保dataDir的目录不是在这个设备上。

- globalOutstandingLimit

  （Java system property: **ZooKeeper.globalOutstandingLimit**）客户端可以更快地提交请求比ZooKeeper处理他们，特别是有很多客户端的时候。为了避免因为排队的请求使ZooKeeper内在溢出，ZooKeeper将控制客户端，使在系统中没有多于globalOutstandingLimit 个没有处理的请求。默认的限制是1000。

- preAllocSize

  （Java system property: **ZooKeeper.preAllocSize**）为了避免以preAllocSize千字节的块寻找ZooKeeper分配空间在事务日志文件。默认的块大小是64M。改变这个块大小的原因是减小块大小如果快照被经常拿走。（同时参考snapCount）.

- snapCount

  (Java system property: **ZooKeeper.snapCount**)ZooKeeper记录事务到一个事务日志中。在snapCount个事务被写入到一个日志文件中，一个快照被开始一个新的事务日志文件被创建。默认的snapCount 是100000。

- maxClientCnxns

  (No Java system property)限制被IP地址标识的一个客户端同时连接的数量。这被用来阻止DoS一类的攻击。包含文件描述符消耗。默认的是60。设置为0就公完全地删除了同时连接的数量限制。

- clientPortAddress

  **3.3.0新增内容**：监听客户连接的地址(ipv4,ipv6或者主机名);也就是说，客户端试图连接的地址。这是可选的，默认地我们以这样的方式绑定，任何到**clientPort**的连接将被服务端接受。

- minSessionTimeout

  (No Java system property)3.3.0新增内容，服务端允许的客户端最小的会话超时时间。默认是2倍的tickTime.

maxSessionTimeout(No Java system property)

**3.3.0新增内容**：服务端允许的客户端最大的会话超时时间。默认是20倍的**tickTime**.

- fsync.warningthresholdms

  (Java system property: **fsync.warningthresholdms**)**3.3.4新增内容**：当fsync事务日志花费时间超过这个值，将输出一个警告信息到日志文件中。这个被默认是1000毫秒。这个值只能作为系统参数被设置。

- autopurge.snapRetainCount

  (No Java system property)**3.4.0新增内容**：当启用的时候，ZooKeeper自动清除特性保留最近的**autopurge.snapRetainCount**个快照和相应的事务日志并且删除其它的在**dataDir**和**dataLogDir**。默认是3。最小值是3。

- autopurge.purgeInterval

  (No Java system property)**3.4.0新增内容**：清除任务被触发的以小时为间隔的时间。设置一个正数(1以上)来启用自动清除特性。默认是0。

- syncEnabled

  (Java system property: **ZooKeeper.observer.syncEnabled**)**3.4.6，3.5.0新增内容**：观察者记录事务并且写快照到磁盘上就像一个参与者。这减小了重启时观察者的恢复时间。设置“false”来关闭这个特性。默认是true.

集群选项

这部分的选项是为集群使用设置的 — 也就是说，部署服务集群。

- electionAlg

  (No Java system property)使用的选举实现。0值对应着原来UDP-based版本。1对应着 快速领导选举的non-authenticated UDP-based的版本。2对应着快速领导选举的authenticated UDP-based的版本。3对应着快速领导选举的TCP-based版本。当前，3是默认的。

|      | 0,1,2的领导选举的实现已经过时。在下一个版本我们打算删除它们，那时只有 FastLeaderElection 可用。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

- initLimit

  (No Java system property)时间的值，以ticks为单位（参考tickTime）,允许追随者与领导者连接和同步。如果需要增加这个值，如果被ZooKeeper管理的数据量比较大。

- leaderServes

  (Java system property: ZooKeeper.**leaderServes**)领导者接受客户端连接。默认值是“yes”。领导者机器协调更新。为了更高的更新吞吐量同步，领导者可以被设置成不接受接受客户端连接并且集中协调。这个选项的默认值是yes,意为领导者接受客户端连接。

|      | 开启领导者选择是强烈建议的，当在你的集群当中有多于三台ZooKeeper的时候。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

- server.x=[hostname]:nnnnn[:nnnnn]等等

  (No Java system property)组成ZooKeeper集群的服务端。当服务端启动。它确定它是那一台服务器通过在数据目录中寻找myid文件。这个文件包含服务号，并且它应该和这个配置左边的**server.x**的**x**项匹配。组成ZooKeeper集群的客户端使用服务列表必须和每一个ZooKeeper服务端拥有的服务列表相匹配。这里有两个端口号**nnnnn**。第一个追随者用来连接领导者，每二个是为了领导者选举。领导选举的端口只有在electionAlg是1，2，或3的时候才是必须的。如果electionAlg是0，第二个端口不是必须的。如果你想在一台机器上测试 多个服务，那么不同的端口可以被每一个服务端使用。

- syncLimit

  (No Java system property)时间数量，以ticks为单位，允许追随者和ZooKeeper同步，如果追随者和领导者拉开距离太大，它们将被丢掉。

group.x=nnnnn[:nnnnn]

(No Java system property)

\+ 启用分层法定人数结构。“x"是一个组标识符，并且”=“后面的数字和服务器标识符对应。左边的是一个冒号分割的服务标识号。注意组必须不相交的，并且所有组的单位必须是ZooKeeper集群。

\+ 你也可以在这里找到例子

- weight.x=nnnnn

  (No Java system property)和”group“一块使用，在组成法定人数的时候给一个服务端分配一个权重。当投票的时候这个值和服务端的重要程序相对应。有一部分ZooKeeper要求投票例如领导者选择和原子传播协议。默认的一个服务端的权重是1。如果配置了组，而不是权重，那么1的值将分配给所有的服务端。你可以在这里找到 [例子](https://zookeeper.apache.org/doc/trunk/ZooKeeperHierarchicalQuorums.html)。

- cnxTimeout

  (Java system property: ZooKeeper.cnxTimeout)设置为领导者选举通知打开连接的超时时间。只在如果你的electionAlg为3的时候才是可用的。默认值是5秒

- standaloneEnabled

  (No Java system property)**3.5.0新增内容**：当设置false的时候，一个单独的服务端可以以复制模式启动，一个参与者可以和观察者运行，并且一个集群可以重新配置为一个节点，并且从一个节点启动。这个默认值是true为了向后兼容。它可以被设置通过QuorumPeerConfig的setStandaloneEnabled方法，或通过在服务端的配置文件中增加 "standaloneEnabled=false" 或 "standaloneEnabled=true"。

认证和授权选项

这部分的选项可能控制被服务端执行的认证和授权。

- ZooKeeper.DigestAuthenticationProvider.superDigest

  (Java system property only: **ZooKeeper.DigestAuthenticationProvider.superDigest**)默认这个特性是**关闭**的**3.2中新增内容**：允许ZooKeeper集群管理者访问znode分层结构作为超级用户。特别是被授权为超级用户没有ACL检查。org.apache.ZooKeeper.server.auth.DigestAuthenticationProvider可以被用来生成superDigest，用一个参数"super:<password>"调用它。提供生成的 "super:<data>"作为系统参数当启动每一个集群中的服务端。当授权(从ZooKeeper客户端)一个ZooKeeper服务端传递一个"digest"的方案和"super:<password>"的授权数据时。注意digest auth以明文传递authdata给服务端，这应该谨慎使用这个授权方法在localhost(不通过网络)或通过一加密的连接。

- X509AuthenticationProvider.superUser

  (Java system property: **ZooKeeper.X509AuthenticationProvider.superUser**)采用SSL支持的方式，可以使ZooKeeper系统管理员以“超级”用户身份访问znode层次结构。 当此参数设置为X500主体名称时，只有具有该主体的经身份验证的客户端将能够绕过ACL检查并具有对所有znode的完全权限。

- ssl.keyStore.location and ssl.keyStore.password

  (Java system properties: **ZooKeeper.ssl.keyStore.location and ZooKeeper.ssl.keyStore.password**)指定包含用于SSL连接的本地凭据的JKS的文件路径以及解锁文件的密码。

- ssl.trustStore.location and ssl.trustStore.password

  (Java system properties: **ZooKeeper.ssl.trustStore.location and ZooKeeper.ssl.trustStore.password**)指定包含要用于SSL连接的远程凭据的JKS的文件路径，以及用于解锁文件的密码。

- ssl.authProvider

  (Java system property: **ZooKeeper.ssl.authProvider**)指定用于安全客户端身份验证的**org.apache.ZooKeeper.auth.X509AuthenticationProvider**的子类。 这在不使用JKS的证书密钥基础设施中很有用。 可能需要扩展**javax.net.ssl.X509KeyManager**和**javax.net.ssl.X509TrustManager**以从SSL堆栈获取所需的行为。 要将ZooKeeper服务器配置为使用自定义提供程序进行身份验证，请为自定义AuthenticationProvider选择一个方案名称，并将属性**ZooKeeper.authProvider**。[scheme]设置为自定义实现的完全限定类名称。 这将加载提供程序到ProviderRegistry。 然后设置此属性**ZooKeeper.ssl.authProvider = [scheme]**，该提供程序将用于安全身份验证。

实验性选项/特性

被现在认为是实验性的新特性。

- 只读模式的服务端

  (Java system property: **readonlymode.enabled**)**3.4.0中新增内容**：设置这个值为true来使服务端支持只读模式(默认是关闭的)。ROM允许请求ROM支持的客户端连接连接到一个服务端即使服务端可能被隔离了从法定人数中。在这个模式下，客户端将仍然读数据从ZooKeeper服务端，但是将不会写数据和看到从其它客户端的改变。更多信息请参考 ZooKeeper-784。

不安全的选项

下面的选项可能非常有用，但使用的时候要小心。第一个的风险和这个参考能做什么一块讲解。

- forceSync

  (Java system property: **ZooKeeper.forceSync**)在更新完成处理之前要求更新同步到事务日志上。如果这个选项设置为no,ZooKeeper将不要求更新被同步到设备上。

- jute.maxbuffer:

  (Java system property: **jute.maxbuffer**)这个选项只能被作为Java 系统参数设置。它不是ZooKeeper前缀。它指定了可以被存在在znode中的数据的值。默认是0xfffff,或小于1M.如果这个选项被改变，系统参数必须被设置到所有的服务端和客户端上，否则将会出现问题。这真是一个明智的检查。ZooKeeper被设计成存储以数据大小的顺序存储。

- skipACL

  (Java system property: **ZooKeeper.skipACL**)跳过ACL检查。这可以提高吞吐量。但是对数据树打开完全的访问给所有人。

- quorumListenOnAllIPs

  当设置成true,ZooKeeper 服务端将在所有可用的ip地址上监听所有的连接，并且不仅是在配置文件中的服务列表。它影响处理ZAB协议和快速领导者选举协议的连接。默认是false。

禁用数据目录自动创建

**3.5中新增内容**:ZooKeeper服务端的默认行为是在启动的时候如果没有不存在数据目录，将会自动创建数据目录。这可能是不方便的甚至是危险的在一些情况下。考虑这样的情况，在运行的服务端上改变了一个配置，**dataDir**参数意外地改变了。ZooKeeper服务端被重启后它将创建这个不存在的目录并且开始服务 - 用一个空的znode命名空间。这种情况可能导致"脑裂"(例如，数据同时存在新的不合法的目录和原来的合法数据存储)。像这样有一个关闭自动创建的行为选项将是好的。通常对于生产环境这这应该这样做。不幸的是默认的行为不能被改变现在，因此这必须在案例上进行。

当运行**ZooKeeperServer.sh**自动创建可以被关闭通过设置环境变量**ZOO_DATADIR_AUTOCREATE_DISABLE**为1。当直接从类文件运行ZooKeeper服务端这个可以被实现通过设置**ZooKeeper.datadir.autocreate=false**在java 命令行上，例如**-DZooKeeper.datadir.autocreate=false**

当这个特性被关闭，ZooKeeper服务端检测到需要的目录不存在，它将生成一个错误并拒绝启动。

一个新的**ZooKeeperServer-initialize.sh**被提供来支持这个新特性。如果自动创建被关闭，用户必须先安装ZooKeeper,然后创建数据目录(潜在的事务日志目录)，然后启动服务。否则，正如在前面提到服务将不会启动。运行**ZooKeeperServer-initialize.sh**将创建需要的目录，并且设置myid文件(可选的命令行参数)。这个脚本可以被使用即使自动创建特性没有被使用，并对用户来说有用当这个在过去是一个问题(安装，包括创建myid文件)。注意这个脚本只确保数据目录存在，它不创建配置文件，但是为了执行需要一个可用的配置文件。

性能调试选项

- 3.5.0中的新增内容：**几个子系统已经被重新设计来提高读吞吐量。这包括NIO通信的多线程子系统和请求处理通道(提交处理器)。NIO是默认的客户端/服务端通信 子系统。它的线程模型包括一个接受者线程，1-n个seleector线程和0-m socket I/O工作线程。在请求处理通道，系统可以被配置成一次处理多个读请求同时保证相同的一致性保证(相同的会话，写后读)。提交处理者线程模型包括一个主线程和0-n个工作线程。

默认值是目的是实现在ZooKeeper机器上最大化的读吞吐量。同时子系统需要足够数量的线程来达到高峰的志吞吐量。

- ZooKeeper.nio.numSelectorThreads

  (Java system property only: **ZooKeeper.nio.numSelectorThreads**)**3.5.0新增内容：**NIO selector线程数量。最少需要一个selector线程。建议使用多于一个selector对于大量的客户连接。默认值是sqrt( cpu核心数 / 2 )。

- ZooKeeper.nio.numWorkerThreads

  (Java system property only: **ZooKeeper.nio.numWorkerThreads**)**3.5.0新增内容：**NIO 工作者线程数量。如果被配置成0个工作者线程，selector线程直接使用socket I/O。默认值是2倍的cpu核心数。

- ZooKeeper.commitProcessor.numWorkerThreads

  (Java system property only: **ZooKeeper.commitProcessor.numWorkerThreads**)**3.5.0新增内容：**提交处理器工作线程的数量。如果配置成0个工作者线程，主线程将直接处理请求。默认值是cpu核心数量。

- znode.container.checkIntervalMs

  (Java system property only)**3.6.0中的新增：**每个候选容器节点检查的时间间隔（以毫秒为单位）。 默认值为“60000”。

- znode.container.maxPerMinute

  (Java system property only)**3.6.0中的新增功能：**每分钟可删除的最大容器节点数。 这样可以防止在删除容器时放牧 默认值为“10000”。

使用Netty框架来通信

Netty是一个基于NIO的客户端/服务端通信框架，它为Java应用简化(和直接使用NIO相比)了很多网络层通信的复杂性。另外Netty框架内置支持加密(SSL)和授权(certificates).这些是可选的特性，并且可以被单独地开启和关闭。

在3.5+版本中，ZooKeeper服务器可以使用Netty而不是NIO（默认选项），方法是将环境变量ZooKeeper.serverCnxnFactory设置为org.apache.ZooKeeper.server.NettyServerCnxnFactory; 对于客户端，将ZooKeeper.clientCnxnSocket设置为org.apache.ZooKeeper.ClientCnxnSocketNetty。

TBD(待定) - netty的调试选项 - 现在没有netty的配置选项但我们应该增加一些。例如netty创建的读工作者线程的最大值。

TBD - 怎么管理加密

TBD - 怎么管理证书

管理服务端配置

**3.5.0新增内容：**下面的选项用来设置 AdminServer

- admin.enableServer

  (Java system property: **ZooKeeper.admin.enableServer**)设置为false来关闭AdminServer。默认是开启的。

- admin.serverAddress

  (Java system property: **ZooKeeper.admin.serverAddress**)内置的Jetty服务监听的地址. 默认是 0.0.0.0.

- admin.serverPort

  (Java system property: **ZooKeeper.admin.serverPort**)内置的Jetty服务监听的端口。默认是8080。

- admin.idleTimeout

  (Java system property: **ZooKeeper.admin.idleTimeout**)设置连接在发送或接收数据之前可以等待的最大空闲时间（以毫秒为单位）。 默认为30000 ms。

- admin.commandURL

  (Java system property: **ZooKeeper.admin.commandURL**)用于列举和发起的和root URL相关的命令的URL。默认是"/commands"。

### ZooKeeper 命令

四字母的单词

ZooKeeper响应一组命令。每一个命令由四个字母组成。你在客户端口通过telnet或nc发送命令给ZooKeeper。

三个更有趣的命令：‘stat’给出一些一般信息关于服务端和连接的客户端，"srvr"和"cons"给出更详细的信息关于服务端和客户端。

- conf

  **3.3.0新增：**打印服务端配置的详细信息。

- cons

  **3.3.0新增:** 列出连接到这个服务端的所有客户端会话信息。包括发送和接收包的数量信息，会话id,操作延迟，最后执行的操作等等。

- crst

  **3.3.0新增:** 重置所有连接的会话

- dump

  列出未处理的会话和临时节点。这只在领导者上可用。

- envi

  打印服务端的详细信息

- ruok

  检测如果服务端运行在一个没有错误的状态。服务端将响应imok如果它正在运行。否则它将不会响应。"imok"的响应不能表示服务端已经加入了法定人数。仅仅是服务进程是活跃的和绑定到了指定的客户端口。使用"stat"来查看关于法定人数和客户端连接的详细信息。

- srst

  重置服务端的统计

- srvr

  **3.3.0新增:** 列出服务端的详细信息

- stat

  列出端和连接的客户端的简明信息

- wchs

  **3.3.0新增:** 列出服务端的监视器的简明信息

- wchc

  **3.3.0新增:** 列出服务端的监视器的详细信息，以会话分组。这输出一个带着相关监视器的会话列表。注意，根据监视器的数量，这个操作可能很耗时(也就是说影响服务端性能)，小心使用它。

- dirs

  **3.5.1新增：**以字节为单位显示快照和日志文件的总大小

- wchp

  **3.3.0新增:** 列出服务端关于监视器的详细信息，以路径分组。这输出一个带着相关会话的路径信息。注意，根据监视器的数量，这个操作可能很耗时(也就是说影响服务端性能)，小心使用它。

- mntr

  **3.3.0新增:** 输入可以被用来监视群集健康状态的变量列表。 复制代码`$ echo mntr | nc localhost 2185               ZooKeeper_version  3.4.0              ZooKeeper_avg_latency  0              ZooKeeper_max_latency  0              ZooKeeper_min_latency  0              ZooKeeper_packets_received 70              ZooKeeper_packets_sent 69              ZooKeeper_outstanding_requests 0              ZooKeeper_server_state leader              ZooKeeper_znode_count   4              ZooKeeper_watch_count  0              ZooKeeper_ephemerals_count 0              ZooKeeper_approximate_data_size    27              ZooKeeper_followers    4                   - only exposed by the Leader              ZooKeeper_synced_followers 4               - only exposed by the Leader              ZooKeeper_pending_syncs    0               - only exposed by the Leader              ZooKeeper_open_file_descriptor_count 23    - only available on Unix platforms              ZooKeeper_max_file_descriptor_count 1024   - only available on Unix platforms`输出兼容java属性格式并且内容随着时间可能有变化(加入新关键词)。注意：一些关键词是平台有关的并且一些关键词只对领导者暴露。输出包含多行，以下面的格式：`key \t value`

- isro

  **3.4.0中的新功能：**测试服务器是否以只读模式运行。如果处于只读模式，则服务器将以“ro”响应，如果不是只读模式，则将“rw”响应。

- gtmk

  获取当前跟踪掩码为十进制格式的64位带符号长整型值。请参阅stmk了解可能的值。

- stmk

  设置当前跟踪掩码。跟踪掩码为64位，其中每个位启用或禁用服务器上的特定类别的跟踪记录。必须将Log4J配置为首先启用TRACE级别才能查看跟踪记录消息。跟踪掩码的位对应于以下跟踪日志记录类别。Table 2. 跟踪掩码位值掩码描述0b0000000000未使用，保留供将来使用。0b0000000010记录客户端请求，不包括ping请求。0b0000000100未使用，保留供将来使用。0b0000001000记录客户端ping请求。0b0000010000记录从当前领导者的仲裁对等体接收到的数据包，不包括ping请求。0b0000100000日志添加，删除和验证客户端会话。0b0001000000记录将事件发送到客户端会话。0b0010000000记录从当前引导者的仲裁对等体接收到的数据包。0b0100000000未使用，保留供将来使用。0b1000000000未使用，保留供将来使用。64位值中的所有剩余位都未使用，并保留供将来使用。通过计算记录值的按位OR来指定多个跟踪记录类别。默认跟踪掩码为0b0100110010。因此，默认情况下，跟踪日志记录包括客户端请求，从领导和会话接收的数据包。要设置不同的跟踪掩码，请发送一个包含stmk四字母字的请求，后跟跟踪掩码表示为64位带符号的长整型值。此示例使用Perl包函数构建一个跟踪掩码，该跟踪掩码启用上述所有跟踪日志记录类别，并将其转换为具有大字节顺序的64位带符号长整型值。结果附加到stmk并使用netcat发送到服务器。服务器以十进制格式响应新的跟踪掩码。$ perl -e“print’stmk'，pack（'q>'，0b0011111010）”| nc localhost 2181 250

这里有一个**ruok**的命令例子：

+

```SH
$ echo ruok | nc 127.0.0.1 5111
        imok
```

AdminServer

**3.5.0新增内容：** AdminServer是一个内置的Jettry服务，它提供了一个HTTP接口为四字母单词命令。默认的，服务被启动在8080端口，并且命令被发起通过URL "/commands/[command name]",例如，http://localhost:8080/commands/stat。命令响应以JSON的格式返回。不像原来的协议，命令不是限制为四字母的名字，并且命令可以有多个名字。例如"stmk"可以被指定为"set_trace_mask"。为了查看所有可用命令的列表，指向一个浏览器的URL /commands (例如， http://localhost:8080/commands)。参考 AdminServer configuration options关于怎么改变端口和URLS。

AdminServer默认开启，但是可以被关闭通过下面的方法： * 设置系统属性ZooKeeper.admin.enableServer为false. * 从类路径中移除Jetty.(这个选项是有用的如果你想覆盖ZooKeeper的jetty依赖)。

注意TCP四字母单词接口是仍然可用的如果AdminServer被关闭。

### 数据文件管理

ZooKeeper存储它的数据在数据目录和它的事务日志在事务日志目录里，默认的这两个目录是相同的。服务端可以(应该)被配置成存储事务日志文件到一个单独的目录而不是数据文件目录。吞吐量上升和延迟减小当事务日志放在一个专门的日志设置上。

数据目录

这个目录有两个文件：

| myid            | - 包含一个单独的代表服务器id的数字 |
| --------------- | ---------------------------------- |
| snapshot.<zxid> | - 保存数据树的快照                 |

每一个ZooKeeper服务端有一个唯一的id。这个id被用在两个地方：myid文件和配置文件中。myid文件标识给定数据目录的服务端。配置文件列出联系信息为每一个被它的服务id标识的服务端。当一个ZooKeeper服务端实例启动的时候，它从myid文件中读它的id，然后使用这个id,从配置文件读取找出它应该监视的端口，

存在数据目录中的snapshot文件是模糊的快照，在这个意义上，在ZooKeeper服务端正在操作快照的时间内，更新也正在发生在数据树上。snapshot文件的后缀是zxid，ZooKeeper的最后提交的事务id。因此snapshot包含对数据树更新的一个字集在snapshot正在处理中的时候。snapshot可能不对应任何真实存在的数据树，因为这个原因我们说它是模糊的快照。仍然ZooKeeper可以恢复使用这个快照因为它使用了更新的幂等特性。通过重新演义事务日志对模糊的快照，ZooKeeer获取系统的状态在日志的最后。

日志目录

日志目录包含ZooKeeper的事务日志。在任何更新发生之前，ZooKeeper确保代表这个更新的事务被写入到存储上。一个新的日志文件被开始每次一个快照被开始。日志文件的后缀写到日志的第一个zxid。

文件管理

快照和日志文件格式不会改变在单独的ZooKeeper服务器和不同配置的可复制的ZooKeeper服务器之间。因此，你可以从一个运行的可复制的ZooKeeper服务端把这个文件放到一个单机的ZooKeeper服务端的开发机器上来故障排除。

使用老的日志和快照文件，你可以找到先前的ZooKeeper服务端状态甚至恢复这个状态。 LogFormatter 类允许一个管理者来查看一个日志中的事务。

ZooKeeper服务端创建快照和日志文件，但是从不删除他们。数据和日志文件的保留策略被实现在ZooKeeper服务端之外。服务端自己只需要最新完整的模糊快照和从快照开始的日志文件。参考这个文档的 maintenance部分关于设置保留策略和ZooKeeper存储的更详细信息。

|      | 这个文件中存的数据没有被加密。在ZooKeeper中存储敏感数据的情况下，需要采取必要的方法来防止未授权的访问。这些方法是外部的对ZooKeeper来说。它取决于ZooKeeper部署的机器的单独设置。 |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

### 应该避免的事

这里有一些你可以通过正确设置配置文件来避免的普遍的问题：

- 不一致的服务端列表

  被客户端使用的服务端列表必须和每一个ZooKeeper服务端拥有的服务端列表相匹配。如果客户端列表是一个真实列表的子集工作能正常进行。但事情将很奇怪如果客户端有一个服务端列表和ZooKeeper集群的不一样。同时在每一个ZooKeeper服务端配置文件中的服务端列表应该彼此一样。

- 事务日志的不正确存放

  ZooKeeper性能最关键的部分是事务日志。ZooKeeper同步事务日志到存储设置上在它返回一个响应之前。一个专门的事务日志设置是一贯好性能的关键。把日志放到一个繁忙的劥上将严重地影响性能。如果你只有一个存储设备，在NFS上存入追踪文件并且 减小snapshotCount;它不能消除问题，但是能减轻它。

- 不正确的Java 堆大小

  你应该特别小心，来正确地设置你的Java最大堆大小。特别是你不应试使用ZooKeeper交换到磁盘。磁盘对ZooKeeper来说是致命的。所有事都是有序的，所以如果处理一个请求交换磁盘，所有其它队列中的请求将可能做同样的事。对于磁盘，不要交换。

在你的估计中保持保守：如果你有一个4G的内在，不要设置Java最大堆大小为6G或4G，例如，你更应该使用一个3G的堆对于一个4G的机器，因为操作系统和缓存也需要内存。最好的和只是建议的行为来估计你的系统需要的堆大小是运行压力测试，然后确保正好在可能引起系统交换的使用限制下面。

### 最佳实践

为了最好的结果，重视下面ZooKeeper的最佳实践列表：

对于多用户安装参考这个部分详述ZooKeeper"chroot"支持，这非常有用当部署多个应用接口到一个单独的ZooKeeper群集中。