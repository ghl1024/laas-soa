# Mysql占cpu近100%解决思路

![img](Mysql占cpu近100%解决思路_eclothy的专栏-CSDN博客.assets/reprint.png)

[袁桨](https://blog.csdn.net/eclothy) 2016-03-21 14:53:30 ![img](Mysql占cpu近100%解决思路_eclothy的专栏-CSDN博客.assets/articleReadEyes.png) 10141 ![img](Mysql占cpu近100%解决思路_eclothy的专栏-CSDN博客.assets/tobarCollect.png) 收藏 1

分类专栏： [mysql碎片整理](https://blog.csdn.net/eclothy/category_2169353.html)

当前网站的七日平均日IP为2900，PageView为3.8万左右。网站A用的database目前有39个表，记录数60.1万条，占空间45MB。按这个数据，Mysql不可能占用这么高的资源。

于是在服务器上运行命令，将 mysql 当前的环境变量输出到文件 output.txt：



```css
d:\web\mysql> mysqld.exe --help >output.txt
```


发现 tmp_table_size 的值是默认的 32M，于是修改 My.ini, 将 tmp_table_size 赋值到 200M:





```groovy
d:\web\mysql> notepad c:\windows\my.ini
[mysqld]
tmp_table_size=200M
```


然后重启 MySQL 服务。CPU 占用有轻微下降，以前的CPU 占用波形图是 100% 一根直线，现在则在 97%~100%之间起伏。这表明调整 tmp_table_size 参数对 MYSQL 性能提升有改善作用。但问题还没有完全解决。
于是进入 mysql 的 shell 命令行，调用 show processlist, 查看当前 mysql 使用频繁的 sql 语句：





```shell
mysql> show processlist;
```


反复调用此命令，发现网站 A 的两个 SQL 语句经常在 process list 中出现，其语法如下





```apache
SELECT t1.pid, t2.userid, t3.count, t1.date
FROM _mydata AS t1 
LEFT JOIN _myuser AS t3 ON t1.userid=t3.userid
LEFT JOIN _mydata_body AS t2 ON t1.pid=t3.pid
ORDER BY t1.pid
LIMIT 0,15
```


调用 show columns 检查这三个表的结构 :





```php
mysql> show columns from _myuser;
mysql> show columns from _mydata;
mysql> show columns from _mydata_body;
```



终于发现了问题所在：_mydata 表，只根据 pid 建立了一个 primary key，但并没有为 userid 建立索引。而在这个 SQL 语句的第一个 LEFT JOIN ON 子句中：



```apache
LEFT JOIN _myuser AS t3 ON t1.userid=t3.userid
```


_mydata 的 userid 被参与了条件比较运算。于是我为给 _mydata 表根据字段 userid 建立了一个索引：





```markdown
mysql> ALTER TABLE `_mydata` ADD INDEX ( `userid` )
```


建立此索引之后，CPU 马上降到了 80% 左右。看到找到了问题所在，于是检查另一个反复出现在 show processlist 中的 sql 语句：





```sql
SELECT COUNT(*)
FROM _mydata AS t1, _mydata_key AS t2
WHERE t1.pid=t2.pid and t2.keywords = '孔雀'
```



经检查 _mydata_key 表的结构，发现它只为 pid 建了了 primary key, 没有为 keywords 建立 index。_mydata_key 目前有 33 万条记录，在没有索引的情况下对33万条记录进行文本检索匹配，不耗费大量的 cpu 时间才怪。看来就是针对这个表的检索出问题了。于是同样为 _mydata_key 表根据字段 keywords 加上索引:



```markdown
mysql> ALTER TABLE `_mydata_key` ADD INDEX ( `keywords` )
```


建立此索引之后，CPU立刻降了下来，在 50%~70%之间震荡。
再次调用 show prosslist，网站A 的sql 调用就很少出现在结果列表中了。但发现此主机运行了几个 Discuz 的论坛程序， Discuz 论坛的好几个表也存在着这个问题。于是顺手一并解决，cpu占用再次降下来了(2007.07.09 附注：关于 discuz 论坛的具体优化过程，我后来另写了一篇文章，详见：千万级记录的 Discuz! 论坛导致 MySQL CPU 100% 的 优化笔记http://www.xiaohui.com/dev/server/20070701-discuz-mysql-cpu-100-optimize.htm)。



解决 MYSQL CPU 占用 100% 的经验总结
增加 tmp_table_size 值。mysql 的配置文件中，tmp_table_size 的默认大小是 32M。如果一张临时表超出该大小，MySQL产生一个 The table tbl_name is full 形式的错误，如果你做很多高级 GROUP BY 查询，增加 tmp_table_size 值。 这是 mysql 官方关于此选项的解释：



```sql
tmp_table_size
This variable determines the maximum size for a temporary table in memory. If the table becomes too large, a MYISAM table is created on disk. Try to avoid temporary tables by optimizing the queries where possible, but where this is not possible, try to ensure temporary tables are always stored in memory. Watching the processlist for queries with temporary tables that take too long to resolve can give you an early warning that tmp_table_size needs to be upped. Be aware that memory is also allocated per-thread. An example where upping this worked for more was a server where I upped this from 32MB (the default) to 64MB with immediate effect. The quicker resolution of queries resulted in less threads being active at any one time, with all-round benefits for the server, and available memory.
```


对 WHERE, JOIN, MAX(), MIN(), ORDER BY 等子句中的条件判断中用到的字段,应该根据其建立索引 INDEX。索引被用来快速找出在一个列上用一特定值的行。没有索引，MySQL不得不首先以第一条记录开始并然后读完整个表直到它找出相关的行。表越大，花费时间越多。如果表对于查询的列有一个索引，MySQL能快速到达一个位置去搜寻到数据文件的中间，没有必要考虑所有数据。如果一个表有1000行，这比顺序读取至少快100倍。所有的MySQL索引(PRIMARY、UNIQUE和INDEX)在B树中存储。
根据 mysql 的开发文档，索引 index 用于：

```yaml
1，快速找出匹配一个WHERE子句的行
2，当执行联结(JOIN)时，从其他表检索行。
3，对特定的索引列找出MAX()或MIN()值
4，如果排序或分组在一个可用键的最左面前缀上进行(例如，ORDER BY key_part_1,key_part_2)，排序或分组一个表。如果所有键值部分跟随DESC，键以倒序被读取。
5，在一些情况中，一个查询能被优化来检索值，不用咨询数据文件。如果对某些表的所有使用的列是数字型的并且构成某些键的最左面前缀，为了更快，值可以从索引树被检索出来。
```



假定你发出下列SELECT语句：



```apache
mysql> SELECT * FROM tbl_name WHERE col1=val1 AND col2=val2;
```


如果一个多列索引存在于col1和col2上，适当的行可以直接被取出。如果分开的单行列索引存在于col1和col2上，优化器试图通过决定哪个索引将找到更少的行并来找出更具限制性的索引并且使用该索引取行。