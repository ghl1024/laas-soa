[首页](http://www.uxys.com/) > [数据库](http://www.uxys.com/html/Database/) > [MySQL](http://www.uxys.com/html/MySQL/) > 正文

# MySQL日志管理详解

发布时间：2015-07-10 14:29:26 作者：本站编辑 来源：本站原创 浏览次数：

我有话说  

**摘要：**这篇MySQL栏目下的“MySQL日志管理详解”，介绍的技术点是“mysql日志、MySQL、日志管理、日志、详解、管理”，希望对大家开发技术学习和问题解决有帮助。

日志文件对于一个服务器来说是非常重要的，它记录着服务器的运行信息，许多操作都会写日到日志文件，通过日志文件可以监视服务器的运行状态及查看服务器的性能，还能对服务器进行排错与故障处理，MySQl中有六种不同类型的日志。

**一、日志种类**

―――�C> 1，错误日志：记录启动、运行或停止时出现的问题，一般也会记录警告信息。
―――�C> 2，一般查询日志：记录建立的客户端连接和执行的语句。
―――�C> 3，慢查询日志：记录所有执行时间超过long_query_time秒的所有查询或不使用索引的查询，可以帮我们定位服务器性能问题。
―――�C> 4，二进制日志：任何引起或可能引起数据库变化的操作，主要用于复制和即时点恢复。
―――�C> 5，中继日志：从主服务器的二进制日志文件中复制而来的事件，并保存为的日志文件。
―――�C> 6，事务日志：记录InnoDB等支持事务的存储引擎执行事务时产生的日志。

MySQL中对于日志文件的环境比变量非常多，可以使用以下命令来查看：

```
mysql> show global variables like '%log%';
+-----------------------------------------+-----------------------------------------+
| Variable_name              | Value                  |
+-----------------------------------------+-----------------------------------------+
| back_log                | 50                   |
| binlog_cache_size            | 32768                  |
| binlog_direct_non_transactional_updates | OFF                   |
| binlog_format              | MIXED                  |
| binlog_stmt_cache_size         | 32768                  |
| expire_logs_days            | 0                    |
| general_log               | OFF                   |
| general_log_file            | /mydata/data1/localhost.log       |
| innodb_flush_log_at_trx_commit     | 1                    |
| innodb_locks_unsafe_for_binlog     | OFF                   |
| innodb_log_buffer_size         | 8388608                 |
| innodb_log_file_size          | 5242880                 |
| innodb_log_files_in_group        | 2                    |
| innodb_log_group_home_dir        | ./                   |
| innodb_mirrored_log_groups       | 1                    |
| log                   | OFF                   |
| log_bin                 | ON                   |
| log_bin_trust_function_creators     | OFF                   |
| log_error                | /mydata/data1/localhost.localdomain.err |
| log_output               | FILE                  |
| log_queries_not_using_indexes      | OFF                   |
| log_slave_updates            | OFF                   |
| log_slow_queries            | OFF                   |
| log_warnings              | 1                    |
| max_binlog_cache_size          | 18446744073709547520          |
| max_binlog_size             | 1073741824               |
| max_binlog_stmt_cache_size       | 18446744073709547520          |
| max_relay_log_size           | 0                    |
| relay_log                |                     |
| relay_log_index             |                     |
| relay_log_info_file           | relay-log.info             |
| relay_log_purge             | ON                   |
| relay_log_recovery           | OFF                   |
| relay_log_space_limit          | 0                    |
| slow_query_log             | OFF                   |
| slow_query_log_file           | /mydata/data1/localhost-slow.log    |
| sql_log_bin               | ON                   |
| sql_log_off               | OFF                   |
| sync_binlog               | 0                    |
| sync_relay_log             | 0                    |
| sync_relay_log_info           | 0                    |
+-----------------------------------------+-----------------------------------------+
41 rows in set (0.00 sec)
```

**二、日志功能**

**1，错误日志**
错误日志主要记录如下几种日志：
―――�C> 服务器启动和关闭过程中的信息
―――�C> 服务器运行过程中的错误信息
―――�C> 事件调度器运行一个事件时产生的信息
―――�C> 在从服务器上启动从服务器进程时产生的信息
错误日志定义：
可以用�Clog-error [ = file_name ]选项来指定mysqld保存错误日志文件的位置。如果没有给定file_name值，mysqld使用错误日志名host_name.err 并在数据目录中写入日志文件。如果你执行FLUSH LOGS，错误日志用-old重新命名后缀并且mysqld创建一个新的空日志文件。(如果未给出�Clog-error选项，则不会重新命名）。
错误日志一般有以上两个变量可以定义：

错误日志文件：log_error
启用警告信息：log_warnings （默认启用）

```
mysql> show global variables like 'log_error';
+---------------+-----------------------------------------+
| Variable_name | Value                  |
+---------------+-----------------------------------------+
| log_error   | /mydata/data1/localhost.localdomain.err |
+---------------+-----------------------------------------+
1 row in set (0.00 sec)
mysql> show global variables like 'log_warnings';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_warnings | 1   |
+---------------+-------+
1 row in set (0.00 sec)
```

**2、一般查询日志**

启动开关：general_log={ON|OFF}
日志文件变量：general_log_file [ =/PATH/TO/file]
全局日志开关：log={ON|OFF}  该开关打开后，所有日志都会被启用
记录类型：log_output={TABLE|FILE|NONE}
log_output定义了日志的输出格式，可以是表，文件，若设置为NONE，则不启用日志，因此，要启用通用查询日志，需要至少配置general_log=ON，log_output={TABLE|FILE}。而general_log_file如果没有指定，默认名是host_name.log。由于一般查询使用量比较大，启用写入日志文件，服务器的I/O操作较多，会大大降低服务器的性能，所以默认为关闭的。

```
mysql> show global variables like 'general_log';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| general_log  | OFF  |
+---------------+-------+
1 row in set (0.00 sec)
mysql> show global variables like 'general_log_file';
+------------------+-----------------------------+
| Variable_name  | Value            |
+------------------+-----------------------------+
| general_log_file | /mydata/data1/localhost.log |
+------------------+-----------------------------+
1 row in set (0.01 sec)
```

可以使用以下命令开启general_log：

```
mysql> set global general_log=1;
Query OK, 0 rows affected (0.00 sec)
mysql> show global variables like 'general_log';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| general_log  | ON  |
+---------------+-------+
1 row in set (0.00 sec)
```

**3、慢查询日志**

查询超时时间：long_query_time 
启动慢查日志：log_slow_queries={YES|NO}
启动慢查日志 : slow_query_log          
日志记录文件：slow_query_log_file [= file_name ]
MySQL如果启用了slow_query_log=ON选项，就会记录执行时间超过long_query_time的查询（初使表锁定的时间不算作执行时间）。日志记录文件如果没有给出file_name值， 默认为主机名，后缀为-slow.log。如果给出了文件名，但不是绝对路径名，文件则写入数据目录。

```
mysql> show global variables like '%slow_query_log%';
+---------------------+----------------------------------+
| Variable_name    | Value              |
+---------------------+----------------------------------+
| slow_query_log   | OFF               |
| slow_query_log_file | /mydata/data1/localhost-slow.log |
+---------------------+----------------------------------+
2 rows in set (0.00 sec)
```


默认没有启用慢查询，为了服务器调优，建议开启。

```
mysql> show global variables like 'long_query_time';
+-----------------+-----------+
| Variable_name  | Value   |
+-----------------+-----------+
| long_query_time | 10.000000 |
+-----------------+-----------+
1 row in set (0.00 sec)
```


超长时间默认为10秒，超过了即为慢查询。

**4，二进制日志**

二进制日志启动开关：log-bin [= file_name]
在5.6及以上版本一定要手动指定。5.6以下版本默认file_name为$datadir/mysqld-binlog,二进制日志用于记录所有更改数据的语句，主要用于复制和即时点恢复。二进制日志的主要目的是在数据库存在故障时，恢复时能够最大可能地更新数据库（即时点恢复），因为二进制日志包含备份后进行的所有更新,二进制日志还用于在主复制服务器上记录所有将发送给从服务器的语句。
查看二进制日志的工具为：mysqlbinlog
二进制日志的格式：
――> 基于语句: statement
――> 基于行: row
――> 混合方式: mixed
由于基于语句和基于行的日志格式都有自己的好处，MySQL使用的二进制日志文件是混合方式的二进制日志，内置策略会自动选择最佳的格式。
二进制日志事件：
――> 产生的时间：starttime
――> 相对位置：position
二进制日志文件：
――> 索引文件
――> 二进制日志文件
在数据目录下有一个mysql-bin.index便是索引文件，以mysql-bin开头并以数字结尾的文件为二进制日志文件。
日志的滚动：
MySQL的滚动方式与其他日志不太一样，滚动时会创建一个新的编号大1的日志用于记录最新的日志，而原日志名字不会被改变。每次重启MySQL服务，日志都会自动滚动一次。
另外如果需要手动滚动，则使用命令：

```
mysql> flush logs;
Query OK, 0 rows affected (0.02 sec)
mysql> show master status;  #查看当前正在使用的二进制文件
+------------------+----------+--------------+------------------+
| File       | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| mysql-bin.000033 |   107 |       |         |
+------------------+----------+--------------+------------------+
1 row in set (0.00 sec)
```



其默认的position是从107开始的。

```
mysql> show binary logs;  #查看所有的二进制文件
+------------------+-----------+
| Log_name     | File_size |
+------------------+-----------+
| mysql-bin.000020 |    107 |
| mysql-bin.000021 |    107 |
| mysql-bin.000022 |   50676 |
| mysql-bin.000023 |    150 |
| mysql-bin.000024 |    621 |
| mysql-bin.000025 |    107 |
| mysql-bin.000026 |   4509 |
| mysql-bin.000027 |    150 |
| mysql-bin.000028 |    150 |
| mysql-bin.000029 |    150 |
| mysql-bin.000030 |    357 |
| mysql-bin.000031 |    107 |
| mysql-bin.000032 |    150 |
| mysql-bin.000033 |    107 |
+------------------+-----------+
14 rows in set (0.00 sec)
mysql> use mysql_shiyan;
Database changed
mysql> insert into department(dpt_name) values('feiyu');
Query OK, 1 row affected (0.00 sec)
mysql> show master status;
+------------------+----------+--------------+------------------+
| File       | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| mysql-bin.000033 |   331 |       |         |
+------------------+----------+--------------+------------------+
1 row in set (0.00 sec)
```

插入数据后，position已经发生改变了。

```
mysql> insert into department(dpt_name) values('feiyu1');   #再插入一条数据
Query OK, 1 row affected (0.00 sec)
mysql> show binlog events in 'mysql-bin.000033';   #查看二进制文件中记录的内容
+------------------+-----+-------------+-----------+-------------+-------------------------------------------------------------------------+
| Log_name     | Pos | Event_type | Server_id | End_log_pos | Info                                  |
+------------------+-----+-------------+-----------+-------------+-------------------------------------------------------------------------+
| mysql-bin.000033 |  4 | Format_desc |     1 |     107 | Server ver: 5.5.36-log, Binlog ver: 4                  |
| mysql-bin.000033 | 107 | Query    |     1 |     183 | BEGIN                                  |
| mysql-bin.000033 | 183 | Query    |     1 |     304 | use `mysql_shiyan`; insert into department(dpt_name) values('feiyu') |
| mysql-bin.000033 | 304 | Xid     |     1 |     331 | COMMIT /* xid=12 */                           |
| mysql-bin.000033 | 331 | Query    |     1 |     407 | BEGIN                                  |
| mysql-bin.000033 | 407 | Query    |     1 |     529 | use `mysql_shiyan`; insert into department(dpt_name) values('feiyu1') |
| mysql-bin.000033 | 529 | Xid     |     1 |     556 | COMMIT /* xid=14 */                           |
+------------------+-----+-------------+-----------+-------------+-------------------------------------------------------------------------+
7 rows in set (0.00 sec)
        
mysql> show binlog events in 'mysql-bin.000033' from 407;   #也可以从某个位置查看二进制文件
+------------------+-----+------------+-----------+-------------+-------------------------------------------------------------------------+
| Log_name     | Pos | Event_type | Server_id | End_log_pos | Info                                  |
+------------------+-----+------------+-----------+-------------+-------------------------------------------------------------------------+
| mysql-bin.000033 | 407 | Query   |     1 |     529 | use `mysql_shiyan`; insert into department(dpt_name) values('feiyu1') |
| mysql-bin.000033 | 529 | Xid    |     1 |     556 | COMMIT /* xid=14 */                           |
+------------------+-----+------------+-----------+-------------+-------------------------------------------------------------------------+
2 rows in set (0.00 sec)
     
mysql> purge binary logs to 'mysql-bin.000025';  #删除某个序号之前的日志文件
Query OK, 0 rows affected (0.04 sec)
mysql> show binary logs;
+------------------+-----------+
| Log_name     | File_size |
+------------------+-----------+
| mysql-bin.000025 |    107 |
| mysql-bin.000026 |   4509 |
| mysql-bin.000027 |    150 |
| mysql-bin.000028 |    150 |
| mysql-bin.000029 |    150 |
| mysql-bin.000030 |    357 |
| mysql-bin.000031 |    107 |
| mysql-bin.000032 |    150 |
| mysql-bin.000033 |    556 |
+------------------+-----------+
9 rows in set (0.00 sec)
```



使用命令mysqlbinlog查看二进制日志内容：
基本语法：

mysqlbinlog [options] log-files
常用options（类似字节偏移数）：
--start-position   ：开始位置
--stop-position   ：结束位置
--start-datetime 'yyyy-mm-dd hh:mm:ss' ：开始时间
--stop-datetime 'yyyy-mm-dd hh:mm:ss' ：结束时间

```
←#4#root@localhost ~ →mysqlbinlog --start-position 407 --stop-position 556 mysql-bin.000033
/*!40019 SET @@session.max_insert_delayed_threads=0*/;
/*!50003 SET @OLD_COMPLETION_TYPE=@@COMPLETION_TYPE,COMPLETION_TYPE=0*/;
DELIMITER /*!*/;
mysqlbinlog: File 'mysql-bin.000033' not found (Errcode: 2)
DELIMITER ;
# End of log file
ROLLBACK /* added by mysqlbinlog */;
/*!50003 SET COMPLETION_TYPE=@OLD_COMPLETION_TYPE*/;
```

**5，中继日志**

这个后面会讲到。

**6，事务日志**

事务性存储引擎用于保证（ACID）原子性、一致性、隔离性和持久性；其不会立即写到数据文件中，而是写到事务日志中。
innodb_flush_log_at_trx_commit:
―――�C> 0: 每秒同步，并执行磁盘flush操作；
―――�C> 1：每事务同步，并执行磁盘flush操作；
―――�C> 2: 每事务同步，但不执行磁盘flush操作；

```
mysql> show global variables like 'innodb_flush_log_at_trx_commit';
+--------------------------------+-------+
| Variable_name         | Value |
+--------------------------------+-------+
| innodb_flush_log_at_trx_commit | 1   |
+--------------------------------+-------+
1 row in set (0.00 sec)
```

**三、MySQL中日志相关常用的服务器变量说明：**



**expire_logs_days={0..99}
**



设定二进制日志的过期天数，超出此天数的二进制日志文件将被自动删除。默认为0，表示不启用过期自动删除功能。如果启用此功能，自动删除工作通常发生在MySQL启动时或FLUSH日志时。作用范围为全局，可用于配置文件，属动态变量。

**general_log={ON|OFF}**

设定是否启用查询日志，默认值为取决于在启动mysqld时是否使用了�Cgeneral_log选项。如若启用此项，其输出位置则由�Clog_output选项进行定义，如果log_output的值设定为NONE，即使用启用查询日志，其也不会记录任何日志信息。作用范围为全局，可用于配置文件，属动态变量。

**general_log_file=FILE_NAME**

查询日志的日志文件名称，默认为“hostname.log”。作用范围为全局，可用于配置文件，属动态变量。

**binlog-format={ROW|STATEMENT|MIXED}**

指定二进制日志的类型，默认为STATEMENT，建议更改为MIXED。如果设定了二进制日志的格式，却没有启用二进制日志，则MySQL启动时会产生警告日志信息并记录于错误日志中。作用范围为全局或会话，可用于配置文件，且属于动态变量。

**log={YES|NO}**

是否启用记录所有语句的日志信息于一般查询日志(general query log)中，默认通常为OFF。MySQL 5.6已经弃用此选项。

**log-bin={YES|NO}**

是否启用二进制日志，如果为mysqld设定了�Clog-bin选项，则其值为ON，否则则为OFF。其仅用于显示是否启用了二进制日志，并不反应log-bin的设定值。作用范围为全局级别，属非动态变量。

**log_bin_trust_function_creators={TRUE|FALSE}**

此参数仅在启用二进制日志时有效，用于控制创建存储函数时如果会导致不安全的事件记录二进制日志条件下是否禁止创建存储函数。默认值为0，表示除非用户除了CREATE ROUTING或ALTER ROUTINE权限外还有SUPER权限，否则将禁止创建或修改存储函数，同时，还要求在创建函数时必需为之使用DETERMINISTIC属性，再不然就是附带READS SQL DATA或NO SQL属性。设置其值为1时则不启用这些限制。作用范围为全局级别，可用于配置文件，属动态变量。

**log_error=/PATH/TO/ERROR_LOG_FILENAME**

定义错误日志文件。作用范围为全局或会话级别，可用于配置文件，属非动态变量。

**log_output={TABLE|FILE|NONE}**

定义一般查询日志和慢查询日志的保存方式，可以是TABLE、FILE、NONE，也可以是TABLE及FILE的组合(用逗号隔开)，默认为TABLE。如果组合中出现了NONE，那么其它设定都将失效，同时，无论是否启用日志功能，也不会记录任何相关的日志信息。作用范围为全局级别，可用于配置文件，属动态变量。

**log_query_not_using_indexes={ON|OFF}**

设定是否将没有使用索引的查询操作记录到慢查询日志。作用范围为全局级别，可用于配置文件，属动态变量。

**log_slave_updates**

用于设定复制场景中的从服务器是否将从主服务器收到的更新操作记录进本机的二进制日志中。本参数设定的生效需要在从服务器上启用二进制日志功能。

**log_slow_queries={YES|NO}**

是否记录慢查询日志。慢查询是指查询的执行时间超出long_query_time参数所设定时长的事件。MySQL 5.6将此参数修改为了slow_query_log。作用范围为全局级别，可用于配置文件，属动态变量。

**log_warnings=#**

设定是否将警告信息记录进错误日志。默认设定为1，表示启用；可以将其设置为0以禁用；而其值为大于1的数值时表示将新发起连接时产生的“失败的连接”和“拒绝访问”类的错误信息也记录进错误日志。

**long_query_time=#**

设定区别慢查询与一般查询的语句执行时间长度。这里的语句执行时长为实际的执行时间，而非在CPU上的执行时长，因此，负载较重的服务器上更容易产生慢查询。其最小值为0，默认值为10，单位是秒钟。它也支持毫秒级的解析度。作用范围为全局或会话级别，可用于配置文件，属动态变量。

**max_binlog_cache_size{4096 .. 18446744073709547520}**

二进定日志缓存空间大小，5.5.9及以后的版本仅应用于事务缓存，其上限由max_binlog_stmt_cache_size决定。作用范围为全局级别，可用于配置文件，属动态变量。

**max_binlog_size={4096 .. 1073741824}**

设定二进制日志文件上限，单位为字节，最小值为4K，最大值为1G，默认为1G。某事务所产生的日志信息只能写入一个二进制日志文件，因此，实际上的二进制日志文件可能大于这个指定的上限。作用范围为全局级别，可用于配置文件，属动态变量。

**max_relay_log_size={4096..1073741824}**

设定从服务器上中继日志的体积上限，到达此限度时其会自动进行中继日志滚动。此参数值为0时，mysqld将使用max_binlog_size参数同时为二进制日志和中继日志设定日志文件体积上限。作用范围为全局级别，可用于配置文件，属动态变量。

**innodb_log_buffer_size={262144 .. 4294967295}**

设定InnoDB用于辅助完成日志文件写操作的日志缓冲区大小，单位是字节，默认为8MB。较大的事务可以借助于更大的日志缓冲区来避免在事务完成之前将日志缓冲区的数据写入日志文件，以减少I/O操作进而提升系统性能。因此，在有着较大事务的应用场景中，建议为此变量设定一个更大的值。作用范围为全局级别，可用于选项文件，属非动态变量。

**innodb_log_file_size={108576 .. 4294967295}**

设定日志组中每个日志文件的大小，单位是字节，默认值是5MB。较为明智的取值范围是从1MB到缓存池体积的1/n，其中n表示日志组中日志文件的个数。日志文件越大，在缓存池中需要执行的检查点刷写操作就越少，这意味着所需的I/O操作也就越少，然而这也会导致较慢的故障恢复速度。作用范围为全局级别，可用于选项文件，属非动态变量。

**innodb_log_files_in_group={2 .. 100}**

设定日志组中日志文件的个数。InnoDB以循环的方式使用这些日志文件。默认值为2。作用范围为全局级别，可用于选项文件，属非动态变量。

**innodb_log_group_home_dir=/PATH/TO/DIR**

设定InnoDB重做日志文件的存储目录。在缺省使用InnoDB日志相关的所有变量时，其默认会在数据目录中创建两个大小为5MB的名为ib_logfile0和ib_logfile1的日志文件。作用范围为全局级别，可用于选项文件，属非动态变量。

**innodb_support_xa={TRUE|FLASE}**

存储引擎事务在存储引擎内部被赋予了ACID属性，分布式(XA)事务是一种高层次的事务，它利用“准备”然后“提交”(prepare-then-commit)两段式的方式将ACID属性扩展到存储引擎外部，甚至是数据库外部。然而，“准备”阶段会导致额外的磁盘刷写操作。XA需要事务协调员，它会通知所有的参与者准备提交事务(阶段1)。当协调员从所有参与者那里收到“就绪”信息时，它会指示所有参与者进行真正的“提交”操作。
此变量正是用于定义InnoDB是否支持两段式提交的分布式事务，默认为启用。事实上，所有启用了二进制日志的并支持多个线程同时向二进制日志写入数据的MySQL服务器都需要启用分布式事务，否则，多个线程对二进制日志的写入操作可能会以与原始次序不同的方式完成，这将会在基于二进制日志的恢复操作中或者是从服务器上创建出不同原始数据的结果。因此，除了仅有一个线程可以改变数据以外的其它应用场景都不应该禁用此功能。而在仅有一个线程可以修改数据的应用中，禁用此功能是安全的并可以提升InnoDB表的性能。作用范围为全局和会话级别，可用于选项文件，属动态变量。

**relay_log=file_name**

设定中继日志的文件名称，默认为host_name-relay-bin。也可以使用绝对路径，以指定非数据目录来存储中继日志。作用范围为全局级别，可用于选项文件，属非动态变量。

**relay_log_index=file_name**

设定中继日志的索引文件名，默认为为数据目录中的host_name-relay-bin.index。作用范围为全局级别，可用于选项文件，属非动态变量。

**relay-log-info-file=file_name**

设定中继服务用于记录中继信息的文件，默认为数据目录中的relay-log.info。作用范围为全局级别，可用于选项文件，属非动态变量。

**relay_log_purge={ON|OFF}**

设定对不再需要的中继日志是否自动进行清理。默认值为ON。作用范围为全局级别，可用于选项文件，属动态变量。

**relay_log_space_limit=#**

设定用于存储所有中继日志文件的可用空间大小。默认为0，表示不限定。最大值取决于系统平台位数。作用范围为全局级别，可用于选项文件，属非动态变量。

**slow_query_log={ON|OFF}**

设定是否启用慢查询日志。0或OFF表示禁用，1或ON表示启用。日志信息的输出位置取决于log_output变量的定义，如果其值为NONE，则即便slow_query_log为ON，也不会记录任何慢查询信息。作用范围为全局级别，可用于选项文件，属动态变量。

**slow_query_log_file=/PATH/TO/SOMEFILE**

设定慢查询日志文件的名称。默认为hostname-slow.log，但可以通过�Cslow_query_log_file选项修改。作用范围为全局级别，可用于选项文件，属动态变量。

**sql_log_bin={ON|OFF}**

用于控制二进制日志信息是否记录进日志文件。默认为ON，表示启用记录功能。用户可以在会话级别修改此变量的值，但其必须具有SUPER权限。作用范围为全局和会话级别，属动态变量。

**sql_log_off={ON|OFF}**

用于控制是否禁止将一般查询日志类信息记录进查询日志文件。默认为OFF，表示不禁止记录功能。用户可以在会话级别修改此变量的值，但其必须具有SUPER权限。作用范围为全局和会话级别，属动态变量。

**sync_binlog=#**

设定多久同步一次二进制日志至磁盘文件中，0表示不同步，任何正数值都表示对二进制每多少次写操作之后同步一次。当autocommit的值为1时，每条语句的执行都会引起二进制日志同步，否则，每个事务的提交会引起二进制日志同步。 建议设置为1。

**文章关键词：** [mysql日志](http://www.uxys.com/tag/66561.jspx) [MySQL](http://www.uxys.com/tag/884.jspx) [日志管理](http://www.uxys.com/tag/2296.jspx) [管理](http://www.uxys.com/tag/2165.jspx) [日志](http://www.uxys.com/tag/2175.jspx) [详解](http://www.uxys.com/tag/10135.jspx)