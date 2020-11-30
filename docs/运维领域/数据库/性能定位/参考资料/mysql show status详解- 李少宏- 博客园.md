# [mysql show status详解](https://www.cnblogs.com/descusr/p/3140523.html)

查看服务器目前状态信息的命令，两种方式：

\1.   命令行，进入mysql/bin目录下，输入mysqladmin extended-status

\2.   连接到[**mysql**](http://www.cnblogs.com/descusr/admin/)，输入show status;

\3.   如果要查看某个数据，可以

mysql> show status like 'table%';

+-----------------------+-------+

| Variable_name    | Value |

+-----------------------+-------+

| Table_locks_immediate | 12  |

| Table_locks_waited  | 0  |

+-----------------------+-------+

 

需要关注的部分有：

qcache% ,open%tables,threads%,%key_read%,created_tmp%,sort%,com_select

这几个变量的调优参考“mysql服务器调优”http://www.ibm.com/developerworks/cn/linux/l-tune-lamp-3.html

状态变量详解，可能还有部分新的变量没列出来，

全部状态解释参看mysql手册http://dev.mysql.com/doc/refman/5.0/en/server-status-variables.html（红色部分是调优的时候重点关注的变量）

 

| Aborted_clients                   | 指出由于某种原因客户程序不能正常关闭连接而导致失败的连接的数量。如果客户不在退出之前调整mysql_close()函数，wait_timeout或interactive_timeout的限制已经被超出，或者是客户端程序在传输的过程中被关闭，则这种情况会发生。 |
| --------------------------------- | ------------------------------------------------------------ |
| Aborted_connects                  | 指出试图连接到MYSQL的失败的次数。这种情况在客户尝试用错误的密码进行连接时，没有权限进行连接时，为获得连接的数据包所花费的时间超过了connect_timeout限制的秒数，或数据包中没有包含正确的信息时，都会发生。 |
| Bytes_received                    | 从客户处已经接收到的字节数。                                 |
| Bytes_sent                        | 已经发送给所有客户的字节数。                                 |
| Com_[statement]                   | 用于每一种语句的这些变量中的一种。变量值表示这条语句被执行的次数，如com_select,表示查询语句被执行的次数。 |
| Connections                       | 试图连接到MYSQL服务器的次数。                                |
| Created_tmp_disk_tables           | 执行语句时，磁盘上生成的隐含临时表的数量                     |
| Created_tmp_tables                | 执行语句时，内存中生成的隐含临时表的数量                     |
| Created_tmp_files                 | 由mysqld生成的临时文件的数量                                 |
| Delayed_insert_threads            | 当前正在使用的延迟插入句柄的线程数量                         |
| Delayed_writes                    | 由INSERT DELAYED语句写入的记录的个数                         |
| Delayed_errors                    | 当发生错误时，由INSERT DELAYED语句写入的记录的。绝大多数普通的错误是复制键 |
| Flush_commands                    | 被执行的FLUSH语句的个数                                      |
| Handler_commit                    | 内部COMMIT命令的个数                                         |
| Handler_delete                    | 从一个表中删除行的次数                                       |
| Handler_read_first                | 一条索引中的第一个条目被读取的次数，通常是指完全索引扫描（例如，假定indexed_col被索引，语句SELECT indexed_col from tablename导致了一个完全索引扫描） |
| Handler_read_key                  | 当读取一行数据时，使用索引的请求的个数。如果查询时使用了索引，就希望这个值快速增加 |
| Handler_read_next                 | 按照索引顺序读取下一行数据的请求的个数。如果使用了完全索引进行扫描，或者在一个不变的范围内查询一个索引，则这个值就会增加 |
| Handler_read_prev                 | 按照索引的顺序读取前面一行数据的请求的个数。这个变量值由SELECT fieldlist ORDER BY fields DESC类型的语句使用 |
| Handler_read_rnd                  | 在固定的位置读取一行数据的请求的个数。要求结果被保存起来的查询操作将增加这个计数器的值 |
| Handler_read_rnd_next             | 读取数据文件中下一行数据的请求的个数。一般，这个值不能太高，因为这意味着查询操作不会使用索引，并且必须从数据文件中读取 |
| Handler_rollback                  | 内部ROLLBACK命令的数量                                       |
| Handler_update                    | 在表中更新一条记录的请求的数量                               |
| Handler_write                     | 在表中插入一条记录的请求的数量                               |
| Key_blocks_used                   | 用在键的缓存中的数据块的数量                                 |
| Key_read_requests                 | 引起从键的缓存读取键的数据块的请求的数量。Key_reads与Key_read_requests的比率不应该高于1：100（也就是，1：10很糟糕） |
| Key_reads                         | 引起从磁盘读取键的数据块的物理读取操作的数量。               |
| Key_write_requests                | 引起键的数据块被写入缓存的请求的数量                         |
| Key_writes                        | 向磁盘写入键的数据块的物理写操作的次数                       |
| Max_used_connections              | 在任意时刻，正在使用的连接的最大数量                         |
| Not_flushed_key_blocks            | 在键的缓存中，已经发生了改变但还没有被刷新到磁盘上的键的数据块的数量 |
| Not_flushed_delayed_rows          | 当前在INSERT DELAY队列中，等待被写入的记录的个数             |
| Open_tables                       | 目前打开的表的数量                                           |
| Open_files                        | 当前打开的文件的数量                                         |
| Open_streams                      | 当前打开的流数据的数量。这些流数据主要用于[**日志**](http://www.cnblogs.com/descusr/admin/)记录 |
| Opened_tables                     | 已经被打开的表的数量                                         |
| Questions                         | 初始的查询操作的总数                                         |
| Qcache_queries_in_cache           | 缓存中查询的个数                                             |
| Qcache_inserts                    | 添加到缓存中的查询的个数命中次数除以插入次数就是不中比率；用1减去这个值就是命中率 |
| Qcache_hits                       | 查询缓存被访问的个数                                         |
| Qcache_lowmem_prunes              | 缓存出现内存不足并且必须要进行清理以便为更多查询提供空间的次数。这个数字最好长时间来看；如果这个数字在不断增长，就表示可能碎片非常严重，或者内存很少。（上面的`free_blocks`和`free_memory`可以告诉您属于哪种情况）。 |
| Qcache_not_cached                 | 没有被缓存（由于太大，或因为QUERY_CACHE_TYPE）的查询的数量   |
| Qcache_free_memory                | 仍然可用于查询缓存的内存的数量                               |
| Qcache_free_blocks                | 在查询缓存中空闲内存块的数量，数量大说明可能有碎片           |
| Qcache_total_blocks               | 在查询缓存中数据块的总数                                     |
| Rpl_status                        | 完全复制的状态（这个变量只在MYSQL 4之后的版本中使用）        |
| Select_full_join                  | 已经被执行的没有使用索引的联接的数量。不能将这个变量值设的太高 |
| Handler_rollback                  | 内部ROLLBACK语句的数量                                       |
| Handler_update                    | 在表内更新一行的请求数                                       |
| Handler_write                     | 在表内插入一行的请求数                                       |
| Innodb_buffer_pool_pages_data     | 包含数据的页数(脏或干净)                                     |
| Innodb_buffer_pool_pages_dirty    | 当前的脏页数                                                 |
| Innodb_buffer_pool_pages_flushed  | 要求清空的缓冲池页数                                         |
| Innodb_buffer_pool_pages_free     | 空页数                                                       |
| Innodb_buffer_pool_pages_latched  | 在InnoDB缓冲池中锁定的页数。这是当前正读或写或由于其它原因不能清空或删除的页数 |
| Innodb_buffer_pool_pages_misc     | 忙的页数，因为它们已经被分配优先用作管理，例如行锁定或适用的哈希索引。该值还可以计算为Innodb_buffer_pool_pages_totalInnodb_buffer_pool_pages_freeInnodb_buffer_pool_pages_data |
| Innodb_buffer_pool_pages_total    | 缓冲池总大小（页数）                                         |
| Innodb_buffer_pool_read_ahead_rnd | InnoDB初始化的“随机”read-aheads数。当查询以随机顺序扫描表的一大部分时发生 |
| Innodb_buffer_pool_read_ahead_seq | InnoDB初始化的顺序read-aheads数。当InnoDB执行顺序全表扫描时发生 |
| Innodb_buffer_pool_read_requests  | InnoDB已经完成的逻辑读请求数                                 |
| Innodb_buffer_pool_reads          | 不能满足InnoDB必须单页读取的缓冲池中的逻辑读数量             |
| Innodb_buffer_pool_wait_free      | 一般情况，通过后台向InnoDB缓冲池写。但是，如果需要读或创建页，并且没有干净的页可用，则它还需要先等待页面清空。该计数器对等待实例进行记数。如果已经适>当设置缓冲池大小，该值应小 |
| Innodb_buffer_pool_write_requests | 向InnoDB缓冲池的写数量                                       |
| Innodb_data_fsyncs                | fsync()操作数                                                |
| Innodb_data_pending_fsyncs        | 当前挂起的fsync()操作数                                      |
| Innodb_data_pending_reads         | 当前挂起的读数                                               |
| Innodb_data_pending_writes        | 当前挂起的写数                                               |
| Innodb_data_read                  | 至此已经读取的数据数量（字节）                               |
| Innodb_data_reads                 | 数据读总数量                                                 |
| Innodb_data_writes                | 数据写总数量                                                 |
| Innodb_data_written               | 至此已经写入的数据量（字节）                                 |
| Innodb_dblwr_writes,              | Innodb_dblwr_pages_written已经执行的双写操作数量和为此目的已经写好的页数。 |
| Innodb_log_waits                  | 我们必须等待的时间，因为日志缓冲区太小，我们在继续前必须先等待对它清空 |
| Innodb_buffer_pool_bytes_data     | 当前bufferpool缓存的数据大小，包括脏数据                     |
| Key_blocks_unused                 | 未使用的缓存簇(blocks)数                                     |
| Key_blocks_used                   | 曾经用到的最大的blocks数                                     |
| Key_blocks_unused                 | 太小要么增加key_buffer_size，要么就是过渡索引了，把缓存占满了。 |