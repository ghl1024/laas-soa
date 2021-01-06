# MySql8.0 打开慢查询日志的方法

![img](MySql8.0 打开慢查询日志的方法_走错路的程序员-CSDN博客_mysql8 慢查询.assets/original.png)

[走错路的程序员](https://blog.csdn.net/phker) 2018-10-18 14:54:55 ![img](MySql8.0 打开慢查询日志的方法_走错路的程序员-CSDN博客_mysql8 慢查询.assets/articleReadEyes.png) 5499 ![img](MySql8.0 打开慢查询日志的方法_走错路的程序员-CSDN博客_mysql8 慢查询.assets/tobarCollect.png) 收藏 1

版权

不知何时起,mysql的慢查询日志打开方式. 无需到服务器上重启服务器进行配置.
只需要在查询分析器里面执行命令就可以了
windows 系统下一定要给文件夹分配权限.
注意双斜杠, 代表一个斜杠,

好像还可以把日志写入一个表中,然后直接远程查询就可以了.
下面就是可以把慢查询的sql 日志写入一个表的使用方法

```sql
Show variables like '%slow_query%'; -- 可以用这个查询所有的变量

//第一步
set global log_output='TABLE'; -- 开启慢日志,纪录到 mysql.slow_log 表
set global long_query_time=2; -- 设置超过2秒的查询为慢查询
set global slow_query_log='ON';-- 打开慢日志记录

//第二步 运行一下比较慢的功能,执行下面的语句
select convert(sql_text using utf8) sql_text from mysql.slow_log -- 查询慢sql的 日志
//第三步 记得关上日志
set global slow_query_log='OFF'; -- 如果不用了记得关上日志
123456789101112
```

下面是清除日志的方法，实际上就是删掉老表重新建一个新的

```sql
SET GLOBAL slow_query_log = 'OFF';

ALTER TABLE mysql.slow_log RENAME mysql.slow_log_drop;


 CREATE TABLE `mysql`.`slow_log` (
  `start_time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `user_host` mediumtext NOT NULL,
  `query_time` time(6) NOT NULL,
  `lock_time` time(6) NOT NULL,
  `rows_sent` int(11) NOT NULL,
  `rows_examined` int(11) NOT NULL,
  `db` varchar(512) NOT NULL,
  `last_insert_id` int(11) NOT NULL,
  `insert_id` int(11) NOT NULL,
  `server_id` int(10) unsigned NOT NULL,
  `sql_text` mediumblob NOT NULL,
  `thread_id` bigint(21) unsigned NOT NULL
) ENGINE=CSV DEFAULT CHARSET=utf8 COMMENT='Slow log';


 

SET GLOBAL slow_query_log = 'ON';

DROP TABLE mysql.slow_log_drop; 
```