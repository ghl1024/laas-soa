时间转换公式: 1秒=1k毫秒=1k*1k微妙

目标Redis集群信息:

```
192.168.2.240:7001,192.168.3.100:7001,192.168.4.195:7001
```

# 整体信息

```
info
```

显示结果如下:

```
"# Server
redis_version:4.0.8
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:45e95bda1da5edf3
redis_mode:standalone
os:Linux 3.10.0-957.12.1.el7.x86_64 x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:atomic-builtin
gcc_version:4.8.5
process_id:3668
run_id:7143499c8f2a0e57bd903a3db94d108dc4dc288a
tcp_port:7000
uptime_in_seconds:12270432
uptime_in_days:142
hz:10
lru_clock:12955227
executable:/data/redis/redis-4.0.8/src/redis-server
config_file:/data/redis/redis-sentinel/redis-7000/redis.conf

# Clients
connected_clients:863
client_longest_output_list:0
client_biggest_input_buf:0
blocked_clients:0

# Memory
used_memory:99171500
used_memory_human:94.58M
used_memory_rss:352563200
used_memory_rss_human:336.23M
used_memory_peak:304200532
used_memory_peak_human:290.11M
used_memory_peak_perc:32.60%
used_memory_overhead:30708138
used_memory_startup:835442
used_memory_dataset:68463362
used_memory_dataset_perc:69.62%
total_system_memory:8201089024
total_system_memory_human:7.64G
used_memory_lua:51200
used_memory_lua_human:50.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
mem_fragmentation_ratio:3.56
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0

# Persistence
loading:0
rdb_changes_since_last_save:3695
rdb_bgsave_in_progress:0
rdb_last_save_time:1606790679
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:1
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:49430528
aof_enabled:1
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:15548416
aof_current_size:81284213
aof_base_size:66989731
aof_pending_rewrite:0
aof_buffer_length:0
aof_rewrite_buffer_length:0
aof_pending_bio_fsync:0
aof_delayed_fsync:0

# Stats
total_connections_received:4266460
total_commands_processed:898465963
instantaneous_ops_per_sec:144
total_net_input_bytes:150342838530
total_net_output_bytes:436058713497
instantaneous_input_kbps:50.92
instantaneous_output_kbps:222.07
rejected_connections:0
sync_full:1
sync_partial_ok:1
sync_partial_err:1
expired_keys:90242760
evicted_keys:0
keyspace_hits:246952778
keyspace_misses:95203618
pubsub_channels:1
pubsub_patterns:1
latest_fork_usec:8493
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0

# Replication
role:master
connected_slaves:2
slave0:ip=192.168.2.240,port=7000,state=online,offset=145178809693,lag=1
slave1:ip=192.168.4.195,port=7000,state=online,offset=145178808485,lag=1
master_replid:a26de1a344e3e95707e20b941d5b3af526bb3a62
master_replid2:5bedcfd31bf217a67f9d0e272eb19c086e6bc1cb
master_repl_offset:145178907778
second_repl_offset:20245116330
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:145177859203
repl_backlog_histlen:1048576

# CPU
used_cpu_sys:28768.67
used_cpu_user:40557.79
used_cpu_sys_children:5842.90
used_cpu_user_children:35723.61

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=136236,expires=135427,avg_ttl=6323046619
db2:keys=49,expires=49,avg_ttl=192911
"
```

因此可以发现:



# 主从信息

```
info Replication
```

显示:

```
"# Replication
role:master
connected_slaves:2
slave0:ip=192.168.2.240,port=7000,state=online,offset=145243870207,lag=0
slave1:ip=192.168.4.195,port=7000,state=online,offset=145243870207,lag=0
master_replid:a26de1a344e3e95707e20b941d5b3af526bb3a62
master_replid2:5bedcfd31bf217a67f9d0e272eb19c086e6bc1cb
master_repl_offset:145243870244
second_repl_offset:20245116330
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:145242821669
repl_backlog_histlen:1048576
"
```

Redis集群架构为1主2从

| 主/从 | 连接信息           |
| ----- | ------------------ |
| 主    | 192.168.3.100:7001 |
| 从    | 192.168.4.195:7001 |
| 从    | 192.168.2.240:7001 |

整个集群目前就一个master在服务, master的性能代表了集群的性能, slaver的可用率代表了集群的可用率

重点看主节点

# 客户端连接

```
info Clients
```

显示:

```
"# Clients
connected_clients:863
client_longest_output_list:0
client_biggest_input_buf:0
blocked_clients:1
"
```

Redis最大连接数1w

在服务不多的情况下, 连接数过多, 高达863

客户端连接数有点异常, 数量过多, 排查一下是否有异常客户端连接

使用 client list 查看客户端连接信息

​	发现有69次空连接

​	

查看redis配置文件发现timeout参数值为0, 这意味着永不清理历史连接, 设置为3600(1小时), 重启redis

```
config get timeout
config set timeout 3600
config rewrite
```



当blocked_clients阻塞连接过多时说明redis处理慢或者达到主节点最大承受量, 目前没有问题

# 内存(重点)

```
info Memory
```

显示:

```
"# Memory
used_memory:98888272
used_memory_human:94.31M
used_memory_rss:352563200
used_memory_rss_human:336.23M
used_memory_peak:304200532
used_memory_peak_human:290.11M
used_memory_peak_perc:32.51%
used_memory_overhead:30256578
used_memory_startup:835442
used_memory_dataset:68631694
used_memory_dataset_perc:69.99%
total_system_memory:8201089024
total_system_memory_human:7.64G
used_memory_lua:44032
used_memory_lua_human:43.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
mem_fragmentation_ratio:3.57
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0
"
```



used_memory_human*mem_fragmentation_ratio=used_memory_rss_human



最大内存没有设置

设置最大内存(75%系统内存)

```
config set maxmemory 6150816768
config rewrite
```

目前, 碎片率过大(大于1.5), 系统内存资源浪费度高, 而如果碎片率过低, 说明内存不足, 性能急剧降低



设置自动清理碎片

```
当碎片率达到一定比率的时候

# 开启自动清理碎片
config set activedefrag yes

# 当碎片率达到百分之150时开始清理, 即 mem_fragmentation_ratio:1.5
active-defrag-threshold-lower 50

# 仍然可以手动清理, 不建议
memory purge

# 将配置写入配置文件, 重启后依然生效
config rewrite
```

发现当内存使用率低的时候碎片清理不下来



设置最大内存

MAXMEMORY

# 问题



redis资源使用率过低, 可能是业务系统基本上没有用缓存, 督促服务使用缓存以及加深缓存的使用

