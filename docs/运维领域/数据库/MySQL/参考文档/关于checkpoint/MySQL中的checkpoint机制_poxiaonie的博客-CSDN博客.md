检查点(checkpoint)：

一种让数据库redo和data文件保持一致的机制

作用：

将BP中的脏页刷盘
通过频度适当的刷盘，减少实例恢复时间
重做日志不够用时，将脏页刷盘

实现

通过LSN实现
实例恢复时，假如checkpointLSN=1000,而redoLSN=1200，则LSN=[1001,1200]均需要重做

LSN：

Log Sequence Number:日志序列号，一个不断增大的数字,表示redo log的增量（字节数）。
用途：类似oracle的SCN，用来标识数据库变更版本，保证磁盘上的redo和data文件处于一致状态。实例恢复时，比较page的LSN和redo里记录的该page的LSN是否一致。若小于，则需要将redo重做到page里。
存在于：redo log中每个page的头部

查看当前innodb的LSN：

```
show engine innodb status\G;
```

![这里写图片描述](MySQL中的checkpoint机制_poxiaonie的博客-CSDN博客.assets/20170603001929239)
Log sequence number: log buffer中已经写入的LSN值
Log flushed up to: 已经刷新到redo logfile的LSN值
Last checkpoint at:最近一次checkpoint时的LSN值

checkpoint种类：

全量检查点：
发出checkpoint时，全部脏页刷盘。
I/O负载极高，不适合流量高峰。
增量检查点：
发出checkpoint时，将包含最老LSN脏页刷盘。

在以下条件，增量检查点进行刷盘：

1. master thread 每10秒一次
2. redo log不够用时，从flush list上刷新一定脏页.checkpoint_age=redo_lsn – checkpoint_lsn
3. freelist不够用时，从LRU list上刷新一定脏页
4. 达到innodb_max_dirty_pages_pct

checkpoint干的事情：
将缓冲池中的脏页刷新回磁盘，不同之处在于每次从哪里取多少脏页刷新到磁盘，以及什么时候触发checkpoint。

checkpoint解决的问题：

1. 缩短数据库的恢复时间
2. 缓冲池不够用时，将脏页刷新到磁盘(缓冲池不够用时，根据LRU算会溢出最近最少使用的页，若此页为脏页，需要强制执行checkpoint将脏页刷回磁盘)
3. 重做日志不可用时，刷新脏页(采用循环使用的，并不是无限增大。当重用时，此时的重做日志还需要使用，就必须强制执行checkpoint将脏页刷回磁盘)

checkpoint分类：

1.Sharp Checkpoint
发生在数据库关闭时将所有的脏页刷回磁盘，这是默认的。通过参数innodb_fast_shutdown=1来设置。

2.Fuzzy Checkpoint
在InnoDB存储引擎内部使用Fuzzy Checkpoint进行页的刷新，即只刷新一部分脏页，而不是全部刷新。大致分为以下几种情况：

a.Master Thread Checkpoint
差不多以每秒或者每十秒从缓冲池的脏页列表(Flush列表)，这是异步操作，InnoDB存储引擎可以进行其他的操作部分不会发生堵塞。

b.FLUSH_LUR_LIST Checkpoint
InnoDB存储引擎需要保证LRU列表中有差不多100个空闲页可供使用。在InnoDB1.1.X版本之前，需要检查LRU列表中是否有足够的可用空间操作发生在用户查询线程中，显然这会阻塞用户的查询操作。倘若没有100个空闲页，那么InnoDB存储引擎会将LRU列表尾端的页移除，如果这些页中有脏页，那么需要进行Checkpoint，而这些来自于LRU列表的被称为FLUSH_LRU_LIST Checkpoint。但是在MySQL5.6版本后这个检查被放在了一个单独的Page Cleaner Thread中进行，通过参数innodb_lru_scan_depth来设置可用页的数量。

c.Async/Sync Flush Checkpoint
在重做日志文件不可用的情况下，需要将一些也刷新回磁盘，而操作发生在Flush列表上。若将已经写入到重做日志的LSN记为redo_lsn，将已经刷新回磁盘最新的LSN记为checkpoint_lsn,则可以定义:checkpoint_age = redo_lsn-checkpoint_lsn在定义一下的变量async_water_mark=75%*total_redo_log_file_size、sync_water_mark=90%*total_redo_file_size。若每个重做日志的大小为1G且定义了两个重做日志共2G。那么async_water_mark=1.5G,sync_water_mark=1.8G。

当checkpoint_age < async_water_mark时，不需要刷新任何脏数据到磁盘；

当async_water_mark < checkpoint_age < sync_water_mark时，触发Async Flush从Flush列表刷新足够的脏页会磁盘，使得刷新后满足checkpoint_age < async_water_mark；

当checkpoint_age > sync_water_mark时，这种情况很少发生除非设置的重做日志文件太小，并且进行类似于LOAD DATA的BULK INSRET操作。这个时候触发Sync Flush从Flush列表刷新足够的脏页会磁盘，使得刷新后满足checkpoint_age < async_water_mark；

Async Flush Checkpoint会阻塞发现问题的用户查询线程，Sync Flush Checkpoint会阻塞所有的用户查询线程，并且等待脏页刷新完成。但是从MySQL5.6版本开始这部分操作放入单独的Page Cleaner Thread中，不再会堵塞用户查询线程。

d.Dirty Page too much Checkpoint

脏页的数量太多导致InnoDB存储引擎强制进行Checkpoint，其目的是为了保证缓冲池中有足够的页可以用。可以通过参数innodb_max_dirty_pages_pct来设置。