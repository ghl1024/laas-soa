### 文章目录

- - - [1、Java JDK环境配置](https://blog.csdn.net/u014630623/article/details/103695314#1Java_JDK_3)
    - - - [1.1 jdk包下载](https://blog.csdn.net/u014630623/article/details/103695314#11_jdk_7)
        - [1.2 解压jdk包并将文件夹移动到指定位置](https://blog.csdn.net/u014630623/article/details/103695314#12_jdk_11)
        - [1.3 添加系统环境变量](https://blog.csdn.net/u014630623/article/details/103695314#13__20)
        - [1.4 检查是否配置成功](https://blog.csdn.net/u014630623/article/details/103695314#14__34)
    - [2、集群版zookeeper 配置](https://blog.csdn.net/u014630623/article/details/103695314#2zookeeper__48)
    - - - [2.1 zookeeper安装包下载](https://blog.csdn.net/u014630623/article/details/103695314#21_zookeeper_58)
        - [2.2 解压安装包并创建软连接](https://blog.csdn.net/u014630623/article/details/103695314#22__74)
        - [2.3 设置myid](https://blog.csdn.net/u014630623/article/details/103695314#23_myid_86)
        - [2.4 zookeeper配置zoo.cfg修改----静态配置](https://blog.csdn.net/u014630623/article/details/103695314#24_zookeeperzoocfg_110)
        - [2.5 zookeeper动态配置文件](https://blog.csdn.net/u014630623/article/details/103695314#25_zookeeper_163)
        - [2.6 /bin/zkEnv.sh配置修改](https://blog.csdn.net/u014630623/article/details/103695314#26_binzkEnvsh_199)
        - [2.7 conf/log4j.properties 配置修改](https://blog.csdn.net/u014630623/article/details/103695314#27_conflog4jproperties__212)
        - [2.8 启动、重启、暂停zookeeper集群](https://blog.csdn.net/u014630623/article/details/103695314#28_zookeeper_223)
        - [2.9 zookeeper服务验证](https://blog.csdn.net/u014630623/article/details/103695314#29_zookeeper_240)
        - [1.9 需要注意的一些问题](https://blog.csdn.net/u014630623/article/details/103695314#19__271)


​ 前面说明了zookeeper3.4.14的配置说明，3.5.6版本zookeeper一个最大的特点就是可以动态的修改配置文件，另外配置文件的部署也和3.4.14有略微不同，分成了动态和静态配置文件两个，区别主要在于2.4和2.5章节。



### 1、Java JDK环境配置

 由于zookeeper是使用java语言编写，所以在搭建zookeeper服务之前，服务器必须具备java环境（若已具备该环境，可直接跳过）

##### 1.1 jdk包下载

官网下载地址：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

##### 1.2 解压jdk包并将文件夹移动到指定位置

```shell
tar -xvzf jdk-8u231-linux-x64.tar.gz
mv jdk1.8.0_231 /usr/local/
```

##### 1.3 添加系统环境变量

向/etc/profile文件末尾中添加如下配置后，并执行source /etc/profile

```powershell
JAVA_HOME=/usr/local/jdk1.8.0_231
JRE_HOME=$JAVA_HOME/jre
PATH=$PATH:$JAVA_HOME/bin
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
JVMFLAGS="-Xmx3550m -Xms3550m -Xmn2g -Xss128k"
```

##### 1.4 检查是否配置成功

```shell
$ java -version
java version "1.8.0_231"
Java(TM) SE Runtime Environment (build 1.8.0_231-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.231-b11, mixed mode)
$ javac 
Usage: javac <options> <source files>
...
```

### 2、集群版zookeeper 配置

 本文安装zookeeper使用版本3.4.14版本进行搭建，安装包从官网进行下载，Zookeeper机器间不需要设置免密码登录。本文使用三台服务器进行zookeeper集群的搭建，ip分别为：

- 9.134.128.1
- 9.134.128.2
- 9.134.128.3

##### 2.1 zookeeper安装包下载

 官网下载地址：https://archive.apache.org/dist/zookeeper/。

 特别注意，从版本3.5.5开始，需要下载带有bin名称的包，带有bin名称的包中有编译之后的的二进制包。而之前普通的tar.gz中只有源码无法直接使用。使用不带bin的包直接启动会报错：

 Error: Could not find or load main class org.apache.zookeeper.server.quorum.QuorumPeerMain

 在zookeeper3.5.0之前，zookeeper集群的全体成员以及它的配置参数都是在启动时静态加载的，并且在运行时不可变。因此当zookeeper集群需要扩缩容的时候，我们只能通过**手动修改配置文件然后滚动重启**的方式来完成zk集群的扩容或缩容。当集群中机器较多的时候，可以会因为人工导致误操作的概率加大。

 在zookeeper3.5.0版本之后，zookeeper集群开始支持**动态修改集群中的服务器配置**，而修改的方式只需要通过zk提供的客户端命令reconfig进行操作。可以通过rename命令对集群中的服务器进行增加、删除，还可以改变服务器的端口配置以及服务器在集群中的角色，participant/observer。

 而实现zookeeper进行动态配置的一个很重要的前提就是它将zookeeper的**动态配置与静态配置**进行了分离，动态配置文件通过静态配置文件中的**dynamicConfigFile**关键词与动态配置文件进行链接。同样的，zookeeper3.5之后的版本兼容旧版本的集群配置，使用旧版本配置，zookeeper服务器会将静态文件中的动态部分自动分离出来。



##### 2.2 解压安装包并创建软连接

 此处安装创建软连接的目的是为了方便我们在使用的时候不需要带版本号方便，又能方便的知道当前zookeeper是那一版本的。

```shell
tar -xvzf ./apache-zookeeper-3.5.6-bin.tar.gz
mv /data/apache-zookeeper-3.5.6-bin /data/zookeeper-3.5.6
ln -s /data/zookeeper-3.5.6/ /data/zookeeper
```

##### 2.3 设置myid

 myid是zookeeper集群中每台服务器的唯一标识，因此每台机器不能重复，建议从1开始进行递增。myid放在dataDir文件夹下，文件中只有一个id来标识这台机器。

此处约定：

| IP          | 标识数值 |
| ----------- | -------- |
| 9.134.128.1 | 1        |
| 9.134.128.2 | 2        |
| 9.134.128.3 | 3        |

分别在三台机器上添加myid文件

```shell
echo 1 > /data/zookeeper/data/myid
echo 2 > /data/zookeeper/data/myid
echo 3 > /data/zookeeper/data/myid
```

##### 2.4 zookeeper配置zoo.cfg修改----静态配置

zookeeper服务启动时默认寻找conf文件夹下的zoo.cfg，故在conf下创建文件zoo.cfg。

```shell
touch /data/zookeeper/conf/zoo.cfg
```

zoo.cfg内填入以下配置:

```shell
tickTime=2000
initLimit=5
syncLimit=2
dataDir=/data/zookeeper/data
dataLogDir=/data/zookeeper/datalog

autopurge.purgeInterval=1
autopurge.snapRetainCount=10

extendedTypesEnabled=true
reconfigEnabled=true
standaloneEnabled=false

dynamicConfigFile=/data/zookeeper/conf/zoo.cfg.dynamic
```

**特别注意：**

 从3.5.0开始clientPort和clientPortAddress配置参数不应该被使用，这些配置应该放在动态配置中进行配置。

**配置说明：**

zookeeper选填的配置项较多，其他配置项无需填写直接默认即可，只需要配置上述选项。

- tickTime：服务器与服务器之间、服务器与客户端之间心跳检查的时间间隔。同时它也是一个时间单位，initLimit和syncLimit参数都以该值作为时间单位
- initLimit：集群中的follower服务器(F)与leader服务器(L)之间初始连接时能容忍的最多心跳数（tickTime的数量）。此处表示当已经超过5个心跳时间之后leader还没收到follower的返回信息，则表示当前follower链接失败。
- syncLimit：这个配置项标识 Leader 与 Follower 之间发送消息，请求和应答时间长度，最长不能超过多少个 tickTime 的时间长度，总的时间长度就是 2*2000=4 秒
- dataDir：zookeeper保存快照数据的目录，默认情况下，zookeeper将写数据的日志也保留在这里。
- dataLogDir:指定事务日志文件存放目录。若没指定该值，该日志写在dataDir下
- autopurge.purgeInterval：指定自动清理快照文件和事务日志文件的时间，单位为小时，默认为0表示不自动清理，这个时候可以使用脚本zkCleanup.sh手动清理。不清理的结果是占用的磁盘空间越来越大。
- autopurge.snapRetainCount：指定保留快照文件和事务日志文件的个数，默认为3
- extendedTypesEnabled:开启zookeeper扩展功能，如果需要使用到zookeeper的ttl node功能，需要设置当前参数为true。
- reconfigEnabled：从3.5.0开始，3.5.3之前，无法禁用动态重新配置功能。由于该功能的安全问题，所以在3.5.3之后，zookeeper引入了reconfigEnabled配置，默认情况下，该配置的默认值为false，即无法修改服务器配置，该种状态下所有尝试修改集群配置的命令将都会出错。所以如果需要进行对服务器进行配置，必须将该字段的值设置为true。
- standaloneEnabled：在3.5.0之前，可以在独立模式或分布式模式下运行ZooKeeper。这些是单独的实现堆栈，并且无法在运行时在它们之间进行切换。默认情况下（为了向后兼容），*standaloneEnabled*设置为 *true*。使用此默认值的结果是，如果以单个服务器启动，则不允许集合增长，并且如果从多个服务器启动，则不允许缩小以包含少于两个参与者。将标志设置为*false会*指示系统运行分布式软件堆栈，即使整体中只有一个参与者也是如此。
- dynamicConfigFile：指定当前服务的动态配置。

##### 2.5 zookeeper动态配置文件

首先创建上述静态配置中链接的动态配置文件

```powershell
touch /data/zookeeper/conf/zoo.cfg.dynamic
```

然后在动态配置文件中填入以下配置：

```powershell
server.1=9.134.147.78:2888:3888:participant;2181
server.2=9.134.75.254:2888:3888:participant;2181
server.3=9.134.118.145:2888:3888:participant;2181
```

**配置文件说明：**

```powershell
server.<positive id> = <address1>:<port1>:<port2>[:role];[<client port address>:]<client port>
```

- positive id：zk中的服务器id
- address1:服务器ip地址
- port1:服务器与集群中的leader交换信息的端口。
- Port2: leader选举专用端口
- role:当前服务器在集群中的角色，该角色包括participant或者observer(默认是participant)。observer不参与选举
- client port address：客户端端口ip，默认为0.0.0.0
- client port：客户端链接ip，2181。

##### 2.6 /bin/zkEnv.sh配置修改

zookeeper的系统运行日志默认打印在zookeeper.out文件中，由于zookeeper.out文件不会滚动和自动清理，会导致文件越来越大，所以此处需要修改zkEnv.sh配置，使其系统日志强制输出到日志文件中并支持滚动。

```shell
# 设置系统日志存放目录，将下面命令直接放在zkEnv.sh的最后
export ZOO_LOG_DIR=/data/zookeeper/datalog
# 设置日志输出方式，在zkEnv.sh中寻找ZOO_LOG4J_PROP，将该值修改为:
ZOO_LOG4J_PROP="INFO,ROLLINGFILE"
```

##### 2.7 conf/log4j.properties 配置修改

设置每个日志文件大小为100M，滚动10个文件

```shell
log4j.appender.ROLLINGFILE.MaxFileSize=100MB
log4j.appender.ROLLINGFILE.MaxBackupIndex=10
```

##### 2.8 启动、重启、暂停zookeeper集群

zookeeper集群启动部分先后顺序，可选择任意顺序启动，不过先启动的服务可能会连不上其他服务器，所以在启动之前会有错误日志，这个是正常情况。

```shell
# 启动zookeeper服务
cd /data/zookeeper/bin && ./zkServer.sh start

# 重启zookeeper服务
cd /data/zookeeper/bin && ./zkServer.sh restart

# 停止zookeeper服务
cd /data/zookeeper/bin && ./zkServer.sh stop
```

##### 2.9 zookeeper服务验证

服务安装完毕后，需要验证zookeeper服务是否搭建成功，直接运行./zkServer.sh status即可。

```shell
# 对于leader命令返回值为：
$ ./zkServer.sh status
/usr/local/jdk1.8.0_231/bin/java
ZooKeeper JMX enabled by default
Using config: /data/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost.
Mode: leader

# 对于folllower 命令返回值为：
$ ./zkServer.sh status
/usr/local/jdk1.8.0_231/bin/java
ZooKeeper JMX enabled by default
Using config: /data/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost.
Mode: follower

# 若出现一下错误，可能是zookeeper服务还没完全起来，稍后在进行验证
[hadoop@DEVNET-154-77 ~/zookeeper/bin]$ ./zkServer.sh status
JMX enabled by default
Using config: /data/zookeeper/bin/../conf/zoo.cfg
Client port found: 2181. Client address: localhost.
Error contacting service. It is probably not running.
```

##### 1.9 需要注意的一些问题

 注意当使用老的zoo.cfg配置进行升级为新的配置的时候，**旧配置文件中的clientPort一定要保留**。若不保留，会导致集群起来之后dynamic文件恢复为最新的集群配置，最新集群配置中没有端口，新的zoo.cfg中也没有clientPort，导致出问题。

**参考链接：**

1、[ZooKeeper-3.4.6分布式安装指南](http://blog.chinaunix.net/uid-20682147-id-4220311.html)

2、 [ZooKeeper的配置文件优化性能（转）](https://www.cnblogs.com/EasonJim/p/7488834.html)

3、[zookeeper集群管理配置优化总结](http://www.voidcn.com/article/p-qystdlle-bhe.html)

4、[分布式服务框架 Zookeeper — 管理分布式环境中的数据](https://www.ibm.com/developerworks/cn/opensource/os-cn-zookeeper/index.html)

5、[ZooKeeper动态配置(十四)](https://www.cnblogs.com/dupang/p/5649843.html)

6、[ZooKeeper动态重新配置](https://blog.csdn.net/Aria_Miazzy/article/details/86609693)