**以下描述中用`zk`代指`ZooKeeper`**

## 背景

`04.11`对内部系统使用的`zk`集群执行变更导致集群`4分钟`不可用。

详情如下：

- `Pigeon`使用的`zk`集群原本有`5个节点`（`myid`为`0~5`，以下描述中使用`zk0`指代`id`为`0`的节点，依此类推）
- `zk0`、`zk1`、`zk2`提供对外提供服务（其中，`zk2`为`leader`），`zk3`、`zk4`从未对外提供服务（服务域名中未包含）
- `4月初`机柜迁移，未服务的`zk3`、`zk4`在需要迁移的机柜上，将`zk3`、`zk4`先下线了
- 从提供服务的`zk0`、`zk1`、`zk2`里的配置中删除已经下线的`zk3`、`zk4`，择机重启
- 计划`04.11`进行重启节点的变更
- 此时之前下线的`zk3`、`zk4`已经关机，无法`ping`通
- `2017-04-11 11:19:13`重启完`zk1`之后，集群选举持续无法成功，导致`4分钟`不可用
- 直到`2017-04-11 11:23:01`把其余两个节点（`zk0`、`zk2`）也重启了，集群才恢复可用

变更之前在线下模拟了操作流程，一切正常，对客户端影响都在数秒以内。
这个问题，经过数天的排查，终于找到原因并且重现了。
**`05.09`对`Kafka`依赖的`zk`集群下线节点变更，利用前面的经验制定了下线的步骤，表现与预期相符，至此，验证了结论。**
转眼，已经过了一个月了，小心翼翼地分享下彼时的排查过程，当然，写得异常混乱。

## 懵逼

对于故障排查，可以按照`是否有现场`、`是否能重现`、`是否有详细上下文信息`等几个因素分为划分，因素里面`否`越多，排查难度越大。
`04.11`的问题等到排查的时候，属于`无现场`/`不能重现`/`有详细上下文信息`，毕竟有完整的`ZooKeeper`的日志。

`zk1`日志内容摘取部分如下：

```
...
2017-04-11 11:19:18,797 [myid:1] - LOOKING
2017-04-11 11:19:18,799 [myid:1] - New election. My id =  1, proposed zxid=0x724cd35ff
2017-04-11 11:19:18,808 [myid:1] - Notification: 1 (message format version), 0 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 0 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
2017-04-11 11:19:18,808 [myid:1] - Have smaller server identifier, so dropping the connection: (2, 1)
2017-04-11 11:19:18,809 [myid:1] - Notification: 1 (message format version), 1 (n.leader), 0x724cd35ff (n.zxid), 0x1 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
2017-04-11 11:19:18,810 [myid:1] - Notification: 1 (message format version), 0 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
2017-04-11 11:19:18,811 [myid:1] - Notification: 1 (message format version), 0 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
2017-04-11 11:19:18,813 [myid:1] - Have smaller server identifier, so dropping the connection: (2, 1)
2017-04-11 11:19:19,014 [myid:1] - FOLLOWING
...
2017-04-11 11:19:19,033 [myid:1] - Unexpected exception, tries=0, connecting to /zk0:2888
2017-04-11 11:19:20,034 [myid:1] - Unexpected exception, tries=1, connecting to /zk0:2888
2017-04-11 11:19:21,035 [myid:1] - Unexpected exception, tries=2, connecting to /zk0:2888
2017-04-11 11:19:22,036 [myid:1] - Unexpected exception, tries=3, connecting to /zk0:2888
2017-04-11 11:19:23,037 [myid:1] - Exception when following the leader
...
2017-04-11 11:19:23,904 [myid:1] - Notification time out: 400
...
```

看到这样的信息我是很崩溃的，完全不知道是什么意思。彼时的`ZooKeeeper`对于我来说，就是一个黑盒，探索原因的手段非常有限，眼看成疑案了。谷律师说过，“疑案从无”，换到排查问题也一样，有疑案，说明排查的人修为不够。**彼时，唯有硬啃代码了。**

## 硬啃

`zk1`的日志里面有：

```
2017-04-11 11:19:19,030 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 231
```

按理说，这个时候，`LEADER ELECTION TOOK`的字样已经出现了，选举应该已经结束了。
但是从当时[四字命令](https://zookeeper.apache.org/doc/trunk/zookeeperAdmin.html#The+Four+Letter+Words)`cons`的结果来看，集群里面3台机器确实都处于`This ZooKeeper instance is not currently serving requests`的状态。

再看下`zk2`的日志：

```
2017-04-11 11:23:03,922 [myid:2] - LEADING - LEADER ELECTION TOOK - 232
```

一直到恢复的时候才打印了`LEADER ELECTION TOOK`，`zk0`也是差不多的时间打印这个日志的。

难道`zk1`一直都在自嗨么？再看下`zk1`的日志：

```
2017-04-11 11:19:19,030 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 231
2017-04-11 11:20:24,067 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 61028
2017-04-11 11:20:34,079 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6006
2017-04-11 11:20:44,089 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6003
2017-04-11 11:20:54,100 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6005
2017-04-11 11:21:06,350 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 8245
2017-04-11 11:21:16,361 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6005
2017-04-11 11:21:26,370 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6004
2017-04-11 11:21:36,377 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6002
2017-04-11 11:21:46,382 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 5999
2017-04-11 11:21:56,388 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6002
2017-04-11 11:22:06,393 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 5999
2017-04-11 11:22:16,399 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6000
2017-04-11 11:22:26,405 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6002
2017-04-11 11:22:36,411 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6000
2017-04-11 11:22:46,416 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 5999
2017-04-11 11:22:56,422 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 6000
2017-04-11 11:23:03,904 [myid:1] - FOLLOWING - LEADER ELECTION TOOK - 3476
```

契而不舍地自嗨了`10`多次，这个其实是可以理解的，**`zk1`认为集群里面只有3个节点，拿到两票一致，就认为选举结束了，而`zk0`、`zk2`还是认为集群里面有`5`个节点，所以需要`3`个节点的投票完全统一，才能结束选举**。

这时候有一个问题：为什么`zk1`进入了`FOLLOWING`状态之后，会再一次进行`Looking`状态，重新参与选举呢？

### 问题A

> 为什么`zk1`进入了`FOLLOWING`状态之后，会再一次进行`Looking`状态，重新参与选举呢？

`zk`节点进行`FOLLOWING`状态之后会调用`Follower.followLeader`（代码位于`src/java/main/org/apache/zookeeper/server/quorum/Follower.java`），如果处于正常状态，会一直处于`followLeader`方法的一个`loop`中。

摘取部分代码如下：

```
/**
 * the main method called by the follower to follow the leader
 *
 * @throws InterruptedException
 */
void followLeader() throws InterruptedException {
    self.end_fle = System.currentTimeMillis();
    LOG.info("FOLLOWING - LEADER ELECTION TOOK - " +
          (self.end_fle - self.start_fle));
    self.start_fle = 0;
    self.end_fle = 0;
    fzk.registerJMX(new FollowerBean(this, zk), self.jmxLocalPeerBean);
    try {
        // get InetSocketAddress of current vote id
        InetSocketAddress addr = findLeader();
        try {
            // zk1进行这个方法时，会去调用connectToLeader去连接leader
            connectToLeader(addr);
            ...
            // 如果处于正常状态，线程会一直处于这个loop中
            while (self.isRunning()) {
                readPacket(qp);
                processPacket(qp);
            }
        } catch (IOException e) {
            // 在我们的case中，connectToLeader抛出的异常会在这里捕获，打印日志，然后退出followLeader方法
            LOG.warn("Exception when following the leader", e);
            ...
        }
    } finally {
        zk.unregisterJMX((Learner)this);
    }
}
```

如上面代码中的中文注释所示，`zk1`会去调用`connectToLeader`，那么连接`leader`的哪个端口呢？
我们回头看一下配置文件`conf/zoo.cfg`的内容：

```
...
clientPort=2181
...
server.0=zk0:2888:3888
server.1=zk1:2888:3888
server.2=zk2:2888:3888
server.3=zk3:2888:3888
server.4=zk4:2888:3888
...
```

一共存在`2181`、`2888`、`3888`这3个端口。

- `2181`最常见，是客户端使用的、提供服务的端口
- `2888`是`Leader`的专属端口，只有`Leader`会启动这个端口，就像`Leader`的权杖一样
- `3888`是`zk`节点在选举期间进行通信的

所以，`connectToLeader`会去连接`leader`（这时候从投票结果中，`zk1`认为`zk0`是`leader`）的`2888`端口，而这时，`zk0`并没有认为自己是`leader`，并没有启动`2888`端口，所以`zk1`的日志中会有如下的报错：

```
2017-04-11 11:19:19,033 [myid:1] - Unexpected exception, tries=0, connecting to /zk0:2888
```

`connectToLeader`中会重试`5`次，每次重试之前间隔`1s`，全部重试失败之后，会抛出异常到上层，从而导致`followLeader`方法退出。
再看看`QuorumPeer.run`（代码位于`src/java/main/org/apache/zookeeper/server/quorum/QuorumPeer.java`）方法里面，节点进入`FOLLOWING`状态后的处理：

```
case FOLLOWING:
    // in another word, when our state switch to FOLLOWING ..
    try {
        LOG.info("FOLLOWING");
        setFollower(makeFollower(logFactory));
        // 我们的case中，zk1调用followLeader后会因为连接不上leader而退出
        follower.followLeader();
    } catch (Exception e) {
        LOG.warn("Unexpected exception",e);
    } finally {
        // followLeader退出之后，会进行到这里，关闭follower
        follower.shutdown();
        setFollower(null);
        // 关闭掉follower之后，会重新将节点状态设置为LOOKING
        setPeerState(ServerState.LOOKING);
    }
    break;
```

所以这个问题的路径是：
`=>` `zk1`进入`FOLLOWING`状态
`=>` `zk1`调用`followLeader`去连接`leader`
`=>` `zk1`认为的`leader`-`zk0`并不认为是`leader`，没有启动`2888`端口
`=>` `zk1`连接`leader`失败
`=>` `zk1`退出`FOLLOWING`状态，进入`LOOKING`状态

这时候有一个问题：为什么`zk0`没有进入`leader`状态；如果是因为`zk2`没有投票给`zk0`，为什么`zk2`没有投票给`zk0`？

### 问题B

> 为什么`zk0`没有进入`leader`状态；如果是因为`zk2`没有投票给`zk0`，为什么`zk2`没有投票给`zk0`？

`zk0`没有进入`leader`状态说明没有获取足够的票数，从`zk1`的日志里面可以看到，`zk1`已经投票给了`zk0`：

```
2017-04-11 11:19:18,811 [myid:1] - Notification: 1 (message format version), 0 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
```

这里解释一下，`zk`选举过程中最关键的日志的格式。这个日志是在`FastLeaderElection.printNotification`（代码位于`src/java/main/org/apache/zookeeper/server/quorum/FastLeaderElection.java`）中打印的。逐段来看下含义：

- `1 (message format version)`
  消息协议的版本号，从代码里面看，这个字段比较好的版本里面是`0`，`ZooKeeper 3.4.6`里面，这个版本号是`1`。
- `0 (n.leader)`
  收到的投票里面的`leader`对应的`id`。例子里面这张投票是投给`zk0`的。
- `0x724cd3601 (n.zxid)`
  收到的投票里面的`leader`对应的`zxid`，`zxid`的高`32`位代表`epoch`（选出`leader`后会对`epoch`进行更新），低`32`位代表日志偏移。例子里面的数据说明，收到的这张投票里面。
- `0x8 (n.round)`
  投票发送方的`logicalclock`，这个值和节点进入`FastLeaderElection.lookForLeader`方法的次数是相关的，譬如我们的`case`中，`zk1`频繁地进行`LOOKING`->`FOLLOWING`->`LOOKING`状态的转换，所以`logicalclock`会不断地增加。如果节点收到一张投票，`n.round`是比自己的`logicalclock`大时，就会更新自己的`logicalclock`，更新自己的票为收到的投票信息或者初始票（初始票即为投票信息填写的是节点自己的信息）。`zk1`每次重新进行`LOOKING`状态时，`logicalclock`都比别的节点要大，但是`zk1`的`zxid`比其它两个节点要小，所以`zk0`和`zk1`会各自重新投票给自己。
- `LOOKING (n.state)`
  投票发送方的状态。例子里面发送方`zk1`的状态为`LOOKING`。
- `1 (n.sid)`
  投票发送方的`id`。例子里面这张投票是`zk1`发送出来的。
- `0x7 (n.peerEpoch)`
  收到的投票里面的`leader`对应的`epoch`，当然，这个值已经被`n.zxid`所涵盖了
- `LOOKING (my state)`
  寄几的状态，即投票接收方当前的状态。

解释完了日志的信息，再从`zk0`的日志里面去看下为什么`zk0`没有获得足够的票：

```
# 这里由于zk1重启，zk0进入了LOOKING状态
2017-04-11 11:19:13,037 [myid:0] - LOOKING
...
# 进行选举阶段，这时候，会把自己的信息放入选票中，投给所有的节点：zk0/zk1/zk2/zk3/zk4
# 我们把这次选票投递标记成 Proposal1
# zk1此时关闭了，还没启动起来，3888端口没有打开；zk3/zk4目前已经关机，ping不通了
2017-04-11 11:19:13,662 [myid:0] - New election. My id = 0, proposed zxid=0x724cd3601
# 收到了自己 Proposal1阶段 的投票
2017-04-11 11:19:13,663 [myid:0] - Notification: 1 (message format version), 0 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 0 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
# 选票发送给zk1的时候失败，因为zk1此时还没有启动
2017-04-11 11:19:13,674 [myid:0] - Cannot open channel to 1 at election address /zk1:3888
# 由于zk中只能由id大的节点向id小的节点建立链接，所以，zk0会把已经建立的到zk2的链接关闭掉
2017-04-11 11:19:13,675 [myid:0] - Have smaller server identifier, so dropping the connection: (2, 0)
# 收到zk2的链接，这个是zk2也进入了选举阶段之后，向各个节点发送选票的时候，建立的链接
2017-04-11 11:19:13,676 [myid:0] - Received connection request /zk2:22864
# zk0收到zk2的两张选票，第一张选票的epoch是0x6，怀疑是上一次选举留下的
2017-04-11 11:19:13,677 [myid:0] - Notification: 1 (message format version), 2 (n.leader), 0x6002c6134 (n.zxid), 0x7 (n.round), LOOKING (n.state), 2 (n.sid), 0x6 (n.peerEpoch) LOOKING (my state)
# zk0收到zk2的第二张选票，里面携带的是zk2自己的信息，zk2的epoch/zxid和zk0相同，但是id比zk0要大
# 这个时候，zk0应该修改自己的当前选票，推举zk2为leader，并把这个选票发送给所有的节点
# 我们把这次选票投递标记成 Proposal2
# 但是，从下面的日志看来，zk0迟迟没有收到自己的这张投票
2017-04-11 11:19:13,730 [myid:0] - Notification: 1 (message format version), 2 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 2 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
# 长时间zk0没有收到任何的投票，zk0/zk2仿佛都沉默了
2017-04-11 11:19:13,930 [myid:0] - Notification time out: 400
2017-04-11 11:19:14,331 [myid:0] - Notification time out: 800
2017-04-11 11:19:15,131 [myid:0] - Notification time out: 1600
2017-04-11 11:19:16,732 [myid:0] - Notification time out: 3200
# 这个时候，还在投递 Proposal1 阶段向zk3发送投票，因为zk3此时已下线，ping不能，所以需要等待connect操作超时
# connect过程位于QuorumCnxManager.connectOne中，超时时间由zookeeper.cnxTimeout这个系统属性决定，默认5s
# 从 Proposal1 阶段开始的时间11:19:13,662到这里，刚好是5s，非常吻合
# 投票都是先发送到sendqueue里面，再由FastLeaderElection.WorkerSender取出，调用QuorumCnxManager.toSend
# QuorumCnxManager.toSend会去调用QuorumCnxManager.connectOne连接选票接收方
# 所以， Proposal1 阶段的选票还没有从sendqueue队列里面出来，是无法发送Proposal2 阶段的选票
# 令人沮丧的是，zk3/zk4都无法ping通，导致每次Proposal需要耗时10s
2017-04-11 11:19:18,695 [myid:0] - Cannot open channel to 3 at election address /zk3:3888
# 这个时候，zk1重启完成，发送自己的选票，连接到了zk0
2017-04-11 11:19:18,803 [myid:0] - Received connection request /zk1:4935
# 收到zk1的第一张选票，可以看到zk1的zxid比zk0/zk2是要小的
2017-04-11 11:19:18,806 [myid:0] - Notification: 1 (message format version), 1 (n.leader), 0x724cd35ff (n.zxid), 0x1 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
# 收到zk1的第二张选票，此时，zk1已经认为zk0是leader了
2017-04-11 11:19:18,809 [myid:0] - Notification: 1 (message format version), 0 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
2017-04-11 11:19:22,010 [myid:0] - Notification time out: 6400
# 收到zk1的第三张选票，这个时候，zk1已经从FOLLOWING状态再次进入了Looking状态，又一次投票给了自己
2017-04-11 11:19:23,677 [myid:0] - Notification: 1 (message format version), 1 (n.leader), 0x724cd35ff (n.zxid), 0x9 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
# 这个时候，还在投递 Proposal1 阶段向zk4发送投票
2017-04-11 11:19:23,701 [myid:0] - Cannot open channel to 4 at election address /zk4:3888
2017-04-11 11:19:23,701 [myid:0] - Notification: 1 (message format version), 2 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 0 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
2017-04-11 11:19:23,742 [myid:0] - Notification: 1 (message format version), 1 (n.leader), 0x724cd35ff (n.zxid), 0x9 (n.round), LOOKING (n.state), 1 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
# zk0收到zk2的第三张选票，距离上次收到zk2的投票时间，11:19:13,677，已经过去了10s
# zk2也面临着和zk0一样的问题，连接zk3/zk4的时间会耗时10s
2017-04-11 11:19:23,789 [myid:0] - Notification: 1 (message format version), 2 (n.leader), 0x724cd3601 (n.zxid), 0x8 (n.round), LOOKING (n.state), 2 (n.sid), 0x7 (n.peerEpoch) LOOKING (my state)
```

所以`问题B`的答案：

- 为什么`zk0`没有进入`leader`状态？
  在`zk1`从`LOOKING`进入`FOLLOWING`的期间（`11:19:18 - 11:19:19`），`zk0`早已将自己的选票投给了`zk2`，`zk0`是不可能成为`leader`的。只是由于`zk3`/`zk4`的缘故，`zk0`的第二张选票（认为`zk2`是`leader`的投票），一直到`11:19:23`以后才发送给`zk1`，为时已晚。
- 如果是因为`zk2`没有投票给`zk0`，为什么`zk2`没有投票给`zk0`
  在`zk1`从`LOOKING`进入`FOLLOWING`的期间（`11:19:18 - 11:19:19`），`zk2`还卡在连接`zk3`/`zk4`上，选票无法发送出去；即使选票能发送出去，这个状态下也只可能`zk2`能变成`leader`，因为它同时拥有最大的`epoch`、`zxid`、`id`。

所以，问题的根本原因在于，`zk0`/`zk2`变成了半哑巴，它们在集群里面说一句话，需要间隔`10s`，导致`zk1`频繁地进行状态地切换，即使它找到了正确的`leader`-`zk2`，`zk2`也会因为收不到`zk0`的选票而无法变成`leader`。

基于这个判断，使用`Byteman`模拟连接超时来重现故障场景。

## 重现

### 版本信息

重现过程中使用的版本如下：

- `ZooKeeper`: `3.4.6`
- `Byteman`: `3.0.6`
- `Saltstack`: `salt 2015.8.8 (Beryllium)`

### 重现步骤

#### 1. 创建`5节点`的`ZooKeeper集群`

使用`Saltstack`在本地创建`5节点`的`zk集群`

```
salt '*' state.apply zookeeper-cluster.start
```

集群对应目录如下：

```
tree /tmp/zookeeper-cluster -L 1

/tmp/zookeeper-cluster
├── zk0
├── zk1
├── zk2
├── zk3
└── zk4
```

`zoo.cfg`中节点相关的配置如下：

```
server.0=localhost:8000:9000
server.1=localhost:8001:9001
server.2=localhost:8002:9002
server.3=localhost:8003:9003
server.4=localhost:8004:9004
```

`5节点`对应的`clientPort`为`7000~7004`。

**以下描述中用`zk0`代指`clientPort`为`7000`的`zk节点`，依此类推**

查看各个节点中集群创建完毕之后的角色

```
for i in `seq 7000 7004`; do echo $i: `echo mntr |nc localhost $i |grep -E "zk_server_state|not currently serving"`; done

7000: zk_server_state follower
7001: zk_server_state follower
7002: zk_server_state leader
7003: zk_server_state follower
7004: zk_server_state follower
```

#### 2. 下线节点并修改配置

下线节点`zk3`/`zk4`：

```
for i in `seq 3 4`; do cd /tmp/zookeeper-cluster/zk$i; ./bin/zkServer.sh stop; cd -; done
```

在`zk0`/`zk1`/`zk2`的配置中注释掉`zk3`/`zk4`的配置：

```
for i in `seq 0 2`; do gsed -i 's/server.\([34]\)/# server.\1/g' /tmp/zookeeper-cluster/zk$i/conf/zoo.cfg ; done
```

注释之后的配置如下：

```
server.0=localhost:8000:9000
server.1=localhost:8001:9001
server.2=localhost:8002:9002
# server.3=localhost:8003:9003
# server.4=localhost:8004:9004
```

这时候，各节点的角色如下：

```
for i in `seq 7000 7004`; do echo $i: `echo mntr |nc localhost $i |grep -E "zk_server_state|not currently serving"`; done

7000: zk_server_state follower
7001: zk_server_state follower
7002: zk_server_state leader
7003:
7004:
```

#### 3. 模拟连接`zk3`/`zk4`超时

对`zk0`/`zk2`加载`Byteman`脚本，模拟连接`zk3`/`zk4`超时的问题。

##### 打开监控端口

```
for i in `echo 0 2`; do port=1001$i; pid=`cat /tmp/zookeeper-cluster/zk$i/data/zookeeper_server.pid`; bminstall.sh -b -Dorg.jboss.byteman.transform.all -p $port $pid; done
```

##### 加载`Byteman`脚本

```
for i in `echo 0 2`; do port=1001$i; echo zk$i; bmsubmit.sh -p $port Issue170411.btm; done

zk0
install rule trace pigeon.enter_connect_one_and_sleep_5s

zk2
install rule trace pigeon.enter_connect_one_and_sleep_5s
```

脚本`Issue170411.btm`内容如下：

```
RULE trace pigeon.enter_connect_one_and_sleep_5s
CLASS org.apache.zookeeper.server.quorum.QuorumCnxManager
METHOD connectOne
AT ENTRY
IF $1 > 2
DO
  traceln("*** enter QuorumCnxManager.connectOne, sid: " + $1 + ", ts: " + System.currentTimeMillis() / 1000 + " s");
  Thread.sleep(5000);
  traceln("*** end sleep in QuorumCnxManager.connectOne, sid: " + $1 + ", ts: " + System.currentTimeMillis() / 1000 + " s");
ENDRULE
```

#### 4. 重启`zk1`

重启`zk1`，此时`zk1`的配置中只有`zk0`/`zk1`/`zk2`这3个节点。

```
i=1; cd /tmp/zookeeper-cluster/zk$i; ./bin/zkServer.sh stop; sleep 5; ./bin/zkServer.sh start; cd -
```

这时候，就可以看到选举一直无法成功，`no matter how long it takes ... :(`

```
for i in `seq 7000 7004`; do echo $i: `echo mntr |nc localhost $i |grep -E "zk_server_state|not currently serving"`; done

7000: This ZooKeeper instance is not currently serving requests
7001: This ZooKeeper instance is not currently serving requests
7002: This ZooKeeper instance is not currently serving requests
7003:
7004:
```

## 小结

**无疑，这次问题出现是因为下线操作不合理。**
`zk0`/`zk1`/`zk2`/`zk3`/`zk4`这样`5节点`的`zk`集群，需要下线`zk3`/`zk4`两个节点的时候，如果`zk3`/`zk4`不是原集群的`leader`，合理规范的操作应该是：

- 修改`zk0`/`zk1`/`zk2`的配置为`3节点`
- 逐台重启`zk0`/`zk1`/`zk2`，最后重启`leader`

这样，只有在重启`leader`时才会影响集群的可用性。

```
上联：软柿子，越捏越不爽
下联：硬骨头，啃啃更健康
横批：迎难而上
```

## 参考

- http://siye1982.github.io/2015/06/16/zookeeper/
- https://zookeeper.apache.org/doc/trunk/zookeeperReconfig.html
- https://zookeeper.apache.org/doc/r3.4.6/zookeeperInternals.html
- http://stackoverflow.com/questions/18168541/what-is-zookeeper-port-and-its-usage