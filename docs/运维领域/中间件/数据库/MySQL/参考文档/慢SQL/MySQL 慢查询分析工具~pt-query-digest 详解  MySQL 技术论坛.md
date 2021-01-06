# MySQL 慢查询分析工具~pt-query-digest 详解

[3](javascript:;)[3](javascript:;)[0](https://learnku.com/articles/40376#replies)

[![img](MySQL 慢查询分析工具~pt-query-digest 详解  MySQL 技术论坛.assets/44x44) MySQL ](https://learnku.com/mysql)/ 31 / 0 / 发布于 10个月前 / 更新于 10个月前

## 介绍

> pt-query-digest 是用于分析 mysql 慢查询的一个工具，它可以分析 binlog、general log、slowlog，也可以通过 SHOW PROCESSLIST 或者通过 tcpdump 抓取的 MySQL 协议数据来进行分析。
>
> 可以把分析结果输出到文件中，分析过程是先对查询语句的条件进行参数化，然后对参数化以后的查询进行分组统计，统计出各查询的执行时间、次数、占比等，可以借助分析结果找出问题进行优化。

## 安装（yum 安装）

> yum install perl-DBI
>
> yum install perl-DBD-MySQL
>
> yum install perl-Time-HiRes
>
> yum install perl-IO-Socket-SSL
>
> wget percona.com/get/pt-query-digest
>
> chmod u+x pt-query-digest
>
> mv pt-query-digest /usr/bin/

## 语法

> pt-query-digest [OPTIONS] [FILES] [DSN]
>
> --create-review-table 当使用 --review 参数把分析结果输出到表中时，如果没有表就自动创建。
>
> --create-history-table 当使用 --history 参数把分析结果输出到表中时，如果没有表就自动创建。
>
> --filter 对输入的慢查询按指定的字符串进行匹配过滤后再进行分析。
>
> --limit 限制输出结果百分比或数量，默认值是 20, 即将最慢的 20 条语句输出，如果是 50% 则按总响应时间占比从大到小排序，输出到总和达到 50% 位置截止。
>
> --host mysql 服务器地址
>
> --user mysql 用户名
>
> --password mysql 用户密码
>
> --history 将分析结果保存到表中，分析结果比较详细，下次再使用 --history 时，如果存在相同的语句，且查询所在的时间区间和历史表中的不同，则会记录到数据表中，可以通过查询同一 CHECKSUM 来比较某类型查询的历史变化。
>
> --review 将分析结果保存到表中，这个分析只是对查询条件进行参数化，一个类型的查询一条记录，比较简单。当下次使用 --review 时，如果存在相同的语句分析，就不会记录到数据表中。
>
> --output 分析结果输出类型，值可以是 report (标准分析报告)、slowlog (Mysql slow log)、json、json-anon，一般使用 report，以便于阅读。
>
> --since 从什么时间开始分析，值为字符串，可以是指定的某个”yyyy-mm-dd [hh:mm:ss]” 格式的时间点，也可以是简单的一个时间值：s (秒)、h (小时)、m (分钟)、d (天)，如 12h 就表示从 12 小时前开始统计。
>
> --until 截止时间，配合 —since 可以分析一段时间内的慢查询。

## 分析 pt-query-digest 输出结果

#### 第一部分：总体统计结果

> Overall：总共有多少条查询
>
> Time range：查询执行的时间范围
>
> unique：唯一查询数量，即对查询条件进行参数化以后，总共有多少个不同的查询
>
> total：总计  min：最小  max：最大 avg：平均
>
> 95%：把所有值从小到大排列，位置位于 95% 的那个数，这个数一般最具有参考价值
>
> median：中位数，把所有值从小到大排列，位置位于中间那个数

```php
# 该工具执行日志分析的用户时间，系统时间，物理内存占用大小，虚拟内存占用大小
# 340ms user time, 140ms system time, 23.99M rss, 203.11M vsz
# 工具执行时间
# Current date: Fri Nov 25 02:37:18 2016
# 运行分析工具的主机名
# Hostname: localhost.localdomain
# 被分析的文件名
# Files: slow.log
# 语句总数量，唯一的语句数量，QPS，并发数
# Overall: 2 total, 2 unique, 0.01 QPS, 0.01x concurrency ________________
# 日志记录的时间范围
# Time range: 2016-11-22 06:06:18 to 06:11:40
# 属性               总计      最小    最大    平均    95%  标准    中等
# Attribute          total     min     max     avg     95%  stddev  median
# ============     ======= ======= ======= ======= ======= ======= =======
# 语句执行时间
# Exec time             3s   640ms      2s      1s      2s   999ms      1s
# 锁占用时间
# Lock time            1ms       0     1ms   723us     1ms     1ms   723us
# 发送到客户端的行数
# Rows sent              5       1       4    2.50       4    2.12    2.50
# select语句扫描行数
# Rows examine     186.17k       0 186.17k  93.09k 186.17k 131.64k  93.09k
# 查询的字符数
# Query size           455      15     440  227.50     440  300.52  227.50
```

#### 第二部分：查询分组统计结果

> Rank：所有语句的排名，默认按查询时间降序排列，通过 --order-by 指定
>
> Query ID：语句的 ID，（去掉多余空格和文本字符，计算 hash 值）
>
> Response：总的响应时间
>
> time：该查询在本次分析中总的时间占比
>
> calls：执行次数，即本次分析总共有多少条这种类型的查询语句
>
> R/Call：平均每次执行的响应时间
>
> V/M：响应时间 Variance-to-mean 的比率
>
> Item：查询对象

```php
# Profile
# Rank Query ID           Response time Calls R/Call V/M   Item
# ==== ================== ============= ===== ====== ===== ===============
#    1 0xF9A57DD5A41825CA  2.0529 76.2%     1 2.0529  0.00 SELECT
#    2 0x4194D8F83F4F9365  0.6401 23.8%     1 0.6401  0.00 SELECT wx_member_base
```

#### 第三部分：每一种查询的详细统计结果

> 由下面查询的详细统计结果，最上面的表格列出了执行次数、最大、最小、平均、95% 等各项目的统计。
>
> ID：查询的 ID 号，和上图的 Query ID 对应
>
> Databases：数据库名
>
> Users：各个用户执行的次数（占比）
>
> Query_time distribution ：查询时间分布，长短体现区间占比，本例中 1s-10s 之间查询数量是 10s 以上的两倍。
>
> Tables：查询中涉及到的表
>
> Explain：SQL 语句

```php
# Query 1: 0 QPS, 0x concurrency, ID 0xF9A57DD5A41825CA at byte 802 ______
# This item is included in the report because it matches --limit.
# Scores: V/M = 0.00
# Time range: all events occurred at 2016-11-22 06:11:40
# Attribute    pct   total     min     max     avg     95%  stddev  median
# ============ === ======= ======= ======= ======= ======= ======= =======
# Count         50       1
# Exec time     76      2s      2s      2s      2s      2s       0      2s
# Lock time      0       0       0       0       0       0       0       0
# Rows sent     20       1       1       1       1       1       0       1
# Rows examine   0       0       0       0       0       0       0       0
# Query size     3      15      15      15      15      15       0      15
# String:
# Databases    test
# Hosts        192.168.8.1
# Users        mysql
# Query_time distribution
#   1us
#  10us
# 100us
#   1ms
#  10ms
# 100ms
#    1s  ################################################################
#  10s+
# EXPLAIN /*!50100 PARTITIONS*/
select sleep(2)\G
```

## 使用例子

```php
1.直接分析慢查询文件
pt-query-digest  slow.log > slow_report.log
2.分析最近12小时内的查询
pt-query-digest  --since=12h  slow.log > slow_report2.log
3.分析指定时间范围内的查询
pt-query-digest slow.log --since '2020-01-07 09:30:00' --until '2020-01-07 10:00:00'> > slow_report3.log
3.分析指含有select语句的慢查询
pt-query-digest --filter '$event->{fingerprint} =~ m/^select/i' slow.log> slow_report4.log
4.分析最近12小时内的查询
pt-query-digest  --since=12h  slow.log > slow_report2.log
5.针对某个用户的慢查询
pt-query-digest --filter '($event->{user} || "") =~ m/^root/i' slow.log> slow_report5.log
6.查询所有所有的全表扫描或full join的慢查询
pt-query-digest --filter '(($event->{Full_scan} || "") eq "yes") ||(($event->{Full_join} || "") eq "yes")' slow.log> slow_report6.log
7.把查询保存到query_review表
pt-query-digest --user=root –password=abc123 --review  h=localhost,D=test,t=query_review--create-review-table  slow.log
8.把查询保存到query_history表
pt-query-digest  --user=root –password=abc123 --review  h=localhost,D=test,t=query_history--create-review-table  slow.log_0001
pt-query-digest  --user=root –password=abc123 --review  h=localhost,D=test,t=query_history--create-review-table  slow.log_0002
9.通过tcpdump抓取mysql的tcp协议数据，然后再分析
tcpdump -s 65535 -x -nn -q -tttt -i any -c 1000 port 3306 > mysql.tcp.txt
pt-query-digest --type tcpdump mysql.tcp.txt> slow_report9.log
10.分析binlog
mysqlbinlog mysql-bin.000093 > mysql-bin000093.sql
pt-query-digest  --type=binlog  mysql-bin000093.sql > slow_report10.log
11.分析general log
pt-query-digest  --type=genlog  localhost.log > slow_report11.log
```

## 安装遇到的问题

> 问题：
>
> [root@vipstone bin]# pt-query-digest /usr/local/mysql/data/slow.log
>
> Can't locate Digest/MD5.pm in @INC (@INC contains: /usr/local/lib64/perl5 /usr/local/share/perl5 /usr/lib64/perl5/vendor_perl /usr/share/perl5/vendor_perl /usr/lib64/perl5 /usr/share/perl5 .) at /usr/local/bin/pt-query-digest line 2470.
>
> BEGIN failed--compilation aborted at /usr/local/bin/pt-query-digest line 2470.
>
> 解决：
>
> yum -y install perl-Digest-MD5

##### 参考资料：

> 原作者：鲁玉成
>
> 出处：[https://www.cnblogs.com/luyucheng/p/626587...](https://www.cnblogs.com/luyucheng/p/6265873.html)

 [mysql](https://learnku.com/blog/zhangdeTalk/tags/mysql_487) [pt-query-digest](https://learnku.com/blog/zhangdeTalk/tags/pt-query-digest_52921)

> 本作品采用[《CC 协议》](https://learnku.com/docs/guide/cc4.0/6589)，转载必须注明作者和本文链接