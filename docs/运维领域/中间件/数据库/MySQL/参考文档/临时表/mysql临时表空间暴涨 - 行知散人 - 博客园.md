# [mysql临时表空间暴涨](https://www.cnblogs.com/mikeluwen/p/7651144.html)

（此文刚好遇到转载记录）

一、内部临时表使用

在某些情况下，服务器在处理语句时创建内部临时表，而用户无法直接控制临时表何时发生，完全有MySQL内部自行决定。

MySQL在以下几种情况会创建临时表：

1、UNION查询（MySQL 5.7起，执行UNION ALL不再产生临时表，除非需要额外排序。）；

2、用到TEMPTABLE算法或者是UNION查询中的视图；

3、ORDER BY和GROUP BY的子句不一样时；

4、表连接中，ORDER BY的列不是驱动表中的；

5、DISTINCT查询并且加上ORDER BY时；

6、SQL中用到SQL_SMALL_RESULT修饰符的查询；

7、FROM中的子查询（派生表）；

8、子查询或者semi-join时创建的表；

9、评估多表UPDATE语句；

10、评价GROUP_CONCAT()或COUNT(DISTINCT) 表达式计算；

要确定语句是否需要临时表，请使用EXPLAIN并检查Extra列以查看是否显示Using temporary。但对于派生或实物化的临时表EXPLAIN不一定会显示Using temporary。

MySQL内部参数tmp_table_size表示内部的临时表的最大值，其实生效的是tmp_table_size和max_heap_table_size这两个值之间的最小的那个值。当创建的临时表超过这个值(或者max_heap_table_size)时，MySQL将会在磁盘上创建临时表。

 

| 12345678 | mysql> show global variables like '%table_size%';+---------------------+----------+\| Variable_name    \| Value  \|+---------------------+----------+\| max_heap_table_size \| 16777216 \|\| tmp_table_size   \| 16777216 \|+---------------------+----------+2 rows in set (0.00 sec) |
| -------- | ------------------------------------------------------------ |
|          |                                                              |

当服务器创建内部临时表（在内存或磁盘上）时，会增加Created_tmp_tables状态变量（SHOW PROCESSLIST可以看到）。如果服务器在磁盘上创建表（最初或通过转换内存中的表），它会增加Created_tmp_disk_tables状态变量。

 

| 123456789 | mysql> show global status like '%Created_tmp%';+-------------------------+-------+\| Variable_name      \| Value \|+-------------------------+-------+\| Created_tmp_disk_tables \| 12495 \|\| Created_tmp_files    \| 12268 \|\| Created_tmp_tables   \| 39887 \|+-------------------------+-------+3 rows in set (0.00 sec) |
| --------- | ------------------------------------------------------------ |
|           |                                                              |

通过检查Created_tmp_disk_tables和Created_tmp_tables这两个global状态值来判断在磁盘上创建临时表的次数来进行相应的调优。

某些查询条件阻止使用内存中临时表，在以下几种情况下，会创建磁盘临时表：

1、表中存在BLOB或TEXT列；

2、在SELECT列表中存在任何字符串列的最大长度大于512（二进制字符串的字节，非二进制字符的字符），如果被UNION或UNION ALL使用；

3、SHOW COLUMNS FROM DB和DESCRIBE语句中使用BLOB作为用于某些列的类型；

服务器不使用符合特定条件的UNION语句的临时表。相反, 它只保留临时表创建执行结果列类型转换所需的数据结构。该表没有完全实例化, 并且没有写入或读取任何行，行直接发送到客户端。结果是减少了内存和磁盘要求, 并且在第一行发送到客户端之前的延迟较小, 因为服务器不需要等到执行最后一个查询块。解释和优化器跟踪输出反映了此执行策略: UNION结果查询块不存在, 因为该块对应于从临时表中读取的部分。

二、用于临时表的存储引擎

内部临时表可以在内存中保持并且由MEMORY存储引擎处理，或者由存储在磁盘上的InnoDB或MyISAM存储引擎处理。

如果内部临时表被创建为内存中的表，但是变得太大后，MySQL会自动将其转换为磁盘表。内存中临时表的最大大小是由tmp_table_size和max_heap_table_size 两个值中的较小值的决定。这与使用create table显式创建的内存引擎表不同，对于此类表，只有max_heap_table_size系统变量确定允许表增长的大小, 并且不能转换为磁盘上的格式。

从MySQL 5.7.5开始，新增一个系统选项internal_tmp_disk_storage_engine可定义磁盘临时表的引擎类型为InnoDB，而在这以前，只能使用MyISAM。

 

| 1234567 | mysql> show global variables like '%internal_tmp_disk_storage_engine%';+----------------------------------+--------+\| Variable_name          \| Value \|+----------------------------------+--------+\| internal_tmp_disk_storage_engine \| InnoDB \|+----------------------------------+--------+1 row in set (0.00 sec) |
| ------- | ------------------------------------------------------------ |
|         |                                                              |

而在MySQL 5.6.3以后新增的系统选项default_tmp_storage_engine是控制CREATE TEMPORARY TABLE创建的临时表的引擎类型，在以前默认是MEMORY，不要把这二者混淆了。

 

| 1234567 | mysql> show global variables like '%default_tmp_storage_engine%';+----------------------------+--------+\| Variable_name       \| Value \|+----------------------------+--------+\| default_tmp_storage_engine \| InnoDB \|+----------------------------+--------+1 row in set (0.00 sec) |
| ------- | ------------------------------------------------------------ |
|         |                                                              |

如下，创建一个显式临时表（当前线程退出临时表就会删除）：

 

| 12   | mysql> CREATE TEMPORARY TABLE tt(id int);     Query OK, 0 rows affected (0.00 sec) |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

在tmpdir参数控制存放磁盘路径的目录下有frm文件，如下：

 

| 1234567 | mysql> show global variables like 'tmpdir';+---------------+-------+\| Variable_name \| Value \|+---------------+-------+\| tmpdir    \| /tmp \|+---------------+-------+1 row in set (0.00 sec) |
| ------- | ------------------------------------------------------------ |
|         |                                                              |

 

 

| 123  | $ ll /tmp/total 12-rw-r----- 1 mysql mysql 8632 Sep 5 23:59 #sql298d_5c2_0.frm |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

但是这里只能看到frm文件，MySQL 5.7开始增加了临时表空间ibtmp1，数据都在ibtmp1空间中存储。

三、临时表存储格式

内存中临时表由MEMORY存储引擎管理，MEMORY存储引擎使用固定长度的行格式。并将VARCHAR和VARBINARY类型填充到最大列长度，实际上将它们存储为CHAR和BINARY类型。

在磁盘上的临时表由管理InnoDB或MyISAM存储引擎（取决于internal_tmp_disk_storage_engine设置）。两个引擎使用dynamic-width行格式存储临时表。列只需要尽可能多的存储空间，与使用固定长度行的磁盘表相比，减少了磁盘I/O和空间要求以及处理时间。

对于最初在内存中创建内部临时表的语句，然后将其转换为磁盘表，可能会通过跳过转换步骤并在磁盘上创建表来实现更好的性能。所述big_tables系统变量可以用来迫使内部临时表的磁盘存储。

 

| 1234567 | mysql> show global variables like '%big_tables%';+---------------+-------+\| Variable_name \| Value \|+---------------+-------+\| big_tables  \| OFF  \|+---------------+-------+1 row in set (0.01 sec) |
| ------- | ------------------------------------------------------------ |
|         |                                                              |

四、临时表空间使用

MySQL 5.7起，开始采用独立的临时表空间（和独立的undo表空间不是一回事哟），命名ibtmp1文件，初始化12M，且默认无上限。

选项innodb_temp_data_file_path可配置临时表空间相关参数。

 

| 1234567 | mysql> show global variables like '%innodb_temp_data_file_path%';+----------------------------+-----------------------+\| Variable_name       \| Value         \|+----------------------------+-----------------------+\| innodb_temp_data_file_path \| ibtmp1:12M:autoextend \|+----------------------------+-----------------------+1 row in set (0.00 sec) |
| ------- | ------------------------------------------------------------ |
|         |                                                              |

临时表空间的几点说明：

1、临时表空间不像普通InnoDB表空间那样，不支持裸设备（raw device）。

2、临时表空间使用动态的表空间ID，因此每次重启时都会变化（每次重启时，都会重新初始化临时表空间文件）。

3、当选项设置错误或其他原因（权限不足等原因）无法创建临时表空间时，mysqld实例也无法启动。

4、临时表空间中存储这非压缩的InnoDB临时表，如果是压缩的InnoDB临时表，则需要单独存储在各自的表空间文件中，文件存放在 tmpdir（/tmp）目录下。

5、临时表元数据存储在INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO视图中。

临时表使用的几点建议：

1、设置innodb_temp_data_file_path选项，设定文件最大上限（innodb_temp_data_file_path = ibtmp1:12M:autoextend:max:200M），超过上限时，需要生成临时表的SQL无法被执行（一般这种SQL效率也比较低，可借此机会进行优化）。

2、检查INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO，找到最大的临时表对应的线程，kill之即可释放，但ibtmp1文件则不能释放（除非重启）。

3、择机重启实例，释放ibtmp1文件，和ibdata1不同，ibtmp1重启时会被重新初始化而ibdata1则不可以。

4、定期检查运行时长超过N秒（比如N=300）的SQL，考虑干掉，避免垃圾SQL长时间运行影响业务。

临时表测试案例：

你可以往CREATE TEMPORARY TABLE里插入数据，ibtmp1会持续增长。另外你也可以产生一个union查询的慢SQL，MySQL 5.7起，执行UNION ALL不再产生临时表（除非需要额外排序）。

 

| 1    | mysql> select * from sbtest1 union select * from sbtest2; |
| ---- | --------------------------------------------------------- |
|      |                                                           |

查看ibtmp1文件会持续增长。

 

| 12   | $ du -sh /var/lib/mysql/ibtmp17.8G  /var/lib/mysql/ibtmp1 |
| ---- | --------------------------------------------------------- |
|      |                                                           |

有时执行SQL请求时会产生临时表，极端情况下，可能导致临时表空间文件暴涨，有案例中最高涨到快300G，比以前遇到的ibdata1文件暴涨还要猛。所以对于临时表空间的使用也是一定要多注意的。

------

MySQL 5.7起，开始采用独立的临时表空间（和独立的undo表空间不是一回事哟），命名ibtmp1文件，初始化12M，且默认无上限。

选项 **innodb_temp_data_file_path** 可配置临时表空间相关参数。

> ```
> innodb_temp_data_file_path = ibtmp1:12M:autoextend
> ```

### 临时表空间的几点说明

- 临时表空间不像普通InnoDB表空间那样，不支持裸设备（raw device）。
- 临时表空间使用动态的表空间ID，因此每次重启时都会变化（每次重启时，都会重新初始化临时表空间文件）。
- 当选项设置错误或其他原因（权限不足等原因）无法创建临时表空间时，mysqld实例也无法启动。
- 临时表空间中存储这非压缩的InnoDB临时表，如果是压缩的InnoDB临时表，则需要单独存储在各自的表空间文件中，文件存放在**tmpdir**（/tmp）目录下。
- 临时表元数据存储在 **INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO** 视图中。

有时执行SQL请求时会产生临时表，极端情况下，可能导致临时表空间文件暴涨，帮人处理过的案例中最高涨到快300G，比以前遇到的 ibdata1 文件暴涨还要猛…

### 临时表使用的几点建议

- 设置 **innodb_temp_data_file_path** 选项，设定文件最大上限，超过上限时，需要生成临时表的SQL无法被执行（一般这种SQL效率也比较低，可借此机会进行优化）。
- 检查 **INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO**，找到最大的临时表对应的线程，kill之即可释放，但 ibtmp1 文件则不能释放（除非重启）。
- 择机重启实例，释放 ibtmp1 文件，和 ibdata1 不同，ibtmp1 重启时会被重新初始化而 ibdata1 则不可以。
- 定期检查运行时长超过N秒（比如N=300）的SQL，考虑干掉，避免垃圾SQL长时间运行影响业务。

### 附：临时表测试案例

表DDL

> ```
> CREATE TEMPORARY TABLE `tmp1` (
>   `id` int(10) unsigned NOT NULL DEFAULT '0',
>   `name` varchar(50) NOT NULL DEFAULT '',
>   `aid` int(10) unsigned NOT NULL AUTO_INCREMENT,
>   `nid` int(11) unsigned GENERATED ALWAYS AS ((`id` + 1)) VIRTUAL NOT NULL,
>   `nnid` int(11) unsigned GENERATED ALWAYS AS ((`id` + 1)) STORED NOT NULL,
>   PRIMARY KEY (`aid`),
>   KEY `name` (`name`),
>   KEY `id` (`id`),
>   KEY `nid` (`nid`)
> ) ENGINE=InnoDB DEFAULT CHARSET=utf8
> ```

原表大小只有 120MB，从这个表直接 **INSERT…SELECT** 导数据到tmp1表。

> ```
> -rw-r-----  1 yejr  imysql   120M Apr 14 10:52 /data/mysql/test/sid.ibd
> ```

生成临时表（去掉虚拟列，临时表不支持虚拟列，然后写入数据），还更大了（我也不解，以后有机会再追查原因）。

> ```
> -rw-r-----  1 yejr  imysql   140M Jun 25 09:55 /Users/yejinrong/mydata/ibtmp1
> ```

查看临时表元数据信息

> ```
> yejr@imysql.com [test]>select * from 
>  INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO\G
> *********************** 1. row ***********************
>             TABLE_ID: 405
>                 NAME: #sql14032_300000005_3
>               N_COLS: 6
>                SPACE: 421
> PER_TABLE_TABLESPACE: FALSE
>        IS_COMPRESSED: FALSE
> ```

再删除索引，结果，又更大了

> ```
> -rw-r-----  1 yejr  imysql   204M Jun 25 09:57 /data/mysql/ibtmp1
> ```

第二次测试删除索引后，变成了200M（因为第二次测试时，我设置了临时表最大200M）

> ```
> innodb_temp_data_file_path = ibtmp1:12M:autoextend:max:200M
> -rw-r-----  1 yejr  imysql   200M Jun 25 10:15 /data/mysql/ibtmp1
> ```

执行一个会产生临时表的慢SQL。
**注**：MySQL 5.7起，执行UNION ALL不再产生临时表（除非需要额外排序）。

> ```
> yejr@imysql.com [test]>explain select * from tmp1 union 
>   select id,name,aid from sid\G
> *************************** 1. row ***************************
>            id: 1
>   select_type: PRIMARY
>         table: tmp1
>    partitions: NULL
>          type: ALL
> possible_keys: NULL
>           key: NULL
>       key_len: NULL
>           ref: NULL
>          rows: 3986232
>      filtered: 100.00
>         Extra: NULL
> *************************** 2. row ***************************
>            id: 2
>   select_type: UNION
>         table: sid
>    partitions: NULL
>          type: ALL
> possible_keys: NULL
>           key: NULL
>       key_len: NULL
>           ref: NULL
>          rows: 802682
>      filtered: 100.00
>         Extra: NULL
> *************************** 3. row ***************************
>            id: NULL
>   select_type: UNION RESULT
>         table: <union1,2>
>    partitions: NULL
>          type: ALL
> possible_keys: NULL
>           key: NULL
>       key_len: NULL
>           ref: NULL
>          rows: NULL
>      filtered: NULL
>         Extra: Using temporary
> ```

文件涨到588M还没结束，我直接给卡了

> ```
> -rw-r-----  1 yejr  imysql   588M Jun 25 10:07 /data/mysql/ibtmp1
> ```

第二次测试时，设置了临时表空间文件最大200M，再执行会报错：

> ```
> yejr@imysql.com [test]>select * from tmp1 union 
>  select id,name,aid from sid;
> ERROR 1114 (HY000): The table '/var/folders/bv/j4tjn6k54dj5jh1tl8yn6_y00000gn/T/#sql14032_5_8' is full
> ```