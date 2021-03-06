# 索引作用

索引能够显著加快查询速度(去重、加速、免排序、覆盖)，降低删除、修改、新增速度

# 使用索引

创建索引

```
ALTER TABLE <table_name> ADD INDEX <index_name> (idx_<column_list>)
```

如果是字典表的字典字段时, 使用联合索引(谨慎)

```
ALTER TABLE <table_name> ADD UNIQUE (uniq_<column_list>)
```

如果字段类型为Text相关类型时

```
ALTER TABLE <table_name> ADD FULLTEXT index_name(idx_<column_list>)
```

# 复合索引的限制

最多只能包含16个字段, 最长只能小于900(字节)

字段只能来自一个表

# 索引存在情况

删除表后会删除整个索引, 删除字段会删除单索引以及复合索引中的该字段, 修改字段会重建索引

# 索引匹配规则

一次查询只会命中一个索引, 单表最多5个单索引和5个复合索引

索引分为单索引和复合索引

单索引优先级比复合索引优先级更高

查询条件的字段列表会严格按复合索引中声明的字段顺序从左到右进行完全匹配(右侧可以缺失查询条件)

例如:

索引为(a,b,c)

查询条件分别为:

a生效: where a=1

都不生效: where b=1

都不生效: where c=1

a/b生效: where a=1 and b=1

a生效: where a=1 and c=1

都不生效: where b=1 and b=c

a/b/c生效: where a=1 and b=1 and b=c

# 索引失效规则

## 查询条件中包含以下

MySQL觉得数据量少时会失效

以下例子会导致自身失效:

```
字段类型和值类型不匹配, 例如: name = 123123 , 但是 aget = 'sdfsfs' 又没问题
```

以下例子会导致后续失效:

```
>
<
between
like '%<text_content>', 但是 like 'fdsfs%'又没问题
```

以下例子会导致整体失效:

```
+
-
*
/
exist
!= 或者 <>
is null
or <其他条件没有索引>
not in()
<函数>(<字段>)
```



# 使用索引优化查询

## 为主键(默认)、外键加索引

## 为唯一标识加索引

唯一性索引的值是唯一的，可以更快速的通过该索引来确定某条记录。例如，学生表中学号是具有唯一性的字段。为该字段建立唯一性索引可以很快的确定某个学生的信息。如果使用姓名的话，可能存在同名现象，从而降低查询速度。

## 为常用排序、分组和联合条件加索引

经常需要ORDER BY、GROUP BY、DISTINCT和UNION等操作的字段，排序操作会浪费很多时间。如果为其建立索引，可以有效地避免排序操作。

## 为常用条件加索引

如果某个字段经常用来做查询条件，那么该字段的查询速度会影响整个表的查询速度。因此，为这样的字段建立索引，可以提高整个表的查询速度。

## 为区分度高加索引

区分度的公式是count(distinct col)/count(*)，表示字段不重复的比例，比例越大我们扫描的记录数越少，唯一键的区分度是1，而一些状态、性别字段可能在大数据面前区分度就 是0。合并区分度低的字段的索引。

## 为高频条件加索引

应对高并发

## 索引列不参与计算，保持列“干净”。

比如from_unixtime(create_time) = ’2014-05-29’就不能使用到索引，原因很简单，b+树中存的都是数据表中的字段值，但进行检索时，需要把所有元素都应用函数才能比较，显然成本 太大。所以语句应该写成create_time = unix_timestamp(’2014-05-29’);

## 为需要计算的字段建立函数索引(5.7+)

```
# 先建立虚拟字段
alter table 表名 add column 字段名_index datetime GENERATED ALWAYS AS (函数(字段))

例如
alter table executor_data add column create_time_index datetime GENERATED ALWAYS AS (date_format(create_datetime,'%Y-%m-%d'))

# 再建立索引
ALTER TABLE 表名 ADD INDEX idx_字段名_index (字段名_index)
ALTER TABLE executor_data ADD INDEX idx_create_time_index (create_time_index)
```

# 使用索引优化变更(新增、删除、修改)

## 索引的数目超过一定数量(5)时减少/合并索引

索引的数目不是越多越好。每个索引都需要占用磁盘空间，索引越多，需要的磁盘空间就越大。修改表时，对索引的重构和更新很麻烦。越多的索引，会使更新表变得很浪费时间。

## 删除字段长度过长

如果索引的值很长，那么查询的速度会受到影响。例如，对一个CHAR(100)类型的字段进行全文检索需要的时间肯定要比对CHAR(10)类型的字段需要的时间要多。 适当调小该字段长度

## 删除全文检索字段

如果索引字段的值很长，尽量使用值的前缀来索引。例如，TEXT和BLOG类型的字段，进行全文检索会很浪费时间。如果只检索字段的前面的若干个字符，这样可以提高检索速度。改为匹配前缀

## 删除不再使用或者很少使用

表中的数据被大量更新，或者数据的使用方式被改变后，原有的一些索引可能不再需要。数据库管理员应当定期找出这些索引，将它们删除，从而减少索引对更新操作的影响。对删除次数多导致索引碎片化的表进行重建索引以提高查询效率

## 删除被包含在复合索引

除非该字段是唯一标志, 否则如果表中已经有a的索引，现在要加(a,b)的索引，那么只需要修改原来的索引即可

## 删除数据少(300/1000)

对于规模小的数据表建立索引 不仅不会提高功能,相反使用索引查找可能比简单的全表扫描还要嫚而且建索引还会占用一部分的存储空间

## 删除区分度低的

如性别字段

## 创建索引动作要在变更操作之后

有索引的好处是搜索比较快但是在有索引的前提下进行插入、更新操作会很慢