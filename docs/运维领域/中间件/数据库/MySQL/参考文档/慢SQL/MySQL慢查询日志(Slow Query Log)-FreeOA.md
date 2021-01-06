MySQL慢查询日志(Slow Query Log)

![创建时间](MySQL慢查询日志(Slow Query Log)-FreeOA.assets/datetime_icon.gif)2018-04-08 10:13:30 ![作者](MySQL慢查询日志(Slow Query Log)-FreeOA.assets/user_icon.gif)阿炯

------

同大多数关系型数据库一样，日志文件是MySQL数据库的重要组成部分。MySQL有几种不同的日志文件，通常包括错误日志文件，二进制日志，通用日志，慢查询日志，等等。这些日志可以帮助我们定位mysqld内部发生的事件，数据库性能故障，记录数据的变更历史，用户恢复数据库等等。本文主要描述慢查询日志。

**MySQL日志文件系统的组成**
a、错误日志：记录启动、运行或停止mysqld时出现的问题。
b、通用日志：记录建立的客户端连接和执行的语句。
c、更新日志：记录更改数据的语句。该日志在MySQL 5.1中已不再使用。
d、二进制日志：记录所有更改数据的语句。还用于复制。
e、慢查询日志：记录所有执行时间超过long_query_time秒的所有查询或不使用索引的查询。
f、Innodb日志：innodb redo log

缺省情况下，所有日志创建于mysqld数据目录中。可以通过刷新日志，来强制mysqld来关闭和重新打开日志文件(或者在某些情况下切换到一个新的日志)。当你执行一个FLUSH LOGS语句或执行mysqladmin flush-logs或mysqladmin refresh时，则日志被老化。对于存在MySQL复制的情形下，从复制服务器将维护更多日志文件，被称为接替日志。

**慢查询日志**
慢查询日志是将mysql服务器中影响数据库性能的相关SQL语句记录到日志文件，通过对这些特殊的SQL语句分析，改进以达到提高数据库性能的目的。在MySQL中，慢查询日志默认是关闭的，若要开启，在my.cnf中加入该配置项：
\#将慢查询记录至一个表或日志文件中
\#默认记录至文件hostname-slow.log中，如果使用了log-output=TABLE，则记录至表mysql.slow_log中。要使其他慢查询配置项生效，必须启用此配置项
\#默认值：OFF
slow-query-log

然后可以重启MySQL，就开启了慢查询。从MySQL 5.1开始，long_query_time开始以微秒记录SQL语句运行时间，之前仅用秒为单位记录。如果记录到表里面，只会记录整数部分，不会记录微秒部分。

通过使用--slow_query_log[={0|1}]选项来启用慢查询日志，所有执行时间超过long_query_time秒的SQL语句都会被记录到慢查询日志，缺省情况下hostname-slow.log为慢查询日志文件安名，存放到数据目录，同时缺省情况下未开启慢查询日志。缺省情况下数据库相关管理型SQL(比如OPTIMIZE TABLE、ANALYZE TABLE和ALTER TABLE)不会被记录到日志。对于管理型SQL可以通过--log-slow-admin-statements开启记录管理型慢SQL。

mysqld在语句执行完并且所有锁释放后记入慢查询日志，记录顺序可以与执行顺序不相同。获得初使表锁定的时间不算作执行时间。

将慢查询日志记录到指定的文件：
\#name为文件名
\#默认值：host_name-slow.log
slow-query-log-file=name

指定慢查询时长：
\#记录所有执行时间超过long_query_time秒的查询到慢查询日志
\#该参数将被视为带小数的数值，并且精确到微秒级
\#默认值：10
long-query-time=n

限定查询扫描的行数：
\#扫描行数小于该值的查询，不记入慢查询日志
\#默认值：0
min-examined-row-limit=n

记录执行缓慢的MySQL管理命令：
\#记录执行缓慢的OPTIMIZE、ANALYZE、ALTER和其他管理命令语句
\#默认值：OFF
log-slow-admin-statements

记录没有使用索引的查询，而不考虑执行时间的长短：
\#记录那些执行时没有从任何索引中受益的查询
\#默认值：OFF
log-queries-not-using-indexes

限制每分钟记录的不使用索引的查询数：
\#每分钟记录最多这么多条“不使用索引”的警告至慢查询日志
\#任何更多的警告都将被压缩概括为一行。值为0则禁用该限制
\#除非设置了log-queries-not-using-indexes，否则该项不生效
\#默认值：0
log-throttle-queries-not-using-indexes=n

指定日志输出的目的地：
\# 语法：log-output=value[,value...]，“value”可以是TABLE、FILE或NONE
\# 默认值：FILE
log-output=name

写入更少的信息：
\#不记录扩展信息
\#默认值：FALSE
log-short-format

记录从库线程执行的慢查询语句：
\# 默认值：OFF
log-slow-slave-statements

可以使用mysqldumpslow命令获得日志中显示的查询摘要来处理慢查询日志。用查询缓存处理的查询不加到慢查询日志中，表有零行或一行而不能从索引中受益的查询也不写入慢查询日志。MySQL服务器按以下顺序记录SQL是否写入到慢查询日志：
a. The query must either not be an administrative statement, or --log-slow-adminstatements must have been specified.

b. The query must have taken at least long_query_time seconds, or log_queries_not_using_indexes must be enabled and the query used no indexes for row lookups.

c. The query must have examined at least min_examined_row_limit rows.

d. The query must not be suppressed according to the log_throttle_queries_not_using_indexes setting.

**慢查询日志相关参数**
long_query_time：设定慢查询的阀值，超出次设定值的SQL即被记录到慢查询日志，缺省值为10s  
slow_query_log：指定是否开启慢查询日志，1表示开启，0表示关闭
log_slow_queries：旧版(5.6以下版本)MySQL数据库慢查询日志存储路径。可以不设置该参数，系统则会默认给一个缺省的文件host_name-slow.log  
slow_query_log_file：新版(5.6及以上版本)MySQL数据库慢查询日志存储路径。可以不设置该参数，系统则会默认给一个缺省的文件host_name-slow.log  
min_examined_row_limit：查询检查返回少于该参数指定行的SQL不被记录到慢查询日志  
log_queries_not_using_indexes：不使用索引的慢查询日志是否记录到索引
log_output：日志存储方式。log_output='FILE'表示将日志存入文件，默认值是'FILE'。log_output='TABLE'表示将日志存入数据库，这样日志信息就会被写入到mysql.slow_log表中。MySQL数据库支持同时两种日志存储方式，配置的时候以逗号隔开即可，如：log_output='FILE,TABLE'。日志记录到系统的专用日志表中，要比记录到文件耗费更多的系统资源，因此对于需要启用慢查询日志，又需要能够获得更高的系统性能，那么建议优先记录到文件。


long_query_time为一个MySQL选项参数。这个参数记录了超过执行时间超过该值以上的SQL，但这个问题在于：是按真正执行的时间(real time)，不包括等待锁的时间。举个例子：如果long_query_time设置为1秒，一个insert被lock了10秒，执行只耗了0.5秒，那么不会被记录到慢日志。

lock_time与query_time为slow log中所记录的两个属性：
lock_time：waiting for xxx lock的时间
query_time：real time + lock time的总时间

某些场景下，一条十分简单的sql也可能执行很长，被记录到slow log，那么可能就需要关注一下lock time是否很大了。

start_time
为slow log中所记录的属性。
start_time：看字面意思很容易会被误认为"sql开始的时间"，但实际上记录的是sql结束的时间。真正的开始时间计算的方法也很简单：start_time - query_time 即为sql真正开始的时间。

log_output
枚举型，动态参数。
用于设置slow log和general log的输出对象。可以设置为none，table，file，分别代表：不输出，存于表，存于文件。

并且也可以组合设置：
比如SET GLOBAL log_output='table,file';则代表同时输出到表和文件中。如果设置SET GLOBAL log_output='none,file' 或 'none,table' 或 'table,file,none' 均代表'none'。

slow_query_log与slow_query_log_file
slow_query_log 布尔型，动态参数，默认为OFF。
用于控制是否开启slow log。

slow_query_log_file 动态参数，指定slow log文件的名称和路径。若未设置，则slow log的文件名取默认值$host_name-slow.log，存放于$datadir下。

long_query_time
动态参数，默认值为10。
记录执行时间(real time)超过该值以上的SQL。

log_queries_not_using_indexes
布尔型，动态参数，默认为OFF。
若开启，则表示记录所有未使用索引的SQL，无论是否超过long_query_time所设置的值。
不遵循long_query_time，忽略long_query_time的设置。

log_throttle_queries_not_using_indexes
整型，动态参数，默认为0。
如果log_queries_not_using_indexes开启，那么log_throttle_queries_not_using_indexes用于限制每分钟所记录的slow log数量。
设置为0则表示"不限制"。

log_slow_admin_statements
布尔型，动态参数，默认为OFF。5.7后新增的参数。
可用于控制slow log是否记录数据库管理的SQL。若开启，则表示记录这些SQL。数据库管理的SQL包括：ALTER TABLE, ANALYZE TABLE, CHECK TABLE, CREATE INDEX, DROP INDEX, OPTIMIZE TABLE, REPAIR TABLE。
遵循long_query_time。

第一次执行check table，时间超过2秒，但未被记录。第二次执行check table，开启log_queries_not_using_indexes，超过2秒将会被记录。

log_slow_slave_statements
布尔型，动态参数，默认为OFF。5.7后新增的参数。
开启后，在slave上将会记录超过long_query_time的日志记录。即便开启了这个选项，也不会立刻生效，新的变更需要再一次START SLAVE后生效。

min_examined_row_limit
整型，动态参数，默认为0。
设置该值，则表示返回行数大于等于该值的sql，将会被记录到slow log中。

log-short-format
默认为FLASE，该选项仅仅为启动时选项，并不支持系统变量。如果该选项被激活，则表示在slow log中记录更少的信息。

log_timestamps
枚举型，动态，默认为UTC，5.7.2后出现。
这个参数是用于控制记录在error log、general log、slow log中，对应日期时区的选项。

MySQL 5.7 日志时间(log_timestamps)与系统时间不一致

5.7.2后，MySQL加入了一个参数，log_timestamps这个参数是用于控制error log、general log、slow log日期时区的。当然只对log_output=FILE的general log、slow log生效。

那么如果没有在5.7的配置文件中额外设置的情况下，就会出现如下问题：错误日志中的时间不对之类的问题，而之前的版本默认为本地的系统时区：
Before 5.7.2, timestamps in log messages were written using the local system time zone by default, not UTC. If you want the previous log message time zone default, set log_timestamps=SYSTEM.

该变量目前为枚举类型，并只支持"UTC"与"SYSTEM"，并且可以动态修改：
SET GLOBAL log_timestamps=SYSTEM;  SELECT @@log_timestamps;

写在配置文件里重启的错误日志效果立现。

Query time include the Lock time in mysql

specific query time it was Query_time - Lock_time

The Lock_time represents how long the query spent waiting to acquire a lock, whether the lock was just on the row (for tables using the InnoDB storage engine) or on the entire table (MyISAM storage engine).

To reduce the Lock_time, you can consider changing the storage engine of your table to InnoDB, which supports the locking of individual rows during UPDATE, INSERT, and other statements which modify the content of the database. MyISAM locks the entire table for such operations.

The lock_time in the slow query log is actually the amount of time the query spent waiting to acquire the lock it needs to run. For example, UPDATES queries need a write lock.

The locking also depends on the storage engine you are using in the table. When writing, InnoDB will use row-level locking and only lock the rows that are being changed. MyISAM will lock the entire table until the update/insert/delete is complete.

The Locking of the entire table for MyISAM is a big reason SELECT queries will have a lock_time in your slow query log.

**格式化慢查询日志**
结构化慢查询日志就是把慢查询日志中的重要信息按照便于阅读以及按照特定的排序方式来提取SQL，这种方式有点类似于Oracle中有个tkprof来格式化oracle的trace文件，对于前面的慢查询日志我们使用mysqldumpslow来提取如下：
\# mysqldumpslow -s at,al /var/lib/mysql/freeoa-slow.log

以下是按照最大耗用时间排最后，只显示2条的方式格式化日志文件：
\# mysqldumpslow -r -t 2 /var/lib/mysql/freeoa-slow.log

mysqldumpslow --help
Usage: mysqldumpslow [ OPTS... ] [ LOGS... ]

Parse and summarize the MySQL slow query log. Options are
 --verbose  verbose
 --debug   debug
 --help    write this text to standard output
 -v      verbose
 -d      debug
 -s ORDER   what to sort by (al, at, ar, c, l, r, t), 'at' is default
  al: average lock time
  ar: average rows sent
  at: average query time
  c: count
  l: lock time
  r: rows sent
  t: query time
 -r      reverse the sort order (largest last instead of first)
 -t NUM    just show the top n queries
 -a      don't abstract all numbers to N and strings to 'S'
 -n NUM    abstract numbers with at least n digits within names
 -g PATTERN  grep: only consider stmts that include this string
 -h HOSTNAME hostname of db server for *-slow.log filename (can be wildcard),default is '*', i.e. match all
 -i NAME   name of server instance (if using mysql.server startup script)
 -l      don't subtract lock time from total time

-s, 是表示按照何种方式排序，
  c: 访问计数
  l: 锁定时间
  r: 返回记录
  t: 查询时间
  al:平均锁定时间
  ar:平均返回记录数
  at:平均查询时间

-t, 是top n的意思，即为返回前面多少条的数据；

-g, 后边可以写一个正则匹配模式，大小写不敏感的；

例如

得到返回记录集最多的10个SQL
mysqldumpslow -s r -t 10 /database/mysql/mysql_slow.log

得到访问次数最多的10个SQL
mysqldumpslow -s c -t 10 /database/mysql/mysql_slow.log

得到按照时间排序的前10条里面含有左连接的查询语句
mysqldumpslow -s t -t 10 -g “left join” /database/mysql/mysql_slow.log

另外建议在使用这些命令时结合管道和more使用，否则有可能出现刷屏的情况
mysqldumpslow -s r -t 20 /mysqldata/mysql/mysql06-slow.log | more

**mysql库中的slow_log表**
log_output参数为TABLE时，慢查询记录到mysql.slow_log表里，但这时这个系统表没有任何索引，我们一般可以在start_time列自行加上索引方便检索，如果存放时间长一点，可将表引擎设为myisam。

start_time指的是SQL结束时间，而不是开始执行时间。

log_queries_not_using_indexes为1时，会记录任何不使用索引的sql，从而无视long_query_time参数(set global log_queries_not_using_indexes=1)。在log_queries_not_using_indexes为1的情况下，默认没走索引的sql有多少就记录多少，而设置了log_throttle_queries_not_using_indexes为N后，表示1分钟内该SQL最多记录N条，这个参数在5.6.5后支持。

默认情况下不会记录DDL操作，不管执行时间多长，除非将log_slow_admin_statements参数设置为1，而这个参数只在5.6.11后支持。

默认情况下有记录就记录，而设置了min_examined_row_limit为N后，表示只有返回条数大于N才记录到慢查询。

只有sql的实际执行时间超过long_query_time，才会记录到慢查询(这里的实际执行时间排除了lock的时间)，而当记录到slow_log后，query_time列记录的时间是实际执行时间+lock_time的时间。

默认slave不会记录主库传过来的慢查询，除非开启log_slow_slave_statements为1(官方文档是这么说的)，但是我在主从上都打开了这个参数，发现从库还是没有记录(5.6.11支持这个参数)。

在my.cnf配置文件中修改
slow_query_log = 1
long_query_time = 2
log_output = FILE,TABLE
general-log
expire_logs_days = n # 二进制日志保留的天数，默认值为10
log_queries_not_using_indexes

命令行中即时生效
set global log_slow_queries = 1;
set global long_query_time = 2;
set global log_output = 'FILE,TABLE';
or
SET GLOBAL log_output='file,table';
set global general_log = 1;
set global expire_logs_days = n;


mysql> show create table mysql.slow_log\G
*************************** 1. row ***************************
Table: slow_log
Create Table: CREATE TABLE `slow_log` (
 `start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 `user_host` mediumtext NOT NULL,
 `query_time` time NOT NULL,
 `lock_time` time NOT NULL,
 `rows_sent` int(11) NOT NULL,
 `rows_examined` int(11) NOT NULL,
 `db` varchar(512) NOT NULL,
 `last_insert_id` int(11) NOT NULL,
 `insert_id` int(11) NOT NULL,
 `server_id` int(10) unsigned NOT NULL,
 `sql_text` mediumtext NOT NULL
) ENGINE=CSV DEFAULT CHARSET=utf8 COMMENT='Slow log'

ALTER TABLE mysql.slow_log ENGINE = MyISAM;
ALTER TABLE mysql.slow_log ADD INDEX (start_time);


修改表的存储结构前需要对日志系统先停用后启用，否则不会成功：
mysql> ALTER TABLE mysql.slow_log ENGINE = MyISAM;
ERROR 1580 (HY000): You cannot 'ALTER' a log table if logging is enabled

set global slow_query_log=0;
ALTER TABLE mysql.slow_log ENGINE = MyISAM;
ALTER TABLE mysql.slow_log ADD INDEX (start_time);
set global slow_query_log=1;

这个操作同样适用于general_log通用日志表。

参考来源：
[mysql.slow_log Table](https://mariadb.com/kb/en/library/mysqlslow_log-table/)

[Selecting General Query and Slow Query Log Output Destinations](https://dev.mysql.com/doc/refman/5.6/en/log-destinations.html)

[理解Mysql日志](http://www.freeoa.net/osuport/db/the-mysql-log_1480.html)