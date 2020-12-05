### 0.现象

es 集群报red ，有unassigned shared ,
用命令 curl localhost:9200/_cat/shards |grep UNASSIGNED 可以查看。
即使你马上加节点，还是没有改善。新节点并不会正常工作，可能跟集群red有关系。

### 1.根本原因

节点磁盘不足，导致某些分片无法分配，一般情况下都有集群会有水位设置，比如说可以设置50G或者到85%的时候就不往里写数据了，
但是之前一次出了故障导致必须放开这个限制，之后没加上。

可以用命令:

```
GET /_cluster/allocation/explain
```

查看详细原因。

### 2.解决方案

```
POST /_cluster/reroute?retry_failed=true
```

es的机制貌似是try了5次就停了，重启master或者node都无效，执行上面的命令可以再retry。