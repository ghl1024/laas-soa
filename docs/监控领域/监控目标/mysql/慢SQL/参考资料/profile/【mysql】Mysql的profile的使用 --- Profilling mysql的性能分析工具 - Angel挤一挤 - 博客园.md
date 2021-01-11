分析SQL执行带来的开销是优化SQL的重要手段。

 

在MySQL数据库中，可以通过配置profiling参数来启用SQL剖析。该参数可以在全局和session级别来设置。对于全局级别则作用于整个MySQL实例，而session级别紧影响当前session。

 

该参数开启后，后续执行的SQL语句都将记录其资源开销，诸如IO，上下文切换，CPU，Memory等等。根据这些开销进一步分析当前SQL瓶颈从而进行优化与调整。 【时间单位为 s】

 

[![复制代码](【mysql】Mysql的profile的使用 --- Profilling mysql的性能分析工具 - Angel挤一挤 - 博客园.assets/copycode.gif)](javascript:void(0);)

```
1.有关profile的解释
--当前版本
mysql> show variables like 'version';
+---------------+------------+
| Variable_name | Value      |
+---------------+------------+
| version       | 5.5.29-log |
+---------------+------------+
 
--查看profiling系统变量
mysql> show variables like '%profil%';
+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| profiling              | OFF   |   --开启SQL语句剖析功能。0或OFF表示关闭(默认模式)。1或ON表示开启
| profiling_history_size | 15    |   --设置保留profiling的数目，缺省为15(即使用show profiles;命令展示的默认是最近执行的15条sql的记录)，范围为0至100，为0时将禁用profiling。这个参数在MySQL 5.6.8过期，在后期版本中会被移除。
+------------------------+-------+
 
如果将profiling_history_size参数设置为0，同样具有关闭MySQL的profiling效果。
 
--获取profile的帮助
mysql> help profile;
Name: 'SHOW PROFILE'
Description:
Syntax:
SHOW PROFILE [type [, type] ... ]
    [FOR QUERY n]      --如果不指定，只是显示最近执行的语句；如果指定会显示语句n，n对应query_id的值
    [LIMIT row_count [OFFSET offset]]
  
type:
    ALL                --显示所有的开销信息
  | BLOCK IO           --显示块IO相关开销
  | CONTEXT SWITCHES   --上下文切换相关开销
  | CPU                --显示CPU相关开销信息
  | IPC                --显示发送和接收相关开销信息
  | MEMORY             --显示内存相关开销信息
  | PAGE FAULTS        --显示页面错误相关开销信息
  | SOURCE             --显示和Source_function，Source_file，Source_line相关的开销信息
  | SWAPS              --显示交换次数相关开销的信息
 
Profiling由会话级别参数profiling控制。缺省是显示状态和持续时间。
上面描述从5.6.7开始该命令将会被移除，用Performance Schema instead代替
 
2、开启porfiling
 
--启用session级别的profiling
mysql> set profiling=1;
Query OK, 0 rows affected, 1 warning (0.00 sec)
  
--验证修改后的结果
mysql> show variables like '%profil%';
+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| profiling              | ON    |
| profiling_history_size | 15    |
+------------------------+-------+
  
--执行SQL查询
mysql> show databases;
mysql> show tables;
mysql> select count(*) from emp
  
--查看当前session所有已产生的profile【注意，要显示Query_ID 和 Query列，需要使用的命令是 show profiles;】
mysql> show profiles;
+----------+------------+-------------------------------------------------------+
| Query_ID | Duration   | Query                                                                                                                                                                                                                                                                                                        |
--------------------------------------------------------------------------------+
|        1 | 0.00037700 | show variables like '%profil%'                                                                                                                                                                                                                                                                               |
|        2 | 0.00029500 | show databases                                                                                                                                                                                                                                                                                               |
|        3 | 0.00030800 | show tables                                                                                                                                                                                                                                                                                                  |
|        4 | 0.00135700 | select count(*) from emp
+----------+------------+-------------------------------------------------------+
 
3、获取SQL语句的开销信息
  
--可以直接使用show profile来查看上一条SQL语句的开销信息
--注，show profile之类的语句不会被profiling，即自身不会产生Profiling
mysql> show profile;
+--------------------+----------+
| Status             | Duration |
+--------------------+----------+
| starting           | 0.000997 |
| Opening tables     | 0.000015 |
| System lock        | 0.000003 |
| Table lock         | 0.000515 |
| optimizing         | 0.000093 |
| statistics         | 0.151343 |
| preparing          | 0.000082 |
| executing          | 0.000027 |
| Sending data       | 0.081436 |
| init               | 0.000024 |
| optimizing         | 0.000006 |
| statistics         | 0.000006 |
| preparing          | 0.000007 |
| executing          | 0.000005 |
| Sending data       | 0.000046 |
| end                | 0.000004 |
| query end          | 0.000003 |
| freeing items      | 0.000076 |
| removing tmp table | 0.000006 |
| closing tables     | 0.000004 |
| logging slow query | 0.000002 |
| cleaning up        | 0.000004 |
+--------------------+----------+
 
--显示所有性能信息【这里的9  就是使用上面的 show profiles;命令获取到的 自己想要查看的哪个 sql语句的 Query_ID】
mysql> show profile all for query 9;
+--------------------+----------+----------+------------+-------------------+---------------------+--------------+---------------+---------------+-------------------+-------------------+-------------------+-------+------------------+---------------+-------------+
| Status             | Duration | CPU_user | CPU_system | Context_voluntary | Context_involuntary | Block_ops_in | Block_ops_out | Messages_sent | Messages_received | Page_faults_major | Page_faults_minor | Swaps | Source_function  | Source_file   | Source_line |
+--------------------+----------+----------+------------+-------------------+---------------------+--------------+---------------+---------------+-------------------+-------------------+-------------------+-------+------------------+---------------+-------------+
| starting           | 0.000997 | 0.000000 |   0.000000 |                 0 |                   1 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | NULL             | NULL          |        NULL |
| Opening tables     | 0.000015 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_base.cc   |        4622 |
| System lock        | 0.000003 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | lock.cc       |         260 |
| Table lock         | 0.000515 | 0.001000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | lock.cc       |         271 |
| optimizing         | 0.000093 | 0.000000 |   0.000000 |                 0 |                   1 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |         835 |
| statistics         | 0.151343 | 0.124981 |   0.023996 |                 1 |                 155 |            0 |             0 |             0 |                 0 |                 0 |                39 |     0 | unknown function | sql_select.cc |        1026 |
| preparing          | 0.000082 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        1048 |
| executing          | 0.000027 | 0.000000 |   0.000000 |                 0 |                   1 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        1789 |
| Sending data       | 0.081436 | 0.072989 |   0.006999 |                 0 |                  82 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        2347 |
| init               | 0.000024 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        2537 |
| optimizing         | 0.000006 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |         835 |
| statistics         | 0.000006 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        1026 |
| preparing          | 0.000007 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        1048 |
| executing          | 0.000005 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        1789 |
| Sending data       | 0.000046 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        2347 |
| end                | 0.000004 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |        2583 |
| query end          | 0.000003 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_parse.cc  |        5123 |
| freeing items      | 0.000076 | 0.001000 |   0.000000 |                 1 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_parse.cc  |        6147 |
| removing tmp table | 0.000006 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |       10929 |
| closing tables     | 0.000004 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_select.cc |       10954 |
| logging slow query | 0.000002 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_parse.cc  |        1735 |
| cleaning up        | 0.000004 | 0.000000 |   0.000000 |                 0 |                   0 |            0 |             0 |             0 |                 0 |                 0 |                 0 |     0 | unknown function | sql_parse.cc  |        1703 |
+--------------------+----------+----------+------------+-------------------+---------------------+--------------+---------------+---------------+-------------------+-------------------+-------------------+-------+------------------+---------------+-------------+
 
--获取指定查询的开销
mysql> show profile for query 9;
+--------------------+----------+
| Status             | Duration |
+--------------------+----------+
| starting           | 0.000997 |
| Opening tables     | 0.000015 |
| System lock        | 0.000003 |
| Table lock         | 0.000515 |
| optimizing         | 0.000093 |
| statistics         | 0.151343 |
| preparing          | 0.000082 |
| executing          | 0.000027 |
| Sending data       | 0.081436 |
| init               | 0.000024 |
| optimizing         | 0.000006 |
| statistics         | 0.000006 |
| preparing          | 0.000007 |
| executing          | 0.000005 |
| Sending data       | 0.000046 |
| end                | 0.000004 |
| query end          | 0.000003 |
| freeing items      | 0.000076 |
| removing tmp table | 0.000006 |
| closing tables     | 0.000004 |
| logging slow query | 0.000002 |
| cleaning up        | 0.000004 |
+--------------------+----------+
 
mysql> show profile for query 9 limit 3;
+----------------+----------+
| Status         | Duration |
+----------------+----------+
| starting       | 0.000997 |
| Opening tables | 0.000015 |
| System lock    | 0.000003 |
+----------------+----------+
 
mysql> show profile for query 9 limit 3 offset 5;
+------------+----------+
| Status     | Duration |
+------------+----------+
| statistics | 0.151343 |
| preparing  | 0.000082 |
| executing  | 0.000027 |
+------------+----------+
 
--查看特定部分的开销，如下为CPU部分的开销
mysql> show profile cpu for query  9;
+--------------------+----------+----------+------------+
| Status             | Duration | CPU_user | CPU_system |
+--------------------+----------+----------+------------+
| starting           | 0.000997 | 0.000000 |   0.000000 |
| Opening tables     | 0.000015 | 0.000000 |   0.000000 |
| System lock        | 0.000003 | 0.000000 |   0.000000 |
| Table lock         | 0.000515 | 0.001000 |   0.000000 |
| optimizing         | 0.000093 | 0.000000 |   0.000000 |
| statistics         | 0.151343 | 0.124981 |   0.023996 |
| preparing          | 0.000082 | 0.000000 |   0.000000 |
| executing          | 0.000027 | 0.000000 |   0.000000 |
| Sending data       | 0.081436 | 0.072989 |   0.006999 |
| init               | 0.000024 | 0.000000 |   0.000000 |
| optimizing         | 0.000006 | 0.000000 |   0.000000 |
| statistics         | 0.000006 | 0.000000 |   0.000000 |
| preparing          | 0.000007 | 0.000000 |   0.000000 |
| executing          | 0.000005 | 0.000000 |   0.000000 |
| Sending data       | 0.000046 | 0.000000 |   0.000000 |
| end                | 0.000004 | 0.000000 |   0.000000 |
| query end          | 0.000003 | 0.000000 |   0.000000 |
| freeing items      | 0.000076 | 0.001000 |   0.000000 |
| removing tmp table | 0.000006 | 0.000000 |   0.000000 |
| closing tables     | 0.000004 | 0.000000 |   0.000000 |
| logging slow query | 0.000002 | 0.000000 |   0.000000 |
| cleaning up        | 0.000004 | 0.000000 |   0.000000 |
+--------------------+----------+----------+------------+
 
 
--如下为MEMORY部分的开销
mysql> show profile memory for query 9 ;
+--------------------+----------+
| Status             | Duration |
+--------------------+----------+
| starting           | 0.000997 |
| Opening tables     | 0.000015 |
| System lock        | 0.000003 |
| Table lock         | 0.000515 |
| optimizing         | 0.000093 |
| statistics         | 0.151343 |
| preparing          | 0.000082 |
| executing          | 0.000027 |
| Sending data       | 0.081436 |
| init               | 0.000024 |
| optimizing         | 0.000006 |
| statistics         | 0.000006 |
| preparing          | 0.000007 |
| executing          | 0.000005 |
| Sending data       | 0.000046 |
| end                | 0.000004 |
| query end          | 0.000003 |
| freeing items      | 0.000076 |
| removing tmp table | 0.000006 |
| closing tables     | 0.000004 |
| logging slow query | 0.000002 |
| cleaning up        | 0.000004 |
+--------------------+----------+
  
--同时查看不同资源开销
mysql> show profile block io,cpu for query 9;
+--------------------+----------+----------+------------+--------------+---------------+
| Status             | Duration | CPU_user | CPU_system | Block_ops_in | Block_ops_out |
+--------------------+----------+----------+------------+--------------+---------------+
| starting           | 0.000997 | 0.000000 |   0.000000 |            0 |             0 |
| Opening tables     | 0.000015 | 0.000000 |   0.000000 |            0 |             0 |
| System lock        | 0.000003 | 0.000000 |   0.000000 |            0 |             0 |
| Table lock         | 0.000515 | 0.001000 |   0.000000 |            0 |             0 |
| optimizing         | 0.000093 | 0.000000 |   0.000000 |            0 |             0 |
| statistics         | 0.151343 | 0.124981 |   0.023996 |            0 |             0 |
| preparing          | 0.000082 | 0.000000 |   0.000000 |            0 |             0 |
| executing          | 0.000027 | 0.000000 |   0.000000 |            0 |             0 |
| Sending data       | 0.081436 | 0.072989 |   0.006999 |            0 |             0 |
| init               | 0.000024 | 0.000000 |   0.000000 |            0 |             0 |
| optimizing         | 0.000006 | 0.000000 |   0.000000 |            0 |             0 |
| statistics         | 0.000006 | 0.000000 |   0.000000 |            0 |             0 |
| preparing          | 0.000007 | 0.000000 |   0.000000 |            0 |             0 |
| executing          | 0.000005 | 0.000000 |   0.000000 |            0 |             0 |
| Sending data       | 0.000046 | 0.000000 |   0.000000 |            0 |             0 |
| end                | 0.000004 | 0.000000 |   0.000000 |            0 |             0 |
| query end          | 0.000003 | 0.000000 |   0.000000 |            0 |             0 |
| freeing items      | 0.000076 | 0.001000 |   0.000000 |            0 |             0 |
| removing tmp table | 0.000006 | 0.000000 |   0.000000 |            0 |             0 |
| closing tables     | 0.000004 | 0.000000 |   0.000000 |            0 |             0 |
| logging slow query | 0.000002 | 0.000000 |   0.000000 |            0 |             0 |
| cleaning up        | 0.000004 | 0.000000 |   0.000000 |            0 |             0 |
+--------------------+----------+----------+------------+--------------+---------------+
 
--显示swap的次数。
mysql> show profile swaps for query 9;
+--------------------+----------+-------+
| Status             | Duration | Swaps |
+--------------------+----------+-------+
| starting           | 0.000997 |     0 |
| Opening tables     | 0.000015 |     0 |
| System lock        | 0.000003 |     0 |
| Table lock         | 0.000515 |     0 |
| optimizing         | 0.000093 |     0 |
| statistics         | 0.151343 |     0 |
| preparing          | 0.000082 |     0 |
| executing          | 0.000027 |     0 |
| Sending data       | 0.081436 |     0 |
| init               | 0.000024 |     0 |
| optimizing         | 0.000006 |     0 |
| statistics         | 0.000006 |     0 |
| preparing          | 0.000007 |     0 |
| executing          | 0.000005 |     0 |
| Sending data       | 0.000046 |     0 |
| end                | 0.000004 |     0 |
| query end          | 0.000003 |     0 |
| freeing items      | 0.000076 |     0 |
| removing tmp table | 0.000006 |     0 |
| closing tables     | 0.000004 |     0 |
| logging slow query | 0.000002 |     0 |
| cleaning up        | 0.000004 |     0 |
+--------------------+----------+-------+
 
--下面的SQL语句用于查询query_id为9的SQL开销，且按最大耗用时间倒序排列
mysql> set @query_id=9;
  
mysql> SELECT STATE,
    ->        SUM(DURATION) AS Total_R,
    ->        ROUND(100 * SUM(DURATION) /
    ->              (SELECT SUM(DURATION)
    ->                 FROM INFORMATION_SCHEMA.PROFILING
    ->                WHERE QUERY_ID = @query_id),
    ->              2) AS Pct_R,
    ->        COUNT(*) AS Calls,
    ->        SUM(DURATION) / COUNT(*) AS "R/Call"
    ->   FROM INFORMATION_SCHEMA.PROFILING
    ->  WHERE QUERY_ID = @query_id
    ->  GROUP BY STATE
    ->  ORDER BY Total_R DESC;
+--------------------+----------+-------+-------+--------------+
| STATE              | Total_R  | Pct_R | Calls | R/Call       |
+--------------------+----------+-------+-------+--------------+
| statistics         | 0.151349 | 64.49 |     2 | 0.0756745000 |--最大耗用时间部分为statistics
| Sending data       | 0.081482 | 34.72 |     2 | 0.0407410000 |
| starting           | 0.000997 |  0.42 |     1 | 0.0009970000 |
| Table lock         | 0.000515 |  0.22 |     1 | 0.0005150000 |
| optimizing         | 0.000099 |  0.04 |     2 | 0.0000495000 |
| preparing          | 0.000089 |  0.04 |     2 | 0.0000445000 |
| freeing items      | 0.000076 |  0.03 |     1 | 0.0000760000 |
| executing          | 0.000032 |  0.01 |     2 | 0.0000160000 |
| init               | 0.000024 |  0.01 |     1 | 0.0000240000 |
| Opening tables     | 0.000015 |  0.01 |     1 | 0.0000150000 |
| removing tmp table | 0.000006 |  0.00 |     1 | 0.0000060000 |
| cleaning up        | 0.000004 |  0.00 |     1 | 0.0000040000 |
| end                | 0.000004 |  0.00 |     1 | 0.0000040000 |
| closing tables     | 0.000004 |  0.00 |     1 | 0.0000040000 |
| query end          | 0.000003 |  0.00 |     1 | 0.0000030000 |
| System lock        | 0.000003 |  0.00 |     1 | 0.0000030000 |
| logging slow query | 0.000002 |  0.00 |     1 | 0.0000020000 |
+--------------------+----------+-------+-------+--------------+
  
--开启profiling后，我们可以通过show profile等方式查看，其实质是这些开销信息被记录到information_schema.profiling表
--如下面的查询，部分信息省略
mysql> select * from profiling limit 3,3\G;
*************************** 1. row ***************************
           QUERY_ID: 2
                SEQ: 4
              STATE: Table lock
           DURATION: 0.000007
           CPU_USER: 0.000000
         CPU_SYSTEM: 0.000000
  CONTEXT_VOLUNTARY: 0
CONTEXT_INVOLUNTARY: 0
       BLOCK_OPS_IN: 0
      BLOCK_OPS_OUT: 0
      MESSAGES_SENT: 0
  MESSAGES_RECEIVED: 0
  PAGE_FAULTS_MAJOR: 0
  PAGE_FAULTS_MINOR: 0
              SWAPS: 0
    SOURCE_FUNCTION: unknown function
        SOURCE_FILE: lock.cc
        SOURCE_LINE: 271
*************************** 2. row ***************************
           QUERY_ID: 2
                SEQ: 5
              STATE: init
           DURATION: 0.000010
           CPU_USER: 0.000000
         CPU_SYSTEM: 0.000000
  CONTEXT_VOLUNTARY: 0
CONTEXT_INVOLUNTARY: 0
       BLOCK_OPS_IN: 0
      BLOCK_OPS_OUT: 0
      MESSAGES_SENT: 0
  MESSAGES_RECEIVED: 0
  PAGE_FAULTS_MAJOR: 0
  PAGE_FAULTS_MINOR: 0
              SWAPS: 0
    SOURCE_FUNCTION: unknown function
        SOURCE_FILE: sql_select.cc
        SOURCE_LINE: 2537
*************************** 3. row ***************************
           QUERY_ID: 2
                SEQ: 6
              STATE: optimizing
           DURATION: 0.000003
           CPU_USER: 0.000000
         CPU_SYSTEM: 0.000000
  CONTEXT_VOLUNTARY: 0
CONTEXT_INVOLUNTARY: 0
       BLOCK_OPS_IN: 0
      BLOCK_OPS_OUT: 0
      MESSAGES_SENT: 0
  MESSAGES_RECEIVED: 0
  PAGE_FAULTS_MAJOR: 0
  PAGE_FAULTS_MINOR: 0
              SWAPS: 0
    SOURCE_FUNCTION: unknown function
        SOURCE_FILE: sql_select.cc
        SOURCE_LINE: 835
3 rows in set (0.00 sec)
 
ERROR:
No query specified
 
mysql>
  
--停止profile,可以设置profiling参数，或者在session退出之后,profiling会被自动关闭
mysql> set profiling=off;
Query OK, 0 rows affected, 1 warning (0.00 sec)
```