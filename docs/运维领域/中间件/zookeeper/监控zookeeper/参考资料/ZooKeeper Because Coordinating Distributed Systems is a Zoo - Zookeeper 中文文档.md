# ooKeeper Administrator's Guide

### A Guide to Deployment and Administration

- 部署方式
  - 系统要求
    - [支持平台](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_supportedPlatforms)
    - [所需软件](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_requiredSoftware)
  - [群集（多服务器）设置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_zkMulitServerSetup)
  - [单服务器和开发人员设置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_singleAndDevSetup)
- 管理
  - 设计ZooKeeper部署
    - [跨机要求](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_CrossMachineRequirements)
    - [单机要求](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Single+Machine+Requirements)
  - [供应](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_provisioning)
  - [要考虑的事情：ZooKeeper的优势和局限性](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_strengthsAndLimitations)
  - [管理](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_administering)
  - 保养
    - [正在进行的数据目录清除](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Ongoing+Data+Directory+Cleanup)
    - [调试日志清除（log4j）](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Debug+Log+Cleanup+(log4j))
  - [监理](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_supervision)
  - [监控方式](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_monitoring)
  - [记录中](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_logging)
  - [故障排除](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_troubleshooting)
  - 配置参数
    - [最低配置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_minimumConfiguration)
    - [进阶设定](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_advancedConfiguration)
    - [集群选项](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_clusterOptions)
    - [加密，身份验证，授权选项](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_authOptions)
    - [实验选项/功能](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Experimental+Options%2FFeatures)
    - [不安全的选择](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Unsafe+Options)
    - [禁用数据目录自动创建](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Disabling+data+directory+autocreation)
    - [启用数据库存在验证](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_db_existence_validation)
    - [性能调整选项](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_performance_options)
    - [AdminServer配置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver_config)
  - 使用Netty框架进行通信
    - [仲裁TLS](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Quorum+TLS)
    - [无需停机即可升级现有的非TLS群集](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Upgrading+existing+nonTLS+cluster)
  - ZooKeeper命令
    - [四个字母的单词](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_4lw)
    - [AdminServer](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver)
  - 资料档案管理
    - [数据目录](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#The+Data+Directory)
    - [日志目录](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#The+Log+Directory)
    - [文件管理](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_filemanagement)
    - [恢复-TxnLogToolkit](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#Recovery+-+TxnLogToolkit)
  - [避免的事情](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_commonProblems)
  - [最佳实践](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_bestPractices)



## Deployment

本节包含有关部署Zookeeper的信息，并涵盖以下主题：

- [系统要求](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_systemReq)
- [群集（多服务器）设置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_zkMulitServerSetup)
- [单服务器和开发人员设置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_singleAndDevSetup)

前两个部分假定您对在生产环境（例如数据中心）中安装ZooKeeper感兴趣。最后一部分介绍了在有限的基础上设置ZooKeeper（用于评估，测试或开发）但在生产环境中没有设置的情况。



### System Requirements



#### Supported Platforms

ZooKeeper由多个组件组成。某些组件受到广泛支持，而其他组件仅在较小的一组平台上受支持。

- **客户端**是Java客户端库，应用程序使用它来连接到ZooKeeper集合。
- **服务器**是在ZooKeeper集成节点上运行的Java服务器。
- **Native Client**是类似于Java客户端的用C语言实现的客户端，应用程序使用该客户端连接到ZooKeeper集成。
- **Contrib**是指多个可选的附加组件。

以下矩阵描述了为在不同的操作系统平台上运行每个组件而承诺的支持级别。

##### Support Matrix

| Operating System | Client   | Server   | Native Client | Contrib  |
| ---------------- | -------- | -------- | ------------- | -------- |
| GNU / Linux      | 开发生产 | 开发生产 | 开发生产      | 开发生产 |
| 的Solaris        | 开发生产 | 开发生产 | 不支持        | 不支持   |
| FreeBSD          | 开发生产 | 开发生产 | 不支持        | 不支持   |
| 视窗             | 开发生产 | 开发生产 | 不支持        | 不支持   |
| Mac OS X         | 仅开发   | 仅开发   | 不支持        | 不支持   |

对于矩阵中未明确提及的任何操作系统，组件可能会起作用，也可能不会起作用。ZooKeeper社区将修复在其他平台上报告的明显错误，但没有完全支持。



#### Required Software

ZooKeeper在Java 1.8版或更高版本中运行（JDK 8 LTS，JDK 11 LTS，JDK 12-不支持Java 9和10）。它作为ZooKeeper服务器的*整体*运行。建议三个最小的ZooKeeper服务器是一个整体的最小大小，我们也建议它们在单独的计算机上运行。在Yahoo！，ZooKeeper通常部署在专用的RHEL盒上，该盒具有双核处理器，2GB RAM和80GB IDE硬盘。



### Clustered (Multi-Server) Setup

为了获得可靠的ZooKeeper服务，您应该在称为*ensemble*的群集中部署ZooKeeper 。只要大多数合奏正常，该服务便可用。因为Zookeeper占多数，所以最好使用奇数台计算机。例如，对于四台计算机，ZooKeeper只能处理单台计算机的故障；如果两台计算机发生故障，则其余两台计算机不占多数。但是，使用五台计算机，ZooKeeper可以处理两台计算机的故障。

###### 注意

> 如《[ZooKeeper入门指南》中所述](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperStarted.html)，容错群集设置至少需要三台服务器，并且强烈建议您使用奇数个服务器。
>
> 通常，对于生产安装而言，三台服务器绰绰有余，但是为了在维护期间获得最大的可靠性，您可能希望安装五台服务器。对于三台服务器，如果在其中一台服务器上执行维护，则在该维护过程中容易遭受其他两台服务器之一故障的影响。如果其中有五个正在运行，则可以将其中一个停机进行维护，并知道如果其他四个突然发生故障，则您仍然可以。
>
> 您的冗余注意事项应包括环境的所有方面。如果您有三台ZooKeeper服务器，但它们的网络电缆均插入同一网络交换机，则该交换机的故障将使您的整个系统瘫痪。

以下是设置将成为整体一部分的服务器的步骤。这些步骤应该在集合中的每个主机上执行：

1. 安装Java JDK。您可以将本机打包系统用于您的系统，也可以从以下[网址](http://java.sun.com/javase/downloads/index.jsp)下载JDK：[http](http://java.sun.com/javase/downloads/index.jsp) : [//java.sun.com/javase/downloads/index.jsp](http://java.sun.com/javase/downloads/index.jsp)

2. 设置Java堆大小。这对于避免交换非常重要，因为交换会严重降低ZooKeeper的性能。要确定正确的值，请使用负载测试，并确保您已远远低于会导致交换的使用限制。保守一点-对于4GB的计算机，最大堆大小为3GB。

3. 安装ZooKeeper服务器软件包。可以从以下[网址](http://zookeeper.apache.org/releases.html)下载：http：[//zookeeper.apache.org/releases.html](http://zookeeper.apache.org/releases.html)

4. 创建一个配置文件。这个文件可以叫任何东西。使用以下设置作为起点：

   ```
   tickTime=2000
   dataDir=/var/lib/zookeeper/
   clientPort=2181
   initLimit=5
   syncLimit=2
   server.1=zoo1:2888:3888
   server.2=zoo2:2888:3888
   server.3=zoo3:2888:3888
   ```

   您可以在“ [配置参数](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_configuration) ”部分中找到这些以及其他配置设置的含义。这里只说几句：作为ZooKeeper合奏一部分的每台机器都应该知道该合奏中的每台其他机器。您可以使用**server.id = host：port：port**形式的一系列行来完成此操作。（参数**host**和**port**很简单，对于每个服务器，您需要首先指定Quorum端口，然后指定用于ZooKeeper领导者选举的专用端口）。从ZooKeeper 3.6.0开始，您还可以[指定多个地址](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_multi_address)对于每个ZooKeeper服务器实例（当可以在群集中并行使用多个物理网络接口时，这可以提高可用性）。通过为服务器创建一个名为*myid*的文件，将服务器ID分配给每台计算机，该文件位于配置文件参数**dataDir**指定的该服务器数据目录中。

5. myid文件由仅包含该机器ID的文本的一行组成。因此，服务器1的*myid*将包含文本“ 1”，*除此之外*没有其他内容。id在集合中必须唯一，并且值必须在1到255之间。**重要说明：**如果启用TTL节点等扩展功能（请参阅下文），由于内部限制，id必须在1到254之间。

6. 创建初始化标记文件*初始化*在同一目录*身份识别码*。该文件表明应该有一个空的数据目录。如果存在，将创建一个空数据库并删除标记文件。如果不存在，则空的数据目录将意味着该对等方将没有投票权，并且在与活动的领导者通信之前不会填充该数据目录。预期用途是仅在调出新的合奏时创建此文件。

7. 如果设置了配置文件，则可以启动ZooKeeper服务器：

   ```
   $ java -cp zookeeper.jar:lib/*:conf org.apache.zookeeper.server.quorum.QuorumPeerMain zoo.conf
   ```

QuorumPeerMain启动了ZooKeeper服务器，还注册了[JMX](http://java.sun.com/javase/technologies/core/mntr-mgmt/javamanagement/)管理bean，它允许通过JMX管理控制台进行管理。该[ZooKeeper的JMX文件](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperJMX.html)包含有关使用JMX管理ZooKeeper的细节。有关启动服务器实例的示例，请参阅发行版中包含的脚本*bin / zkServer.sh*。8.通过连接到主机来测试部署：在Java中，您可以运行以下命令来执行简单的操作：

```
    $ bin/zkCli.sh -server 127.0.0.1:2181
```



### Single Server and Developer Setup

如果要出于开发目的设置ZooKeeper，则可能要设置ZooKeeper的单个服务器实例，然后在开发计算机上安装Java或C客户端库和绑定。

设置单个服务器实例的步骤与上述步骤相似，只是配置文件更简单。您可以在《[ZooKeeper入门指南》的“ ](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperStarted.html)[在单服务器模式下安装和运行ZooKeeper”](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperStarted.html#sc_InstallingSingleMode)部分中找到完整的说明。

有关安装客户端库的信息，请参阅《[ZooKeeper程序员指南》的“ ](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperProgrammers.html)[绑定”](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperProgrammers.html#ch_bindings)部分。



## Administration

本节包含有关运行和维护ZooKeeper的信息，并涵盖以下主题：

- [设计ZooKeeper部署](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_designing)
- [供应](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_provisioning)
- [要考虑的事情：ZooKeeper的优势和局限性](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_strengthsAndLimitations)
- [管理](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_administering)
- [保养](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_maintenance)
- [监理](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_supervision)
- [监控方式](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_monitoring)
- [记录中](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_logging)
- [故障排除](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_troubleshooting)
- [配置参数](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_configuration)
- [ZooKeeper命令](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_zkCommands)
- [资料档案管理](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_dataFileManagement)
- [避免的事情](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_commonProblems)
- [最佳实践](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_bestPractices)



### Designing a ZooKeeper Deployment

ZooKeeper的可靠性基于两个基本假设。

1. 部署中只有少数服务器将发生故障。在这种情况下，*故障*意味着机器崩溃，或者是网络中的某些错误，这些错误将服务器与大多数服务器分开。
2. 部署的计算机正常运行。正确操作意味着正确执行代码，使时钟正常工作以及使存储和网络组件一致运行。

以下各节包含ZooKeeper管理员要考虑的因素，以最大程度地使这些假设成立。其中一些是跨计算机的考虑因素，而其他则是部署中每台计算机都应考虑的事项。



#### Cross Machine Requirements

为了使ZooKeeper服务处于活动状态，必须有大多数可以相互通信的非故障机器。要创建可以容忍F机故障的部署，您应该指望部署2xF + 1机。因此，由三台计算机组成的部署可以处理一个故障，而由五台计算机组成的部署可以处理两个故障。请注意，部署六台计算机只能处理两个故障，因为三台计算机不是多数。因此，ZooKeeper部署通常由奇数台计算机组成。

为了最大程度地容忍故障，您应该尝试使机器故障独立。例如，如果大多数计算机共享同一交换机，则该交换机的故障可能导致相关的故障并导致服务中断。共享电源电路，冷却系统等也是如此。



#### Single Machine Requirements

如果ZooKeeper必须与其他应用程序竞争以访问诸如存储介质，CPU，网络或内存之类的资源，则其性能将显着下降。ZooKeeper具有很强的耐用性保证，这意味着它可以在允许负责更改的操作完成之前使用存储介质记录更改。然后，您应该意识到这种依赖性，如果要确保媒体不阻止ZooKeeper的操作，请格外小心。您可以采取以下措施来最大程度地减少这种退化：

- ZooKeeper的事务日志必须位于专用设备上。（专用分区是不够的。）ZooKeeper会按顺序写入日志，而不进行查找。与其他进程共享日志设备可能导致查找和争用，进而导致数秒的延迟。
- 不要将ZooKeeper放在可能引起交换的情况下。为了使ZooKeeper能够以任何及时的方式运行，完全不能允许它互换。因此，请确保分配给ZooKeeper的最大堆大小不大于ZooKeeper可用的实际内存量。有关更多信息，请参见下面的[避免注意事项](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_commonProblems)。



### Provisioning



### Things to Consider: ZooKeeper Strengths and Limitations



### Administering



### Maintenance

ZooKeeper群集几乎不需要长期维护，但是您必须注意以下几点：



#### Ongoing Data Directory Cleanup

ZooKeeper [数据目录](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#var_datadir)包含文件，这些文件是由特定服务集合存储的znode的永久副本。这些是快照和事务日志文件。对znode进行更改时，这些更改将附加到事务日志中。有时，当日志变大时，会将所有znodes当前状态的快照写入文件系统，并为将来的事务创建新的事务日志文件。在快照过程中，ZooKeeper可能会继续将传入的事务追加到旧的日志文件中。因此，一些比快照新的事务可能会在快照之前的最后一个事务日志中找到。

使用默认配置（请参阅下面的自动清除）时，ZooKeeper服务器**不会删除旧的快照和日志文件**，这是操作员的责任。每个服务环境都不同，因此安装之间（例如备份）的管理这些文件的要求可能会有所不同。

PurgeTxnLog实用程序实现了管理员可以使用的简单保留策略。该[API文档](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/index-2.html)包含调用约定（参数等）的详细信息。

在以下示例中，将保留最后一个计数快照及其对应的日志，并删除其他快照。的价值 通常应大于3（尽管不是必需的，但是在最近的日志损坏的情况下，这可以提供3个备份）。这可以作为ZooKeeper服务器计算机上的cron作业运行，以每天清理日志。

```
java -cp zookeeper.jar:lib/slf4j-api-1.7.5.jar:lib/slf4j-log4j12-1.7.5.jar:lib/log4j-1.2.17.jar:conf org.apache.zookeeper.server.PurgeTxnLog <dataDir> <snapDir> -n <count>
```

自动清除快照和相应的事务日志是在3.4.0版中引入的，可以通过以下配置参数**autopurge.snapRetainCount**和**autopurge.purgeInterval启用**。有关更多信息，请参见下面的[高级配置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_advancedConfiguration)。



#### Debug Log Cleanup (log4j)

请参阅本文档中有关[登录](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_logging)的部分。期望您将使用内置的log4j功能来设置滚动文件追加程序。发行版tar的conf / log4j.properties中的样本配置文件提供了一个示例。



### Supervision

您将需要一个管理流程来管理您的每个ZooKeeper服务器流程（JVM）。ZK服务器被设计为“快速失败”，这意味着如果发生无法恢复的错误，它将关闭（进程退出）。由于ZooKeeper服务群集高度可靠，因此这意味着尽管服务器可能宕机，但群集仍处于活动状态并正在处理请求。此外，由于群集是“自我修复”的，因此一旦失败的服务器重新启动，将自动重新加入该集合，而无需任何手动交互。

有一个监控程序，例如[daemontools](http://cr.yp.to/daemontools.html)或[SMF](http://en.wikipedia.org/wiki/Service_Management_Facility)（也可以使用其他监控程序选项，这取决于您要使用的哪个，这只是两个示例），管理ZooKeeper服务器可确保该进程确实退出时将自动重启并迅速重新加入集群。

还建议将ZooKeeper服务器进程配置为在发生OutOfMemoryError **时终止并转储其堆。这是通过分别在Linux和Windows上使用以下参数启动JVM来实现的。ZooKeeper *附带*的*zkServer.sh*和*zkServer.cmd*脚本设置了这些选项。

```
-XX:+HeapDumpOnOutOfMemoryError -XX:OnOutOfMemoryError='kill -9 %p'

"-XX:+HeapDumpOnOutOfMemoryError" "-XX:OnOutOfMemoryError=cmd /c taskkill /pid %%%%p /t /f"
```





### Monitoring

ZooKeeper服务可以通过以下两种主要方式之一进行监视：1）通过使用[4个字母词](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_zkCommands)的命令端口和2）[JMX](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperJMX.html)。请参阅适合您的环境/要求的部分。



### Logging

ZooKeeper使用**[SLF4J](http://www.slf4j.org/)** 1.7.5版作为其日志记录基础结构。为了向后兼容，它绑定到**LOG4J，**但是您可以使用**[LOGBack](http://logback.qos.ch/)**或您选择的任何其他受支持的日志记录框架。

ZooKeeper的默认*log4j.properties*文件位于*conf*目录中。Log4j要求*log4j.properties*位于工作目录（运行ZooKeeper的目录）中，或者可以从类路径访问。

有关SLF4J的更多信息，请参[见其手册](http://www.slf4j.org/manual.html)。

有关LOG4J的更多信息，请参见log4j手册的[Log4j默认初始化过程](http://logging.apache.org/log4j/1.2/manual.html#defaultInit)。



### Troubleshooting

- *服务器由于文件损坏*而无法启动：由于ZooKeeper服务器的事务日志中的某些文件损坏，服务器可能无法读取其数据库并无法启动。在加载ZooKeeper数据库时，您将看到一些IOException。在这种情况下，请确保您集合中的所有其他服务器都已启动并正常工作。在命令端口上使用“ stat”命令查看它们是否状况良好。确认集成中的所有其他服务器都已启动后，可以继续清理损坏的服务器的数据库。删除datadir / version-2和datalogdir / version-2 /中的所有文件。重新启动服务器。



### Configuration Parameters

ZooKeeper的行为由ZooKeeper配置文件控制。设计此文件的目的是，假设磁盘布局相同，组成ZooKeeper服务器的所有服务器都可以使用完全相同的文件。如果服务器使用不同的配置文件，则必须注意确保所有不同配置文件中的服务器列表都匹配。

###### 注意

> 在3.5.0及更高版本中，其中一些参数应放置在动态配置文件中。如果将它们放置在静态配置文件中，则ZooKeeper会自动将它们移到动态配置文件中。有关更多信息，请参见[动态重新配置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperReconfig.html)。



#### Minimum Configuration

以下是必须在配置文件中定义的最低配置关键字：

- *clientPort*：监听客户端连接的端口；即客户端尝试连接的端口。

- *secureClientPort*：使用SSL侦听安全客户端连接的端口。**clientPort**指定用于纯文本连接的端口，而**secureClientPort**指定用于SSL连接的端口。同时指定两者都将启用混合模式，而省略其中任何一个将禁用该模式。请注意，当用户将Zookeeper.serverCnxnFactory，zookeeper.clientCnxnSocket插入为Netty时，将启用SSL功能。

- *viewerMasterPort*：侦听观察者连接的端口；也就是观察者尝试连接的端口。如果设置了该属性，则服务器将在处于跟随者模式时（除了处于领导者模式时）托管观察者连接，并且在观察者模式时将相应地尝试连接到任何投票对等方。

- *dataDir*：ZooKeeper将存储内存数据库快照的位置，除非另有说明，否则将存储数据库更新的事务日志。

  ###### 注意

  > 请注意将事务日志放在何处。专用的事务日志设备是保持良好性能的关键。将日志放在繁忙的设备上会对性能产生不利影响。

- *tickTime*：单个刻度的长度，这是ZooKeeper使用的基本时间单位，以毫秒为单位。它用于调节心跳和超时。例如，最小会话超时将是两个刻度。



#### Advanced Configuration

本节中的配置设置是可选的。您可以使用它们进一步调整ZooKeeper服务器的行为。也可以使用Java系统属性来设置某些属性，通常形式为*zookeeper.keyword*。可用时，确切的系统属性在下面列出。

- dataLogDir

  ：（无Java系统属性）此选项将指示计算机将事务日志写入

  dataLogDir

  而不是

  dataDir

  。这允许使用专用的日志设备，并有助于避免日志记录和快照之间的竞争。

  ###### 注意

  > 拥有专用的日志设备对吞吐量和稳定的延迟有很大的影响。强烈建议先指定一个日志设备并将**dataLogDir**设置为指向该设备上的目录，然后确保将**dataDir**指向该设备上*不*存在的目录。

- *globalOutstandingLimit*：（Java系统属性：**zookeeper.globalOutstandingLimit。**）客户端可以比ZooKeeper更快地提交请求，尤其是在有很多客户端的情况下。为了防止ZooKeeper由于排队的请求而耗尽内存，ZooKeeper会限制客户端，以便系统中的未完成请求不超过globalOutstandingLimit。默认限制为1,000。

- *preAllocSize*：（Java系统属性：**zookeeper.preAllocSize**）为了避免查找，ZooKeeper以preAllocSize千字节的块为单位在事务日志文件中分配空间。默认块大小为64M。更改块大小的原因之一是如果更频繁地拍摄快照，则减小块大小。（另请参见**snapCount**和**snapSizeLimitInKb**）。

- *snapCount*：（Java系统属性：**zookeeper.snapCount**）ZooKeeper使用快照和事务日志（请考虑预写日志）记录其事务。在可以拍摄快照之前事务日志中记录的事务数（并且事务日志已滚动） ）由snapCount确定。为了防止仲裁中的所有机器同时拍摄快照，当交易日志中的交易数量达到运行时生成的[snapCount / 2 + 1]随机值时，每个ZooKeeper服务器都会拍摄快照。 ，snapCount]范围。默认的snapCount是100,000。

- *commitLogCount* * ：（ Java系统属性：**zookeeper.commitLogCount**）Zookeeper维护最近提交的请求的内存列表，以便在关注者不太落后时与关注者快速同步。如果快照很大（> 100,000），可以提高同步性能。默认的commitLogCount值为500。

- *snapSizeLimitInKb*：（Java系统属性：**zookeeper.snapSizeLimitInKb**）ZooKeeper使用快照和事务日志（请考虑预写日志）记录其事务。在可以拍摄快照（和滚动交易日志）之前，交易日志中记录的交易集中允许的总字节大小由snapSize决定。为了防止仲裁中的所有计算机同时拍摄快照，当[交易日志中的交易集的字节大小达到运行时生成的随机值时，每个ZooKeeper服务器都将拍摄快照。 snapSize / 2 + 1，snapSize]范围。每个文件系统都有一个最小的标准文件大小，为了使此功能有效运行，所选的数字必须大于该值。默认的snapSizeLimitInKb为4,194,304（4GB）。非正值将禁用该功能。

- *txnLogSizeLimitInKb*：（Java系统属性：**zookeeper.txnLogSizeLimitInKb**）也可以使用txnLogSizeLimitInKb来直接控制Zookeeper事务日志文件。当使用事务日志完成同步时，较大的txn日志可能导致较慢的跟随者同步。这是因为领导者必须扫描磁盘上适当的日志文件以查找要从其开始同步的事务。默认情况下，此功能是关闭的，snapCount和snapSizeLimitInKb是唯一限制事务日志大小的值。启用后，当达到任何限制时，Zookeeper都会滚动日志。请注意，实际日志大小可能会超出此值，超出序列化事务的大小。另一方面，如果此值设置得太接近（或小于）**preAllocSize**，这可能会导致Zookeeper为每个事务滚动日志。尽管这不是正确性问题，但这可能会导致性能严重下降。为避免这种情况并充分利用此功能，建议将值设置为N * **preAllocSize**，其中N> = 2。

- *maxCnxns*：（Java系统属性：**zookeeper.maxCnxns**）限制可以与Zookeeper服务器建立的并发连接总数（每个服务器的每个客户端端口）。这用于防止某些类的DoS攻击。默认值为0，将其设置为0将完全消除对并发连接总数的限制。serverCnxnFactory和secureServerCnxnFactory的连接数是分开计算的，因此，只要它们是适当的类型，就可以允许对等方承载最多2 * maxCnxns。

- *maxClientCnxns*：（无Java系统属性）将单个客户端（由IP地址标识）可以与ZooKeeper集成中的单个成员建立的并发连接数（在套接字级别）限制为多少。这用于防止某些类的DoS攻击，包括文件描述符耗尽。默认值为60。将其设置为0将完全消除并发连接的限制。

- *clientPortAddress*：**3.3.0中的新功能：**用于侦听客户端连接的地址（ipv4，ipv6或主机名）；即客户端尝试连接的地址。这是可选的，默认情况下，我们以这种方式绑定，即可以接受服务器上任何地址/接口/ NIC 到**clientPort的**任何连接。

- *minSessionTimeout*：（无Java系统属性）**3.3.0中的新增功能：**服务器允许客户端进行协商的最小会话超时（以毫秒为单位）。默认为**tickTime的** 2倍。

- *maxSessionTimeout*：（无Java系统属性）**3.3.0中的新增功能：**服务器允许客户端进行协商的最大会话超时（以毫秒为单位）。默认为**tickTime的** 20倍。

- *fsync.warningthresholdms*：（Java系统属性：**zookeeper.fsync.warningthresholdms**）**3.3.4中的新增功能：**每当事务日志（WAL）中的fsync花费的时间超过此值时，就会向该日志输出警告消息。该值以毫秒为单位指定，默认为1000。只能将其设置为系统属性。

- *maxResponseCacheSize*：（Java系统属性：**zookeeper.maxResponseCacheSize**）设置为正整数时，它将确定用于存储最近读取记录的序列化形式的缓存的大小。帮助节省流行znode上的序列化成本。指标**response_packet_cache_hits**和**response_packet_cache_misses**可用于将该值调整为给定的工作负载。默认情况下，该功能处于打开状态，其值为400，设置为0或负整数以关闭该功能。

- *maxGetChildrenResponseCacheSize*：（Java系统属性：**zookeeper.maxGetChildrenResponseCacheSize**）**3.6.0的新功能：**类似于**maxResponseCacheSize**，但适用于获取子级请求。度量**response_packet_get_children_cache_hits**和**response_packet_get_children_cache_misses**可用于将该值调整为给定的工作负载。默认情况下，该功能处于打开状态，其值为400，设置为0或负整数以关闭该功能。

- *autopurge.snapRetainCount*：（无Java系统属性）**3.4.0中的新增**功能**：**启用后，ZooKeeper自动清除功能**会将autopurge.snapRetainCount**最新快照和相应的事务日志分别保留在**dataDir**和**dataLogDir中，**并删除其余部分。默认值为3。最小值为3。

- *autopurge.purgeInterval*：（无Java系统属性）**3.4.0中的新增功能：**必须触发清除任务的时间间隔（以小时为单位）。设置为正整数（1或更大）以启用自动清除。预设为0。

- *syncEnabled*：（Java系统属性：**zookeeper.observer.syncEnabled**）**新的3.4.6，3.5.0：**现在的观察员在默认情况下，如参与者登录交易和写入快照磁盘。这减少了重新启动时观察者的恢复时间。设置为“ false”以禁用此功能。默认值为“ true”

- *fastleader.minNotificationInterval*：（Java系统属性：**zookeeper.fastleader.minNotificationInterval**）领导者选举的两次连续通知检查之间的时间长度下限。此间隔确定对等方等待检查选举投票集的时间，并影响选举可以解决的速度。对于长选举，该间隔遵循从配置的最小值（this）和配置的最大值（fastleader.maxNotificationInterval）开始的退避策略。

- *fastleader.maxNotificationInterval*：（Java系统属性：**zookeeper.fastleader.maxNotificationInterval**）对领导者选举的两次连续通知检查之间的时间长度上限。此间隔确定对等方等待检查选举投票集的时间，并影响选举可以解决的速度。对于长选举，该间隔遵循从配置的最小值（fastleader.minNotificationInterval）和配置的最大值（this）开始的退避策略。

- *connectionMaxTokens*：（Java系统属性：**zookeeper.connection_throttle_tokens**）**3.6.0中的新增功能：**这是用于调整服务器端连接调节器的参数之一，它是基于令牌的速率限制机制，具有可选的概率丢弃功能。该参数定义令牌桶中令牌的最大数量。设置为0时，节流被禁用。默认值为0。

- *connectionTokenFillTime*：（Java系统属性：**zookeeper.connection_throttle_fill_time**）**3.6.0的新增功能：**这是用于调整服务器端连接调节器的参数之一，它是基于令牌的速率限制机制，具有可选的概率丢弃。该参数定义令牌桶用*connectionTokenFillCount*令牌重新填充时的时间间隔（以毫秒为单位）。默认值为1。

- *connectionTokenFillCount*：（Java系统属性：**zookeeper.connection_throttle_fill_count**）**3.6.0中的新增功能：**这是用于调整服务器端连接调节器的参数之一，这是基于令牌的速率限制机制，具有可选的概率丢弃。此参数定义每个*connectionTokenFillTime*毫秒要添加到令牌桶的令牌数量。默认值为1。

- *connectionFreezeTime*：（Java系统属性：**zookeeper.connection_throttle_freeze_time**）**3.6.0中的新增功能：**这是用于调整服务器端连接调节器的参数之一，它是基于令牌的速率限制机制，具有可选的概率丢弃功能。此参数定义调整下降概率时的间隔（以毫秒为单位）。设置为-1时，禁用概率丢弃。默认值为-1。

- *connectionDropIncrease*：（Java系统属性：**zookeeper.connection_throttle_drop_increase**）**3.6.0中的新增功能：**这是用于调整服务器端连接调节器的参数之一，这是基于令牌的速率限制机制，具有可选的概率丢弃。此参数定义下降的可能性增加。节流阀检查每个*connectionFreezeTime*毫秒，如果令牌桶为空，则通过*connectionDropIncrease*会增加丢弃概率。默认值为0.02。

- *connectionDropDecrease*：（Java系统属性：**zookeeper.connection_throttle_drop_decrease**）**3.6.0中的新增功能：**这是用于调整服务器端连接调节器的参数之一，这是基于令牌的速率限制机制，具有可选的概率丢弃。此参数定义下降的下降概率。节流阀会检查每个*connectionFreezeTime*毫秒，如果令牌桶中的令牌超过阈值，则下降的概率将由*connectionDropDecrease*降低。阈值为*connectionMaxTokens* * *connectionDecreaseRatio*。默认值为0.002。

- *connectionDecreaseRatio*：（Java系统属性：**zookeeper.connection_throttle_decrease_ratio**）**3.6.0中的新增功能：**这是用于调整服务器端连接调节器的参数之一，它是基于令牌的速率限制机制，具有可选的概率丢弃。此参数定义阈值以降低掉落概率。默认值为0。

- *zookeeper.connection_throttle_weight_enabled*：（仅Java系统属性）**3.6.0中的新增功能：**节流时是否考虑连接权重。仅在启用连接限制时有用，即，connectionMaxTokens大于0。默认值为false。

- *zookeeper.connection_throttle_global_session_weight*：（仅Java系统属性）**3.6.0中的新增功能：**全局会话的权重。它是全局会话请求通过连接限制器所需的令牌数。它必须是一个不小于本地会话权重的正整数。预设值为3。

- *zookeeper.connection_throttle_local_session_weight*：（仅Java系统属性）**3.6.0中的新增功能：**本地会话的权重。它是本地会话请求通过连接限制器所需的令牌数。它必须是一个正整数，不大于全局会话或续订会话的权重。预设值为1。

- *zookeeper.connection_throttle_renew_session_weight*：（仅Java系统属性）**3.6.0中的新增功能：**更新会话的权重。它也是重新连接请求通过调节器所需的令牌数。它必须是一个不小于本地会话权重的正整数。预设值为2。

- *clientPortListenBacklog*：*3.4.14、3.5.5、3.6.0中的***新增功能：** ZooKeeper服务器套接字的套接字积压长度。这控制了将由ZooKeeper服务器处理的将在服务器端排队的请求数。超过此长度的连接将收到网络超时（30s），这可能会导致ZooKeeper会话过期问题。默认情况下，此值是unset（`-1`），在Linux上，该值使用的积压`50`。此值必须为正数。

- *serverCnxnFactory*：（Java系统属性：**zookeeper.serverCnxnFactory**）指定ServerCnxnFactory的实现。应该将其设置为`NettyServerCnxnFactory`使用基于TLS的服务器通信。默认值为`NIOServerCnxnFactory`。

- *flushDelay*：（Java系统属性：**zookeeper.flushDelay**）延迟提交日志刷新的时间（以毫秒为单位）。不影响*maxBatchSize*定义的限制。默认情况下禁用（值为0）。具有高写入速率的组件可能会看到吞吐量提高了10-20 ms。

- *maxWriteQueuePollTime*：（Java系统属性：**zookeeper.maxWriteQueuePollTime**）如果启用了*flushDelay*，则此方法确定没有新请求排队时在刷新之前等待的时间（以毫秒为单位）。默认情况下设置为*flushDelay* / 3（默认情况下默认禁用）。

- *maxBatchSize*：（Java系统属性：**zookeeper.maxBatchSize**）在触发提交日志刷新之前服务器中允许的事务数。不影响*flushDelay*定义的限制。默认值为1000。

- *requestThrottleLimit*：（Java系统属性：**zookeeper.request_throttle_max_requests**）**3.6.0中的新增功能：** RequestThrottler开始停止之前允许的未完成请求总数。设置为0时，节流被禁用。默认值为0。

- *requestThrottleStallTime*：（Java系统属性：**zookeeper.request_throttle_stall_time**）**3.6.0中的新增功能：**线程可能等待被通知其可以继续处理请求的最大时间（以毫秒为单位）。默认值为100。

- *requestThrottleDropStale*：（Java系统属性：**request_throttle_drop_stale**）**3.6.0中的新增**功能**：**启用后，调节器将丢弃过时的请求，而不是将其发布到请求管道。过时的请求是由现在关闭的连接发送的请求，和/或请求的延迟要高于sessionTimeout的请求。默认值为true。

- *requestStaleLatencyCheck*：（Java系统属性：**zookeeper.request_stale_latency_check**）**3.6.0的新增**功能**：**启用后，如果请求延迟时间大于其关联的会话超时，则该请求被视为过时的。默认禁用。

- *requestStaleConnectionCheck*：（Java系统属性：**zookeeper.request_stale_connection_check**）**3.6.0的新增**功能**：**启用后，如果请求的连接已关闭，则该请求被视为过时的。默认启用。

- *zookeeper.request_throttler.shutdownTimeout*：（仅Java系统属性）**3.6.0中的新增功能：** RequestThrottler在关机期间等待请求队列耗尽之前强制关闭的时间（以毫秒为单位）。默认值为10000。

- *advancedFlowControlEnabled*：（Java系统属性：**zookeeper.netty.advancedFlowControl.enabled**）根据ZooKeeper管道的状态在netty中使用精确的流控制，以避免直接缓冲区OOM。它将禁用Netty中的AUTO_READ。

- *enableEagerACLCheck*：（仅Java系统属性：**zookeeper.enableEagerACLCheck**）设置为“ true”时，在将请求发送到仲裁之前，对每个本地服务器上的写请求启用急切的ACL检查。默认值为“ false”。

- *maxConcurrentSnapSyncs*：（Java系统属性：**zookeeper.leader.maxConcurrentSnapSyncs**）领导者或关注者可以同时服务的最大快照同步数。预设值为10。

- *maxConcurrentDiffSyncs*：（Java系统属性：**zookeeper.leader.maxConcurrentDiffSyncs**）领导者或关注者可以同时服务的最大差异同步数。默认值为100。

- *摘要.enabled*：（仅Java系统属性：**zookeeper.digest.enabled**）**3.6.0**中的新增功能：添加了摘要功能，以在从磁盘加载数据库，追赶和跟随领导者时检测ZooKeeper内部的数据不一致，并逐步进行哈希处理根据中提到的adHash文件检查DataTree

  ```
  https://cseweb.ucsd.edu/~daniele/papers/IncHash.pdf
  ```

  这个想法很简单，DataTree的哈希值将基于对数据集的更改而增量更新。领导者准备txn时，它将根据公式发生的更改来预先计算树的哈希值：

  ```
  current_hash = current_hash + hash(new node data) - hash(old node data)
  ```

  如果正在创建新节点，则哈希（旧节点数据）将为0，如果它是删除节点op，则哈希（新节点数据）将为0。

  在将txn应用于数据树之后，此哈希将与每个txn关联，以表示预期的哈希值，并将其与原始提议一起发送给关注者。在将txn应用于数据树后，学习者将实际哈希值与txn中的哈希值进行比较，如果不一致，则报告不匹配。

  这些摘要值还将与磁盘上的每个txn和快照一起保留，因此，当服务器重新启动并从磁盘加载数据时，它将进行比较并查看是否存在哈希不匹配，这将有助于检测磁盘上的数据丢失问题。

  对于实际的哈希函数，我们在内部使用CRC，它不是无冲突哈希函数，但与无冲突哈希相比效率更高，而且冲突的可能性确实很少，并且已经可以满足我们的需求。

  此功能是向后和向前兼容的，因此它可以安全地滚动升级，降级，启用和以后禁用，而不会出现任何兼容问题。以下是已涵盖和测试的方案：

  1. 当领导者使用新代码运行，而跟随者使用旧代码运行时，摘要将附加到每个txn的末尾，跟随者将仅读取标头和txn数据，txn中的摘要值将被忽略。它不会影响跟随者读取和处理下一个txn。
  2. 当Leader用旧代码运行，而Follower用新代码运行时，摘要将不会与txn一起发送，当Follower尝试读取摘要时，它将抛出EOF，它将EOF捕获并妥善处理，并将摘要值设置为null。
  3. 当使用新代码加载旧快照时，尝试读取不存在的摘要值时，它将引发IOException，并且将捕获异常并将摘要设置为null，这意味着在加载此快照时我们不会比较摘要，预计在滚动升级期间会发生
  4. 使用旧代码加载新快照时，它将在反序列化数据树后成功完成，快照文件末尾的摘要值将被忽略
  5. 带有标志更改的滚动重新启动的方案与上面讨论的第一种和第二种方案类似，如果启用了领导程序但没有启用跟随程序，则摘要值将被忽略，并且跟随程序在运行时不会比较摘要；如果禁用了领导者但启用了跟随者，则跟随者将获得EOF异常，该异常将得到适当处理。

  注意：由于/ zookeeper / quota stat节点中潜在的不一致，当前摘要计算不包括/ zookeeper下的节点，我们可以在解决此问题之后将其包括在内。

  默认情况下，此功能已禁用，设置为“ true”将其启用。

- *snapshot.trust.empty*：（Java系统属性：**zookeeper.snapshot.trust.empty**）**3.5.6中的新增功能：**此属性控制ZooKeeper是否应将丢失的快照文件视为无法恢复的致命状态。设置为true允许ZooKeeper服务器在没有快照文件的情况下恢复。仅应在从旧版本的ZooKeeper（3.4.x，3.5.3之前）进行升级的过程中进行设置，在该版本中，ZooKeeper可能仅具有事务日志文件，而没有快照文件。如果在升级期间设置了该值，我们建议在升级后将该值重新设置为false并重新启动ZooKeeper进程，以便ZooKeeper可以在恢复过程中继续进行正常的数据一致性检查。默认值为false。

- *audit.enable*：（Java系统属性：**zookeeper.audit.enable**）**3.6.0中的新增功能：**默认情况下，禁用审计日志。设置为“ true”以启用它。默认值为“ false”。请参阅[ZooKeeper审核日志](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAuditLogs.html)以获取更多信息。

- *audit.impl.class*：（Java系统属性：**zookeeper.audit.impl.class**）**3.6.0中的新增功能：**用于实现审计记录器的类。默认情况下，使用基于log4j的审核记录器org.apache.zookeeper.audit .Log4jAuditLogger。请参阅[ZooKeeper审核日志](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAuditLogs.html)以获取更多信息。

- *largeRequestMaxBytes*：（Java系统属性：**zookeeper.largeRequestMaxBytes**）**3.6.0中的新增功能：**所有正在进行的大型请求的最大字节数。如果即将到来的大请求导致超出限制，则连接将关闭。默认值为100 * 1024 * 1024。

- *largeRequestThreshold*：（Java系统属性：**zookeeper.largeRequestThreshold**）**3.6.0中的新增功能：**大小阈值，超过该阈值后，请求将被视为大请求。如果为-1，则所有请求均被视为较小，从而有效地关闭了较大的请求限制。默认值为-1。

- *outstandingHandshake.limit*（java的系统属性只有：**zookeeper.netty.server.outstandingHandshake.limit**）飞行TLS握手连接可能在ZooKeeper的最大值，连接超过这个限制将开始握手之前被拒绝。此设置不限制最大TLS并发性，但有助于避免在进行中的TLS握手过多时由于TLS握手超时而导致的羊群效应。将其设置为250左右足以避免羊群效应。



#### Cluster Options

本节中的选项设计用于与一组服务器一起使用，即在部署服务器群集时。

- lectionAlg

  ：（无Java系统属性）要使用的选举实现。值“ 1”对应于快速领导者选择的未经身份验证的基于UDP的版本，“ 2”对应于快速领导者的基于身份验证的UDP的版本，而“ 3”对应于快速领导者的基于TCP的版本选举。在3.2.0中将算法3设置为默认算法，而以前的版本（3.0.0和3.1.0）也使用算法1和2。

  ###### 注意

  > 领导者选举1和2的实现在3.4.0 中**已弃用**。从3.6.0版本开始，只有FastLeaderElection可用，如果要进行升级，则必须关闭所有服务器，然后使用lectionAlg = 3（或通过从配置文件中删除该行）重新启动它们。>

- *initLimit*：（无Java系统属性）允许跟随者连接并同步到领导者的时间（以[秒为单位](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_tickTime)）（请参阅[tickTime](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_tickTime)）。如果ZooKeeper管理的数据量很大，请根据需要增加此值。

- *connectToLearnerMasterLimit*：（Java系统属性：饲养员**connectToLearnerMasterLimit**）的时间，在蜱（见[滚动时间](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_tickTime)），以使追随者领导人选举后与领导。默认为initLimit的值。当initLimit很高时使用，因此连接到学习者主机不会导致更高的超时。

- *leaderServes*：（Java系统属性：饲养员**leaderServes**）负责接受客户端连接。默认值为“是”。领导机器协调更新。为了获得较高的更新吞吐量，而以读取吞吐量为代价，可以将领导者配置为不接受客户端并专注于协调。此选项的默认值为“是”，这意味着领导者将接受客户端连接。

  ###### 注意

  > 当您在一个集合中拥有三个以上的ZooKeeper服务器时，强烈建议打开领导者选择。

- server.x = [主机名]：nnnnn [：nnnnn]等

  ：（没有Java系统属性）构成ZooKeeper集合的服务器。服务器启动时，它通过在数据目录中查找文件

  myid

  来确定它是哪台服务器。该文件包含了服务器数量，在ASCII，它应该与

  X

  在

  server.x

  在此设置的左侧。客户端使用的组成ZooKeeper服务器的服务器列表必须与每个ZooKeeper服务器具有的ZooKeeper服务器列表匹配。有两个端口号

  nnnnn

  。第一个跟随者用于连接领导者，第二个跟随者用于领导者选举。如果要在一台计算机上测试多个服务器，则可以为每个服务器使用不同的端口。

  从ZooKeeper 3.6.0开始，可以为每个ZooKeeper服务器指定**多个地址**（请参阅[ZOOKEEPER-3188](https://issues.apache.org/jira/projects/ZOOKEEPER/issues/ZOOKEEPER-3188)）。要启用此功能，必须将*multiAddress.enabled*配置属性设置为*true*。这有助于提高可用性并为ZooKeeper添加网络级别的弹性。当服务器使用多个物理网络接口时，ZooKeeper能够在所有接口上进行绑定，并在发生网络错误时将运行时切换到工作接口。可以在配置中使用竖线（'|'）字符指定不同的地址。使用多个地址的有效配置如下所示：

  ```
  server.1=zoo1-net1:2888:3888|zoo1-net2:2889:3889
  server.2=zoo2-net1:2888:3888|zoo2-net2:2889:3889
  server.3=zoo3-net1:2888:3888|zoo3-net2:2889:3889
  ```

  ###### 注意

  > 通过启用此功能，Quorum协议（ZooKeeper服务器-服务器协议）将更改。用户不会注意到这一点，并且当任何人使用新配置启动ZooKeeper群集时，一切都会正常工作。但是，如果旧的ZooKeeper群集不支持*multiAddress*功能（和新的Quorum协议），则无法在滚动升级期间启用此功能并指定多个地址。如果您需要此功能，但还需要从*3.6.0之前*的ZooKeeper集群执行滚动升级，则首先需要在不启用MultiAddress功能的情况下进行滚动升级，然后再使用新功能进行滚动重启。将**multiAddress.enabled**设置为**true的**配置 并提供了多个地址。

- *syncLimit*：（无Java系统属性）允许以关注者与ZooKeeper同步的时间（以滴答为[单位](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_tickTime)）（请参阅[tickTime](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_tickTime)）。如果追随者远远落后于领导者，他们将被丢弃。

- *group.x = nnnnn [：nnnnn]*：（无Java系统属性）启用分层仲裁。“ x”是组标识符，“ =”后的数字对应于服务器标识符。分配的左侧是用冒号分隔的服务器标识符列表。请注意，组必须是不相交的，并且所有组的并集必须是ZooKeeper集合。您会[在这里](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperHierarchicalQuorums.html)找到一个例子

- *weight.x = nnnnn*：（无Java系统属性）与“ group”一起使用，它在形成仲裁时为服务器分配权重。该值对应于投票时服务器的权重。ZooKeeper的某些部分需要投票，例如领导人选举和原子广播协议。默认情况下，服务器的权重为1。如果配置定义了组，但没有定义权重，则将为所有服务器分配值1。您会[在这里](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperHierarchicalQuorums.html)找到一个例子

- *cnxTimeout*：（Java系统属性：饲养员**cnxTimeout**）设置为打开领导人选举通知连接超时值。仅在您使用选举算法3时适用。

  ###### 注意

  > 默认值为5秒。

- quorumCnxnTimeoutMs

  ：（Java系统属性：饲养员

  quorumCnxnTimeoutMs

  ）设置为领导人选举通知的连接读取超时值。仅在您使用选举算法3时适用。

  ###### 注意

  > 默认值为-1，然后它将使用syncLimit * tickTime作为超时。

- *standaloneEnabled*：（无Java系统属性）**3.5.0中的新增功能：**设置为false时，可以以复制模式启动单个服务器，可以由观察者运行单个参与者，并且群集可以重新配置为一个节点，然后从一个节点。为了向后兼容，默认值为true。可以使用QuorumPeerConfig的setStandaloneEnabled方法或通过将“ standaloneEnabled = false”或“ standaloneEnabled = true”添加到服务器的配置文件中来进行设置。

- *reconfigEnabled*：（无Java系统属性）**3.5.3的新增功能：**这控制启用或禁用[动态重新配置](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperReconfig.html)功能。启用此功能后，假设用户被授权执行此类操作，则用户可以通过ZooKeeper客户端API或通过ZooKeeper命令行工具执行重新配置操作。禁用此功能后，包括超级用户在内的任何用户都无法执行重新配置。任何重新配置的尝试都将返回错误。可以将**“ reconfigEnabled”**选项设置为**“ reconfigEnabled = false”**或**“ reconfigEnabled = true”**到服务器的配置文件，或使用QuorumPeerConfig的setReconfigEnabled方法。默认值为false。如果存在，则该值在整个集合中的每个服务器上都应保持一致。在某些服务器上将该值设置为true，而在其他服务器上将该值设置为false，则将导致不一致的行为，具体取决于哪个服务器被选为领导者。如果领导者的设置为**“ reconfigEnabled = true”**，则集成将启用重新配置功能。如果领导者的设置为**“ reconfigEnabled = false”**，则该集成将禁用重新配置功能。因此，建议在集成服务器中的**“ reconfigEnabled”**具有一致的值。

- *4lw.commands.whitelist*：（Java系统属性：**zookeeper.4lw.commands.whitelist**）**3.5.3的新增功能：**用户要使用的逗号分隔的[四个字母单词](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_4lw)命令列表。必须在此列表中输入有效的四个字母的命令，否则ZooKeeper服务器将不会启用该命令。默认情况下，白名单仅包含zkServer.sh使用的“ srvr”命令。默认情况下，其余四个字母单词命令是禁用的。这是启用stat，ruok，conf和isro命令同时禁用其余四个字母单词命令的配置示例：

  ```
  4lw.commands.whitelist=stat, ruok, conf, isro
  ```

如果确实需要默认情况下启用所有四个字母词命令，则可以使用星号选项，这样您就不必在列表中一个接一个地添加每个命令。例如，这将启用所有四个字母词命令：

```
4lw.commands.whitelist=*
```

- *tcpKeepAlive*：（Java系统属性：**zookeeper.tcpKeepAlive**）**3.5.4的新增功能：**将此属性设置为true可以在仲裁成员用于执行选举的套接字上设置TCP keepAlive标志。当存在可能破坏仲裁成员的网络基础结构时，这将允许仲裁成员之间的连接保持连接状态。对于长时间运行或空闲的连接，某些NAT和防火墙可能会终止或丢失状态。启用此选项取决于操作系统级别的设置才能正常工作，有关更多信息，请检查操作系统有关TCP keepalive的选项。默认为**false**。
- *lectionPortBindRetry*：（仅Java系统属性：**zookeeper.electionPortBindRetry**）该属性设置当Zookeeper服务器无法绑定领导者选举端口时的最大重试次数。此类错误可以是临时的且可恢复的（例如[ZOOKEEPER-3320中](https://issues.apache.org/jira/projects/ZOOKEEPER/issues/ZOOKEEPER-3320)描述的DNS问题），也可以是不可重试的（例如已在使用的端口）。
  如果出现暂时性错误，此属性可以提高Zookeeper服务器的可用性并帮助其自我恢复。默认值3.在容器环境中，尤其是在Kubernetes中，应增加该值或将其设置为0（无限重试），以解决与DNS名称解析有关的问题。
- *reader.reconnectDelayMs*：（Java系统属性：**zookeeper.observer.reconnectDelayMs**）当观察者与领导者失去联系时，它会等待指定的值，然后再尝试与领导者重新建立联系，以使整个观察员队伍都不会尝试运行领导者选举并立即重新与领导者联系。默认值为0毫秒。
- *viewer.election.DelayMs*：（Java系统属性：**zookeeper.observer.election.DelayMs**）在断开连接时延迟观察者参加领导者选举，以防止在此过程中对投票对等方产生意外的额外负担。默认为200毫秒。
- *localSessionsEnabled*和*localSessionsUpgradingEnabled*：**3.5的新增功能：**可选值是true或false。它们的默认值为false。通过设置*localSessionsEnabled = true来*打开本地会话功能。打开*localSessionsUpgradingEnabled*可以根据需要自动将本地会话升级到全局会话（例如，创建临时节点），这仅在启用*localSessionsEnabled*时才重要。



#### Encryption, Authentication, Authorization Options

本节中的选项允许控制服务执行的加密/认证/授权。

在此页面旁边，您还可以在《[程序员指南》中](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperProgrammers.html#sc_java_client_configuration)找到有关客户端配置的有用信息。ZooKeeper Wiki还提供了有关[ZooKeeper SSL支持](https://cwiki.apache.org/confluence/display/ZOOKEEPER/ZooKeeper+SSL+User+Guide)和[ZooKeeper的SASL身份验证的](https://cwiki.apache.org/confluence/display/ZOOKEEPER/ZooKeeper+and+SASL)有用页面。

- *DigestAuthenticationProvider.superDigest*：（Java系统属性：**zookeeper.DigestAuthenticationProvider.superDigest**）默认情况下，此功能**处于****禁用状态** 。3.2中的**新增**功能**：**使ZooKeeper集成管理员以“超级”用户身份访问znode层次结构。特别是，对于通过身份验证为超级的用户，不会进行ACL检查。org.apache.zookeeper.server.auth.DigestAuthenticationProvider可用于生成superDigest，并使用一个参数“ super： 提供生成的“超级”： 作为启动集合的每个服务器时的系统属性值。（从ZooKeeper客户端向ZooKeeper服务器进行身份验证时，传递“ digest”方案和“ super：authdata”方案） “。请注意，摘要身份验证将纯文本身份验证数据传递给服务器，因此，最好仅在本地主机（而不是通过网络）或加密连接上使用此身份验证方法。

- *X509AuthenticationProvider.superUser*：（ Java系统属性：**zookeeper.X509AuthenticationProvider.superUser**）SSL支持的方法，使ZooKeeper集成管理员能够以“超级”用户身份访问znode层次结构。当此参数设置为X500主体名称时，只有具有该主体的经过身份验证的客户端才能够绕过ACL检查，并具有对所有znode的完全特权。

- *zookeeper.superUser*：（Java系统属性：**zookeeper.superUser**）类似于**zookeeper.X509AuthenticationProvider.superUser，**但对于基于SASL的登录名是通用的。它存储可以作为“超级”用户访问znode层次结构的用户名。

- *ssl.authProvider*：（Java系统属性：**zookeeper.ssl.authProvider**）指定用于安全客户端身份验证的**org.apache.zookeeper.auth.X509AuthenticationProvider**的子类。这在不使用JKS的证书密钥基础结构中很有用。可能需要扩展**javax.net.ssl.X509KeyManager**和**javax.net.ssl.X509TrustManager**才能从SSL堆栈中获得所需的行为。要将ZooKeeper服务器配置为使用自定义提供程序进行身份验证，请为自定义AuthenticationProvider选择方案名称，然后设置属性**zookeeper.authProvider。[方案]**自定义实现的全限定类名。这会将提供程序加载到ProviderRegistry中。然后设置此属性**zookeeper.ssl.authProvider = [scheme]**，该提供程序将用于安全身份验证。

- *zookeeper.ensembleAuthName*：（仅Java系统属性：**zookeeper.ensembleAuthName**）**3.6.0中的新增功能：**指定以逗号分隔的集成有效名称/别名的列表。客户端可以提供打算连接的整体名称作为方案“整体”的凭据。EnsembleAuthenticationProvider将根据接收连接请求的集成的名称/别名列表检查凭据。如果凭据不在列表中，则连接请求将被拒绝。这样可以防止客户端意外连接到错误的集合。

- *zookeeper.sessionRequireClientSASLAuth*：（仅Java系统属性：**zookeeper.sessionRequireClientSASLAuth**）**3.6.0中的新增功能：**设置为**true时**，ZooKeeper服务器将仅接受来自通过SASL向服务器认证的客户端的连接和请求。未配置SASL身份验证或未配置SASL但身份验证失败的客户端（即具有无效凭据的客户端）将无法与服务器建立会话。在这种情况下，将提供键入的错误代码（-124），此后Java和C客户端都会关闭与服务器的会话，而无需进一步尝试重新尝试连接。

  默认情况下，此功能处于禁用状态。希望加入的用户可以通过将**zookeeper.sessionRequireClientSASLAuth**设置为**true**来启用该功能。

  此功能否决了 zookeeper.allowSaslFailedClients 选项，因此即使服务器配置为允许未通过SASL身份验证的客户端登录，如果启用此功能，客户端也将无法与服务器建立会话。

- *sslQuorum*：（Java系统属性：**zookeeper.sslQuorum**）**3.5.5的新增功能：**启用加密的仲裁通信。默认值为`false`。

- *ssl.keyStore.location和ssl.keyStore.password*和*ssl.quorum.keyStore.location*和*ssl.quorum.keyStore.password*：（Java系统属性：**zookeeper.ssl.keyStore.location**和**zookeeper.ssl.keyStore.password**和**zookeeper .ssl.quorum.keyStore.location**和**zookeeper.ssl.quorum.keyStore.password**）**3.5.5中的新增功能：**指定Java密钥库的文件路径，该路径包含用于客户端和仲裁TLS连接的本地凭据以及密码解锁文件。

- *ssl.keyStore.type*和*ssl.quorum.keyStore.type*：（Java系统属性：**zookeeper.ssl.keyStore.type**和**zookeeper.ssl.quorum.keyStore.type**）**3.5.5中的新增功能：**指定客户端和客户端的文件格式。法定密钥库。值：JKS，PEM，PKCS12或为空（按文件名检测）。
  默认值：空

- *ssl.trustStore.location*和*ssl.trustStore.password*和*ssl.quorum.trustStore.location*和*ssl.quorum.trustStore.password*：（Java系统属性：**zookeeper.ssl.trustStore.location**和**zookeeper.ssl.trustStore.password**和**zookeeper .ssl.quorum.trustStore.location**和**zookeeper.ssl.quorum.trustStore.password**）**3.5.5中的新增功能：**指定Java信任库的文件路径，该路径包含用于客户端和仲裁TLS连接的远程凭据以及密码解锁文件。

- *ssl.trustStore.type*和*ssl.quorum.trustStore.type*：（Java系统属性：**zookeeper.ssl.trustStore.type**和**zookeeper.ssl.quorum.trustStore.type**）**3.5.5中的新增功能：**指定客户端和客户端的文件格式。仲裁信任库。值：JKS，PEM，PKCS12或为空（按文件名检测）。
  默认值：空

- *ssl.protocol*和*ssl.quorum.protocol*：（Java系统属性：**zookeeper.ssl.protocol**和**zookeeper.ssl.quorum.protocol**）**3.5.5中的新增功能：**指定要在客户端和仲裁TLS协商中使用的协议。默认值：TLSv1.2

- *ssl.enabledProtocols*和*ssl.quorum.enabledProtocols*：（Java系统属性：**zookeeper.ssl.enabledProtocols**和**zookeeper.ssl.quorum.enabledProtocols**）**3.5.5中的新增**功能**：**指定客户端和仲裁TLS协商中的已启用协议。默认值：`protocol`属性值

- *ssl.ciphersuites*和*ssl.quorum.ciphersuites*：（Java系统属性：**zookeeper.ssl.ciphersuites**和**zookeeper.ssl.quorum.ciphersuites**）**3.5.5中的新增**功能**：**指定在客户端和仲裁TLS协商中使用的已启用密码套件。默认值：启用的密码套件取决于所使用的Java运行时版本。

- *ssl.context.supplier.class*和*ssl.quorum.context.supplier.class*：（Java系统属性：**zookeeper.ssl.context.supplier.class**和**zookeeper.ssl.quorum.context.supplier.class**）**3.5.5中的新功能：**指定用于在客户端和仲裁SSL通信中创建SSL上下文的类。这使您可以使用自定义SSL上下文并实现以下方案：

  1. 使用使用PKCS11或类似工具加载的硬件密钥库。
  2. 您无权访问软件密钥库，但可以从其容器中检索已经构造的SSLContext。默认值：空

- *ssl.hostnameVerification*和*ssl.quorum.hostnameVerification*：（Java系统属性：**zookeeper.ssl.hostnameVerification**和**zookeeper.ssl.quorum.hostnameVerification**）**3.5.5的新增功能：**指定是否在客户端和仲裁TLS协商过程中启用主机名验证。仅建议出于测试目的禁用它。默认值：true

- *ssl.crl*和*ssl.quorum.crl*：（Java系统属性：**zookeeper.ssl.crl**和**zookeeper.ssl.quorum.crl**）**3.5.5中的新增功能：**指定是否在客户端和仲裁TLS协议中启用证书吊销列表。默认值：false

- *ssl.ocsp*和*ssl.quorum.ocsp*：（Java系统属性：**zookeeper.ssl.ocsp**和**zookeeper.ssl.quorum.ocsp**）**3.5.5中的新增功能：**指定是否在客户端和仲裁TLS协议中启用了“在线证书状态协议”。默认值：false

- *ssl.clientAuth*和*ssl.quorum.clientAuth*：（Java系统属性：**zookeeper.ssl.clientAuth**和**zookeeper.ssl.quorum.clientAuth**）**3.5.5中的新增功能：** TBD

- *ssl.handshakeDetectionTimeoutMillis*和*ssl.quorum.handshakeDetectionTimeoutMillis*：（Java系统属性：**zookeeper.ssl.handshakeDetectionTimeoutMillis**和**zookeeper.ssl.quorum.handshakeDetectionTimeoutMillis**）**3.5.5中的新功能：** TBD

- *client.portUnification*：（Java系统属性：**zookeeper.client.portUnification**）指定客户端端口应接受SSL连接（使用与安全客户端端口相同的配置）。默认值：false

- *authProvider*：（Java系统属性：**zookeeper.authProvider**）您可以为ZooKeeper指定多个身份验证提供程序类。通常，您可以使用此参数来指定SASL身份验证提供程序，例如：`authProvider.1=org.apache.zookeeper.server.auth.SASLAuthenticationProvider`

- *kerberos.removeHostFromPrincipal*（Java系统属性：**zookeeper.kerberos.removeHostFromPrincipal**），您可以指示ZooKeeper在身份验证期间从客户端主体名称中删除主机。（例如，zk / myhost @ EXAMPLE.COM客户端主体将在ZooKeeper中作为zk@EXAMPLE.COM进行身份验证）默认值：false

- *kerberos.removeRealmFromPrincipal*（Java系统属性：**zookeeper.kerberos.removeRealmFromPrincipal**），您可以指示ZooKeeper在身份验证期间从客户端主体名称中删除领域。（例如，zk / myhost @ EXAMPLE.COM客户端主体将在ZooKeeper中以zk / myhost身份验证）默认值：false

- *multiAddress.enabled*：（Java系统属性：**zookeeper.multiAddress.enabled**）**3.6.0中的新增功能：**自ZooKeeper 3.6.0起，您还可以为每个ZooKeeper服务器实例[指定多个地址](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_multi_address)（当可以使用多个物理网络接口时，这可以提高可用性。在群集中并行）。将此参数设置为**true**将启用此功能。请注意，如果旧的ZooKeeper群集的版本低于3.6.0，则无法在滚动升级期间启用此功能。默认值为**false**。

- *multiAddress.reachabilityCheckTimeoutMs*：（Java系统属性：**zookeeper.multiAddress.reachabilityCheckTimeoutMs**）**3.6.0中的新增功能：**自ZooKeeper 3.6.0起，您还可以[指定多个地址](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_multi_address)对于每个ZooKeeper服务器实例（当可以在群集中并行使用多个物理网络接口时，这可以提高可用性）。ZooKeeper将执行ICMP ECHO请求或尝试在目标主机的端口7（回显）上建立TCP连接，以查找可到达的地址。仅当您在配置中提供多个地址时，才会发生这种情况。在此属性中，您可以设置超时检查（以毫秒为单位）。该检查针对不同的地址并行进行，因此您在此处设置的超时是通过检查所有地址的可达性而花费的最长时间。默认值为**1000**。

  除非您通过设置*multiAddress.enabled = true*启用MultiAddress功能，否则此参数无效。



#### Experimental Options/Features

当前被认为是实验性的新功能。

- *只读模式服务器*：（Java系统属性：**readonlymode.enabled**）**3.4.0中的新增功能：**将此值设置为true可启用只读模式服务器支持（默认情况下禁用）。ROM允许请求ROM支持的客户端会话连接到服务器，即使服务器可能已从定额分区。在这种模式下，ROM客户端仍可以从ZK服务读取值，但是将无法写入值并查看其他客户端的更改。有关更多详细信息，请参见ZOOKEEPER-784。



#### Unsafe Options

以下选项可能有用，但是在使用它们时要小心。解释每个变量的风险以及变量作用的解释。

- *forceSync*：（Java系统属性：**zookeeper.forceSync**）在完成更新处理之前，需要将更新同步到事务日志的媒体。如果此选项设置为no，则ZooKeeper将不需要将更新同步到媒体。

- *jute.maxbuffer*：（Java系统属性：**jute.maxbuffer**）。

  - 此选项只能设置为Java系统属性。上面没有Zookeeper前缀。它指定可以存储在znode中的数据的最大大小。单位是：字节。默认值为0xfffff（1048575）字节，或略低于1M。
  - 如果更改此选项，则必须在所有服务器和客户端上设置系统属性，否则会出现问题。
  - 当客户端的*jute.maxbuffer*大于服务器端时，客户端要写入的数据超过服务器端的*jute.maxbuffer*，服务器端将得到**java.io.IOException：Len错误**
  - 当客户端的*jute.maxbuffer*小于服务器端时，客户端要读取的数据超过客户端的*jute.maxbuffer*，客户端将得到**java.io.IOException：长度不合理**或**Packet len超出范围！**
  - 这确实是一个健全性检查。ZooKeeper旨在存储大小为千字节的数据。在生产环境中，由于以下原因，不建议将此属性增加为超过默认值：
  - 大型znode会导致不必要的延迟尖峰，从而恶化吞吐量
  - 较大的znode会使领导者和跟随者之间的同步时间无法预测且无法收敛（有时会超时），导致仲裁不稳定

- *jute.maxbuffer.extrasize*：（Java系统属性：**zookeeper.jute.maxbuffer.extrasize**）**3.5.7的新增功能：**在处理客户端请求时，ZooKeeper服务器在将其持久化为事务之前将一些附加信息添加到请求中。之前，此附加信息的大小固定为1024字节。对于许多情况，特别是jute.maxbuffer值大于1 MB并且请求类型为多的情况，此固定大小是不够的。为了处理所有情况，其他信息大小从1024字节增加到与jute.maxbuffer大小相同，并且还可以通过jute.maxbuffer.extrasize对其进行配置。通常，由于默认值是最佳值，因此不需要配置此属性。

- *skipACL*：（Java系统属性：**zookeeper.skipACL**）跳过ACL检查。这样可以提高吞吐量，但是每个人都可以完全访问数据树。

- *quorumListenOnAllIPs*：设置为true时，ZooKeeper服务器将在所有可用IP地址上侦听来自其对等方的连接，而不仅仅是在配置文件的服务器列表中配置的地址。它影响处理ZAB协议和快速领导者选举协议的连接。默认值为**false**。

- *multiAddress.reachabilityCheckEnabled*：（Java系统属性：**zookeeper.multiAddress.reachabilityCheckEnabled**）**3.6.0的新增功能：**自ZooKeeper 3.6.0起，您还可以为每个ZooKeeper服务器实例[指定多个地址](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#id_multi_address)（当可以使用多个物理网络接口时，这可以提高可用性。在群集中并行）。ZooKeeper将执行ICMP ECHO请求或尝试在目标主机的端口7（回显）上建立TCP连接，以查找可到达的地址。仅当您在配置中提供多个地址时，才会发生这种情况。如果您尝试在单个计算机上启动大型（例如11+）合奏成员集群以进行测试，则达到某些ICMP速率限制（例如，在MacOS上）时，可达检查可能会失败。

  默认值为**true**。通过将此参数设置为“ false”，可以禁用可达性检查。请注意，禁用可达性检查将导致群集在网络出现问题期间无法正确地重新配置自身，因此建议仅在测试期间禁用此功能。

  除非您通过设置*multiAddress.enabled = true*启用MultiAddress功能，否则此参数无效。



#### Disabling data directory autocreation

**3.5中的新增功能：** ZooKeeper服务器的默认行为是在启动时自动创建数据目录（在配置文件中指定），如果该目录尚不存在。在某些情况下，这可能会带来不便甚至危险。以对正在运行的服务器进行配置更改的情况为例，其中**dataDir**参数被意外更改。当ZooKeeper服务器重新启动时，它将创建一个不存在的目录并开始提供服务-带有一个空的znode命名空间。这种情况可能导致有效的“裂脑”情况（即新无效目录和原始有效数据存储区中的数据）。因此，最好有一个选项来关闭此自动创建行为。通常，对于生产环境，应该这样做，但是不幸的是，此时默认的旧行为无法更改，因此必须根据具体情况进行更改。这留给用户和ZooKeeper发行版的打包者。

当运行**zkServer.sh时，**可以通过将环境变量**ZOO_DATADIR_AUTOCREATE_DISABLE**设置为1 来禁用自动**创建**。当直接从类文件运行ZooKeeper服务器时，可以通过在Java命令行（即**-Dzookeeper.datadir）**上设置**zookeeper.datadir.autocreate = false**来实现。**.autocreate = false**

如果禁用此功能，并且ZooKeeper服务器确定所需的目录不存在，它将生成错误并拒绝启动。

提供了一个新脚本**zkServer-initialize.sh**以支持此新功能。如果禁用了自动创建，则用户必须首先安装ZooKeeper，然后创建数据目录（可能还有txnlog目录），然后启动服务器。否则，如前一段所述，服务器将无法启动。运行**zkServer-initialize.sh**将创建所需的目录，并可选地设置myid文件（可选的命令行参数）。即使不使用自动创建功能本身，也可以使用此脚本，并且该脚本可能已被用户使用，因为过去（用户，包括创建myid文件的设置）这一直是用户的问题。请注意，此脚本确保数据目录仅存在，它不会创建配置文件，而是需要一个配置文件才能执行。



#### Enabling db existence validation

**3.6.0中的新增功能：**当没有找到数据树时，ZooKeeper服务器在启动时的默认行为是将zxid设置为零，并以投票成员的身份加入仲裁。如果某些事件（例如流氓“ rm -rf”）在服务器关闭时删除了数据目录，则可能很危险，因为该服务器可能会帮助选择丢失事务的领导者。如果找不到数据树，则启用数据库存在验证将更改启动时的行为：服务器以无表决权的参与者的身份加入整体，直到能够与领导者同步并获取最新版本的整体数据。为了指示期望有一个空的数据树（集成创建），用户应将文件“ initialize”放置在与“ myid”相同的目录中。服务器将在启动时检测并删除此文件。

当直接从类文件运行ZooKeeper服务器时，可以通过在Java命令行上设置**zookeeper.db.autocreate = false**来启用初始化验证，即**-Dzookeeper.db.autocreate = false**。运行**zkServer-initialize.sh**将创建所需的初始化文件。



#### Performance Tuning Options

**3.5.0中的新增功能：**已对多个子系统进行了改进，以提高读取吞吐量。这包括NIO通信子系统和请求处理管道（Commit Processor）的多线程。NIO是默认的客户端/服务器通信子系统。它的线程模型包括1个接收器线程，1-N个选择器线程和0-M个套接字I / O工作线程。在请求处理管道中，系统可以配置为一次处理多个读取请求，同时保持相同的一致性保证（相同的会话写入后读取）。提交处理器线程模型包括1个主线程和0-N个工作线程。

默认值旨在最大化专用ZooKeeper机器上的读取吞吐量。这两个子系统都需要有足够数量的线程才能达到峰值读取吞吐量。

- *zookeeper.nio.numSelectorThreads*：（仅Java系统属性：**zookeeper.nio.numSelectorThreads**）**3.5.0中的新增功能：** NIO选择器线程数。至少需要1个选择器线程。对于大量的客户端连接，建议使用多个选择器。默认值为sqrt（cpu核心数/ 2）。
- *zookeeper.nio.numWorkerThreads*：（仅Java系统属性：**zookeeper.nio.numWorkerThreads**）**3.5.0中的新增功能：** NIO工作线程数。如果配置了0个工作线程，则选择器线程直接执行套接字I / O。默认值为cpu核心数的2倍。
- *zookeeper.commitProcessor.numWorkerThreads*：（仅Java系统属性：**zookeeper.commitProcessor.numWorkerThreads**）**3.5.0中的新增功能：**提交处理器工作线程数。如果配置了0个工作线程，则主线程将直接处理请求。默认值为cpu核心数。
- *zookeeper.commitProcessor.maxReadBatchSize*：（仅限Java系统属性：**zookeeper.commitProcessor.maxReadBatchSize**）在切换到处理提交之前，要从queuedRequests处理的最大读取数。如果值<0（默认值），则在有本地写操作和挂起的提交时切换。较高的读取批处理大小将延迟提交处理，从而导致提供过时的数据。如果已知读取将以固定大小的批次到达，则将该批次大小与该属性的值匹配可以使队列性能变得平稳。由于读取是并行处理的，因此建议您设置此属性以使其与*zookeeper.commitProcessor.numWorkerThread*（默认为cpu核心数）或更小。
- *zookeeper.commitProcessor.maxCommitBatchSize*：（仅限Java系统属性：**zookeeper.commitProcessor.maxCommitBatchSize**）在处理读取之前要处理的最大提交数。我们将尝试处理尽可能多的远程/本地提交，直到达到此数量为止。较高的提交批处理大小将延迟读取，同时处理更多的提交。较低的提交批处理大小将有利于读取。建议仅在集成正在为高提交率的工作负载提供服务时设置此属性。如果已知写入将达到一定数量的批处理，则将该批处理大小与该属性的值匹配可以使队列性能变得平稳。一种通用方法是将该值设置为等于整体大小，以便在处理每批数据时，当前服务器将概率性地处理与其直接客户端之一相关的写操作。默认值为“ 1”。不支持负值和零值。
- *znode.container.checkIntervalMs*：（仅Java系统属性）**3.6.0中的新增功能：**候选容器和ttl节点的每次检查的时间间隔（以毫秒为单位）。默认值为“ 60000”。
- *znode.container.maxPerMinute*：（仅Java系统属性）**3.6.0中的新增功能：**每分钟可以删除的容器和ttl节点的最大数量。这样可以防止在删除容器时放牧。默认值为“ 10000”。
- *znode.container.maxNeverUsedIntervalMs*：（仅适用**于** Java系统属性）**3.6.0中的新增功能：**保留从未有任何子代的容器的最大间隔（以毫秒为单位）。应该足够长，以使您的客户可以创建容器，进行任何必要的工作然后创建子级。默认值为“ 0”，用于指示从未删除过任何子代的容器不会被删除。



#### Debug Observability Configurations

**3.6.0中的新增功能：**引入了以下选项，以使Zookeeper易于调试。

- *zookeeper.messageTracker.BufferSize*：（仅Java系统属性）控制存储在**MessageTracker中**的最大消息数。值应为正整数。默认值是10。**MessageTracker**在引入**3.6.0**记录最后一组服务器（跟随器或观察者）和龙头之间的消息，当服务器断开与领导者。这些消息集将被转储到Zookeeper的日志文件中，将有助于在断开连接时重建服务器的状态，并且对于调试目的很有用。
- *zookeeper.messageTracker.Enabled*：（仅Java系统属性）设置为“ true”时，将启用**MessageTracker**跟踪和记录消息。默认值为“ false”。



#### AdminServer configuration

**3.6.0中的新增功能：**以下选项用于配置[AdminServer](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver)。

- *admin.portUnification*：（Java系统属性：**zookeeper.admin.portUnification**）启用管理端口以接受HTTP和HTTPS通信。默认为禁用。

**3.5.0中的新增功能：**以下选项用于配置[AdminServer](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver)。

- *admin.enableServer*：（Java系统属性：**zookeeper.admin.enableServer**）设置为“ false”以禁用AdminServer。默认情况下，AdminServer是启用的。
- *admin.serverAddress*：（Java系统属性：**zookeeper.admin.serverAddress**）嵌入式Jetty服务器侦听的地址。默认为0.0.0.0。
- *admin.serverPort*：（Java系统属性：**zookeeper.admin.serverPort**）嵌入式Jetty服务器侦听的端口。默认为8080
- *admin.idleTimeout*：（Java系统属性：**zookeeper.admin.idleTimeout**）设置连接在发送或接收数据之前可以等待的最大空闲时间（以毫秒为单位）。默认为30000毫秒
- *admin.commandURL*：（Java系统属性：**zookeeper.admin.commandURL**）相对于根URL列出和发布命令的URL。默认为“ / commands”。

### Metrics Providers

**3.6.0中的新增功能：**以下选项用于配置指标。

默认情况下，ZooKeeper服务器使用[AdminServer](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver)公开有用的指标。和[四个字母词](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_4lw)界面。

从3.6.0开始，您可以配置其他度量标准提供程序，该度量标准将度量标准导出到您喜欢的系统。

从3.6.0版本开始，ZooKeeper二进制软件包将与[Prometheus.io](https://prometheus.io/)的集成捆绑在一起。

- *metricsProvider.className*：设置为“ org.apache.zookeeper.metrics.prometheus.PrometheusMetricsProvider”以启用Prometheus.io导出器。
- *metricsProvider.httpPort*：Prometheus.io导出器将启动Jetty服务器并绑定到该端口，默认为7000。Prometheus端点为http：// hostname：httPort / metrics。
- *metricsProvider.exportJvmInfo*：如果将此属性设置为**true，则** Prometheus.io将导出有关JVM的有用度量。默认值为true。



### Communication using the Netty framework

[Netty](http://netty.io/)是基于NIO的客户端/服务器通信框架，它简化了Java应用程序的网络级通信的许多复杂性（通过直接使用的NIO）。此外，Netty框架内置了对加密（SSL）和身份验证（证书）的支持。这些是可选功能，可以单独打开或关闭。

在版本3.5+中，通过将环境变量**zookeeper.serverCnxnFactory**设置为**org.apache.zookeeper.server.NettyServerCnxnFactory**，ZooKeeper服务器可以使用Netty代替NIO（默认选项）；对于客户端，将**zookeeper.clientCnxnSocket**设置为**org.apache.zookeeper.ClientCnxnSocketNetty**。



#### Quorum TLS

*3.5.5的新功能*



基于Netty Framework，可以将ZooKeeper集成设置为在其通信通道中使用TLS加密。本节介绍如何在仲裁通信中设置加密。

请注意，Quorum TLS封装了确保领导者选举和法定通信协议的安全。

1. 创建SSL密钥库JKS以存储本地凭据

应该为每个ZK实例创建一个密钥库。

在此示例中，我们生成一个自签名证书，并将其与私钥一起存储在中`keystore.jks`。这适合于测试目的，但是您可能需要正式的证书才能在生产环境中对密钥进行签名。

请注意，别名（`-alias`）和专有名称（`-dname`）必须与关联计算机的主机名匹配，否则主机名验证将不起作用。

```
keytool -genkeypair -alias $(hostname -f) -keyalg RSA -keysize 2048 -dname "cn=$(hostname -f)" -keypass password -keystore keystore.jks -storepass password
```

1. 从密钥库中提取签名的公钥（证书）

*仅对于自签名证书，才需要执行此步骤。*

```
keytool -exportcert -alias $(hostname -f) -keystore keystore.jks -file $(hostname -f).cer -rfc
```

1. 创建包含所有ZooKeeper实例证书的SSL信任库JKS

应该在集合的参与者之间共享同一信任库（存储所有接受的证书）。您需要使用不同的别名将多个证书存储在同一信任库中。别名的名称无关紧要。

```
keytool -importcert -alias [host1..3] -file [host1..3].cer -keystore truststore.jks -storepass password
```

1. 您需要`NettyServerCnxnFactory`用作serverCnxnFactory，因为NIO不支持SSL。将以下配置设置添加到您的`zoo.cfg`配置文件中：

```
sslQuorum=true serverCnxnFactory=org.apache.zookeeper.server.NettyServerCnxnFactory ssl.quorum.keyStore.location=/path/to/keystore.jks ssl.quorum.keyStore.password=password ssl.quorum.trustStore.location=/path/to/truststore.jks ssl.quorum.trustStore.password=password
```

1. 在日志中验证您的集成正在TLS上运行：

```
INFO [main:QuorumPeer@1789] - Using TLS encrypted quorum communication INFO [main:QuorumPeer@1797] - Port unification disabled ... INFO [QuorumPeerListener:QuorumCnxManager$Listener@877] - Creating TLS-only quorum server socket
```



#### Upgrading existing non-TLS cluster with no downtime

*3.5.5的新功能*

这是通过利用端口统一功能在不停机的情况下将已经运行的ZooKeeper集成升级到TLS所需的步骤。

1. 如上一节所述，为所有ZK参与者创建必要的密钥库和信任库
2. 添加以下配置设置并重新启动第一个节点

```
sslQuorum=false portUnification=true serverCnxnFactory=org.apache.zookeeper.server.NettyServerCnxnFactory ssl.quorum.keyStore.location=/path/to/keystore.jks ssl.quorum.keyStore.password=password ssl.quorum.trustStore.location=/path/to/truststore.jks ssl.quorum.trustStore.password=password
```

请注意，尚未启用TLS，但我们打开了端口统一。

1. 在其余节点上重复步骤2。验证您在日志中看到以下条目：

```
INFO [main:QuorumPeer@1791] - Using insecure (non-TLS) quorum communication INFO [main:QuorumPeer@1797] - Port unification enabled ... INFO [QuorumPeerListener:QuorumCnxManager$Listener@874] - Creating TLS-enabled quorum server socket
```

在每个节点重新启动后，您还应该仔细检查仲裁是否再次恢复正常。

1. 在每个节点上启用Quorum TLS并进行滚动重启：

```
sslQuorum=true portUnification=true
```

1. 验证整个集成在TLS上运行后，您可以禁用端口统一并再次滚动重启

```
sslQuorum=true portUnification=false
```



### ZooKeeper Commands



#### The Four Letter Words

ZooKeeper响应少量命令。每个命令由四个字母组成。您可以在客户端端口通过telnet或nc向ZooKeeper发出命令。

三个更有趣的命令：“ stat”提供有关服务器和连接的客户端的一些常规信息，而“ srvr”和“ cons”分别提供有关服务器和连接的扩展详细信息。

**3.5.3中的新增功能：**四个字母词必须在使用前明确列出白色。有关详细信息，请参考[群集配置部分中](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_clusterOptions)描述的**4lw.commands.whitelist**。展望未来，不推荐使用四个字母词，请改用[AdminServer](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver)。

- *conf*：**3.3.0中的新增功能：**打印有关服务配置的详细信息。

- *缺点*：**3.3.0中的新增功能：**列出了连接到该服务器的所有客户端的完整连接/会话详细信息。包括有关已接收/已发送的数据包数量，会话ID，操作等待时间，最后执行的操作等信息。

- *crst*：**3.3.0中的新增功能：**重置所有连接的连接/会话统计信息。

- *dump*：列出未完成的会话和临时节点。

- *envi*：打印有关服务环境的详细信息

- *ruok*：测试服务器是否以非错误状态运行。如果服务器正在运行，它将以imok响应。否则，它将完全不响应。响应“ imok”不一定表示服务器已加入仲裁，只是服务器进程处于活动状态并绑定到指定的客户端端口。使用“ stat”获取有关状态仲裁和客户端连接信息的详细信息。

- *srst*：重置服务器统计信息。

- *srvr*：**3.3.0中的新功能：**列出服务器的完整详细信息。

- *stat*：列出服务器和连接的客户端的简要详细信息。

- *wchs*：**3.3.0中的新增功能：**列出有关服务器*监视的*简要信息。

- *wchc*：**3.3.0中的新增功能：**按会话列出有关服务器*监视的*详细信息。这将输出具有相关监视（路径）的会话（连接）列表。请注意，根据手表的数量，此操作可能会很昂贵（即影响服务器性能），请小心使用。

- *dirs*：**3.5.1中的新增功能：**以字节为单位显示快照和日志文件的总大小

- *wchp*：**3.3.0中的新增功能：**按路径列出有关服务器*监视的*详细信息。这将输出具有关联会话的路径（znode）列表。请注意，根据手表的数量，此操作可能会很昂贵（即影响服务器性能），请小心使用。

- *mntr*：**3.4.0中的新增功能：**输出可用于监视集群运行状况的变量列表。

  $ echo mntr | 数控本地主机2185 zk_version 3.4.0 zk_avg_latency 0.7561 - 是考虑到小数点后四位zk_max_latency 0 zk_min_latency 0 zk_packets_received 70 zk_packets_sent 69个zk_outstanding_requests 0 zk_server_state领导zk_znode_count 4 zk_watch_count 0 zk_ephemerals_count 0 zk_approximate_data_size 27个zk_followers 4 - 只有领导者zk_synced_followers 4曝光 - 只露Leader zk_pending_syncs 0-仅由Leader zk_open_file_descriptor_count公开23-仅在Unix平台上可用zk_max_file_descriptor_count 1024-仅在Unix平台上可用

输出与Java属性格式兼容，并且内容可能会随时间变化（添加了新键）。您的脚本应该期待更改。注意：一些密钥是特定于平台的，而某些密钥仅由Leader导出。输出包含具有以下格式的多行：

```
key \t value
```

- *isro*：**3.4.0中的新增功能：**测试服务器是否以只读模式运行。如果服务器处于只读模式，则服务器将以“ ro”响应，如果不是处于只读模式，则服务器将以“ rw”响应。

- *hash*：**3.6.0中的新增功能：**返回与zxid关联的树摘要的最新历史记录。

- *gtmk*：以十进制格式获取当前的跟踪掩码，作为64位带符号的long值。请参阅`stmk`以获取可能值的说明。

- *stmk*：设置当前的跟踪掩码。跟踪掩码是64位，其中每个位启用或禁用服务器上特定类别的跟踪日志记录。必须将Log4J配置为`TRACE`首先启用级别，才能查看跟踪日志记录消息。跟踪掩码的位对应于以下跟踪日志记录类别。

  | Trace Mask Bit Values |                                                              |
  | --------------------- | ------------------------------------------------------------ |
  | 0b0000000000          | 未使用，保留以备将来使用。                                   |
  | 0b0000000010          | 记录客户端请求，但不包括ping请求。                           |
  | 0b0000000100          | 未使用，保留以备将来使用。                                   |
  | 0b0000001000          | 记录客户端ping请求。                                         |
  | 0b0000010000          | 记录从作为当前领导者的仲裁对等方收到的数据包，但不包括ping请求。 |
  | 0b0000100000          | 记录客户端会话的添加，删除和验证。                           |
  | 0b0001000000          | 记录监视事件到客户端会话的传递。                             |
  | 0b0010000000          | 记录从作为当前领导者的仲裁对等方收到的ping数据包。           |
  | 0b0100000000          | 未使用，保留以备将来使用。                                   |
  | 0b1000000000          | 未使用，保留以备将来使用。                                   |

  64位值中的所有其余位均未使用，并保留以供将来使用。通过计算记录值的按位或，可以指定多个跟踪日志记录类别。默认跟踪掩码为0b0100110010。因此，默认情况下，跟踪日志记录包括客户端请求，从领导者接收的数据包和会话。要设置其他跟踪掩码，请发送一个包含`stmk`四个字母的单词的请求，后跟一个跟踪掩码，表示为一个64位带符号的long值。本示例使用Perl `pack`函数构造一个跟踪掩码，该掩码启用上述所有跟踪日志记录类别，并将其转换为具有big-endian字节顺序的64位有符号long值。`stmk`使用netcat 将结果附加到服务器并发送到服务器。服务器以十进制格式响应新的跟踪掩码。

  $ perl -e“打印'stmk'，pack（'q>'，0b0011111010）” | nc本地主机2181 250

这是**ruok**命令的示例：

```
$ echo ruok | nc 127.0.0.1 5111
    imok
```



#### The AdminServer

**3.5.0中的新增功能：** AdminServer是嵌入式Jetty服务器，为四个字母单词命令提供HTTP接口。默认情况下，服务器在端口8080上启动，并且通过访问URL“ / commands / [command name]”发出命令，例如http：// localhost：8080 / commands / stat。命令响应作为JSON返回。与原始协议不同，命令不限于四个字母的名称，命令可以具有多个名称。例如，“ stmk”也可以称为“ set_trace_mask”。要查看所有可用命令的列表，请将浏览器指向URL / commands（例如，http：// localhost：8080 / commands）。请参阅[AdminServer配置选项，](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_adminserver_config)以了解如何更改端口和URL。

AdminServer默认情况下处于启用状态，但可以通过以下任一方式禁用：

- 将zookeeper.admin.enableServer系统属性设置为false。
- 从类路径中删除Jetty。（如果您想覆盖ZooKeeper的码头依赖，则此选项很有用。）

请注意，如果AdminServer被禁用，则TCP四字母词接口仍然可用。

可用的命令包括：

- *connection_stat_reset / crst*：重置所有客户端连接统计信息。没有返回新字段。
- *configuration / conf / config*：打印有关服务配置的基本详细信息，例如客户端端口，数据目录的绝对路径。
- *connections / cons*：有关客户端与服务器的连接的信息。注意，根据客户端连接的数量，此操作可能会很昂贵（即影响服务器性能）。返回“连接”，即连接信息对象的列表。
- *hash*：历史摘要列表中的Txn摘要。每128个事务记录一次。返回“摘要”，这是事务摘要对象的列表。
- *dirs*：有关日志文件目录和快照目录大小的信息（以字节为单位）。返回“ datadir_size”和“ logdir_size”。
- *dump*：有关会话到期和临时信息。注意，根据全局会话和临时消息的数量，此操作可能会很昂贵（即影响服务器性能）。以地图形式返回“ expiry_time_to_session_ids”和“ session_id_to_ephemeral_paths”。
- *环境/环境/环境*：所有定义的环境变量。返回每个作为其自己的字段。
- *get_trace_mask / gtmk*：当前的跟踪掩码。*set_trace_mask的*只读版本。有关更多详细信息，请参见四字母命令*stmk*的描述。返回“ tracemask”。
- *initial_configuration / icfg*：打印用于启动对等方的配置文件的文本。返回“ initial_configuration”。
- *is_read_only / isro*：如果此服务器处于只读模式，则为true / false。返回“ read_only”。
- *last_snapshot / lsnp*：*Zookeeper*服务器已完成将其保存到磁盘的最后一个快照的信息。如果在服务器启动到服务器完成保存其第一张快照的初始时间段内调用该命令，则该命令将返回启动服务器时读取的快照的信息。返回“ zxid”和“ timestamp”，后者使用秒的时间单位。
- *领导者/领导者*：如果将集成配置为仲裁模式，则将发出对等方的当前领导者状态和当前领导者位置。返回“ is_leader”，“ leader_id”和“ leader_ip”。
- *monitor / mntr*：发出各种有用的监视信息。包括性能统计信息，有关内部队列的信息以及数据树的摘要（以及其他内容）。返回每个作为其自己的字段。
- *reader_connection_stat_reset / orst*：重置所有观察者连接统计信息。对*观察者的*随行指挥。没有返回新字段。
- *ruok*：无操作命令，检查服务器是否正在运行。响应不一定表示服务器已加入仲裁，只是管理服务器处于活动状态并绑定到指定端口。没有返回新字段。
- *set_trace_mask / stmk*：设置跟踪掩码（因此，它需要一个参数）。编写*get_trace_mask的*版本。有关更多详细信息，请参见四字母命令*stmk*的描述。返回“ tracemask”。
- *server_stats / srvr*：服务器信息。返回多个字段，以简要概述服务器状态。
- *stats / stat*：与*server_stats*相同，但还会返回“连接”字段（有关详细信息，请参见*连接*）。注意，根据客户端连接的数量，此操作可能会很昂贵（即影响服务器性能）。
- *stat_reset / srst*：重置服务器统计信息。这是*server_stats*和*stats*返回的信息的子集。没有返回新字段。
- *observerr / obsr*：有关服务器观察器连接的信息。始终在领导者上可用，在跟随者上作为学习者的主人可用。返回“ synced_observers”（int）和“ observers”（每个观察者属性的列表）。
- *system_properties / sysp*：所有定义的系统属性。返回每个作为其自己的字段。
- *Voting_view*：在集合中提供当前的投票成员。返回“ current_config”作为映射。
- *watch / wchc*：按会话汇总的观看信息。请注意，根据手表的数量，此操作可能会很昂贵（即影响服务器性能）。返回“ session_id_to_watched_paths”作为地图。
- *watch_by_path / wchp*：按路径汇总的观看信息。请注意，根据手表的数量，此操作可能会很昂贵（即影响服务器性能）。返回“ path_to_session_ids”作为地图。
- *watch_summary / wchs*：汇总的观看信息。返回“ num_total_watches”，“ num_paths”和“ num_connections”。
- *zabstate*：对等*方正*在运行的Zab协议的当前阶段，以及它是否是有投票权的成员。对等可以处于以下阶段之一：选举，发现，同步，广播。返回字段“ voting”和“ zabstate”。



### Data File Management

ZooKeeper将其数据存储在数据目录中，并将其事务日志存储在事务日志目录中。默认情况下，这两个目录相同。可以（并且应该）将服务器配置为将事务日志文件存储在与数据文件不同的目录中。当事务日志驻留在专用日志设备上时，吞吐量增加而延迟减少。



#### The Data Directory

该目录中包含两个或三个文件：

- *myid-*在人类可读的ASCII文本中包含一个表示服务器ID的整数。
- *初始化* -存在指示缺少数据树。创建数据树后清除。
- *快照。* -保存数据树的模糊快照。

每个ZooKeeper服务器都有一个唯一的ID。此id在两个地方使用：*myid*文件和配置文件。该*身份识别码*文件标识服务器对应于给定的数据目录。配置文件列出了由服务器ID标识的每个服务器的联系信息。当ZooKeeper服务器实例启动时，它会从*myid*文件中读取其ID ，然后使用该ID从配置文件中读取，并查找其应侦听的端口。

从某种意义上说，存储在数据目录中的*快照*文件是模糊快照，即在ZooKeeper服务器获取快照的过程中，正在对数据树进行更新。*快照*文件名的后缀是*zxid*快照开始时最后提交的事务的ZooKeeper事务ID。因此，快照包括在快照进行过程中发生的数据树更新的子集。因此，快照可能不对应于实际存在的任何数据树，因此，我们将其称为模糊快照。尽管如此，ZooKeeper仍可以使用此快照进行恢复，因为它利用了其更新的幂等性质。通过针对模糊快照重播事务日志，ZooKeeper可以在日志末尾获取系统状态。



#### The Log Directory

日志目录包含ZooKeeper事务日志。在进行任何更新之前，ZooKeeper确保将代表更新的事务写入非易失性存储。当写入当前日志文件的事务数达到（可变）阈值时，将启动一个新的日志文件。使用影响快照频率的相同参数计算阈值（请参见上面的snapCount和snapSizeLimitInKb）。日志文件的后缀是写入该日志的第一个zxid。



#### File Management

在独立的ZooKeeper服务器和复制的ZooKeeper服务器的不同配置之间，快照和日志文件的格式不会更改。因此，您可以将这些文件从运行中的复制ZooKeeper服务器拉到带有独立ZooKeeper服务器的开发计算机上，以进行故障排除。

使用较旧的日志和快照文件，您可以查看ZooKeeper服务器的先前状态，甚至可以恢复该状态。LogFormatter类允许管理员查看日志中的事务。

ZooKeeper服务器创建快照和日志文件，但从不删除它们。数据和日志文件的保留策略是在ZooKeeper服务器外部实现的。服务器本身仅需要最新的完整模糊快照，其后的所有日志文件以及其前的最后一个日志文件。后一个要求是必需的，以包括在启动此快照之后发生的更新，但该更新当时已存在于现有的日志文件中。之所以可能这样做，是因为在ZooKeeper中日志的快照和翻转有点独立地进行。有关设置保留策略和维护ZooKeeper存储的更多详细信息，请参阅本文档的[维护](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperAdmin.html#sc_maintenance)部分。

###### 注意

> 这些文件中存储的数据未加密。如果将敏感数据存储在ZooKeeper中，则需要采取必要的措施来防止未经授权的访问。此类措施在ZooKeeper外部（例如，控制对文件的访问），并且取决于部署该文件的各个设置。



#### Recovery - TxnLogToolkit

更多细节可以在[这里](http://zookeeper.apache.org/doc/current/zookeeperTools.html#zkTxnLogToolkit)找到



### Things to Avoid

通过正确配置ZooKeeper，可以避免以下一些常见问题：

- *服务器*列表*不一致*：客户端使用的ZooKeeper服务器列表必须与每个ZooKeeper服务器具有的ZooKeeper服务器列表匹配。如果客户端列表是真实列表的子集，则一切正常，但如果客户端具有位于不同ZooKeeper群集中的ZooKeeper服务器列表，则事情真的会很奇怪。另外，每个Zookeeper服务器配置文件中的服务器列表应彼此一致。
- *事务日志的不正确放置*：ZooKeeper最重要的性能部分是事务日志。ZooKeeper在返回响应之前将事务同步到媒体。专用的事务日志设备是保持良好性能的关键。将日志放在繁忙的设备上会对性能产生不利影响。如果只有一个存储设备，请增加snapCount，以减少快照文件的生成频率；它不能消除问题，但是可以为事务日志提供更多资源。
- *不正确的Java堆大小*：您应该特别注意正确设置Java最大堆大小。特别是，不应创建ZooKeeper交换到磁盘的情况。磁盘对ZooKeeper来说是死亡。一切都是有序的，因此，如果处理一个请求交换了磁盘，则所有其他排队的请求可能也会执行相同的操作。磁盘。不要交换。保守估计：如果您有4G RAM，请不要将Java最大堆大小设置为6G甚至4G。例如，您很有可能在4G机器上使用3G堆，因为操作系统和缓存也需要内存。估算系统所需堆大小的最佳建议方法是运行负载测试，然后确保您的使用率远低于导致系统交换的使用限制。
- *可公开访问的部署*：ZooKeeper集成有望在受信任的计算环境中运行。因此，建议将ZooKeeper部署在防火墙后面。



### Best Practices

为了获得最佳结果，请注意以下Zookeeper良好做法列表：

对于多租户安装看到[部分](https://www.geek-book.com/src/docs/zookeeper3.6.1/zookeeper3.6.1/zookeeper.apache.org/doc/r3.6.1/zookeeperProgrammers.html#ch_zkSessions)细节的ZooKeeper“chroot环境”的支持，部署很多应用程序/服务的接口，以单一的ZooKeeper集群时，这是非常有用的。