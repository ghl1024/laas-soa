## MySQL8.0之执行计划

[梓杰](https://yq.aliyun.com/users/k5fbrebkyhlei) 2019-08-03 15:16:36 浏览1968

- [数据存储与数据库](https://yq.aliyun.com/tags/type_blog-tagid_6/)
-  

- [执行计划](https://yq.aliyun.com/tags/type_blog-tagid_5502/)
-  

- [新特性](https://yq.aliyun.com/tags/type_blog-tagid_6270/)
-  

- [mysql8.0](https://yq.aliyun.com/tags/type_blog-tagid_14541/)

## 一、SQL执行过程

### 1.1 SQL语句内部执行过程

  MySQL分为Server层和存储引擎层两部分。Server层包括连接器、分析器、优化器、执行器等等，而存储引擎层负责数据的存储和读取。
  SQL执行时，会通过连接器建立连接、获取权限；连接器会维持和管理连接。
  然后，MySQL会通过分析器对SQL语句进行解析，分析语句各部分含义，然后按照语法规则判断SQL是否符合MySQL的语法。
  经过分析器分析后，MySQL会对SQL请求进行优化器的处理，优化器对语句索引、连接顺序等情况判断，决定使用哪种执行方案最合适。
  最后，就到了执行器的阶段，执行器根据表的引擎定义，去调用引擎接口，执行SQL语句。

### 1.2 SQL语句执行顺序

1、FROM #对FROM的左边的表和右边的表计算笛卡尔积，产生虚拟表VT1。
2、ON #对虚拟表VT1进行ON筛选，只有那些符合条件的行才会被记录在虚拟表VT2中。
3、JOIN #如果指定了外连接(比如left join、right join)，那么保留表中未匹配的行就会作为外部行添加到虚拟表VT2中，产生虚拟表VT3。from子句中包含两个以上的表的话，那么就会对上一个join连接产生的结果VT3和下一个表重复执行步骤1~3这三个步骤，一直到处理完所有的表为止。
4、WHERE #对虚拟表VT3进行WHERE条件过滤。只有符合条件的记录才会被插入到虚拟表VT4中。
5、GROUP BY #根据group by子句中的列，对VT4中的记录进行分组操作，产生虚拟表VT5。
6、AVG, SUM ... #对虚拟表VT5进行AVG或者SUM操作，产生虚拟表VT6。
7、HAVING #对虚拟表VT6应用having过滤，只有符合的记录才会被插入到虚拟表VT7中。
8、SELECT #执行select操作，选择指定的列，插入到虚拟表VT8中。
9、DISTINCT #对VT8中的记录进行去重。产生虚拟表VT9。
10、ORDER BY #将虚拟表VT9中的记录按照指定列进行排序操作，产生虚拟表VT10。
11、LIMIT #取出指定行的记录，产生虚拟表VT11, 并将结果返回。

## 二、执行计划解读

### 2.1如何查看SQL语句执行计划

  MySQL内置EXPLAIN命令来查看SQL语句的执行计划，EXPLAIN支持SELECT、DELETE、INSERT、REPLACE和UPDATE等语句，也支持对分区表的解析。在MySQL8.0.17中EXPLAIN不在支持`EXPLAIN PARTITIONS`和`EXPLAIN EXTENDED`语法，并且`FORMAT`新增`TREE`格式。通过EXPLAIN展示的信息我们可以了解到表查询的顺序，表连接的方式等，并根据这些信息判断语句执行效率，决定是否添加索引或改写SQL语句优化表连接方式以提高执行效率。
  EXPLAIN语法如下：

```
{EXPLAIN | DESCRIBE | DESC}
    tbl_name [col_name | wild]

{EXPLAIN | DESCRIBE | DESC}
    [explain_type]
    {explainable_stmt | FOR CONNECTION connection_id}

explain_type: {
    FORMAT = format_name
}

format_name: {
    TRADITIONAL
  | JSON
  | TREE
}

explainable_stmt: {
    SELECT statement
  | DELETE statement
  | INSERT statement
  | REPLACE statement
  | UPDATE statement
}
DESCRIBE和EXPLAIN语句是同义词。但DESCRIBE关键字更常用来获取关于表的信息结构，而EXPLAIN用于获取查询执行计划。
```

  本文将对EXPLAIN的三种格式的执行计划输出进行讲解：

### 2.2 TRADITIONAL格式输出说明

  RADITIONAL格式也就是默认格式，输出格式如下:

```
mysql> explain format='TRADITIONAL' select t1.id,t1.address,t2.from_date,t3.dept_name from t1 left join t2 on t1.id=t2.id left join t3 on t2.dept_id=t3.dept_id where t3.dept_name in (select dept_name from t3 whhere dept_id<1000)
+----+-------------+-------+------------+--------+-----------------------+---------------+---------+-----------------+-------+----------+--------------------------+
| id | select_type | table | partitions | type   | possible_keys         | key           | key_len | ref             | rows  | filtered | Extra                    |
+----+-------------+-------+------------+--------+-----------------------+---------------+---------+-----------------+-------+----------+--------------------------+
|  1 | PRIMARY     | t1    | NULL       | index  | NULL                  | idx_address   | 202     | NULL            | 99975 |   100.00 | Using index              |
|  1 | PRIMARY     | t2    | NULL       | eq_ref | PRIMARY               | PRIMARY       | 4       | test.t1.id      |     1 |   100.00 | NULL                     |
|  1 | PRIMARY     | t3    | NULL       | eq_ref | PRIMARY               | PRIMARY       | 16      | test.t2.dept_id |     1 |   100.00 | Using where              |
|  2 | SUBQUERY    | t3    | NULL       | index  | PRIMARY,idx_dept_name | idx_dept_name | 202     | NULL            | 81406 |    33.33 | Using where; Using index |
+----+-------------+-------+------------+--------+-----------------------+---------------+---------+-----------------+-------+----------+--------------------------+
4 rows in set, 2 warnings (0.01 sec)
```

  各字段含义如下：

| 字段名        | 含义                                     |
| :------------ | :--------------------------------------- |
| id            | 标识符，语句涉及表的执行顺序             |
| select_type   | 表查询类型                               |
| table         | 表名称                                   |
| partitions    | 涉及表哪个分区                           |
| type          | 表的查询(连接)类型                       |
| possible_keys | 表可能使用到的索引                       |
| key           | 表实际使用到的索引                       |
| key_len       | 表实际使用索引的长度，单位:字节          |
| ref           | 表哪些字段或者常量用于连接查找索引上的值 |
| rows          | 查询预估返回表的行数                     |
| filtered      | 表经过条件过滤之后与总数的百分比         |
| Extra         | 额外的说明信息                           |

#### 2.2.1 id

  id值越小越为查询的外部，越大越为查询的内部。id值按照由大到小的顺序执行，如果id值相同，自上而下执行。

#### 2.2.2 select_type

| select_type值        | 含义                                                 |
| :------------------- | :--------------------------------------------------- |
| SIMPLE               | 简单查询，不包含unino查询或子查询                    |
| PRIMARY              | 位于最外部的查询                                     |
| UNION                | 当出现union查询时第二个或之后的查询                  |
| DEPENDENT UNION      | 当出现union查询时第二个或之后的查询，取决于外部查询  |
| UNION RESULT         | union查询的结果集                                    |
| SUBQUERY             | 子查询当中第一个select查询                           |
| DEPENDENT SUBQUERY   | 子查询当中第一个select查询，取决于外部的查询         |
| DERIVED              | 衍生表(FROM子句中的子查询)                           |
| MATERIALIZED         | 物化子查询                                           |
| UNCACHEABLE SUBQUERY | 结果集无法缓存的子查询，必须重新评估外部查询的每一行 |
| UNCACHEABLE UNION    | UNION中第二个或之后的SELECT，属于无法缓存的子查询    |

#### 2.2.3 table

  当前是从哪张表获取数据，如果为表指定了别名，则显示别名，如果没有涉及对表的数据读取，则显示NULL，还有如下几种情形：

```
<unionM,N>: 引用id为M和N UNION后的结果。
<derivedN>: 引用id为N的结果派生出的表。派生表可以是一个结果集，例如派生自FROM中子查询的结果。
<subqueryN>: 引用id为N的子查询结果物化得到的表。即生成一个临时表保存子查询的结果。
```

#### 2.2.4 partitions

  该列显示的为分区表命中的分区情况。非分区表该字段为空（null）。

#### 2.2.5 type

  **按照最好到最差的连接类型依次为：system，const，eq_ref，ref，fulltext，ref_or_null，index_merge，unique_subquery，index_subquery，range，index，ALL。**
  除了ALL之外，其他的type都可以使用到索引，除了index_merge之外，其他的type只可以用到一个索引。

- system：表中只有一行数据或者是空表，这是const类型的一个特例。且只能用于myisam和memory表。如果是Innodb引擎表，type列在这个情况通常都是all或者index。
- const：最多只有一行记录匹配。当联合主键或唯一索引的所有字段跟常量值比较时，join类型为const。其他数据库也叫做唯一索引扫描。
- eq_ref：多表join时，对于来自前面表的每一行，在当前表中只能找到一行。这是除了system和const之外最好的类型。当主键或唯一非NULL索引的所有字段都被用作join联接时会使用此类型。eq_ref可用于使用'='操作符作比较的索引列。比较的值可以是常量，也可以是使用在此表之前读取的表的列的表达式。
- ref：对于来自前面表的每一行，在此表的索引中可以匹配到多行。若联接只用到索引的最左前缀或索引不是主键或唯一索引时，使用ref类型（也就是说，此联接能够匹配多行记录）。ref可用于使用'='或'<=>'操作符作比较的索引列。

```
eq_ref相对于ref区别就是它使用的唯一索引，即主键或唯一索引，而ref使用的是非唯一索引或者普通索引。eq_ref只能找到一行，而ref能找到多行。
```

- fulltext：使用全文索引的时候是这个类型。要注意，全文索引的优先级很高，若全文索引和普通索引同时存在时，mysql不管代价，优先选择使用全文索引
- ref_or_null：跟ref类型类似，只是增加了null值的比较。实际用的不多。
- index_merge：表示查询使用了两个以上的索引，最后取交集或者并集，常见and，or的条件使用了不同的索引，官方排序这个在ref_or_null之后，但是实际上由于要读取多个索引，性能可能大部分时间都不如range
- unique_subquery：用于where中的in形式子查询，子查询返回不重复值唯一值，可以完全替换子查询，效率更高。
- index_subquery：该联接类型类似于unique_subquery。适用于非唯一索引，可以返回重复值。
- range：索引范围查询，常见于使用 =, <>, >, >=, <, <=, IS NULL, <=>, BETWEEN, IN()或者like等运算符的查询中。
- index：索引全表扫描，把索引从头到尾扫一遍。这里包含两种情况：
  一种是查询使用了覆盖索引，那么它只需要扫描索引就可以获得数据，这个效率要比全表扫描要快，因为索引通常比数据表小，而且还能避免二次查询。在extra中显示Using index，反之，如果在索引上进行全表扫描，没有Using index的提示。
- ALL：全表扫描，性能最差。

#### 2.2.6 possible_keys

  显示了MySQL在查找当前表中数据的时候可能使用到的索引，实际意义不大。

#### 2.2.7 key

  显示了MySQL在实际查找数据时决定使用的索引，如果该字段值为NULL，则表明没有使用索引。

#### 2.2.8 key_len

  显示了MySQL实际使用索引的大小，单位字节。可以通过key_len的大小判断评估复合索引使用了哪些部分。
几种常见字段类型索引长度大小如下，假设字符编码为utf8mb4：如果字段允许为NULL，则需要额外增加一个字节；
字符型：
char(n)：4n个字节（中文四字节，英文一个字节）
varchar(n)：4n+2个字节（中文四字节，英文一个字节）
数值型：
tinyint：1个字节
int：4个字节
bigint：8个字节
时间型：
date：3个字节
datetime：5个字节+秒精度字节
timestamp：4个字节+秒精度字节
秒精度字节(最大6位)：
1~2位：1个字节
3~4位：2个字节
5~6位：3个字节

#### 2.2.9 ref

  如果是使用的常数等值查询，这里会显示const，如果是连接查询，被驱动表的执行计划这里会显示驱动表的关联字段，如果是条件使用了表达式或者函数，或者条件列发生了内部隐式转换，这里可能显示为func。

#### 2.2.10 rows

  这是mysql估算的需要扫描的行数（不是精确值）。这个值非常直观显示 SQL的效率好坏, 原则上rows越少越好。

#### 2.2.11 filtered

  这个字段表示存储引擎返回的数据在server层过滤后，剩下多少满足查询的记录数量的比例，注意是百分比，不是具体记录数。

#### 2.2.12 Extra

  EXPLAIN中的很多额外的信息会在 Extra 字段显示,常见的有以下几种内容:

- Using index
    仅查询索引树就可以获取到所需要的数据行，而不需要读取表中实际的数据行。通常适用于select字段就是查询使用索引的一部分，即使用了覆盖索引。

```
mysql> explain select dept_id from t2;
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+--------+----------+-------------+
| id | select_type | table | partitions | type  | possible_keys | key         | key_len | ref  | rows   | filtered | Extra       |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+--------+----------+-------------+
|  1 | SIMPLE      | t2    | NULL       | index | NULL          | idx_dept_id | 16      | NULL | 100035 |   100.00 | Using index |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+--------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
```

- Using index condition
    显示采用了Index Condition Pushdown(ICP)特性通过索引去表中获取数据。关于ICP特性可以参考官方文档：Index Condition Pushdown Optimization。简单说法如下：

  如果开启ICP特性，部分where条件部分可以下推到存储引擎通过索引进行过滤，ICP可以减少存储引擎访问基表的次数；
  如果没有开启ICP特性，则存储引擎根据索引需要直接访问基表获取数据并返回给server层进行where条件的过滤。

```
#set persist optimizer_switch='index_condition_pushdown=off';
mysql> explain select * from t2  where to_date='1980-01-01' and from_date<'1970-01-01';                                                                                                                          
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+------------------------+
| id | select_type | table | partitions | type  | possible_keys | key         | key_len | ref  | rows | filtered | Extra                  |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+------------------------+
|  1 | SIMPLE      | t2    | NULL       | range | idx_from_to   | idx_from_to | 5       | NULL |    1 |    10.00 | Using where; Using MRR |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+------------------------+
1 row in set, 1 warning (0.00 sec)
#set persist optimizer_switch='index_condition_pushdown=on';
mysql> explain select * from t2  where to_date='1980-01-01' and from_date<'1970-01-01';
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+----------------------------------+
| id | select_type | table | partitions | type  | possible_keys | key         | key_len | ref  | rows | filtered | Extra                            |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+----------------------------------+
|  1 | SIMPLE      | t2    | NULL       | range | idx_from_to   | idx_from_to | 5       | NULL |    1 |    10.00 | Using index condition; Using MRR |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+----------------------------------+
1 row in set, 1 warning (0.00 sec)
```

- Using where
  显示MySQL通过索引条件定位之后还需要返回表中获得所需要的数据。

```
mysql> explain select * from t2  where to_date='1980-01-01';
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+-------------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows   | filtered | Extra       |
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+-------------+
|  1 | SIMPLE      | t2    | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 100035 |    10.00 | Using where |
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+-------------+
1 row in set, 1 warning (0.40 sec)
```

- Impossible WHERE
  where子句的条件永远都不可能为真。

```
mysql> explain select * from t2  where 1=0;
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+------------------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra            |
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+------------------+
|  1 | SIMPLE      | NULL  | NULL       | NULL | NULL          | NULL | NULL    | NULL | NULL |     NULL | Impossible WHERE |
+----+-------------+-------+------------+------+---------------+------+---------+------+------+----------+------------------+
1 row in set, 1 warning (0.00 sec)
```

- Using join buffer (Block Nested Loop), Using join buffer (Batched Key Access)
  在表联接过程当中，将先前表的部分数据读取到join buffer缓冲区中，然后从缓冲区中读取数据与当前表进行连接。主要有两种算法：Block Nested Loop和Batched Key Access。

```
#开关BKA参数
SET PERSIST optimizer_switch='mrr=on,mrr_cost_based=off,block_nested_loop=on,batched_key_access=on/off';
mysql> explain select * from t1 join t2 on t1.birth_date=t2.to_date;
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+----------------------------------------------------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref  | rows   | filtered | Extra                                              |
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+----------------------------------------------------+
|  1 | SIMPLE      | t2    | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 100035 |   100.00 | NULL                                               |
|  1 | SIMPLE      | t1    | NULL       | ALL  | NULL          | NULL | NULL    | NULL |  99975 |    10.00 | Using where; Using join buffer (Block Nested Loop) |
+----+-------------+-------+------------+------+---------------+------+---------+------+--------+----------+----------------------------------------------------+
2 rows in set, 1 warning (0.00 sec)

mysql> explain select * from t2 join t3 on t3.dept_id=t2.dept_id;
+----+-------------+-------+------------+-------+---------------+---------------+---------+-----------------+-------+----------+----------------------------------------+
| id | select_type | table | partitions | type  | possible_keys | key           | key_len | ref             | rows  | filtered | Extra                                  |
+----+-------------+-------+------------+-------+---------------+---------------+---------+-----------------+-------+----------+----------------------------------------+
|  1 | SIMPLE      | t3    | NULL       | index | PRIMARY       | idx_dept_name | 202     | NULL            | 81406 |   100.00 | Using index                            |
|  1 | SIMPLE      | t2    | NULL       | ref   | idx_dept_id   | idx_dept_id   | 16      | test.t3.dept_id |     1 |   100.00 | Using join buffer (Batched Key Access) |
+----+-------------+-------+------------+-------+---------------+---------------+---------+-----------------+-------+----------+----------------------------------------+
2 rows in set, 1 warning (0.10 sec)
```

- Using MRR
  读取数据采用多范围读(Multi-Range Read)的优化策略。

```
mysql> explain select * from t2  where to_date='1980-01-01' and from_date<'1970-01-01';                                                                                                                          
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+------------------------+
| id | select_type | table | partitions | type  | possible_keys | key         | key_len | ref  | rows | filtered | Extra                  |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+------------------------+
|  1 | SIMPLE      | t2    | NULL       | range | idx_from_to   | idx_from_to | 5       | NULL |    1 |    10.00 | Using where; Using MRR |
+----+-------------+-------+------------+-------+---------------+-------------+---------+------+------+----------+------------------------+
1 row in set, 1 warning (0.00 sec)
```

- Using temporary
  MySQL需要创建临时表来存放查询结果集。通常发生在有GROUP BY或ORDER BY子句的语句当中。

```
mysql> explain select * from t1 join t2 on t1.birth_date=t2.from_date  order by t2.id;
+----+-------------+-------+------------+------+---------------+-------------+---------+--------------------+-------+----------+----------------------------------------+
| id | select_type | table | partitions | type | possible_keys | key         | key_len | ref                | rows  | filtered | Extra                                  |
+----+-------------+-------+------------+------+---------------+-------------+---------+--------------------+-------+----------+----------------------------------------+
|  1 | SIMPLE      | t1    | NULL       | ALL  | NULL          | NULL        | NULL    | NULL               | 99975 |   100.00 | Using temporary; Using filesort        |
|  1 | SIMPLE      | t2    | NULL       | ref  | idx_from_to   | idx_from_to | 5       | test.t1.birth_date |     1 |   100.00 | Using join buffer (Batched Key Access) |
+----+-------------+-------+------------+------+---------------+-------------+---------+--------------------+-------+----------+----------------------------------------+
2 rows in set, 1 warning (0.00 sec)
```

- Using filesort
  MySQL需要对获取的数据进行额外的一次排序操作，无法通过索引的排序完成。通常发生在有ORDER BY子句的语句当中。

```
mysql> explain select * from t1 join t2 on t1.birth_date=t2.from_date  order by t2.id;
+----+-------------+-------+------------+------+---------------+-------------+---------+--------------------+-------+----------+----------------------------------------+
| id | select_type | table | partitions | type | possible_keys | key         | key_len | ref                | rows  | filtered | Extra                                  |
+----+-------------+-------+------------+------+---------------+-------------+---------+--------------------+-------+----------+----------------------------------------+
|  1 | SIMPLE      | t1    | NULL       | ALL  | NULL          | NULL        | NULL    | NULL               | 99975 |   100.00 | Using temporary; Using filesort        |
|  1 | SIMPLE      | t2    | NULL       | ref  | idx_from_to   | idx_from_to | 5       | test.t1.birth_date |     1 |   100.00 | Using join buffer (Batched Key Access) |
+----+-------------+-------+------------+------+---------------+-------------+---------+--------------------+-------+----------+----------------------------------------+
2 rows in set, 1 warning (0.00 sec)
```

### 2.3 JSON格式输出说明

```
mysql> explain format='JSON' select t1.id,t1.address,t2.from_date,t3.dept_name from t1 left join t2 on t1.id=t2.id left join t3 on t2.dept_id=t3.dept_id where t3.dept_name in (select dept_name from t3 where deppt_id<1000) or  t2.id<10000;
+------------------------------------------------------------------------------------------------+
| EXPLAIN                                               |
| {
  "query_block": { #整个查询块
    "select_id": 1, #等同于默认格式的id
    "cost_info": { #具体成本信息
      "query_cost": "80068.25" #select_id=1时的成本为80068.25
    },
    "nested_loop": [ #记录SQL执行的类型信息
      {
        "table": {#具体表的内容
          "table_name": "t1", #等同于默认格式的table
          "access_type": "index",#等同于默认格式的type
          "key": "idx_address",#等同于默认格式的key
          "used_key_parts": [ #使用到索引的具体部分
            "address"
          ],
          "key_length": "202",#等同于默认格式的key_len
          "rows_examined_per_scan": 99975, #每次扫描的行数
          "rows_produced_per_join": 99975, #每次连接的行数
          "filtered": "100.00",#等同于默认格式的filtered
          "using_index": true, #是否使用到索引
          "cost_info": {#此部分的具体成本
            "read_cost": "88.25",#读取的成本
            "eval_cost": "9997.50",#评估的成本
            "prefix_cost": "10085.75",#加入JOIN中下一个表的成本
            "data_read_per_join": "32M"#JOIN操作应读取的数据量
          },
          "used_columns": [#使用到的字段
            "id",
            "address"
          ]
        }
      },
      {
        "table": {
          "table_name": "t2",
          "access_type": "eq_ref",
          "possible_keys": [
            "PRIMARY"
          ],
          "key": "PRIMARY",
          "used_key_parts": [
            "id"
          ],
          "key_length": "4",
          "ref": [ #等同于默认格式的ref
            "test.t1.id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 99975,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "24993.75",
            "eval_cost": "9997.50",
            "prefix_cost": "45077.00",
            "data_read_per_join": "3M"
          },
          "used_columns": [
            "id",
            "dept_id",
            "from_date"
          ]
        }
      },
      {
        "table": {
          "table_name": "t3",
          "access_type": "eq_ref",
          "possible_keys": [
            "PRIMARY"
          ],
          "key": "PRIMARY",
          "used_key_parts": [
            "dept_id"
          ],
          "key_length": "16",
          "ref": [
            "test.t2.dept_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 99975,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "24993.75",
            "eval_cost": "9997.50",
            "prefix_cost": "80068.25",
            "data_read_per_join": "21M"
          },
          "used_columns": [
            "dept_id",
            "dept_name"
          ],
          "attached_condition": "<if>(found_match(t3), (<in_optimizer>(`test`.`t3`.`dept_name`,`test`.`t3`.`dept_name` in ( <materialize> (/* select#2 */ select `test`.`t3`.`dept_name` from `test`.`t3` where (`test`.`t3`.`dept_id` < 1000) ), <primary_index_lookup>(`test`.`t3`.`dept_name` in <temporary table> on <auto_key> where ((`test`.`t3`.`dept_name` = `materialized-subquery`.`dept_name`))))) or (`test`.`t2`.`id` < 10000)), true)",#显示一些附加条件
          "attached_subqueries": [#附加子查询
            {
              "table": {
                "table_name": "<materialized_subquery>",#物化子查询
                "access_type": "eq_ref",
                "key": "<auto_key>",
                "key_length": "202",
                "rows_examined_per_scan": 1,
                "materialized_from_subquery": {
                  "using_temporary_table": true,#使用了临时表
                  "dependent": true,
                  "cacheable": false,#结果无法缓存
                  "query_block": {
                    "select_id": 2,
                    "cost_info": {
                      "query_cost": "8228.85"
                    },
                    "table": {
                      "table_name": "t3",
                      "access_type": "index",
                      "possible_keys": [
                        "PRIMARY",
                        "idx_dept_name"
                      ],
                      "key": "idx_dept_name",
                      "used_key_parts": [
                        "dept_name"
                      ],
                      "key_length": "202",
                      "rows_examined_per_scan": 81406,
                      "rows_produced_per_join": 27132,
                      "filtered": "33.33",
                      "using_index": true,
                      "cost_info": {
                        "read_cost": "5515.59",
                        "eval_cost": "2713.26",
                        "prefix_cost": "8228.85",
                        "data_read_per_join": "5M"
                      },
                      "used_columns": [
                        "dept_id",
                        "dept_name"
                      ],
                      "attached_condition": "(`test`.`t3`.`dept_id` < 1000)"
                    }
                  }
                }
              }
            }
          ]
        }
      }
    ]
  }
} |
+------------------------------------------------------------------------------------------------+
1 row in set, 2 warnings (0.01 sec)
```

### 2.4 TREE格式输出说明

```
mysql> explain format='TREE' select t1.id,t1.address,t2.from_date,t3.dept_name from t1 left join t2 on t1.id=t2.id left join t3 on t2.dept_id=t3.dept_id where t3.dept_name in (select dept_name from t3 where deppt_id<1000) or  t2.id<10000;
+------------------------------------------------------------------------------------------------+
| EXPLAIN                |
+------------------------------------------------------------------------------------------------+
| -> Filter: (<in_optimizer>(t3.dept_name,t3.dept_name in (select #2)) or (t2.id < 10000))
    -> Nested loop left join
        -> Nested loop left join #连接方式
            -> Index scan on t1 using idx_address #使用到的索引
            -> Single-row index lookup on t2 using PRIMARY (id=t1.id) #具体使用的索引相关信息
        -> Single-row index lookup on t3 using PRIMARY (dept_id=t2.dept_id)
    -> Select #2 (subquery in condition; run only once)#子查询;只运行一次
        -> Filter: (t3.dept_id < 1000)#条件信息
            -> Index scan on t3 using idx_dept_name
 |
+------------------------------------------------------------------------------------------------+
1 row in set, 1 warning (0.11 sec)
```

## 三、总结

  本文对MySQL8.0.17中SQL的内部执行流程、SQL执行顺序以及执行计划的三种格式分别进行了讲述，其他MySQL8.0.17的新特性将在以后的文章中陆续展出。

本文首发在云栖社区，遵循云栖社区版权声明：本文内容由互联网用户自发贡献，版权归用户作者所有，云栖社区不为本文内容承担相关法律责任。云栖社区已在2020年6月升级到阿里云开发者社区。如果您发现有涉嫌抄袭的内容，请填写[侵权投诉表单](https://yida.alibaba-inc.com/o/right)进行举报，一经查实，阿里云开发者社区将协助删除涉嫌侵权内容。