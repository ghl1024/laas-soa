# ZooKeeper 动态重新配置



- [Overview](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_intro)
- [更改配置格式](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_format)
- [指定 Client 端端口](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_clientport)
  - [standaloneEnabled 标志](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_standaloneEnabled)
  - [reconfigEnabled 标志](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_reconfigEnabled)
  - [动态配置文件](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_file)
  - [Backward compatibility](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_backward)
- [升级到 3.5.0](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_upgrade)
- [ZooKeeper 合奏的动态重新配置](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_dyn)
- [API](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_api)
  - [Security](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_access_control)
  - [检索当前动态配置](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_retrieving)
  - [修改当前动态配置](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_modifying)
- [General](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_general)
  - [Incremental mode](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_incremental)
  - [Non-incremental mode](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_nonincremental)
  - [Conditional reconfig](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_conditional)
  - [Error conditions](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_errors)
  - [Additional comments](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_additional)
- [重新平衡 Client 端连接](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_rebalancing)



## Overview

在 3.5.0 发行版之前，Zookeeper 的成员资格和所有其他配置参数是静态的-在引导过程中加载，并且在运行时不可变。运算符诉诸“滚动重启”-一种手动密集型且易于出错的更改配置的方法，该配置已导致数据丢失和 Producing 的不一致。

从 3.5.0 开始，不再需要“滚动重启”！ ZooKeeper 完全支持自动配置更改：可以动态更改 Zookeeper 服务器的集合，它们的角色(参与者/观察者)，所有端口，甚至仲裁系统，而不会中断服务并保持数据一致性。就像 ZooKeeper 中的其他操作一样，可以立即执行重新配置。可以使用单个重新配置命令来进行多个更改。动态重新配置功能不限制操作并发性，不需要在重新配置期间停止 Client 端操作，对 Management 员而言界面非常简单，并且不会给其他 Client 端操作增加复杂性。

新的 Client 端功能允许 Client 端了解配置更改，并更新存储在其 ZooKeeper 句柄中的连接字符串(服务器及其 Client 端端口的列表)。概率算法用于在新配置服务器之间重新平衡 Client 端，同时保持 Client 端迁移的程度与整体成员资格的变化成比例。

本文档提供了用于重新配置的 Management 员手册。有关重新配置算法，性能测量等的详细说明，请参见我们的论文：

- - Shraer，A.，Reed，B.，Malkhi，D.，Junqueira，F.主/备份群集的动态重新配置。在* USENIX 年度技术会议(ATC)*(2012)，425-437 *中：链接：[paper (pdf)](https://www.usenix.org/system/files/conference/atc12/atc12-final74.pdf)，[slides (pdf)](https://www.usenix.org/sites/default/files/conference/protected-files/shraer_atc12_slides.pdf)，[video](https://www.usenix.org/conference/atc12/technical-sessions/presentation/shraer)，[hadoop 峰会幻灯片](http://www.slideshare.net/Hadoop_Summit/dynamic-reconfiguration-of-zookeeper)

**注意：** 从 3.5.3 开始，动态重配置功能默认情况下处于禁用状态，必须通过[reconfigEnabled](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperAdmin.html#sc_advancedConfiguration)配置选项显式打开。



## 对配置格式的更改



### 指定 Client 端端口

服务器的 Client 端端口是服务器接受 Client 端连接请求的端口。从 3.5.0 开始，* clientPort *和* clientPortAddress *配置参数将不再使用。而是，此信息现在成为服务器关键字规范的一部分，该规范如下：

```shell
server.<positive id> = <address1>:<port1>:<port2>[:role];[<client port address>:]<client port>**
```

Client 端端口规范在分号的右边。Client 端端口地址是可选的，如果未指定，则默认为“ 0.0.0.0”。通常，角色也是可选的，它可以是*参与者*或*观察者*(默认情况下为*参与者*)。

合法服务器声明的示例：

```shell
server.5 = 125.23.63.23:1234:1235;1236
server.5 = 125.23.63.23:1234:1235:participant;1236
server.5 = 125.23.63.23:1234:1235:observer;1236
server.5 = 125.23.63.23:1234:1235;125.23.63.24:1236
server.5 = 125.23.63.23:1234:1235:participant;125.23.63.23:1236
```



### standaloneEnabled 标志

在 3.5.0 之前，可以在 Standalone 模式或 Distributed 模式下运行 ZooKeeper。这些是单独的实现堆栈，因此无法在运行时在它们之间进行切换。默认情况下(为了向后兼容)，* standaloneEnabled *设置为* true *。使用此默认值的结果是，如果从一台服务器启动，则该集合将无法增长；如果是从多台服务器启动，则该集合将不能缩小为包含两个以下参与者。

将标志设置为* false *会指示系统运行分布式软件堆栈，即使合奏中只有一个参与者也是如此。为此，(静态)配置文件应包含：

```shell
standaloneEnabled=false**
```

通过此设置，可以启动包含单个参与者的 ZooKeeper 集成，并通过添加更多服务器来动态扩展它。同样，可以通过删除服务器来缩小整体规模，以便仅剩下一个参与者。

由于运行分布式模式可提供更大的灵 Active，因此建议将标志设置为* false *。我们希望将来不再使用传统的独立模式。



### reconfigEnabled 标志

从 3.5.0 开始到 3.5.3 之前，无法禁用动态重新配置功能。我们希望提供禁用重新配置功能的选项，因为启用重新配置后，我们担心安全性，即恶意行为者可以对 ZooKeeper 集成的配置进行任意更改，包括向该集成中添加受损的服务器。我们宁愿让用户自行决定是否启用它，并确保已采取适当的安全措施。因此，在 3.5.3 中引入了[reconfigEnabled](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperAdmin.html#sc_advancedConfiguration)配置选项，以便可以完全禁用重新配置功能，并且除非将 **reconfigEnabled** 设置为 **，否则默认情况下任何通过带有或不带有身份验证的 reconfig API 重新配置群集的尝试都将失败.正确** 。

要将选项设置为 true，配置文件(zoo.cfg)应包含：

```shell
reconfigEnabled=true
```



### 动态配置文件

从 3.5.0 开始，我们区分了动态配置参数和静态配置参数，动态配置参数可以在运行时更改，而静态配置参数是在服务器启动时从配置文件读取的，在执行过程中不会更改。目前，以下配置关键字被视为动态配置的一部分：* server *，* group *和* weight *。

动态配置参数存储在服务器上的单独文件中(我们称为动态配置文件)。使用新的* dynamicConfigFile *关键字从静态配置文件链接此文件。

**Example**

#### zoo_replicated1.cfg

```shell
tickTime=2000
dataDir=/zookeeper/data/zookeeper1
initLimit=5
syncLimit=2
dynamicConfigFile=/zookeeper/conf/zoo_replicated1.cfg.dynamic
```

#### zoo_replicated1.cfg.dynamic

```shell
server.1=125.23.63.23:2780:2783:participant;2791
server.2=125.23.63.24:2781:2784:participant;2792
server.3=125.23.63.25:2782:2785:participant;2793
```

当整体配置更改时，静态配置参数保持不变。动态参数由 ZooKeeper 推送，并覆盖所有服务器上的动态配置文件。因此，不同服务器上的动态配置文件通常是相同的(它们仅在进行重新配置时，或者如果新配置尚未传播到某些服务器时，才可能暂时不同)。创建动态配置文件后，不应手动对其进行更改。仅通过下面概述的新的重新配置命令进行更改。请注意，更改脱机群集的配置可能会导致存储在 ZooKeeper 日志(以及从日志填充的特殊配置 znode)方面的配置信息不一致，因此不建议这样做。

**Example 2**

用户可能更喜欢最初指定一个配置文件。因此，以下内容也是合法的：

#### zoo_replicated1.cfg

```shell
tickTime=2000
dataDir=/zookeeper/data/zookeeper1
initLimit=5
syncLimit=2
clientPort=
```

如果每个服务器上的配置文件尚未采用这种格式，则它们将自动分为动态和静态文件。因此，上面的配置文件将自动转换为示例 1 中的两个文件。请注意，如果有多余，则在此过程中将自动删除 clientPort 和 clientPortAddress 行(如果指定)(如上例所示)。备份了原始静态配置文件(在.bak 文件中)。



### Backward compatibility

我们仍然支持旧的配置格式。例如，以下配置文件是可以接受的(但不推荐)：

#### zoo_replicated1.cfg

```shell
tickTime=2000
dataDir=/zookeeper/data/zookeeper1
initLimit=5
syncLimit=2
clientPort=2791
server.1=125.23.63.23:2780:2783:participant
server.2=125.23.63.24:2781:2784:participant
server.3=125.23.63.25:2782:2785:participant
```

在引导过程中，将创建一个动态配置文件，其中包含配置的动态部分，如前所述。但是，在这种情况下，“ clientPort = 2791”行将保留在服务器 1 的静态配置文件中，因为它不是多余的-并未使用以下格式将其指定为“ server.1 = ...”的一部分[更改配置格式](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#ch_reconfig_format)部分中说明。如果调用重新配置来设置服务器 1 的 Client 端端口，我们将从静态配置文件中删除“ clientPort = 2791”(动态文件现在包含此信息，作为服务器 1 规范的一部分)。



## 升级到 3.5.0

仅在将集成升级到 3.4.6 版本后，才应将正在运行的 ZooKeeper 集成升级到 3.5.0. 请注意，这仅对于滚动升级是必需的(如果可以完全关闭系统，则不必执行 3.4.6)。如果您尝试滚动升级而不通过 3.4.6(例如从 3.4.5 开始)，则可能会出现以下错误：

```shell
2013-01-30 11:32:10,663 [myid:2] - INFO [localhost/127.0.0.1:2784:QuorumCnxManager$Listener@498] - Received connection request /127.0.0.1:60876
2013-01-30 11:32:10,663 [myid:2] - WARN [localhost/127.0.0.1:2784:QuorumCnxManager@349] - Invalid server id: -65536
```

在滚动升级过程中，将依次关闭每个服务器，并使用新的 3.5.0 二进制文件重新启动。在使用 3.5.0 二进制文件启动服务器之前，我们强烈建议更新配置文件，以使所有服务器语句“ server.x = ...”都包含 Client 端端口(请参阅[指定 Client 端端口](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_clientport))。如前所述，您可以将配置保留在单个文件中，也可以保留 clientPort/clientPortAddress 语句(尽管如果您以新格式指定 Client 端端口，则这些语句现在是多余的)。



## ZooKeeper 合奏的动态重新配置

ZooKeeper Java 和 C API 使用 getConfig 和 reconfig 命令进行了扩展，这些命令有助于重新配置。这两个命令都有一个同步(阻塞)变量和一个异步变量。我们在这里使用 Java CLI 演示了这些命令，但是请注意，您可以类似地使用 C CLI 或像其他任何 ZooKeeper 命令一样直接从程序中调用命令。



### API

Java 和 CClient 端都有两组 API。

- ***重新配置 API** *：重新配置 API 用于重新配置 ZooKeeper 集群。从 3.5.3 开始，将重新配置 Java API 从 ZooKeeper 类移入 ZooKeeperAdmin 类，并且使用此 API 需要 ACL 设置和用户身份验证(有关更多信息，请参见[Security](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_access_control))。
- ***获取配置 API** *：获取配置 API 用于检索存储在/ zookeeper/config znode 中的 ZooKeeper 集群配置信息。使用此 API 不需要特定的设置或身份验证，因为/ zookeeper/config 对任何用户都是可读的。



### Security

在 **3.5.3** 之前，在重新配置上没有强制的安全机制，因此可以连接到 ZooKeeper 服务器集合的任何 ZooKeeperClient 端都可以通过重新配置来更改 ZooKeeper 群集的状态。因此，恶意 Client 端可能会将受感染的服务器添加到集合中，例如添加受感染的服务器或删除合法服务器。此类情况可能是个案性的安全漏洞。

为了解决此安全问题，我们从 **3.5.3** 开始引入了对 reconfig 的访问控制，这样，只有特定的一组用户才能使用 reconfig 命令或 API，并且需要明确配置这些用户。另外，ZooKeeper 群集的设置必须启用身份验证，以便可以对 ZooKeeperClient 端进行身份验证。

我们还为在安全环境(即公司防火墙后)中与 ZooKeeper 集成体进行操作并与之交互的用户提供了一个逃生舱口。对于那些想要使用重新配置功能但又不想为授权用户配置显式列表以进行重新配置访问检查的开销的用户，可以将["skipACL"](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperAdmin.html#sc_authOptions)设置为“是”，这将跳过 ACL 检查并允许任何用户重新配置集群。

总体而言，ZooKeeper 为重新配置功能提供了灵活的配置选项，允许用户根据用户的安全要求进行选择。用户自行决定是否采取适当的安全措施。

- ***访问控制** *：动态配置存储在特殊的 znode ZooDefs.CONFIG_NODE =/zookeeper/config 中。默认情况下，该节点对所有用户都是只读的，但超级用户和明确配置为写访问权限的用户除外。需要使用 reconfig 命令或 reconfig API 的 Client 端应配置为对 CONFIG_NODE 具有写权限的用户。默认情况下，只有超级用户拥有完全控制权，包括对 CONFIG_NODE 的写入权限。通过设置具有与指定用户相关联的写许可权的 ACL，可以通过超级用户授予其他用户写访问权限。在 ReconfigExceptionTest.java 和 TestReconfigServer.cc 中可以找到一些有关如何设置 ACL 以及如何使用带有身份验证的重新配置 API 的示例。
- ***身份验证** *：用户的身份验证与访问控制正交，并委托给 ZooKeeper 的可插入身份验证方案支持的现有身份验证机制。有关此主题的更多详细信息，请参见[ZooKeeper 和 SASL](https://cwiki.apache.org/confluence/display/ZOOKEEPER/Zookeeper+and+SASL)。
- ***禁用 ACL 检查** *：ZooKeeper 支持["skipACL"](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperAdmin.html#sc_authOptions)选项，如果将 skipACL 设置为“是”，则将完全跳过 ACL 检查。在这种情况下，任何未经身份验证的用户都可以使用重新配置 API。



### 检索当前动态配置

动态配置存储在特殊的 znode ZooDefs.CONFIG_NODE =/zookeeper/config 中。新的`config` CLI 命令读取此 znode(当前它只是`get /zookeeper/config`的包装器)。与普通读取一样，要检索最新的提交值，应先执行`sync`。

```shell
[zk: 127.0.0.1:2791(CONNECTED) 3] config
server.1=localhost:2780:2783:participant;localhost:2791
server.2=localhost:2781:2784:participant;localhost:2792
server.3=localhost:2782:2785:participant;localhost:2793
```

注意输出的最后一行。这是配置版本。版本等于创建此配置的重新配置命令的 zxid。第一个构建的配置的版本等于第一个成功构建的领导者发送的 NEWLEADER 消息的 zxid。将配置写入动态配置文件时，该版本会自动成为文件名的一部分，并且静态配置文件将使用新动态配置文件的路径进行更新。保留与早期版本相对应的配置文件以用于备份。

在引导期间，将从文件名中提取版本(如果存在)。用户或系统 Management 员切勿手动更改版本。系统使用它来了解哪个配置是最新的。手动操作可能会导致数据丢失和不一致。

就像`get`命令一样，`config` CLI 命令接受* -w *标志用于在 znode 上设置监视，并接受* -s *标志用于显示 znode 的统计信息。它还接受一个新标志* -c *，该标志仅输出与当前配置相对应的版本和 Client 端连接字符串。例如，对于上述配置，我们将获得：

```shell
[zk: 127.0.0.1:2791(CONNECTED) 17] config -c
400000003 localhost:2791,localhost:2793,localhost:2792
```

请注意，直接使用 API 时，此命令称为`getConfig`。

作为任何读取命令，它都会返回 Client 端连接到的关注者已知的配置，该配置可能会有些过时。可以使用`sync`命令获得更强的保证。例如，使用 Java API：

```shell
zk.sync(ZooDefs.CONFIG_NODE, void_callback, context);
zk.getConfig(watcher, callback, context);
```

注意：在 3.5.0 中，传递到`sync()`命令的路径并不重要，因为所有服务器的状态都与领导者保持最新(因此，可以使用其他路径代替 ZooDefs.CONFIG_NODE)。但是，将来可能会改变。



### 修改当前动态配置

修改配置是通过`reconfig`命令完成的。有两种重新配置模式：增量和非增量(批量)。非增量简单地指定系统的新动态配置。增量指定对当前配置的更改。 `reconfig`命令返回新配置。

以下是一些示例：* ReconfigTest.java *，* ReconfigRecoveryTest.java *和* TestReconfigServer.cc *。



#### General

**删除服务器：** 可以删除任何服务器，包括领导服务器(尽管删除领导服务器将导致短暂的不可用性，请参见[paper](https://www.usenix.org/conference/usenixfederatedconferencesweek/dynamic-reconﬁguration-primarybackup-clusters)中的图 6 和图 8)。服务器将不会自动关闭。相反，它成为“无投票权的追随者”。这有点类似于观察者，因为其投票不计入提交操作所需的投票法定人数。但是，与不投票的关注者不同，观察者实际上看不到任何操作建议，也不会对其进行确认。因此，与观察者相比，无投票权的跟随者对系统吞吐量具有更大的负面影响。在关闭服务器或将其添加为追随者或作为整体的观察者之前，无表决权的追随者模式仅应用作临时模式。我们没有自动关闭服务器的原因有两个。第一个原因是我们不希望所有连接到该服务器的 Client 端都立即断开连接，从而导致到其他服务器的连接请求泛滥。相反，最好由每个 Client 端决定何时进行独立迁移。第二个原因是有时(很少)需要删除服务器才能将其从“观察者”更改为“参与者”(这在[Additional comments](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_additional)部分中进行了说明)。

请注意，新配置应具有最少的参与者数量，才能被视为合法。如果建议的更改将使集群中的参与者少于 2 人，并且启用了独立模式(standaloneEnabled = true，请参见[standaloneEnabled 标志](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_standaloneEnabled)部分)，则将不处理重新配置(BadArgumentsException)。如果禁用了独立模式(standaloneEnabled = false)，则其合法性可以保留 1 个或更多参与者。

**添加服务器：** 在调用重新配置之前，Management 员必须确保新配置的法定(多数)参与者已连接并与当前主持人同步。为此，我们需要先将新加入的服务器连接到领导者，然后再正式成为领导者。这是通过使用服务器的初始列表启动加入服务器来完成的，从技术上讲，这不是系统的合法配置，但是(a)包含加入者，并且(b)向加入者提供足够的信息以便其查找和连接给现任领导人。我们列出了一些安全地执行此操作的选项。

- 联接器的初始配置由处于最后提交配置的服务器和一个或多个联接器组成，其中 **联接器被列为观察者.** 例如，如果服务器 D 和 E 同时添加到(A，B， C)并且服务器 C 被删除，D 的初始配置可以是(A，B，C，D)或(A，B，C，D，E)，其中 D 和 E 被列为观察者。同样，E 的配置可以是(A，B，C，E)或(A，B，C，D，E)，其中 D 和 E 被列为观察者。 **请注意，将加入者列为观察者实际上并不会使他们成为观察者-这只会防止他们与其他加入者无意间形成仲裁.** 相反，他们将以当前配置联系服务器并采用最近提交的配置( A，B，C)，其中没有连接符。出现这种情况时，将备份并自动替换连接器的配置文件。连接到当前的领导者之后，加入者将成为无投票权的跟随者，直到重新配置系统并将其添加到集合(作为参与者或观察者，视情况而定)为止。
- 每个加入者的初始配置由最后提交的配置中的服务器组成 **加入者本身，列为参与者.** 例如，向包含服务器(A，B，C)的配置中添加新服务器 D，Management 员可以使用由服务器(A，B，C，D)组成的初始配置文件启动 D。如果将 D 和 E 同时添加到(A，B，C)，则 D 的初始配置可以是(A，B，C，D)，E 的配置可以是(A，B，C， E)。同样，如果同时添加 D 和删除 C，则 D 的初始配置可能是(A，B，C，D)。切勿在初始配置中列出多个加入者作为参与者(请参阅下面的警告)。
- 无论将加入者列为观察者还是参与者，只要列表中没有当前领导者，也可以不列出所有当前配置服务器。例如，添加 D 时，如果 A 是当前的领导者，我们可以从仅由(A，D)组成的配置文件开始 D。但是，这更加脆弱，因为如果 A 在 D 正式加入合奏之前失败，则 D 不会认识其他任何人，因此 Management 员将不得不干预并重新启动 D 的另一个服务器列表。

###### Note

Note

##### Warning

请勿在与参与者相同的初始配置中指定多个加入服务器。当前，加入的服务器不知道它们正在加入现有的集成。如果列出了多个加入者，则它们可能会形成一个独立的仲裁，从而形成裂脑情况，例如独立于您的主要合奏处理操作。可以在初始配置中将多个加入者列出为观察者。

如果现有服务器的配置发生更改，或者在联接器成功连接并了解有关配置更改之前它们不可用，则可能需要使用更新的配置文件重新启动联接器才能进行连接。

最后，请注意，连接到领导者后，联接器将采用上次提交的配置，该配置中不存在联接器(在重写之前先备份联接器的初始配置)。如果联接程序在此状态下重新启动，则它将无法启动，因为其配置文件中没有该联接器。为了启动它，您将不得不再次指定一个初始配置。

**修改服务器参数：** 可以通过使用不同参数将其添加到集合中来修改服务器的任何端口或其角色(参与者/观察者)。这适用于增量和批量重新配置模式。无需先删除服务器再将其添加回去。只需指定新参数，就好像服务器尚未在系统中一样。服务器将检测配置更改并执行必要的调整。请参见[Incremental mode](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_incremental)部分中的示例，以及[Additional comments](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_additional)部分中此规则的 exception。

也可以更改集成使用的仲裁系统(例如，将多数仲裁系统即时更改为分层仲裁系统)。但是，仅在使用批量(非增量)重新配置模式时才允许这样做。通常，增量重新配置仅适用于多数仲裁系统。批量重新配置可与分层仲裁系统和多数仲裁系统一起使用。

**性能影响：** 删除关注者时几乎不会对性能造成影响，因为它不会自动关闭(删除影响是不再计入服务器的票数)。添加服务器时，无需更改领导者，也不会明显影响性能。有关详细信息和图表，请参见[paper](https://www.usenix.org/conference/usenixfederatedconferencesweek/dynamic-reconﬁguration-primarybackup-clusters)中的图 6、7 和 8.

在导致以下情况之一的情况下，如果导致更换领导者，则将发生最严重的中断：

- 领导者被从合奏中删除。
- 领导者的角色从参与者变成观察者。
- 领导者用于将 Transaction 发送给其他人的端口(仲裁端口)已修改。

在这些情况下，我们执行领导者交接，其中旧领导者提名新领导者。所产生的不可用性通常比领导者崩溃时更短，因为不必要检测到领导者失败，并且通常可以在交接期间避免选举新领导者(请参见[paper](https://www.usenix.org/conference/usenixfederatedconferencesweek/dynamic-reconﬁguration-primarybackup-clusters)中的图 6 和图 8)。

修改服务器的 Client 端端口后，它不会删除现有的 Client 端连接。与服务器的新连接将必须使用新的 Client 端端口。

**进度保证：** 在调用 reconfig 操作之前，必须有一定数量的旧配置可用并已连接，以便 ZooKeeper 能够进步。调用重新配置后，旧配置和新配置的法定人数必须可用。一旦(a)激活了新配置，并且(b)提交了由领导者激活的新配置之前安排的所有操作，便完成了最终转换。一旦(a)和(b)发生，仅需要新配置的法定人数。但是请注意，(a)和(b)对 Client 都不可见。具体而言，当进行重新配置操作时，仅表示领导者发出了激活消息。这不一定意味着新配置的定额获得了此消息(激活该消息是必需的)或发生了(b)。如果要确保(a)和(b)都已经发生(例如，为了知道可以安全地关闭已删除的旧服务器)，则可以简单地调用更新(`set-data`或其他一些仲裁操作，而不是`sync`)，然后 await 其提交。实现此目的的另一种方法是向重新配置协议引入另一回合(为了简化和与 Zab 的兼容性，我们决定避免该协议)。



#### Incremental mode

增量模式允许向当前配置添加和删除服务器。允许进行多个更改。例如：

```shell
> reconfig -remove 3 -add
server.5=125.23.63.23:1234:1235;1236
```

add 和 remove 选项都获得一个逗号分隔的参数列表(无空格)：

```shell
> reconfig -remove 3,4 -add
server.5=localhost:2111:2112;2113,6=localhost:2114:2115:observer;2116
```

服务器语句的格式与第[指定 Client 端端口](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_clientport)节中所述的格式完全相同，并包含 Client 端端口。请注意，这里您可以说“ 5 =“，而不是“ server.5 =”。在上面的示例中，如果服务器 5 已经在系统中，但是具有不同的端口或不是观察者，则将对其进行更新，一旦配置提交，它将成为观察者并开始使用这些新端口。这是将参与者变成观察者，反之亦然或更改其任何端口的简便方法，而无需重新启动服务器。

ZooKeeper 支持两种类型的 Quorum 系统-简单的多数系统(领导者在收到大多数选民的 ACK 之后执行操作)和更复杂的分层系统，其中不同服务器的投票具有不同的权重，并且服务器被分为投票组。当前，仅当领导者已知的最后一个建议的配置使用多数仲裁系统时才允许进行增量重新配置(否则会抛出 BadArgumentsException)。

增量模式-使用 Java API 的示例：

```shell
List<String> leavingServers = new ArrayList<String>();
leavingServers.add("1");
leavingServers.add("2");
byte[] config = zk.reconfig(null, leavingServers, null, -1, new Stat());

List<String> leavingServers = new ArrayList<String>();
List<String> joiningServers = new ArrayList<String>();
leavingServers.add("1");
joiningServers.add("server.4=localhost:1234:1235;1236");
byte[] config = zk.reconfig(joiningServers, leavingServers, null, -1, new Stat());

String configStr = new String(config);
System.out.println(configStr);
```

还有一个异步 API，以及一个接受逗号分隔的 String 而不是 List 的 API。参见 src/java/main/org/apache/zookeeper/ZooKeeper.java。



#### Non-incremental mode

重新配置的第二种模式是非增量的，从而 Client 端可以提供新动态系统配置的完整说明。可以就地指定新配置，也可以从文件中读取新配置：

```shell
> reconfig -file newconfig.cfg
```

//newconfig.cfg 是动态配置文件，请参见[动态配置文件](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_file)

```shell
> reconfig -members
server.1=125.23.63.23:2780:2783:participant;2791,server.2=125.23.63.24:2781:2784:participant;2792,server.3=125.23.63.25:2782:2785:participant;2793}}
```

新配置可能使用其他 Quorum System。例如，即使当前集成使用多数仲裁系统，您也可以指定分层仲裁系统。

批量模式-使用 Java API 的示例：

```shell
List<String> newMembers = new ArrayList<String>();
newMembers.add("server.1=1111:1234:1235;1236");
newMembers.add("server.2=1112:1237:1238;1239");
newMembers.add("server.3=1114:1240:1241:observer;1242");

byte[] config = zk.reconfig(null, null, newMembers, -1, new Stat());

String configStr = new String(config);
System.out.println(configStr);
```

还有一个异步 API，以及一个接受逗号分隔的包含新成员而不是 List 的 String 的 API。参见 src/java/main/org/apache/zookeeper/ZooKeeper.java。



#### Conditional reconfig

有时(尤其是在非增量模式下)，新提议的配置取决于 Client 端“认为”什么是当前配置，并且应仅应用于该配置。具体来说，只有领导者的最后配置具有指定的版本，`reconfig`才能成功。

```shell
> reconfig -file <filename> -v <version>
```

在前面列出的 Java 示例中，可以指定一个配置版本来代替重新配置，而不是-1.



#### Error conditions

除了正常的 ZooKeeper 错误状况，由于以下原因，重新配置可能会失败：

- 当前正在进行另一个重新配置(ReconfigInProgress)
- 如果启用了独立模式，或者如果禁用了独立模式，则建议的更改将使群集中的参与者少于 2 人(BadArgumentsException)
- 重新配置处理开始时，新配置的仲裁没有与领导者构建连接并保持最新(NewConfigNoQuorum)
- 已指定`-v x`，但最新配置的版本`y`不是`x`(BadVersionException)
- 请求进行增量重新配置，但领导者上的最后配置使用与多数系统(BadArgumentsException)不同的法定系统
- 语法错误(BadArgumentsException)
- 从文件读取配置时发生 I/O 异常(BadArgumentsException)

其中大多数通过* ReconfigFailureCases.java *中的测试用例进行说明。



#### Additional comments

**活动性：** 为了更好地理解增量和非增量重新配置之间的区别，假设 Client 端 C1 将服务器 D 添加到系统中，而另一个 Client 端 C2 添加服务器 E。在非增量模式下，每个 Client 端都会首先调用`config`查找当前配置，然后通过添加自己的建议服务器在本地创建新的服务器列表。然后可以使用非增量`reconfig`命令提交新配置。两种重新配置完成后，将仅添加 E 或 D 中的一个(不是两个)，这取决于哪个 Client 端的请求第二次到达领导者，从而覆盖先前的配置。另一个 Client 端可以重复该过程，直到其更改生效。此方法可确保系统范围内的进度(即，对于其中一个 Client 端而言)，但不能确保每个 Client 端都能成功。为了获得更多控制权，C2 可以请求仅在当前配置的版本未更改的情况下执行重新配置，如[Conditional reconfig](https://www.docs4dev.com/docs/zh/zookeeper/r3.5.6/reference/zookeeperReconfig.html#sc_reconfig_conditional)部分中所述。这样，如果 C1 的配置先到达领导者，则可以避免盲目地覆盖 C1 的配置。

使用增量重新配置，这两种更改都将生效，因为领导者简单地将它们依次应用于当前配置，不管是什么(假设第二个重新配置请求在为第一个重新配置请求发送提交消息后到达领导者) -当前领导者将拒绝提议重新配置(如果另一个已经在 await 中)。由于保证了两个 Client 都能取得进步，因此这种方法可以保证更强的活力。实际上，多个并发重新配置可能很少。当前，非增量重新配置是动态更改仲裁系统的唯一方法。当前仅在多数仲裁系统中才允许进行增量配置。

**将观察者更改为关注者：** 很明显，如果发生错误(2)，即如果剩余的参与人数少于最小允许人数，则将参与投票的服务器更改为观察者可能会失败。但是，将观察者转换为参与者有时可能会因更微妙的原因而失败：例如，假设当前配置为(A，B，C，D)，其中 A 是领导者，B 和 C 是关注者，D 是观察者。另外，假设 B 崩溃了。如果提交了重新配置，其中 D 被称为跟随者，则它将失败，并显示错误(3)，因为在此配置中，新配置中的大多数投票者(任何 3 个投票者)必须已连接并且是最新的与领导。观察者无法确认在重新配置期间发送的历史记录前缀，因此它不计入这 3 个必需的服务器，并且重新配置将被中止。如果发生这种情况，Client 端可以通过两个 reconfig 命令来完成相同的任务：首先调用一个 reconfig 从配置中删除 D，然后调用第二个命令以将其重新添加为参与者(跟随者)。在中间状态 D 期间，它是一个无投票权的跟随者，可以确认在第二次重新配置命令期间执行的状态转移。



## 重新平衡 Client 端连接

启动 ZooKeeper 群集时，如果为每个 Client 端提供了相同的连接字符串(服务器列表)，则 Client 端将在列表中随机选择一个服务器进行连接，这将使每个服务器的预期 Client 端连接数相同。服务器。我们实现了一种方法，该方法在通过重新配置更改服务器组时保留此属性。请参阅[paper](https://www.usenix.org/conference/usenixfederatedconferencesweek/dynamic-reconﬁguration-primarybackup-clusters)中的第 4 和 5.1 节。

为了使该方法起作用，所有 Client 端必须订阅配置更改(通过直接或通过`getConfig` API 命令在/ zookeeper/config 上设置监视)。触发监视后，Client 端应通过调用`sync`和`getConfig`读取新配置，如果配置确实是新配置，则调用`updateServerList` API 命令。为了避免同时进行大量 Client 端迁移，最好让每个 Client 端在调用`updateServerList`之前随机短时间睡眠。

可以在以下示例中找到一些示例：* StaticHostProviderTest.java *和* TestReconfig.cc *

示例(这不是一个菜谱，而是一个简化的示例，仅用于解释总体思想)：

```shell
public void process(WatchedEvent event) {
    synchronized (this) {
        if (event.getType() == EventType.None) {
            connected = (event.getState() == KeeperState.SyncConnected);
            notifyAll();
        } else if (event.getPath()!=null &&  event.getPath().equals(ZooDefs.CONFIG_NODE)) {
            // in prod code never block the event thread!
            zk.sync(ZooDefs.CONFIG_NODE, this, null);
            zk.getConfig(this, this, null);
        }
    }
}

public void processResult(int rc, String path, Object ctx, byte[] data, Stat stat) {
    if (path!=null &&  path.equals(ZooDefs.CONFIG_NODE)) {
        String config[] = ConfigUtils.getClientConfigStr(new String(data)).split(" ");   // similar to config -c
        long version = Long.parseLong(config[0], 16);
        if (this.configVersion == null){
             this.configVersion = version;
        } else if (version > this.configVersion) {
            hostList = config[1];
            try {
                // the following command is not blocking but may cause the client to close the socket and
                // migrate to a different server. In practice its better to wait a short period of time, chosen
                // randomly, so that different clients migrate at different times
                zk.updateServerList(hostList);
            } catch (IOException e) {
                System.err.println("Error updating server list");
                e.printStackTrace();
            }
            this.configVersion = version;
        }
    }
}
```