# [Mysql Explain详解](https://www.cnblogs.com/yuanfy008/p/12110997.html)



**阅读目录**

- [一、背景](https://www.cnblogs.com/yuanfy008/p/12110997.html#_label0)
- [二、语法](https://www.cnblogs.com/yuanfy008/p/12110997.html#_label1)
- [三、explain 输出列详解](https://www.cnblogs.com/yuanfy008/p/12110997.html#_label2)
- [四、参考文献　　](https://www.cnblogs.com/yuanfy008/p/12110997.html#_label3)

[回到顶部](https://www.cnblogs.com/yuanfy008/p/12110997.html#_labelTop)

# 一、背景

在日常工作中，可能会收到一些超时或慢响应的告警，最根到底可能是因为一些执行时间比较的SQL语句，这就跟我们平时开发需要注意细节相关了。那么找到这些SQL语句怎么优化呢？到底是哪里的问题导致SQL执行时间长呢？ 这个时候Explain命令尤其重要，它可以查看该SQL语句有没有使用上索引、使用了哪个索引、有没有做全表扫描、有没有使用临时表等等。下面都是基于mysql 8进行案例说明的。

 

[回到顶部](https://www.cnblogs.com/yuanfy008/p/12110997.html#_labelTop)

# 二、语法

EXPLAIN语句提供有关MySQL如何执行语句的信息。 EXPLAIN 通常与SELECT，DELETE，INSERT，REPLACE和UPDATE语句一起使用。

例如：explain select * from tb_student;

 

[回到顶部](https://www.cnblogs.com/yuanfy008/p/12110997.html#_labelTop)

# 三、explain 输出列详解

| Column                                                       | JSON Name     | Meaning                                        |
| ------------------------------------------------------------ | ------------- | ---------------------------------------------- |
| [id](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_id) | select_id     | The SELECT identifier                          |
| [select_type](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_select_type) | None          | The SELECT type                                |
| [table](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_table) | table_name    | The table for the output row                   |
| [partitions](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_partitions) | partitions    | The matching partitions                        |
| [type](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_type) | access_type   | The join type                                  |
| [possible_keys](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_possible_keys) | possible_keys | The possible indexes to choose                 |
| [key](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_key) | key           | The index actually chosen                      |
| [key_len](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_key_len) | key_length    | The length of the chosen key                   |
| [ref](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_ref) | ref           | The columns compared to the index              |
| [rows](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_rows) | rows          | Estimate of rows to be examined                |
| [filtered](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_filtered) | filtered      | Percentage of rows filtered by table condition |
| [Extra](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_extra) | None          | Additional information                         |

example:

```
+``----+-------------+-------+------------+-------+---------------+--------+---------+------+------+----------+-------------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key` `| key_len | ref | ``rows` `| filtered | Extra |``+``----+-------------+-------+------------+-------+---------------+--------+---------+------+------+----------+-------------+``| 1 | SIMPLE | t | ``NULL` `| ``index` `| ``NULL` `| idx_id | 5 | ``NULL` `| 1 | 100.00 | Using ``index` `|``+``----+-------------+-------+------------+-------+---------------+--------+---------+------+------+----------+-------------+
```

1. id

   ：select标志符，有几个 select 就有几个id，并且id的顺序是按 select 出现的顺序增长的。MySQL将 select 查询分为简单查询和复杂查询。复杂查询可以如下：

   `mysql> explain ``select` `(``select` `1 ``from` `t limit 1) ``from` `t1;``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key`   `| key_len | ref | ``rows` `| filtered | Extra    |``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``| 1 | ``PRIMARY`   `| t1  | ``NULL`    `| ``index` `| ``NULL`     `| ``PRIMARY` `| 4    | ``NULL` `|  1 |  100.00 | Using ``index` `|``| 2 | SUBQUERY  | t   | ``NULL`    `| ``index` `| ``NULL`     `| idx_id | 5    | ``NULL` `|  1 |  100.00 | Using ``index` `|``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+`

1. **select_type**

select_type 表示对应行是是简单还是复杂的查询。总共有12种类型，挑其中几种描述下：

- - simple：简单查询。查询不包含子查询和union

    `mysql> explain ``select` `* ``from` `t;``+``----+-------------+-------+------------+-------+---------------+--------+---------+------+------+----------+-------------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key`  `| key_len | ref | ``rows` `| filtered | Extra    |``+``----+-------------+-------+------------+-------+---------------+--------+---------+------+------+----------+-------------+``| 1 | SIMPLE   | t   | ``NULL`    `| ``index` `| ``NULL`     `| idx_id | 5    | ``NULL` `|  1 |  100.00 | Using ``index` `|``+``----+-------------+-------+------------+-------+---------------+--------+---------+------+------+----------+-------------+`

- - primary：复杂查询中最外层的 select。如上面一个复杂查询
  - union：在 union 中的第二个或随后的 select

```
mysql> explain ``select` `id ``from` `t1 ``union` `select` `id ``from` `t2;``+``----+--------------+------------+------------+-------+---------------+---------+---------+------+------+----------+-----------------+``| id | select_type | ``table`   `| partitions | type | possible_keys | ``key`   `| key_len | ref | ``rows` `| filtered | Extra      |``+``----+--------------+------------+------------+-------+---------------+---------+---------+------+------+----------+-----------------+``| 1 | ``PRIMARY`   `| t1     | ``NULL`    `| ``index` `| ``NULL`     `| ``PRIMARY` `| 4    | ``NULL` `|  1 |  100.00 | Using ``index`   `|``| 2 | ``UNION`    `| t2     | ``NULL`    `| ``index` `| ``NULL`     `| ``PRIMARY` `| 4    | ``NULL` `|  2 |  100.00 | Using ``index`   `|``| ``NULL` `| ``UNION` `RESULT | <union1,2> | ``NULL`    `| ``ALL`  `| ``NULL`     `| ``NULL`  `| ``NULL`  `| ``NULL` `| ``NULL` `|   ``NULL` `| Using ``temporary` `|``+``----+--------------+------------+------------+-------+---------------+---------+---------+------+------+----------+-----------------+
```

- - DEPENDENT UNION UNION中的第二个或后面的SELECT语句，取决于外面的查询

    `mysql> explain ``select` `* ``from` `t ``where` `id ``in` `(``select` `t1.id ``from` `t1 ``union` `select` `id ``from` `t2 );``+``----+--------------------+------------+------------+--------+---------------+---------+---------+------+------+----------+--------------------------+``| id | select_type    | ``table`   `| partitions | type  | possible_keys | ``key`   `| key_len | ref | ``rows` `| filtered | Extra          |``+``----+--------------------+------------+------------+--------+---------------+---------+---------+------+------+----------+--------------------------+``| 1 | ``PRIMARY`      `| t     | ``NULL`    `| ``index` `| ``NULL`     `| idx_id | 5    | ``NULL` `|  1 |  100.00 | Using ``where``; Using ``index` `|``| 2 | DEPENDENT SUBQUERY | t1     | ``NULL`    `| eq_ref | ``PRIMARY`    `| ``PRIMARY` `| 4    | func |  1 |  100.00 | Using ``index`       `|``| 3 | DEPENDENT ``UNION`  `| t2     | ``NULL`    `| eq_ref | ``PRIMARY`    `| ``PRIMARY` `| 4    | func |  1 |  100.00 | Using ``index`       `|``| ``NULL` `| ``UNION` `RESULT    | <union2,3> | ``NULL`    `| ``ALL`  `| ``NULL`     `| ``NULL`  `| ``NULL`  `| ``NULL` `| ``NULL` `|   ``NULL` `| Using ``temporary`     `|``+``----+--------------------+------------+------------+--------+---------------+---------+---------+------+------+----------+--------------------------+`

- - UNION RESULT union的结果，如上。

1. **table**

显示这一行的数据是关于哪张表的, 有时不是真实的表名字,看到的是derivedN(N是个数字)

1. **partitions**

查询将匹配记录的分区。 对于非分区表，该值为NULL

1. **type**

这列很重要，显示了连接使用了哪种类别，有无使用索引。从最好到最差的连接类型为system、const、eq_ref、ref、fulltext、ref_or_null、index_merge、unique_subquery、index_subquery、range、index和ALL

- **system** 该表只有一行（=系统表）。 这是const join类型的特例

- const

   

  该表最多具有一个匹配行，该行在查询开始时读取。 因为只有一行，所以优化器的其余部分可以将这一行中列的值视为常量。 const表非常快，因为它们只能读取一次。当将PRIMARY KEY或UNIQUE索引的所有部分与常量值进行比较时，将使用const。形如：

  `SELECT` `* ``FROM` `tbl_name ``WHERE` `primary_key=1;` `SELECT` `* ``FROM` `tbl_name`` ``WHERE` `primary_key_part1=1 ``AND` `primary_key_part2=2;`

  example:　　

  `mysql> explain ``select` `* ``from` `t1 ``where` `id = 1;``+``----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key`   `| key_len | ref  | ``rows` `| filtered | Extra |``+``----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------+``| 1 | SIMPLE   | t1  | ``NULL`    `| const | ``PRIMARY`    `| ``PRIMARY` `| 4    | const |  1 |  100.00 | ``NULL` `|``+``----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------+`

- **eq_ref**

对于先前表中的每行组合，从此表中读取一行。 除了system和const类型，这是可能的最佳联接类型。 当连接使用索引的所有部分并且索引是PRIMARY KEY或UNIQUE NOT NULL索引时，将使用它。

eq_ref可用于使用=运算符进行比较的索引列。 比较值可以是常量，也可以是使用在此表之前读取的表中列的表达式。 在以下示例中，MySQL可以使用eq_ref连接来处理ref_table：

```
SELECT` `* ``FROM` `ref_table,other_table`` ``WHERE` `ref_table.key_column=other_table.``column``;` `SELECT` `* ``FROM` `ref_table,other_table`` ``WHERE` `ref_table.key_column_part1=other_table.``column`` ``AND` `ref_table.key_column_part2=1;
```

example:

```
mysql> explain ``select` `* ``from` `t1, t2 ``where` `t1.id = t2.id;``+``----+-------------+-------+------------+--------+---------------+---------+---------+---------------+------+----------+-------+``| id | select_type | ``table` `| partitions | type  | possible_keys | ``key`   `| key_len | ref      | ``rows` `| filtered | Extra |``+``----+-------------+-------+------------+--------+---------------+---------+---------+---------------+------+----------+-------+``| 1 | SIMPLE   | t1  | ``NULL`    `| ``ALL`  `| ``PRIMARY`    `| ``NULL`  `| ``NULL`  `| ``NULL`     `|  1 |  100.00 | ``NULL` `|``| 1 | SIMPLE   | t2  | ``NULL`    `| eq_ref | ``PRIMARY`    `| ``PRIMARY` `| 4    | test_db.t1.id |  1 |  100.00 | ``NULL` `|``+``----+-------------+-------+------------+--------+---------------+---------+---------+---------------+------+----------+-------+
```

- **ref**

对于先前表中的每个行组合，将从该表中读取具有匹配索引值的所有行。 如果联接仅使用键的最左前缀，或者如果键不是PRIMARY KEY或UNIQUE索引（换句话说，如果联接无法基于键值选择单个行），则使用ref。 如果使用的键仅匹配几行，则这是一种很好的联接类型。

ref可以用于使用=或<=>运算符进行比较的索引列。 在以下示例中，MySQL可以使用ref联接来处理ref_table：

```
SELECT` `* ``FROM` `ref_table ``WHERE` `key_column=expr;` `SELECT` `* ``FROM` `ref_table,other_table`` ``WHERE` `ref_table.key_column=other_table.``column``;` `SELECT` `* ``FROM` `ref_table,other_table`` ``WHERE` `ref_table.key_column_part1=other_table.``column`` ``AND` `ref_table.key_column_part2=1;
```

example:

```
mysql> explain ``select` `* ``from` `t ``where` `id = 1;``+``----+-------------+-------+------------+------+---------------+--------+---------+-------+------+----------+-------------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key`  `| key_len | ref  | ``rows` `| filtered | Extra    |``+``----+-------------+-------+------------+------+---------------+--------+---------+-------+------+----------+-------------+``| 1 | SIMPLE   | t   | ``NULL`    `| ref | idx_id    | idx_id | 5    | const |  1 |  100.00 | Using ``index` `|``+``----+-------------+-------+------------+------+---------------+--------+---------+-------+------+----------+-------------+
```

- **fulltext** 使用FULLTEXT索引执行连接。
- **ref_or_null**

该连接类型类似于ref，但是MySQL额外搜索包含NULL值的行。 此联接类型优化最常用于解析子查询。 在以下示例中，MySQL可以使用ref_or_null连接来处理ref_table：

```
SELECT` `* ``FROM` `ref_table ``WHERE` `key_column=expr ``OR` `key_column ``IS` `NULL``;
```

- index_merge

此联接类型指示使用索引合并优化。 在这种情况下，输出行中的键列包含使用的索引列表，而key_len包含使用的索引的最长键部分的列表。

```
SELECT` `* ``FROM` `tbl_name ``WHERE` `key1 = 10 ``OR` `key2 = 20;
```

- unique_subquery

此类型将eq_ref替换为以下形式的某些IN子查询, 形如

```
value ``IN` `(``SELECT` `primary_key ``FROM` `single_table ``WHERE` `some_expr)
```

- index_subquery

此连接类型类似于unique_subquery。 它代替了IN子查询，但适用于以下形式的子查询中的非唯一索引，形如：

```
value ``IN` `(``SELECT` `key_column ``FROM` `single_table ``WHERE` `some_expr)
```

- range

使用该索引选择行，仅检索给定范围内的行。 输出行中的键列指示使用哪个索引。 key_len包含使用的最长的键部分。 此类型的ref列为NULL。

使用=，<>，>，> =，<，<=，IS NULL，<=>，BETWEEN，LIKE或IN（）运算符将键列与常量进行比较时，可以使用range.

```
mysql> explain ``select` `* ``from` `t1 ``where` `t1.id > 1;``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key`   `| key_len | ref | ``rows` `| filtered | Extra    |``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``| 1 | SIMPLE   | t1  | ``NULL`    `| range | ``PRIMARY`    `| ``PRIMARY` `| 4    | ``NULL` `|  1 |  100.00 | Using ``where` `|``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``1 row ``in` `set``, 1 warning (0.01 sec)
```

- index

该索引连接类型与ALL相同，除了扫描索引树外。 这发生两种方式：

如果索引是查询的覆盖索引，并且可用于满足表中所需的所有数据，则仅扫描索引树。 在这种情况下，“额外”列显示“使用索引”。 仅索引扫描通常比ALL更快，因为索引的大小通常小于表数据。

使用对索引的读取执行全表扫描，以按索引顺序查找数据行。 

```
mysql> explain ``select` `id ``from` `t1;``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``| id | select_type | ``table` `| partitions | type | possible_keys | ``key`   `| key_len | ref | ``rows` `| filtered | Extra    |``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+``| 1 | SIMPLE   | t1  | ``NULL`    `| ``index` `| ``NULL`     `| ``PRIMARY` `| 4    | ``NULL` `|  1 |  100.00 | Using ``index` `|``+``----+-------------+-------+------------+-------+---------------+---------+---------+------+------+----------+-------------+
```

- all

对来自先前表的行的每个组合进行全表扫描。 如果该表是未标记为const的第一个表，则通常不好，并且在所有其他情况下通常非常糟糕。 通常，您可以通过添加索引来避免ALL，这些索引允许基于早期表中的常量值或列值从表中检索行。

1. **possible_keys**

指MySQL可以从中选择的索引来查找此表中的行。 请注意，此列完全独立于EXPLAIN输出中显示的表顺序。 这意味着在实践中可能无法将某些键用于生成的表顺序。 如果此列为NULL（或在JSON格式的输出中未定义），则没有相关的索引。 在这种情况下，您可以通过检查WHERE子句来检查它是否引用了某些适合索引的列，从而可以提高查询性能。 如果是这样，请创建适当的索引，然后再次使用EXPLAIN检查查询

1. **key**

指MySQL实际决定使用的键（索引）。 如果MySQL决定使用mays_keys索引之一来查找行，则将该索引列为键值。

可能会命名一个可能索引中不存在的索引。 如果没有任何可能的索引索引适合于查找行，但是查询选择的所有列都是其他索引的列，则可能发生这种情况。 也就是说，命名索引覆盖了选定的列，因此尽管不使用索引来确定要检索的行，但索引扫描比数据行扫描更有效。

对于InnoDB，即使查询也选择了主键，辅助索引也可能覆盖选定的列，因为InnoDB将主键值与每个辅助索引一起存储。 如果key为NULL，则MySQL未找到可用于更有效地执行查询的索引。

1. **key_len**

key_len列指示MySQL决定使用的密钥的长度。 key_len的值使您能够确定MySQL实际使用的多部分键的多少部分。 如果键列为NULL，则len_len列也为NULL。使用的索引的长度。在不损失精确性的情况下，长度越短越好

1. **ref**

ref列显示将哪些列或常量与键列中命名的索引进行比较，以从表中选择行。

1. **rows**

rows列显示MySQL认为它执行查询时必须检查的行数。

1. filtered

已过滤的列指示将被表条件过滤的表行的估计百分比。 最大值为100，这表示未过滤行。 值从100减小表示过滤量增加。 rows显示了检查的估计行数，×过滤后的行显示了将与下表连接的行数。 例如，如果行数为1000，过滤条件为50.00（50％），则与下表联接的行数为1000×50％= 500。

1. extra

此列包含有关MySQL如何解析查询的其他信息.

- - Distinct

一旦MYSQL找到了与行相联合匹配的行，就不再搜索了

- - Not exists

MYSQL优化了LEFT JOIN，一旦它找到了匹配LEFT JOIN标准的行， 就不再搜索了

- - Using filesort

看到这个的时候，查询就需要优化了。MYSQL需要进行额外的步骤来发现如何对返回的行排序。它根据连接类型以及存储排序键值和匹配条件的全部行的行指针来排序全部行

- - Using index

列数据是从仅仅使用了索引中的信息而没有读取实际的行动的表返回的，这发生在对表的全部的请求列都是同一个索引的部分的时候

- - Using temporary

看到这个的时候查询需要优化了。这里标示MYSQL需要创建一个临时表来存储结果，这通常发生在对不同的列集进行ORDER BY上，而不是GROUP BY

- - Using where

使用了WHERE从句来限制哪些行将与下一张表匹配或者是返回给用户。如果不想返回表中的全部行，并且连接类型ALL或index，这就会发生，或者是查询有问题

[回到顶部](https://www.cnblogs.com/yuanfy008/p/12110997.html#_labelTop)

# 四、参考文献　　

官方解释：https://dev.mysql.com/doc/refman/8.0/en/explain-output.html

*
*

表结构：

```
mysql> show ``create` `table` `t;``+``-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+``| ``Table` `| ``Create` `Table`                                                                                          `|``+``-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+``| t   | ``CREATE` `TABLE` ``t` (`` ```id` ``int``(11) ``DEFAULT` `NULL``,`` `````name``` ``varchar``(10) ``NOT` `NULL``,`` ``PRIMARY` `KEY` `(```name```),`` ``KEY` ``idx_id` (`id`)``) ENGINE=InnoDB ``DEFAULT` `CHARSET=utf8mb4 ``COLLATE``=utf8mb4_0900_ai_ci |``+``-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+``1 row ``in` `set` `(0.00 sec)` `mysql> show ``create` `table` `t1;``+``-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+``| ``Table` `| ``Create` `Table`                                                                          `|``+``-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+``| t1  | ``CREATE` `TABLE` ``t1` (`` ```id` ``int``(11) ``NOT` `NULL``,`` ```age` ``int``(11) ``NOT` `NULL``,`` ``PRIMARY` `KEY` `(`id`)``) ENGINE=InnoDB ``DEFAULT` `CHARSET=utf8mb4 ``COLLATE``=utf8mb4_0900_ai_ci |``+``-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+``1 row ``in` `set` `(0.00 sec)` `mysql> show ``create` `table` `t2;``+``-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+``| ``Table` `| ``Create` `Table`                                                                          `|``+``-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+``| t2  | ``CREATE` `TABLE` ``t2` (`` ```id` ``int``(11) ``NOT` `NULL``,`` ```sex` ``int``(11) ``NOT` `NULL``,`` ``PRIMARY` `KEY` `(`id`)``) ENGINE=InnoDB ``DEFAULT` `CHARSET=utf8mb4 ``COLLATE``=utf8mb4_0900_ai_ci |``+``-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+``1 row ``in` `set` `(0.00 sec)
```

　　



这就是本该拼搏的年纪，却想得太多，做得太少！

标签: [Mysql](https://www.cnblogs.com/yuanfy008/tag/Mysql/)