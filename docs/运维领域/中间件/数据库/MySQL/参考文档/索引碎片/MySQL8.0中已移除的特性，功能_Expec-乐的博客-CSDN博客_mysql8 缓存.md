# MySQL8.0中已移除的特性，功能

![img](MySQL8.0中已移除的特性，功能_Expec-乐的博客-CSDN博客_mysql8 缓存.assets/original.png)

[Expect-乐](https://blog.csdn.net/qianglei6077) 2019-01-29 09:48:25 ![img](MySQL8.0中已移除的特性，功能_Expec-乐的博客-CSDN博客_mysql8 缓存.assets/articleReadEyes.png) 1958 ![img](MySQL8.0中已移除的特性，功能_Expec-乐的博客-CSDN博客_mysql8 缓存.assets/tobarCollect.png) 收藏 1

分类专栏： [MySQL 8](https://blog.csdn.net/qianglei6077/category_8641199.html)

版权

## 说明

本文所说的都是已经从MySQL8.0中删除的特性，如果是从低版本升级到8.0的应用，如果使用到了这些特性应该注意避免使用这些特性或找到替代的特性。如：对于MySQL5.7和8.0的主从环境，可能会造成一些问题。

### innodb_locks_unsafe_for_binlog系统变量

```
mysql> show variables like 'innodb_locks_unsafe_for_binlog';
Empty set (0.06 sec)
12
```

READ COMMITTED可以提供相似的功能，而且可以在会话和全局级别使用该特性(支持动态修改)，这些优点都是innodb_locks_unsafe_for_binlog所不具备的

更多信息请查看官方文档：

> https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html#isolevel_read-committed

### information_schema_stats

被information_schema_stats_expiry所代替，如下：

```
mysql> show variables like '%information_schema_stats%';
+----------------------------------------------------+--------+
| Variable_name                   | Value |
+----------------------------------------------------+--------+
| information_schema_stats_expiry    | 86400 |
+-----------------------------------------------------+--------+

1 row in set (0.01 sec)
12345678
```

参数的作用：控制缓存中统计信息过期的时间，默认86400秒(24小时)，可以设置到1年。可以在会话和全局级别设置。

如果想要直接从存储引擎获取统计信息，而不是从缓存中，那么可以将其设置为0。

以下几种情况，不会存储或更新在mysql.index_stats和mysql.table_stats字典表中的查询统计信息：

- 缓存统计信息没有过期
- information_schema_stats_expiry设置为0
- 数据库以read_only, super_read_only, transaction_read_only, 或innodb_read_only模式打开
- 查询是查询Performance Schema中的数据

### InnoDB相关系统表

和InnoDB相关系统表的代码在8.0.3版本中已经被移除，INFORMATION_SCHEMA中的关于InnoDB系统表的相关视图已经被重新命名，如下：

| 旧名字                  | 新名字              |
| ----------------------- | ------------------- |
| INNODB_SYS_COLUMNS      | INNODB_COLUMNS      |
| INNODB_SYS_DATAFILES    | INNODB_DATAFILES    |
| INNODB_SYS_FIELDS       | INNODB_FIELDS       |
| INNODB_SYS_FOREIGN      | INNODB_FOREIGN      |
| INNODB_SYS_FOREIGN_COLS | INNODB_FOREIGN_COLS |
| INNODB_SYS_INDEXES      | INNODB_INDEXES      |
| INNODB_SYS_TABLES       | INNODB_TABLES       |
| INNODB_SYS_TABLESPACES  | INNODB_TABLESPACES  |
| INNODB_SYS_TABLESTATS   | INNODB_TABLESTATS   |
| INNODB_SYS_VIRTUAL      | INNODB_VIRTUAL      |

> 注：如果升级到8.0.3，那么需要更新相关脚本中视图的名称。

### 账户相关特性

下面是关于账户相关的特性也已经被移除，不在支持：

#### GRANT命令创建用户

也就是无法再用GRANT命令来创建用户了，只能通过CREATE USER命令。所以NO_AUTO_CREATE_USER的SQL MODE也被移除了。

语法：

```
GRANT
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    TO user_or_role [, user_or_role] ...
    [WITH GRANT OPTION]
123456
```

如：

- 8.0.3：

```
mysql> grant all privileges on *.* to 'lei'@'%' identified by 'lei' with grant option;

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'identified by 'lei' with grant option' at line 1
123
```

- 5.7版本：

```
mysql> grant all privileges on *.* to 'lei'@'%' identified by 'lei' with grant option;

Query OK, 0 rows affected, 1 warning (0.18 sec)
123
```

#### IDENTIFIED BY PASSWORD ‘hash_string’

CREATE USER和GRANT命令中移除了IDENTIFIED BY PASSWORD 'hash_string’语法，由IDENTIFIED WITH auth_plugin AS 'hash_string’所取代。log_builtin_as_identified_by_password系统变量也就没用了，从而也被移除了。

> 注：在5.7就已经废弃了，在8中移除了。

#### PASSWORD()

移除PASSWORD()函数，也就是无法再用SET PASSWORD=PASSWORD(密码)。

#### old_passwords

在5.7中就已经废弃了，在8.0中被移除。

### 查询缓存

查询缓存也被移除，包括以下几方面：

- FLUSH QUERY CACHE 和RESET QUERY CACHE
- 系统变量：query_cache_limit, query_cache_min_res_unit, query_cache_size, query_cache_type, query_cache_wlock_invalidate
  可通过SHOW VARIABLES LIKE ‘’;命令查看，将来版本移除ndb_cache_check_time，have_query_cache变量已废弃并且值一直是NO，在将来版本中被移除。
- 状态变量：Qcache_free_blocks, Qcache_free_memory, Qcache_hits, Qcache_inserts, Qcache_lowmem_prunes, Qcache_not_cached, Qcache_queries_in_cache, Qcache_total_blocks.
  可通过SHOW GLOBAL STATUS命令查看
- 线程状态：checking privileges on cached query, checking query cache for query, invalidating query cache entries, sending cached result to client, storing result in query cache, Waiting for query cache lock.
- SELECT语句中SQL_CACHE选项被移除，在未来版本将移除SQL_NO_CACHE

### 其他

- 数据字典提供有关数据库对象的信息，因此服务器不再检查数据目录中的目录名以查找数据库。所以 --ignore-db-dir和ignore-db-dir系统变量就没用了，所以被移除了。
- tx_isolation和tx_read_only系统变量被移除，被transaction_isolation和transaction_read_only取代。
- sync_frm系统变量被移除，因为.frm文件已经废弃。
- secure_auth系统变量和客户端的–secure-auth选项被移除。同时mysql_options() C语言的API的MYSQL_SECURE_AUTH选项也被移除。
- multi_range_count系统变量移除
- log_warnings系统变量被移除，被log_error_verbosity代替
- sql_log_bin系统变量被移除
- metadata_locks_cache_size 和metadata_locks_hash_instances系统变量被移除
- 没有使用的date_format, datetime_format, time_format和max_tmp_tables系统变量被移除
- 已删除的SQL模式：DB2, MAXDB, MSSQL, MYSQL323, MYSQL40, ORACLE, POSTGRESQL, NO_FIELD_OPTIONS, NO_KEY_OPTIONS, NO_TABLE_OPTIONS。而且mysqldump中—compatible选项也无法指定。
  移除MAXDB意味着通过CREATE TABLE或ALTER TABLE命令来修改表的字段类型是TIMESTAMP只会作为TIMESTAMP而不会当作DATATIME。
- GROUP BY字句中的ASC或DESC被移除，想要排序需要配合ORDER BY使用
- EXPLAIN语句中的EXTENDED和PARTITIONS关键字被移除。
- 加密相关的函数被移除：
  - ENCODE()和DECODE()函数
  - ENCRYPT()函数
  - DES_ENCRYPT()和DES_DECRYPT()函数，–des-key-file 选项，have_crypt 系统变量，FLUSH语句中DES_KEY_FILE选项和HAVE_CRYPT Cmake选项
    可以使用SHA2()来代替ENCRYPT()，其他可以使用AES_ENCRYPT() 和AES_DECRYPT()来代替。
- 解析器不再将/ N视为SQL语句中NULL的同义词。请改用NULL。
  而对于带有LOAD DATA INFILE 或SELECT … INTO OUTFILE的导出，导入操作依然用/N来表示NULL。
- PROCEDURE ANALYSE()语法被移除
- 客户端–ssl和–ssl-verify-server-cert选项已被删除。 使用–ssl-mode = REQUIRED而不是–ssl = 1或–enable-ssl。 使用–ssl-mode = DISABLED而不是–ssl = 0， - skip-ssl或–disable-ssl。 使用–ssl-mode = VERIFY_IDENTITY而不是–ssl-verify-server-cert选项。 （服务器端–ssl选项保持不变。）
- 服务器命令行选项–temp-pool被移除
- 服务器命令行选项–ignore-builtin-innodb 和ignore_builtin_innodb系统变量被移除
- mysql_install_db安装程序被从MySQL发行版本中移除，而有mysqld的–initialize 或–initialize-insecure代替
- 通用分区处理程序已从MySQL服务器中删除。 为了支持给定表的分区，用于表的存储引擎现在必须提供其自己的（“native”）分区处理程序。 --partition和–skip-partition选项已从MySQL服务器中删除， SHOW PLUGINS命令和INFORMATION_SCHEMA.PLUGINS表中不再显示与分区相关的变量信息。

现在两种存储引擎支持native分区：InooDB和NDB(NDBCLUSTER，NDB集群)。而在8.0版本中，只支持InnoDB。

所以如果从Mysql5.7升级到8.0版本，如果有不是InooDB存储引擎的分区表，那么无法升级。有两种解决办法，再升级：

1. 移除表分区：ALTER TABLE … REMOVE PARTITIONING.
2. 修改分区表的存储引擎：ALTER TABLE … ENGINE=INNODB.

- 系统和状态变量信息不再存储在INFORMATION_SCHEMA中。GLOBAL_VARIABLES, SESSION_VARIABLES, GLOBAL_STATUS, SESSION_STATUS几个表也被移除。而查询相应的PERFORMANCE_SCHEMA中的表：global_status，global_variables, session_status, session_variables。
- 删除了Performance Schema setup_timers表，以及performance_timers表中的TICK行。
- The libmysqld embedded server library has been removed, along with:
  - The mysql_options() MYSQL_OPT_GUESS_CONNECTION, MYSQL_OPT_USE_EMBEDDED_CONNECTION, MYSQL_OPT_USE_REMOTE_CONNECTION, andMYSQL_SET_CLIENT_IP options
  - The mysql_config --libmysqld-libs, --embedded-libs, and --embedded options
  - The CMake WITH_EMBEDDED_SERVER, WITH_EMBEDDED_SHARED_LIBRARY, and INSTALL_SECURE_FILE_PRIV_EMBEDDEDDIR options
  - The (undocumented) mysql --server-arg option
  - The mysqltest --embedded-server, --server-arg, and --server-file options
  - The mysqltest_embedded and mysql_client_test_embedded test programs
- mysql_plugin工具已删除。替代方法包括在打开数据库时使用–plugin-load或–plugin-load-add来加载插件，或者在运行时使用INSTALL PLUGIN语句加载插件。
- 以下错误代码未使用且已被删除：
  ER_BINLOG_READ_EVENT_CHECKSUM_FAILURE
  ER_BINLOG_ROW_RBR_TO_SBR
  ER_BINLOG_ROW_WRONG_TABLE_DEF
  ER_CANT_ACTIVATE_LOG
  ER_CANT_CHANGE_GTID_NEXT_IN_TRANSACTION
  ER_CANT_CREATE_FEDERATED_TABLE
  ER_CANT_CREATE_SROUTINE
  ER_CANT_DELETE_FILE
  ER_CANT_GET_WD
  ER_CANT_SET_GTID_PURGED_WHEN_GTID_MODE_IS_OFF
  ER_CANT_SET_WD
  ER_CANT_WRITE_LOCK_LOG_TABLE
  ER_CREATE_DB_WITH_READ_LOCK
  ER_CYCLIC_REFERENCE
  ER_DB_DROP_DELETE
  ER_DELAYED_NOT_SUPPORTED
  ER_DIFF_GROUPS_PROC
  ER_DISK_FULL
  ER_DROP_DB_WITH_READ_LOCK
  ER_DROP_USER
  ER_DUMP_NOT_IMPLEMENTED
  ER_ERROR_DURING_CHECKPOINT
  ER_ERROR_ON_CLOSE
  ER_EVENTS_DB_ERROR
  ER_EVENT_CANNOT_DELETE
  ER_EVENT_CANT_ALTER
  ER_EVENT_COMPILE_ERROR
  ER_EVENT_DATA_TOO_LONG
  ER_EVENT_DROP_FAILED
  ER_EVENT_MODIFY_QUEUE_ERROR
  ER_EVENT_NEITHER_M_EXPR_NOR_M_AT
  ER_EVENT_OPEN_TABLE_FAILED
  ER_EVENT_STORE_FAILED
  ER_EXEC_STMT_WITH_OPEN_CURSOR
  ER_FAILED_ROUTINE_BREAK_BINLOG
  ER_FLUSH_MASTER_BINLOG_CLOSED
  ER_FORM_NOT_FOUND
  ER_FOUND_GTID_EVENT_WHEN_GTID_MODE_IS_OFF__UNUSED
  ER_FRM_UNKNOWN_TYPE
  ER_GOT_SIGNAL
  ER_GRANT_PLUGIN_USER_EXISTS
  ER_GTID_MODE_REQUIRES_BINLOG
  ER_GTID_NEXT_IS_NOT_IN_GTID_NEXT_LIST
  ER_HASHCHK
  ER_INDEX_REBUILD
  ER_INNODB_NO_FT_USES_PARSER
  ER_LIST_OF_FIELDS_ONLY_IN_HASH_ERROR
  ER_LOAD_DATA_INVALID_COLUMN_UNUSED
  ER_LOGGING_PROHIBIT_CHANGING_OF
  ER_MALFORMED_DEFINER
  ER_MASTER_KEY_ROTATION_ERROR_BY_SE
  ER_NDB_CANT_SWITCH_BINLOG_FORMAT
  ER_NEVER_USED
  ER_NISAMCHK
  ER_NO_CONST_EXPR_IN_RANGE_OR_LIST_ERROR
  ER_NO_FILE_MAPPING
  ER_NO_GROUP_FOR_PROC
  ER_NO_RAID_COMPILED
  ER_NO_SUCH_KEY_VALUE
  ER_NO_SUCH_PARTITION__UNUSED
  ER_OBSOLETE_CANNOT_LOAD_FROM_TABLE
  ER_OBSOLETE_COL_COUNT_DOESNT_MATCH_CORRUPTED
  ER_ORDER_WITH_PROC
  ER_PARTITION_SUBPARTITION_ERROR
  ER_PARTITION_SUBPART_MIX_ERROR
  ER_PART_STATE_ERROR
  ER_PASSWD_LENGTH
  ER_QUERY_ON_MASTER
  ER_RBR_NOT_AVAILABLE
  ER_SKIPPING_LOGGED_TRANSACTION
  ER_SLAVE_CHANNEL_DELETE
  ER_SLAVE_MULTIPLE_CHANNELS_HOST_PORT
  ER_SLAVE_MUST_STOP
  ER_SLAVE_WAS_NOT_RUNNING
  ER_SLAVE_WAS_RUNNING
  ER_SP_GOTO_IN_HNDLR
  ER_SP_PROC_TABLE_CORRUPT
  ER_SQL_MODE_NO_EFFECT
  ER_SR_INVALID_CREATION_CTX
  ER_TABLE_NEEDS_UPG_PART
  ER_TOO_MUCH_AUTO_TIMESTAMP_COLS
  ER_UNEXPECTED_EOF
  ER_UNION_TABLES_IN_DIFFERENT_DIR
  ER_UNSUPPORTED_BY_REPLICATION_THREAD
  ER_UNUSED1
  ER_UNUSED2
  ER_UNUSED3
  ER_UNUSED4
  ER_UNUSED5
  ER_UNUSED6
  ER_VIEW_SELECT_DERIVED_UNUSED
  ER_WRONG_MAGIC
  ER_WSAS_FAILED
- 已弃用的INFORMATION_SCHEMA INNODB_LOCKS和INNODB_LOCK_WAITS表已被删除。请改用Performance_Schema 中data_locks和data_lock_waits表。

> 注：在MySQL 5.7中，INNODB_LOCKS表中的LOCK_TABLE列和sys模式innodb_lock_waits和x $ innodb_lock_waits视图中的locked_table列包含组合的模式/表名称值。 在MySQL 8.0中，data_locks表和sys模式视图包含单独的模式名称和表名称列。

- InnoDB不再支持压缩临时表。当innodb_strict_mode=TRUE（默认值）时，如果指定了ROW_FORMAT = COMPRESSED或KEY_BLOCK_SIZE，则CREATE TEMPORARY TABLE将报错。
- 当在MySQL数据文件目录以外创建表空间数据文件时，那么InnoDB不再创建.isl文件(连接文件)。innodb_directories参数现在支持存储数据文件目录以外的表空间文件目录。
  所以在数据库关闭状态了，无法通过手动修改.isl文件来移动表空间。不过可以通过innodb_directories变量来移动远程的表空间。
- 以下InooDB的文件格式配置选项被移除：
  - innodb_file_format
  - innodb_file_format_check
  - innodb_file_format_max
  - innodb_large_prefix

上面这些文件格式选项都是为了兼容5.1版本的表创建，现在随着mysql5.1版本走到了生命尽头，所以将这些选项去除，表示5.1正式退出了历史舞台。
注：INFORMATION_SCHEMA中INNODB_TABLES 和INNODB_TABLESPACES表中国的FILE_FORMAT列从而也被移除。

- innodb_support_xa系统变量也被移除，该变量支持XA事务中的两阶段提交。但是在8.0版本中，已经默认支持XA事务两阶段提交。
- Dtrace被移除
- JSON_APPEND被移除，由JSON_ARRAY_APPEND()代替。
- 在MySQL 8.0.13中不支持在SET以外的语句中设置用户变量。此功能可能会在MySQL 9.0中被移除。
- perror中的—ndb选项被移除，由ndb_perror代替。

perror和Oracle中的oerr工具一样，来查看错误代码的具体错误详细，如：

```
[root@ka-m ~]# perror 1231
MySQL error code MY-001231 (ER_WRONG_VALUE_FOR_VAR): Variable '%-.64s' can't be set to the value of '%-.200s'
```