# mysql服务器参数优化

发表于 2016-11-07 13:17:17  |  分类于 [左手代码 ](https://www.shixinke.com/category-technology.html)[MySQL数据库 ](https://www.shixinke.com/category-mysql.html) |  阅读(1587)  |  评论(0)

#### 一、调整MySQL配置参数的说明

- 调整MySQL服务器参数，性能并不能得到数量级的提升
- 要慎重调整MySQL服务器参数，在有经验的DBA的指导下调整，否则，不合理的调整，可能会造成MySQL的安全性问题，甚至造成MySQL服务的异常
- 有些参数，需要重启MySQL才能起作用，因此要慎重对待。另外要确定MySQL配置文件的正确位置
- 对调整后的参数要进行观察和监控，分析其是否真正起到了优化的作用

#### 二、配置文件及配置项说明

##### 1、确定配置文件位置

```
/usr/local/mysql/bin/mysqld --verbose --help | grep -A 1 'Default options'
```

结果如下：

![img](mysql服务器参数优化 诗心博客.assets/b2d8f994b7751f23f40f6728cba58d42.jpg)

这是查找配置文件的优先级说明

##### 2、配置项说明

对于MySQL配置项，有的配置项是对于一个线程而言的(即为每个线程分配的资源,包括`sort_buffer_size,join_buffer_size,read_buffer_size,read_rnd_buffer_size`是为每个连接线程分配的内存大小)，因此要充分估计MySQL的负载。

#### 三、MySQL配置参数调优

##### 1、内存配置相关参数

内存配置调优的原则：

- 确定MySQL能使用的内存的绝对上限(比如是物理内存的多少)
- 确定MySQL会为每个连接使用多少内存，比如排序缓冲区和临时表(要充分估计最大连接数，如`sort_buffer_size,join_buffer_size,read_buffer_size,read_rnd_buffer_size`)
- 确定操作系统需要多少内存来很好的运行自身，包括机器上其他程序
- 假设以上工作都完成，就可以把剩下的内存分配给MySQL的缓存，如InnoDB的缓存池

###### (1)缓存池配置

- innodb_buffer_pool_size：InnoDB单个缓存池大小

  - 作用：用于缓存索引和数据，所以设置过大或过小都不好，设置过大，不仅造成资源的浪费，还会导致system的swap空间被占用，导致操作系统变慢，从而减低sql查询的效率，设置过小，会影响MySQL的性能。最大最好不要超过MySQL数据量和索引量的总的大小(要考虑后续数据的增长)。
  - 推荐值：MySQL官方推荐其值为MySQL所在服务器物理内存的50%-80%，但我们应该根据具体情况来设定
  - 计算公式：innodb缓存池总大小 <= 物理内存 - 连接数 * 每个连接分配的内存 - 系统程序内存

  `-`物理内存即服务器的总内存大小

  `-` 系统程序内存，包括运行操作系统正常运行的内存，以及系统上其他程序正常运行需要的内存

  `-` 每个连接分配的内存，如排序缓存池`sort_buffer_size、连接缓存池join_buffer_size,读入缓存池read_buffer_size,随机读入缓存池read_rnd_buffer_size`

- innodb_buffer_pool_instances:InnoDB缓存池的数量

- key_buffer_size:MyISAM存储引擎索引缓存池大小

  - 作用：用于缓存MyISAM索引，数据是根据操作系统来决定是否存储(根据索引量来决定，通过计算索引的大小来决定其大小)
  - 推荐值：和MyISAM的索引量大小匹配即可
  - 获取方式：查看MyISAM表的所有索引的数量

```
select sum(index_length) from information_schema.tables where engine="myisam";
```

- sort_buffer_size：排序缓存池大小
  - 作用：是MySql执行排序使用的缓冲大小
  - 推荐值：根据服务器的最大连接数(非专业DBA请采用默认值)、以及排序的场景和服务器配置来决定(针对单个连接)
- join_buffer_size：表连接缓存池大小

- 作用：当我们的join是ALL,index,rang或者Index_merge的时候使用的缓冲区(针对单个连接)

- read_buffer_size：读入缓存池大小
  - 作用：是MySql读入缓冲区大小。对表进行顺序扫描的请求将分配一个读入缓冲区，MySql会为它分配一段内存缓冲区
- read_rnd_buffer_size：随机读入缓存池大小
  作用：是MySql的随机读缓冲区大小。当按任意顺序读取行时(例如，按照排序顺序)，将分配一个随机读缓存区。

###### (2)线程缓存

- thread_cache_size:缓存的线程数量
  - 作用：保存与当前线程无关的线程，以供新连接使用
  - 推荐值：观察threads_created这个变量，如果其值小于10，则不用改变当前的配置；然后再观察threads_connected这个变量，如果其值在100-200之间，可以将缓存的线程数量设置为100，如果它在500-700之间，设置为200即可

###### (3)表缓存

- table_open_cache:打开表的缓存数
  - 作用：为打开的表设置缓存，如果之后打开同名的表，可以从缓存中直接取出，不用直接再打开
  - 推荐值：不断观察open_tables这个状态值来决定其大小。
- table_definition_cache：表定义缓存数
  - 作用：为表的结构定义建立缓存,存放的表的结构定义信息
  - 推荐值：根据表的数据来决定(最大为表的数量，当然最好是常用的表)

##### 2、IO配置相关参数

MySQL为了较高的性能，并不是每次操作都写入磁盘，也是写入事务日志，再根据相关的配置项，定时从事务日志中获取内容再写入到磁盘。

- innodb_log_file_size:单个事务日志的大小
- innodb_flush_log_at_trx_commit:从事务日志中把数据刷新到磁盘的规则
  - 选项值：
    `-` 0表示每秒进行一次log写入cache,并flush log到磁盘
    `-` 1表示每次事务提交执行log写入到cache,并flush log到磁盘
    `-` 2每秒事务提交，执行log数据写入到cache,每秒执行一次flush log到磁盘
  - 推荐值：2
- innodb_flush_method:设置InnoDB同步IO的方式

- 推荐值：O_DIRECT

- innodb_file_per_table:将每个数据库的表的数据存储为一个单独的文件

- 推荐值：1

- innodb_doublewrite ：是否启用双写缓存
  - 推荐值：1
- open_files_limit：最大打开文件数
  - 推荐值：观察open_files来决定其值是否修改
- innodb_read_io_threads:读IO线程数
  - 推荐值：可以与服务器CPU核数匹配
- innodb_write_io_threads:写IO线程数
  - 推荐值：可以与服务器CPU核数匹配
- sync_binlog:是否同步二进制日志(在启用主从复制的服务器上)
  - 推荐值：在主从复制的服务器的主服务器建议开启
- tmp_table_size:内部临时表的大小(为每个线程分配的大小)
  - 作用：在查询时使用到内存临时表时，受该参数影响
  - 推荐值：根据观察created_tmp_tables和created_tmp_disk_tables的大小来决定，如果created_tmp_disk_tables/created_tmp_tables的比例小于0.25时，则已经很好了，不需要修改，如果超过这个比例，则可以修改。这个最大值不能超过max_heap_table_size
- max_heap_table_size：内存表大小(为每个线程分配的大小)

##### 3、安全配置相关参数

- expire_logs_day:二进制日志保存的天数
- read_only:是否只读
  - 推荐值：在从服务器上建议开启该选项
- sql_mode:SQL模式
  - 作用：限制SQL的执行模式
  - 推荐值：生产环境建议为严格模式(STRICT_TRANS_TABLES)

##### 4、其他参数

- max-allowed-packet:设置网络传输中一次消息传输量的最大值，取值范围为1MB~1GB,必须设置为1024的倍数
- max-connect-errors:每个主机在连接请求异常中断的最大次数，当超过该次数，则禁止host的连接请求，直到服务器重启或flush hosts命令清空该host的相关信息
- skip-name-resolve:启动mysql禁用DNS主机名查找

#### 四、修改MySQL配置参数的方法：

##### 1、在命令行下使用set global 参数名 = 参数值，这种在mysql重启后失效。

如：

```
set global innodb_buffer_pool_size = 10240000
```

##### 2、修改mysql配置文件my.cnf，然后重启MySQL服务

将配置项写入到配置文件中。(注意配置文件的正确位置)

#### 五、第三方Mysql配置工具

地址：[https://tools.percona.com](https://tools.percona.com/)

根据提示生成适合自己的一份配置，如：根据本人自身需要生成的配置：

```
[mysql]# CLIENT ## mysql服务器端口号port                           = 3306# mysql socket连接文件(根据自己的需要设置，且/data/mysql要有可写权限)socket = /data/mysql/mysql.sock[mysqld]# GENERAL ## 服务器标识id(用于主从复制)server-id  = 1# 操作mysql的系统用户名user   = mysql# 默认存储引擎default-storage-engine = InnoDB# mysql socket连接文件socket = /data/mysql/mysql.sock# 记录mysql进程的文件pid-file   = /data/mysql/mysql.pid# MyISAM ## 索引缓冲区大小key-buffer-size= 32M# 自动检查和修复没有适当关闭的MyISAM表myisam-recover = FORCE,BACKUP# MyISAM表发生变化时重新排序所需要的缓冲区大小myisam-sort-buffer-size=  128M# 重建索引时所允许的最大临时文件大小 myisam-max-sort-file-size  =  10G# SAFETY ## 设置网络传输中一次消息传输量的最大值，取值范围为1MB~1GB,必须设置为1024的倍数max-allowed-packet = 32M# 每个主机在连接请求异常中断的最大次数，当超过该次数，则禁止host的连接请求，直到服务器重启或flush hosts命令清空该host的相关信息max-connect-errors = 6000# 启动mysql禁用DNS主机名查找skip-name-resolve# SQL模式(在生产环境要设置为严格模式，可以防止非法数据的插入)sql-mode   = STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_AUTO_VALUE_ON_ZERO,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY# 系统时间和当前时间一致sysdate-is-now = 1# DATA STORAGE ## 数据文件位置datadir= /data/mysql/# BINARY LOGGING ## 二进制操作日志文件log-bin= /data/mysql/mysql-bin# 日志有效时间expire-logs-days   = 14# 二进制日志是否同步写入磁盘(1表示每次每写入，是最安全的，但也是最慢的)sync-binlog= 1# CACHES AND LIMITS ## 内存临时表大小(超过其大小会写入磁盘)tmp-table-size = 32M# 可创建的内存表大小max-heap-table-size= 32M# 是否将查询结果放到查询缓存中query-cache-type   = 0# 查询缓存大小(在写入量大的系统，建议关闭)query-cache-size   = 0# 单个查询能够使用的缓冲区大小query-cache-limit  = 4M# mysql最大进程连接数max-connections= 500# 服务器线程缓存大小，类似于缓存池，1G内存建议为8，2G内存建议为16，4G以上可以配置更大thread-cache-size  = 300# 线程并发数，一般设置为核数的2倍，如8核的CPU可以设置为16thread-concurrency = 16# 打开文件描述符的限制(至少在大于 table-open-cache*2+InnoDB表的数量)open-files-limit   = 65535# 表缓存区大小，应该与max_connections设置相关table-cache= 614# 表定义信息缓存(从.frm文件中获取的)table-definition-cache = 1024# 打开表(文件描述符)的缓存数量table-open-cache   = 1024# 读入缓冲区大小read-buffer-size   = 1M# 随机读缓冲区大小read-rnd-buffer-size   = 16M# 批量插入缓冲区大小bulk-insert-buffer-size= 64M# 用于排序的缓冲区大小sort-buffer-size   = 2M# 表间关联的缓冲区大小join-buffer-size   = 2M# INNODB ##innodb刷新日志和数据的模式，有innodb-flush-method= O_DIRECT# 为提高性能，可以以循环方式将日志文件写入到多个文件innodb-log-files-in-group  = 2# 日志缓存区大小innodb-log-buffer-size =  16M# innodb日志文件大小innodb-log-file-size   = 256M# 提交事务后将日志写入磁盘的频率innodb-flush-log-at-trx-commit = 1# 每个innodb表使用一个数据文件innodb-file-per-table  = 1# innodb缓存池大小innodb-buffer-pool-size= 12G# innodb文件IO线程数innodb-file-io-threads =  4# innodb并发线程数(与CPU核数相关)innodb-thread-concurrency  =  8# 在MySQL暂时停止响应新请求前，短时间内的多少个请求可以被存在堆栈中back_log = 600# 设置事务的隔离级别，可以使用READ-UNCOMMITED 读未提交，READ-COMMITED 读已提交；REPEATABLE-READ 可重复读；SERIALIZABLE 串行transaction_isolcation = READ-COMMITED# 表名都小写lower_case_table_names =  1# 避免MySQL外部锁定external-locking = FALSE # LOGGING ## 错误日志文件log-error  = /data/mysql/mysql-error.log# 是否记录未使用索引的查询log-queries-not-using-indexes  = 1# 是否开启慢查询日志slow-query-log = 1# 慢查询日志文件位置slow-query-log-file= /data/mysql/mysql-slow.log
```

注：以上配置并不是最优的配置，只是做一个简要的说明，请根据项目需要自行调整