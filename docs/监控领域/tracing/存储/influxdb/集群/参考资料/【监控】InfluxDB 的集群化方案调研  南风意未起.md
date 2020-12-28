InfluxDB 本身其实是支持集群化的，但是开源的是不支持的。对于开源的 InfluxDB ，怎么去做到集群化？这里找了点相关的资料。



# 阿里巴巴

阿里的集群化方案就是改了源码。采用的是业内的 ETCD/Raft 方案。他们采用了 ETCD/Raft 作为核心组件，移除了原生的 snapshot 过程。同时放弃原生的日志文件部分 WAL，而改用自研方案。也就是他们的 HybridStorage 方案（Raft 日志模块）。即：内存与文件混合存取，内存保留最新热数据，文件保证全部日志落盘，内存、文件追加操作高度一致。

具体的可参考：[阿里云 InfluxDB® Raft HybridStorage 实现方案](https://developer.aliyun.com/article/708318)

## 参考

[阿里云 InfluxDB® 高可用设计](https://developer.aliyun.com/article/738927)

[阿里云 InfluxDB® Raft HybridStorage 实现方案](https://developer.aliyun.com/article/708318)

# 其他公司

携程的方式就比较通俗易懂，他并没有对 InfluxDB 去做源码上的修改，而是对 InfluxDB 进行了包装。在 InfluxDB 做了一层代理，通过这个代理将数据分发到各个 InfluxDB 上去。

## 官方开源 InfluxDB-Relay

1. 采用双写仅仅解决了数据备份的问题，并未解决 influxdb 读写性能的问题；
2. 只是写入了数据，查询还是需要去读 influxdb。增加了配置文件的复杂度不易维护；
3. 并未对写入失败的数据做任何重试机制的处理。

![img](【监控】InfluxDB 的集群化方案调研  南风意未起.assets/loading.gif)

## 饿了么

![img](【监控】InfluxDB 的集群化方案调研  南风意未起.assets/loading.gif)

优势：

1. influx-proxy 是饿了么在 influxdb-relay 满足不了其性能要求、配置维护要求痛定思痛后重构的产物；
2. influxdb 机器支持动态扩缩；
3. 增加了强大的请求失败后的重试机制。

劣势：

1. 架构中使用的组件较多，增加了使用者的学习成本，且不易于后期的维护；
2. 请求失败重试本身是双刃剑，试想机器性能达到极限，重试无形中又增加了机器的负载；
3. 与自身场景需求不相符，我们内部只是做监控数据的持久化存储，应该是最简单的接入和与 influxdb 最小的架构改造。

## 360 的 HA 方案

![img](【监控】InfluxDB 的集群化方案调研  南风意未起.assets/loading.gif)

优势：

1. 以 measurement 为最小拆分单元，从而保证以时序查询 influxdb 的高效性。
2. 支持业务层动态的拆库、拆表操作。

### 参考

[360 influxDB 集群模式实践](https://www.infoq.cn/article/IcvfEmGM8WzS8PO72ZwR)

## 携程 (Hickwall)

![img](【监控】InfluxDB 的集群化方案调研  南风意未起.assets/loading.gif)

在这个架构中监控数据从 Proxy 进来分三路转发，第一路发送给 InfluxDB 集群，确保无论发生任何故障，只要 Hickwall 恢复正常，用户就能立即看到线上系统的当前状态。

第二路发送给 Kafka，由 Down Sample 完成数据聚合后将聚合数据直接写入到 InfluxDB 集群。第三路发送给流式告警，这三路数据互不影响，即使存储和聚合都出现问题，告警依然可以正常工作，确保了告警的可靠稳定。

### InfluxDB 集群设计

![img](【监控】InfluxDB 的集群化方案调研  南风意未起.assets/loading.gif)

优势:

1. 和前面的方案一样（除了阿里以及腾讯除外），没有做代码入侵式的修改
2. 通过在上层维护关于数据分布和查询的元数据，因此当 InfluxDB 有重大发布的时候 InCluster 能够及时更新数据节点。
3. 通过 InCluster 节点写入数据，InCluster 按照数据分布策略将写入请求转发到相关的 Influxdb 节点上，查询的时候按照数据分布策略从各个节点上读取数据并合并查询结果
4. 元数据这一层 InCluster 采用 raft 保证元数据的一致性和分区容错性，在具体数据节点上使用一致性 hash 保证数据的可用性和分区容错性。
5. InCluster 提供了三种数据分布策略 Series、Measurement 和 Measurement+Tag。通过调整数据分布策略，InCluster 能够尽量做到减少数据热点并在查询时减少查询节点

#### 容灾

![img](【监控】InfluxDB 的集群化方案调研  南风意未起.assets/loading.gif)

按照数据分布策略通过读取 InfluxDB 底层的 TSM 数据文件，来恢复损坏的节点上面的数据。Hickwall 的实践经验表明 InCluster 能够做到半个小时恢复一个损坏的节点。

#### 数据聚合的探索

InfluxDB 在数据存储和简单查询方面的表现很优秀，但是在数据聚合上就存在一些问题。

InfluxDB 提供了 Continuous Query Language (CQL) 用于数据聚合。但是 CQL 的内存占用比较大，InfluxDB 的占用内存本身就大，加上 CQL 的内存占用，会造成 节点的不稳定，易宕机。

CQL 无法从不同的节点获取数据进行聚合，在 集群大方案中必定会造成资源浪费，维护复杂等情况。携程将数据聚合功能独立出来，在外部进行数据聚合在写入到 InfluxDB 中去。

时间维度的聚合是有状态的计算，会有两个问题：

1. 中间状态如何减少内存的使用
2. 节点重启时中间状态如何恢复

携程做法:

1. 通过指定每个节点消耗的 Kafka Partition, 使得每个节点需要处理的数据可控，避免 KafkaPartition Rebalance 导致内存不必要的使用；
2. 通过对 Measurement 和 Tag 这些字符串的去重可以减少内存使用；
3. 中间状态恢复方面我们并没有使用保存 CheckPoint 的方法，而是通过提前一段时间消费来恢复中间状态。这种方式避免了保存 CheckPoint 带来的资源损耗。

业务场景聚合主要的挑战在于一次聚合涉及到的指标数太多，聚合逻辑复杂。例如某个应用的某个接口的请求成功率，涉及到的指标数目上千，这种聚合查询 Influxdb 无法支持的。

携程使用 ClickHouse 进行预聚合。ClickHouse 是俄罗斯开源的面向 OLAP 的分布式列式数据库，拥有极高的读写性能，并提供了强大的 SQL 语言和丰富的数据处理函数，可以完成很多指标的处理，例如 P95。

[携程新一代监控告警平台 Hickwall 架构演进](https://www.infoq.cn/article/P3A5EuKl6jowO9v4_ty1)