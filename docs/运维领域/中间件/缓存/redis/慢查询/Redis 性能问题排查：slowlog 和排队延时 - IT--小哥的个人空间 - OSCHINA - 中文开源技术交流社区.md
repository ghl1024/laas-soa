# 一、Redis Slowlog介绍

[**[Redis Slowlog\]**](http://redis.io/commands/slowlog)是排查性能问题关键监控指标。它是记录Redis queries运行时间超时特定阀值的系统。
这类慢查询命令被保存到Redis服务器的一个定长队列，最多保存slowlog-max-len(默认128）个慢查询命令。
当慢查询命令达到128个时，新产生的慢查询被加入前，会从队列中删除最旧的慢查询命令。



## 1.1 Redis Slowlog的配置

redis slowlog通过2个参数配置管理，默认命令耗时超过10毫秒，就会被记录到慢查询日志队列中；队列默认保存最近产生的128个慢查询命令。
**slowlog-log-slower-than:** 慢查询阀值,单位微秒. 默认100000(10毫秒);
生产环境设置1ms,因为Redis是single thread,如果命令都是1ms以上,则实例的吞吐量只有1000QPS.
**slowlog-max-len:** 慢查询存储的最大个数,默认128;
生产设置设置大于1024,因为slowlog会省略过多的参数，慢查询不会占用过多的内存；
慢查询队列满后,淘汰最老的慢查询实体。



## 1.2 Redis Slowlog读取

redis-cli客户端通过slowlog get指令获取最新10条慢查询命令。
当然各语言的client也实现对应的接口。

```
示例：获取最近2个慢查询命令 
127.0.0.1:6381> SLOWLOG get 2
1) 1) (integer) 6
   2) (integer) 1458734263
   3) (integer) 74372
   4) 1) "hgetall"
      2) "max.dsp.blacklist"
2) 1) (integer) 5
   2) (integer) 1458734258
   3) (integer) 5411075
   4) 1) "keys"
      2) "max.dsp.blacklist"
分析slowlog query：
  以第一个HGET命令为例分析，每个slowlog实体共4个字段：
  * 字段1：1个整数,表示这个slowlog出现的序号,server启动后递增, 当前为6.
  * 字段2：表示查询执行时的Unix时间戳.
  * 字段3：表示查询执行微妙数,当前是74372微妙,约74ms.
  * 字段4: 表示查询的命令和参数,如果参数很多或很大,只会显示部分并给数参数个数;
  当前命令是"hgetall"   "max.dsp.blacklist"
```



## 1.3 Redis Slowlog只计算命令的执行时间

如MySQL/MongoDB等常见数据库，慢查询的query_time都会包含命令所有耗时，包含锁等待这类时间； 而Redis的慢查询query_time只记录自己“被cpu服务的时间”，不包含排队等待、IO等待（如AOF SYNC）这类时间。
**理解这点非常重要**

```
参考：
    The Redis Slow Log is a system to log queries that exceeded a 
specified execution time. The execution time does not include I/O 
operations like talking with the client, sending the reply and so forth,
but just the time needed to actually execute the command (this is the only
stage of command execution where the thread is blocked and can not serve
other requests in the meantime).
```



# 二、Redis Slowlog测试

设定请求的响应时间(R),服务时间(S), 排队延时（Q).
**R = S + Q**

我们回到Redis的Slowlog问题上，上节已说slowlog只计算Redis命令被服务的时间，并不包含命令的排队延迟时间。
**2.1 现在做个测试：**
1、redis实例port=6379,分别打开两个session. session-1模拟一个执行耗时6秒的大命令debug sleep 6；隔几秒后session-2执行一个简单的set a b的命令。
2、2个sessions的命令执行完成后，查看redis slowlog记录的命令耗时（slowlog-log-slower-than设置0）

```
session1:
rendeMacBook-Pro:~ rentom$ redis-cli
127.0.0.1:6379> debug sleep 6
OK
(6.00s)

session2:
127.0.0.1:6379> set name tom
OK
(5.14s)
127.0.0.1:6379> slowlog get
1) 1) (integer) 15
   2) (integer) 1538980614
   3) (integer) 4
   4) 1) "set"
      2) "name"
      3) "tom"
   5) "127.0.0.1:53738"
   6) ""
2) 1) (integer) 14
   2) (integer) 1538980614
   3) (integer) 6001061
   4) 1) "debug"
      2) "sleep"
      3) "6"
   5) "127.0.0.1:53737"
   6) ""
```

**2.2 测试结论**
1、从redis响应时间监控(min列），可见set name tom命令耗时5.14s；
但从redis slowlog中查看set name tom命令耗时为4微秒，可见slowlog没有记录set命令排队延迟等待的时间。
2、因Redis是单线程模型，debug sleep阻塞了set命令，set命令的整体**响应时间(R)**是5.14S，而其**服务时间(S)**为4微秒，**排队延迟(Q)约**为5.14秒。



# 三、Redis Single-threads的问题

Redis Server是单线程的处理(bgsave或aof重写时会Fork子进程处理），同一时间只能处理一个命令，并且是同步完成的。
从上节的测试中可见，set命令服务时间只有4微秒，但被debug sleep 6命令阻塞后，响应时间变成5.14秒。
所以RD和DBA在设计keyspace和访问模式时，应尽量避免使用**耗时较大的命令**。
在理想状态下，Redis单实例能处理8~10w的QPS, 如果大量的redis命令大量耗时大于1ms, 其实QPS只能达到1000基于几百。
Redis出现耗时大的命令，导致其他所有请求被阻塞等待，redis处理能力急剧退化，易导致整个服务链雪崩