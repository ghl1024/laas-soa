# [数据库索引-使用、优化、失效](https://www.cnblogs.com/xuwc/p/14002536.html)

参考：

https://www.cnblogs.com/wwxzdl/p/11116446.html

https://blog.csdn.net/tongdanping/article/details/79878302

https://blog.csdn.net/weixin_42181824/article/details/82261988

https://blog.csdn.net/bingxuesiyang/article/details/89314233

https://www.cnblogs.com/liehen2046/p/11052666.html

https://blog.csdn.net/junjunba2689/article/details/82020961 

 

 

 

 

 

# [什么是数据库索引](https://www.cnblogs.com/wwxzdl/p/11116446.html)

**一、数据索引是干什么用的呢？**

数据库索引其实就是为了使查询数据效率快。

**二、数据库索引有哪些呢？**

1. 聚集索引（主键索引）：在数据库里面，所有行数都会按照主键索引进行排序。
2. 非聚集索引：就是给普通字段加上索引。
3. 联合索引：就是好几个字段组成的索引，称为联合索引。

```
key ``'idx_age_name_sex'` `(``'age'``,``'name'``,``'sex'``)
```

 联合索引遵从最左前缀原则，什么意思呢，就比如说一张学生表里面的联合索引如上面所示，那么下面A,B,C,D,E,F哪个会走索引呢？

```
A:select * from student where age = ``16` `and name = ``'小张'``B:select * from student where name = ``'小张'` `and sex = ``'男'``C:select * from student where name = ``'小张'` `and sex = ``'男'` `and age = ``18``D:select * from student where age > ``20` `and name = ``'小张'``E:select * from student where age != ``15` `and name = ``'小张'``<br>``F:select * from student where age = ``15` `and name != ``'小张'
```

 A遵从最左匹配原则，age是在最左边，所以A走索引；

 B直接从name开始，没有遵从最左匹配原则，所以不走索引；

 C虽然从name开始，但是有索引最左边的age，mysql内部会自动转成where age = '18' and name = '小张'  and sex = '男' 这种，所以还是遵从最左匹配原则；

 D这个是因为age>20是范围，范围字段会结束索引对范围后面索引字段的使用，所以只有走了age这个索引；

 E这个虽然遵循最左匹配原则，但是不走索引，因为!= 不走索引；

 F这个只走age索引，不走name索引，原因如上；

**三、有哪些列子不走索引呢？**

 表student中两个字段age,name加了索引

```
key ``'idx_age'` `(``'age'``),``key ``'idx_name'` `(``'name'``)
```

  1.Like这种就是%在前面的不走索引，在后面的走索引

```
A:select * from student where ``'name'` `like ``'王%'``B:select * from student where ``'name'` `like ``'%小'
```

 A走索引，B不走索引

 2.用索引列进行计算的，不走索引

```
A:select * from student where age = ``10``+``8``B:select * from student where age + ``8` `= ``18
```

 A走索引，B不走索引

 3.对索引列用函数了，不走索引

```
A:select * from student where concat(``'name'``,``'哈'``) =``'王哈哈'``;``B:select * from student where name = concat(``'王哈'``,``'哈'``);
```

 A不走索引，B走索引

 \4. 索引列用了!= 不走索引,如下：

```
select * from student where age != ``18`` 
```

 

 

 

 

 

 

 

 

# 深入理解MySQL索引原理和实现——为什么索引可以加速查询？

索引是一个排序的列表，在这个列表中存储着索引的值和包含这个值的数据所在行的物理地址，在数据十分庞大的时候，索引可以大大加快查询的速度，这是因为使用索引后可以不用扫描全表来定位某行的数据，而是先通过索引表找到该行数据对应的物理地址然后访问相应的数据。

# 一、MySQL中索引的语法

创建索引

在创建表的时候添加索引

1.  

   CREATE TABLE mytable(

2.  

   ID INT NOT NULL,

3.  

   username VARCHAR(16) NOT NULL,

4.  

   INDEX [indexName] (username(length))

5.  

   );

在创建表以后添加索引

1.  

   ALTER TABLE my_table ADD [UNIQUE] INDEX index_name(column_name);

2.  

   或者

3.  

   CREATE INDEX index_name ON my_table(column_name);

注意：

1、索引需要占用磁盘空间，因此在创建索引时要考虑到磁盘空间是否足够

2、创建索引时需要对表加锁，因此实际操作中需要在业务空闲期间进行

根据索引查询

1.  

   具体查询：

2.  

   SELECT * FROM table_name WHERE column_1=column_2;(为column_1建立了索引)

3.  

    

4.  

   或者模糊查询

5.  

   SELECT * FROM table_name WHERE column_1 LIKE '%三'

6.  

   SELECT * FROM table_name WHERE column_1 LIKE '三%'

7.  

   SELECT * FROM table_name WHERE column_1 LIKE '%三%'

8.  

    

9.  

   SELECT * FROM table_name WHERE column_1 LIKE '_好_'

10.  

     

11.  

    如果要表示在字符串中既有A又有B，那么查询语句为：

12.  

    SELECT * FROM table_name WHERE column_1 LIKE '%A%' AND column_1 LIKE '%B%';

13.  

     

14.  

    SELECT * FROM table_name WHERE column_1 LIKE '[张李王]三'; //表示column_1中有匹配张三、李三、王三的都可以

15.  

    SELECT * FROM table_name WHERE column_1 LIKE '[^张李王]三'; //表示column_1中有匹配除了张三、李三、王三的其他三都可以

16.  

     

17.  

    //在模糊查询中，%表示任意0个或多个字符；_表示任意单个字符（有且仅有），通常用来限制字符串长度;[]表示其中的某一个字符；[^]表示除了其中的字符的所有字符

18.  

     

19.  

    或者在全文索引中模糊查询

20.  

    SELECT * FROM table_name WHERE MATCH(content) AGAINST('word1','word2',...);

删除索引

1.  

   DROP INDEX my_index ON tablename；

2.  

   或者

3.  

   ALTER TABLE table_name DROP INDEX index_name;

查看表中的索引

```sql
SHOW INDEX FROM tablename
```

查看查询语句使用索引的情况

1.  

   //explain 加查询语句

2.  

   explain SELECT * FROM table_name WHERE column_1='123';

# 二、索引的优缺点

优势：可以快速检索，减少I/O次数，加快检索速度；根据索引分组和排序，可以加快分组和排序；

劣势：索引本身也是表，因此会占用存储空间，一般来说，索引表占用的空间的数据表的1.5倍；索引表的维护和创建需要时间成本，这个成本随着数据量增大而增大；构建索引会降低数据表的修改操作（删除，添加，修改）的效率，因为在修改数据表的同时还需要修改索引表；

# 三、索引的分类

常见的索引类型有：主键索引、唯一索引、普通索引、全文索引、组合索引

1、主键索引：即主索引，根据主键pk_clolum（length）建立索引，不允许重复，不允许空值；

```sql
ALTER TABLE 'table_name' ADD PRIMARY KEY pk_index('col')；
```

2、唯一索引：用来建立索引的列的值必须是唯一的，允许空值

```sql
ALTER TABLE 'table_name' ADD UNIQUE index_name('col')；
```

3、普通索引：用表中的普通列构建的索引，没有任何限制

```sql
ALTER TABLE 'table_name' ADD INDEX index_name('col')；
```

4、全文索引：用大文本对象的列构建的索引（下一部分会讲解）

```sql
ALTER TABLE 'table_name' ADD FULLTEXT INDEX ft_index('col')；
```

5、组合索引：用多个列组合构建的索引，这多个列中的值不允许有空值

```sql
ALTER TABLE 'table_name' ADD INDEX index_name('col1','col2','col3')；
```

*遵循“最左前缀”原则，把最常用作为检索或排序的列放在最左，依次递减，组合索引相当于建立了col1,col1col2,col1col2col3三个索引，而col2或者col3是不能使用索引的。

*在使用组合索引的时候可能因为列名长度过长而导致索引的key太大，导致效率降低，在允许的情况下，可以只取col1和col2的前几个字符作为索引

```sql
ALTER TABLE 'table_name' ADD INDEX index_name(col1(4),col2（3))；
```

表示使用col1的前4个字符和col2的前3个字符作为索引

 

 

# 四、索引的使用策略

 

什么时候要使用索引？

- 主键自动建立唯一索引；
- 经常作为查询条件在WHERE或者ORDER BY 语句中出现的列要建立索引；
- 作为排序的列要建立索引；
- 查询中与其他表关联的字段，外键关系建立索引
- 高并发条件下倾向组合索引；
- 用于聚合函数的列可以建立索引，例如使用了max(column_1)或者count(column_1)时的column_1就需要建立索引

什么时候不要使用索引？

- 经常增删改的列不要建立索引；
- 有大量重复的列不建立索引；
- 表记录太少不要建立索引。只有当数据库里已经有了足够多的测试数据时，它的性能测试结果才有实际参考价值。如果在测试数据库里只有几百条数据记录，它们往往在执行完第一条查询命令之后就被全部加载到内存里，这将使后续的查询命令都执行得非常快--不管有没有使用索引。只有当数据库里的记录超过了1000条、数据总量也超过了MySQL服务器上的内存总量时，数据库的性能测试结果才有意义。

索引失效的情况：

- 在组合索引中不能有列的值为NULL，如果有，那么这一列对组合索引就是无效的。
- 在一个SELECT语句中，索引只能使用一次，如果在WHERE中使用了，那么在ORDER BY中就不要用了。
- LIKE操作中，'%aaa%'不会使用索引，也就是索引会失效，但是‘aaa%’可以使用索引。
- 在索引的列上使用表达式或者函数会使索引失效，例如：select * from users where YEAR(adddate)<2007，将在每个行上进行运算，这将导致索引失效而进行全表扫描，因此我们可以改成：select * from users where adddate<’2007-01-01′。其它通配符同样，也就是说，在查询条件中使用正则表达式时，只有在搜索模板的第一个字符不是通配符的情况下才能使用索引。
- 在查询条件中使用不等于，包括<符号、>符号和！=会导致索引失效。特别的是如果对主键索引使用！=则不会使索引失效，如果对主键索引或者整数类型的索引使用<符号或者>符号不会使索引失效。（经[erwkjrfhjwkdb](https://me.csdn.net/u012483860)同学提醒，不等于，包括&lt;符号、>符号和！，如果占总记录的比例很小的话，也不会失效）
- 在查询条件中使用IS NULL或者IS NOT NULL会导致索引失效。
- 字符串不加单引号会导致索引失效。更准确的说是类型不一致会导致失效，比如字段email是字符串类型的，使用WHERE email=99999 则会导致失败，应该改为WHERE email='99999'。
- 在查询条件中使用OR连接多个条件会导致索引失效，除非OR链接的每个条件都加上索引，这时应该改为两次查询，然后用UNION ALL连接起来。
- 如果排序的字段使用了索引，那么select的字段也要是索引字段，否则索引失效。特别的是如果排序的是主键索引则select * 也不会导致索引失效。
- 尽量不要包括多列排序，如果一定要，最好为这队列构建组合索引；

 

# 五、索引的优化

 

1、最左前缀

索引的最左前缀和和B+Tree中的“最左前缀原理”有关，举例来说就是如果设置了组合索引<col1,col2,col3>那么以下3中情况可以使用索引：col1，<col1,col2>，<col1,col2,col3>，其它的列，比如<col2,col3>，<col1,col3>，col2，col3等等都是不能使用索引的。

根据最左前缀原则，我们一般把排序分组频率最高的列放在最左边，以此类推。

2、带索引的模糊查询优化

在上面已经提到，使用LIKE进行模糊查询的时候，'%aaa%'不会使用索引，也就是索引会失效。如果是这种情况，只能使用全文索引来进行优化（上文有讲到）。

3、为检索的条件构建全文索引，然后使用

```sql
SELECT * FROM tablename MATCH(index_colum) ANGAINST(‘word’);
```

4、使用短索引

对串列进行索引，如果可能应该指定一个前缀长度。例如，如果有一个CHAR(255)的 列，如果在前10 个或20 个字符内，多数值是惟一的，那么就不要对整个列进行索引。短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作。

 

 

 

## **索引的不足之处**

上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：

◆虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。

◆建立索引会占用磁盘空间的索引文件。一般情况这个问题不太严重，但如果你在一个大表上创建了多种组合索引，索引文件的会膨胀很快。

索引只是提高效率的一个因素，如果你的MySQL有大数据量的表，就需要花时间研究建立最优秀的索引，或优化查询语句。

 

## 使用索引的注意事项

使用索引时，有以下一些技巧和注意事项：

◆索引不会包含有NULL值的列

只要列中包含有NULL值都将不会被包含在索引中，复合索引中只要有一列含有NULL值，那么这一列对于此复合索引就是无效的。所以我们在数据库设计时不要让字段的默认值为NULL。

◆使用短索引

对串列进行索引，如果可能应该指定一个前缀长度。例如，如果有一个CHAR(255)的列，如果在前10个或20个字符内，多数值是惟一的，那么就不要对整个列进行索引。短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作。

◆索引列排序

MySQL查询只使用一个索引，因此如果where子句中已经使用了索引的话，那么order by中的列是不会使用索引的。因此数据库默认排序可以符合要求的情况下不要使用排序操作；尽量不要包含多个列的排序，如果需要最好给这些列创建复合索引。

◆like语句操作

一般情况下不鼓励使用like操作，如果非使用不可，如何使用也是一个问题。like “%aaa%” 不会使用索引而like “aaa%”可以使用索引。

◆不要在列上进行运算

1. select * from users where YEAR(adddate)<2007; 

将在每个行上进行运算，这将导致索引失效而进行全表扫描，因此我们可以改成

1. select * from users where adddate<‘2007-01-01’;  

◆不使用NOT IN和<>操作

 

 

 

 

 

 

# 索引使用策略及优化

MySQL的优化主要分为结构优化（Scheme optimization）和查询优化（Query optimization）。本章讨论的高性能索引策略主要属于结构优化范畴。本章的内容完全基于上文的理论基础，实际上一旦理解了索引背后的机制，那么选择高性能的策略就变成了纯粹的推理，并且可以理解这些策略背后的逻辑。

## 示例数据库

为了讨论索引策略，需要一个数据量不算小的数据库作为示例。本文选用MySQL官方文档中提供的示例数据库之一：employees。这个数据库关系复杂度适中，且数据量较大。下图是这个数据库的E-R关系图（引用自MySQL官方手册）：

![图12](http://blog.codinglabs.org/uploads/pictures/theory-of-mysql-index/12.png)图12

 

## 最左前缀原理与相关优化

高效使用索引的首要条件是知道什么样的查询会使用到索引，这个问题和B+Tree中的“最左前缀原理”有关，下面通过例子说明最左前缀原理。

这里先说一下联合索引的概念。在上文中，我们都是假设索引只引用了单个的列，实际上，MySQL中的索引可以以一定顺序引用多个列，这种索引叫做联合索引，一般的，一个联合索引是一个有序元组<a1, a2, …, an>，其中各个元素均为数据表的一列，实际上要严格定义索引需要用到关系代数，但是这里我不想讨论太多关系代数的话题，因为那样会显得很枯燥，所以这里就不再做严格定义。另外，单列索引可以看成联合索引元素数为1的特例。

以employees.titles表为例，下面先查看其上都有哪些索引：

```
 
```

从结果中可以到titles表的主索引为<emp_no, title, from_date>，还有一个辅助索引<emp_no>。为了避免多个索引使事情变复杂（MySQL的SQL优化器在多索引时行为比较复杂），这里我们将辅助索引drop掉：

![img](https://img-blog.csdnimg.cn/20190415161703939.png)

这样就可以专心分析索引PRIMARY的行为了。

### 情况一：全列匹配。

![img](https://img-blog.csdnimg.cn/20190415161720136.png)

很明显，当按照索引中所有列进行精确匹配（这里精确匹配指“=”或“IN”匹配）时，索引可以被用到。这里有一点需要注意，理论上索引对顺序是敏感的，但是由于MySQL的查询优化器会自动调整where子句的条件顺序以使用适合的索引，例如我们将where中的条件顺序颠倒：

![img](https://img-blog.csdnimg.cn/20190415161840157.png)

效果是一样的。

### 情况二：最左前缀匹配。

![img](https://img-blog.csdnimg.cn/20190415161908168.png)

当查询条件精确匹配索引的左边连续一个或几个列时，如<emp_no>或<emp_no, title>，所以可以被用到，但是只能用到一部分，即条件所组成的最左前缀。上面的查询从分析结果看用到了PRIMARY索引，但是key_len为4，说明只用到了索引的第一列前缀。

### 情况三：查询条件用到了索引中列的精确匹配，但是中间某个条件未提供。

![img](https://img-blog.csdnimg.cn/2019041516194788.png)

此时索引使用情况和情况二相同，因为title未提供，所以查询只用到了索引的第一列，而后面的from_date虽然也在索引中，但是由于title不存在而无法和左前缀连接，因此需要对结果进行扫描过滤from_date（这里由于emp_no唯一，所以不存在扫描）。如果想让from_date也使用索引而不是where过滤，可以增加一个辅助索引<emp_no, from_date>，此时上面的查询会使用这个索引。除此之外，还可以使用一种称之为“隔离列”的优化方法，将emp_no与from_date之间的“坑”填上。

首先我们看下title一共有几种不同的值：

![img](https://img-blog.csdnimg.cn/20190415162225660.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jpbmd4dWVzaXlhbmc=,size_16,color_FFFFFF,t_70)

只有7种。在这种成为“坑”的列值比较少的情况下，可以考虑用“IN”来填补这个“坑”从而形成最左前缀：

![img](https://img-blog.csdnimg.cn/20190415162249530.png) 这次key_len为59，说明索引被用全了，但是从type和rows看出IN实际上执行了一个range查询，这里检查了7个key。看下两种查询的性能比较：

![img](https://img-blog.csdnimg.cn/20190415162323835.png)

“填坑”后性能提升了一点。如果经过emp_no筛选后余下很多数据，则后者性能优势会更加明显。当然，如果title的值很多，用填坑就不合适了，必须建立辅助索引。

### 情况四：查询条件没有指定索引第一列。

![img](https://img-blog.csdnimg.cn/20190415162342445.png)

由于不是最左前缀，索引这样的查询显然用不到索引。

### 情况五：匹配某列的前缀字符串。

### ![img](https://img-blog.csdnimg.cn/20190415162409197.png)

此时可以用到索引，但是如果通配符不是只出现在末尾，则无法使用索引。（原文表述有误，如果通配符%不出现在开头，则可以用到索引，但根据具体情况不同可能只会用其中一个前缀）

### 情况六：范围查询。

![img](https://img-blog.csdnimg.cn/20190415162453245.png)

范围列可以用到索引（必须是最左前缀），但是范围列后面的列无法用到索引。同时，索引最多用于一个范围列，因此如果查询条件中有两个范围列则无法全用到索引。

![img](https://img-blog.csdnimg.cn/20190415162509917.png)

可以看到索引对第二个范围索引无能为力。这里特别要说明MySQL一个有意思的地方，那就是仅用explain可能无法区分范围索引和多值匹配，因为在type中这两者都显示为range。同时，用了“between”并不意味着就是范围查询，例如下面的查询：

![img](https://img-blog.csdnimg.cn/20190415162528872.png)

看起来是用了两个范围查询，但作用于emp_no上的“BETWEEN”实际上相当于“IN”，也就是说emp_no实际是多值精确匹配。可以看到这个查询用到了索引全部三个列。因此在MySQL中要谨慎地区分多值匹配和范围匹配，否则会对MySQL的行为产生困惑。

### 情况七：查询条件中含有函数或表达式。

很不幸，如果查询条件中含有函数或表达式，则MySQL不会为这列使用索引（虽然某些在数学意义上可以使用）。例如：

![img](https://img-blog.csdnimg.cn/2019041516254465.png)

虽然这个查询和情况五中功能相同，但是由于使用了函数left，则无法为title列应用索引，而情况五中用LIKE则可以。再如：

![img](https://img-blog.csdnimg.cn/20190415162606451.png)

显然这个查询等价于查询emp_no为10001的函数，但是由于查询条件是一个表达式，MySQL无法为其使用索引。看来MySQL还没有智能到自动优化常量表达式的程度，因此在写查询语句时尽量避免表达式出现在查询中，而是先手工私下代数运算，转换为无表达式的查询语句。

## 索引选择性与前缀索引

既然索引可以加快查询速度，那么是不是只要是查询语句需要，就建上索引？答案是否定的。因为索引虽然加快了查询速度，但索引也是有代价的：索引文件本身要消耗存储空间，同时索引会加重插入、删除和修改记录时的负担，另外，MySQL在运行时也要消耗资源维护索引，因此索引并不是越多越好。一般两种情况下不建议建索引。

第一种情况是表记录比较少，例如一两千条甚至只有几百条记录的表，没必要建索引，让查询做全表扫描就好了。至于多少条记录才算多，这个个人有个人的看法，我个人的经验是以2000作为分界线，记录数不超过 2000可以考虑不建索引，超过2000条可以酌情考虑索引。

另一种不建议建索引的情况是索引的选择性较低。所谓索引的选择性（Selectivity），是指不重复的索引值（也叫基数，Cardinality）与表记录数（#T）的比值：

Index Selectivity = Cardinality / #T

显然选择性的取值范围为(0, 1]，选择性越高的索引价值越大，这是由B+Tree的性质决定的。例如，上文用到的employees.titles表，如果title字段经常被单独查询，是否需要建索引，我们看一下它的选择性：

![img](https://img-blog.csdnimg.cn/20190415162634698.png)

title的选择性不足0.0001（精确值为0.00001579），所以实在没有什么必要为其单独建索引。

有一种与索引选择性有关的索引优化策略叫做前缀索引，就是用列的前缀代替整个列作为索引key，当前缀长度合适时，可以做到既使得前缀索引的选择性接近全列索引，同时因为索引key变短而减少了索引文件的大小和维护开销。下面以employees.employees表为例介绍前缀索引的选择和使用。

从图12可以看到employees表只有一个索引<emp_no>，那么如果我们想按名字搜索一个人，就只能全表扫描了：

![img](https://img-blog.csdnimg.cn/20190415162648370.png)

如果频繁按名字搜索员工，这样显然效率很低，因此我们可以考虑建索引。有两种选择，建<first_name>或<first_name, last_name>，看下两个索引的选择性：

![img](https://img-blog.csdnimg.cn/20190415162704846.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Jpbmd4dWVzaXlhbmc=,size_16,color_FFFFFF,t_70)

<first_name>显然选择性太低，<first_name, last_name>选择性很好，但是first_name和last_name加起来长度为30，有没有兼顾长度和选择性的办法？可以考虑用first_name和last_name的前几个字符建立索引，例如<first_name, left(last_name, 3)>，看看其选择性：

![img](https://img-blog.csdnimg.cn/20190415162722345.png)

选择性还不错，但离0.9313还是有点距离，那么把last_name前缀加到4：

![img](https://img-blog.csdnimg.cn/20190415162736101.png)

这时选择性已经很理想了，而这个索引的长度只有18，比<first_name, last_name>短了接近一半，我们把这个前缀索引 建上：

![img](https://img-blog.csdnimg.cn/20190415162753360.png)

此时再执行一遍按名字查询，比较分析一下与建索引前的结果：

![img](https://img-blog.csdnimg.cn/20190415162806389.png)

性能的提升是显著的，查询速度提高了120多倍。

前缀索引兼顾索引大小和查询速度，但是其缺点是不能用于ORDER BY和GROUP BY操作，也不能用于Covering index（即当索引本身包含查询所需全部数据时，不再访问数据文件本身）。

## InnoDB的主键选择与插入优化

在使用InnoDB存储引擎时，如果没有特别的需要，请永远使用一个与业务无关的自增字段作为主键。

经常看到有帖子或博客讨论主键选择问题，有人建议使用业务无关的自增主键，有人觉得没有必要，完全可以使用如学号或身份证号这种唯一字段作为主键。不论支持哪种论点，大多数论据都是业务层面的。如果从数据库索引优化角度看，使用InnoDB引擎而不使用自增主键绝对是一个糟糕的主意。

上文讨论过InnoDB的索引实现，InnoDB使用聚集索引，数据记录本身被存于主索引（一颗B+Tree）的叶子节点上。这就要求同一个叶子节点内（大小为一个内存页或磁盘页）的各条数据记录按主键顺序存放，因此每当有一条新的记录插入时，MySQL会根据其主键将其插入适当的节点和位置，如果页面达到装载因子（InnoDB默认为15/16），则开辟一个新的页（节点）。

如果表使用自增主键，那么每次插入新的记录，记录就会顺序添加到当前索引节点的后续位置，当一页写满，就会自动开辟一个新的页。如下图所示：

![img](http://blog.codinglabs.org/uploads/pictures/theory-of-mysql-index/13.png)图13

 

这样就会形成一个紧凑的索引结构，近似顺序填满。由于每次插入时也不需要移动已有数据，因此效率很高，也不会增加很多开销在维护索引上。

如果使用非自增主键（如果身份证号或学号等），由于每次插入主键的值近似于随机，因此每次新纪录都要被插到现有索引页得中间某个位置：

![img](http://blog.codinglabs.org/uploads/pictures/theory-of-mysql-index/14.png)图14

 

此时MySQL不得不为了将新记录插到合适位置而移动数据，甚至目标页面可能已经被回写到磁盘上而从缓存中清掉，此时又要从磁盘上读回来，这增加了很多开销，同时频繁的移动、分页操作造成了大量的碎片，得到了不够紧凑的索引结构，后续不得不通过OPTIMIZE TABLE来重建表并优化填充页面。

因此，只要可以，请尽量在InnoDB上采用自增字段做主键。

本文参考：http://blog.codinglabs.org/articles/theory-of-mysql-index.html

 

 

 

 

 

 

 

# [索引失效的7种情况](https://www.cnblogs.com/liehen2046/p/11052666.html)

## 简述

### 什么时候没用

1.有or必全有索引;
2.复合索引未用左列字段;
3.like以%开头;
4.需要类型转换;
5.where中索引列有运算;
6.where中索引列使用了函数;
7.如果mysql觉得全表扫描更快时（数据少）;

### 什么时没必要用

1.唯一性差;
2.频繁更新的字段不用（更新索引消耗）;
3.where中不用的字段;
4.索引使用<>时，效果一般;

## 详述（转）

索引并不是时时都会生效的，比如以下几种情况，将导致索引失效：

- 如果条件中有or，即使其中有部分条件带索引也不会使用(这也是为什么尽量少用or的原因)，例子中user_id无索引

注意：要想使用or，又想让索引生效，只能将or条件中的每个列都加上索引

![img](https://img2018.cnblogs.com/blog/1623038/201906/1623038-20190619181118118-1784753048.png)

- 对于复合索引，如果不使用前列，后续列也将无法使用，类电话簿。
- like查询是以%开头

![img](https://img2018.cnblogs.com/blog/1623038/201906/1623038-20190619181236139-968114236.png)

- 存在索引列的数据类型隐形转换，则用不上索引，比如列类型是字符串，那一定要在条件中将数据使用引号引用起来,否则不使用索引

![img](https://img2018.cnblogs.com/blog/1623038/201906/1623038-20190619181326223-1654473887.png)

- where 子句里对索引列上有数学运算，用不上索引

![img](https://img2018.cnblogs.com/blog/1623038/201906/1623038-20190619181436583-1773123023.png)

- where 子句里对有索引列使用函数，用不上索引

![img](https://img2018.cnblogs.com/blog/1623038/201906/1623038-20190619181457265-1885631328.png)

- 如果mysql估计使用全表扫描要比使用索引快,则不使用索引

> 比如数据量极少的表

## 什么情况下不推荐使用索引？

1) 数据唯一性差（一个字段的取值只有几种时）的字段不要使用索引

> 比如性别，只有两种可能数据。意味着索引的二叉树级别少，多是平级。这样的二叉树查找无异于全表扫描。

2) 频繁更新的字段不要使用索引

> 比如logincount登录次数，频繁变化导致索引也频繁变化，增大数据库工作量，降低效率。

3) 字段不在where语句出现时不要添加索引,如果where后含IS NULL /IS NOT NULL/ like ‘%输入符%’等条件，不建议使用索引

> 只有在where语句出现，mysql才会去使用索引

4） where 子句里对索引列使用不等于（<>），使用索引效果一般

 

 

 

 

 

 

# 索引失效和注意事项

https://blog.csdn.net/hehexiaoxia/article/details/54312130

## 索引失效的情况

如果是同样的sql如果在之前能够使用到索引，那么现在使用不到索引，以下几种主要情况:

> 1. 随着表的增长，where条件出来的数据太多，大于15%，使得索引失效（会导致CBO计算走索引花费大于走全表）
> 2. 统计信息失效 需要重新搜集统计信息
> 3. 索引本身失效 需要重建索引

具体情况：

1.单独引用复合索引里非第一位置的索引列

> 假如有INDEX(a,b,c)，
> 当条件为a或a,b或a,b,c时都可以使用索引，
> 但是当条件为b,c时将不会使用索引。
>
> 复合索引遵守“最左前缀”原则，即在查询条件中使用了复合索引的第一个字段，索引才会被使用。因此，在复合索引中索引列的顺序至关重要。如果不是按照索引的最左列开始查找，则无法使用索引。

2.对索引列运算，运算包括（+、-、*、/、！、<>、%、like’%_’（%放在前面）、or、in、exist等），导致索引失效。

> 错误的例子：select * from test where id-1=9;
> 正确的例子：select * from test where id=10;
> 注意！！
> mysql sql 中如果使用了 not in ， not exists ， （<> 不等于 ！=） 这些不走
> < 小于 > 大于 <= >= 这个根据实际查询数据来判断，如果全盘扫描速度比索引速度要快则不走索引 。

3.对索引应用内部函数，这种情况下应该建立基于函数的索引。

> select * from template t where ROUND(t.logicdb_id) = 1
> 此时应该建ROUND(t.logicdb_id)为索引。

4、类型错误，如字段类型为varchar，where条件用number。

> 例：template_id字段是varchar类型。
>
> 错误写法：select * from template t where t.template_id = 1
>
> 正确写法：select * from template t where t.template_id = ‘1’

5.如果MySQL预计使用全表扫描要比使用索引快，则不使用索引
6.like的模糊查询以%开头，索引失效
7.索引列没有限制 not null，索引不存储空值，如果不限制索引列是not null，oracle会认为索引列有可能存在空值，所以不会按照索引计算

------

## 索引注意事项

https://blog.csdn.net/qq_16239775/article/details/79665972

1.索引不会包含有NULL值的列

只要列中包含有NULL值都将不会被包含在索引中，复合索引中只要有一列含有NULL值，那么这一列对于此复合索引就是无效的。所以我们在数据库设计时不要让字段的默认值为NULL。应该用0、一个特殊的值或者一个空串代替空值。

2.复合索引

比如有一条语句是这样的：`select * from users wherearea=’beijing’ and age=22;`如果我们是在area和age上分别创建单个索引的话，由于mysql查询每次只能使用一个索引，所以虽然这样已经相对不做索引时全表扫描提高了很多效率，但是如果在area、age两列上创建复合索引的话将带来更高的效率。如果我们创建了(area,age,salary)的复合索引，那么其实相当于创建了(area,age,salary)、(area,age)、(area)三个索引，这被称为最佳左前缀特性。因此我们在创建复合索引时应该将最常用作限制条件的列放在最左边，依次递减。

3.使用短索引

对串列进行索引，如果可能应该指定一个前缀长度。例如，如果有一个CHAR(255)的列，如果在前10 个或20 个字符内，多数值是惟一的，那么就不要对整个列进行索引。短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作。

4.排序的索引问题

mysql查询只使用一个索引，因此如果where子句中已经使用了索引的话，那么order by中的列是不会使用索引的。因此数据库默认排序可以符合要求的情况下不要使用排序操作；尽量不要包含多个列的排序，如果需要最好给这些列创建复合索引。

5.like语句操作

一般情况下不鼓励使用like操作，如果非使用不可，如何使用也是一个问题。like“%aaa%” 不会使用索引而like“aaa%”可以使用索引。

6.不要在列上进行运算

select* from users where YEAR(adddate)

7.不使用NOT IN操作

NOT IN操作都不会使用索引将进行全表扫描。NOT IN可以NOT EXISTS代替

------

# 索引的优缺点

优点：

> 第一，通过创建唯一性索引，可以保证数据库表中每一行数据的唯一性。
> 第二，可以大大加快 数据的检索速度，这也是创建索引的最主要的原因。
> 第三，可以加速表和表之间的连接，特别是在实现数据的参考完整性方面特别有意义。
> 第四，在使用分组和排序子句进行数据检索时，同样可以显著减少查询中分组和排序的时间。
> 第五，通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统的性能。

覆盖索引的好处

> 如果一个索引包含所有需要的查询的字段的值，直接根据索引的查询结果返回数据，而无需读表，能够极大的提高性能。因此，可以定义一个让索引包含的额外的列，即使这个列对于索引而言是无用的。

缺点：

> 第一，创建索引和维护索引要耗费时间，这种时间随着数据量的增加而增加；
>
> 第二，索引需要占物理空间，除了数据表占数据空间之外，每一个索引还要占一定的物理空间，如果要建立聚簇索引，那么需要的空间就会更大，如果非聚集索引很多，一旦聚集索引改变，那么所有非聚集索引都会跟着变；
>
> 第三，当对表中的数据进行增加、删除和修改的时候，索引也要动态的维护，一旦一个数据改变，并且改变的列比较多，可能会引起好几个索引跟着改变，这样就降低了数据的维护速度。
>
> 第四、每个索引都有统计信息，索引越多统计信息越多，过多索引会导致优化器优化过程需要评估的组合增多。创建索引的时候，应该仔细考虑在哪些列上可以创建索引，在哪些列上不能创建索引。

------

## 如何选择合适的列创建索引

1 在经常需要搜索的列上，可以加快搜索的速度；

2 在作为主键的列上，强制该列的唯一性和组织表中数据的排列结构；

3 在经常用在连接的列上，这些列主要是一些外键，可以加快连接的速度；

4 在经常需要根据范围进行搜索的列上创建索引，因为索引已经排序，其指定的范围是连续的；这样查询可以利用索引的排序，加快排序查询时间；

5 在经常使用在WHERE子句中的列上面创建索引，加快条件的判断速度。当增加索引时，会提高检索性能，但是会降低修改性能

6 唯一性很差的字段不合适做索引，如性别

7 更新频繁的字段不适合，耗时且影响性能

------

## 索引分类

索引可以分为簇索引和非簇索引

> 簇索引通过重排表中的数据来提高数据的访问速度，
> 非簇索引则通过维护表中的数据指针来提高数据的索引。

聚簇索引的体系结构：

索引的结构类似于树状结构，树的顶部称为叶级，树的其它部分称为非叶级，树的根部在非叶级中。同样，在聚簇索引中，聚簇索引的叶级和非叶级构成了一个树状结构，索引的最低级是叶级。在聚簇索引中，表中的数据所在的数据页是叶级，在叶级之上的索引页是非叶级，索引数据所在的索引页是非叶级。在聚簇索引中，数据值的顺序总是按照升序排列。应该在表中经常搜索的列或者按照顺序访问的列上创建聚簇索引。

当创建聚簇索引时，应该考虑这些因素：

（1）每一个表只能有一个聚簇索引，因为表中数据的物理顺序只能有一个；

（2）表中行的物理顺序和索引中行的物理顺序是相同的，在创建任何非聚簇索引之前创建聚簇索引，这是因为聚簇索引改变了表中行的物理顺序，数据行 按照一定的顺序排列，并且自动维护这个顺序；

（3）关键值的唯一性要么使用UNIQUE关键字明确维护，要么由一个内部的唯一标识符明确维护，这些唯一性标识符是系统自己使用的，用户不能访问；

（4）聚簇索引的平均大小大约是数据表的百分之五，但是，实际的聚簇索引的大小常常根据索引列的大小变化而变化；

（5）在索引的创建过程中，SQL Server临时使用当前数据库的磁盘空间，当创建聚簇索引时，需要1.2倍的表空间的大小，因此，一定要保证有足够的空间来创建聚簇索引。

------

## 主键约束与主键索引

> 主键约束是一种保持数据完整性的逻辑，它限制表中的记录有相同的主键记录。
> 在创建主键约束时，系统自动创建了一个唯一性的聚簇索引。

虽然，在逻辑上，主键约束是一种重要的结构，但是，在物理结构上，与主键约束相对应的结构是唯一性的聚簇索引。换句话说，在物理实现上，不存在主键约束，而只存在唯一性的聚簇索引。同样，在创建唯一性键约束时，也同时创建了索引，这种索引则是唯一性的聚簇索引。因此，当使用约束创建索引时，索引的类型和特征基本上都已经确定了，由用户定制的余地比较小。

当在表上定义主键或者唯一性键约束时，如果表中已经有了使用CREATE INDEX语句创建的标准索引时，那么主键约束或者唯一性键约束创建的索引覆 盖以前创建的标准索引。也就是说，主键约束或者唯一性键约束创建的索引的优先级高于使用CREATE INDEX语句创建的索引。当创建唯一性索引时，应 该认真考虑这些规则：

当在表中创建主键约束或者唯一性键约束时，SQL Server自动创建一个唯一性索引；

如果表中已经包含有数据，那么当创建索引时，SQL Server检查表中已有数据的冗余性；

每当使用插入语句插入数据或者使用修改语句修改数据时，SQL Server检查数据的冗余性：如果有冗余值，那么SQL Server取消该语句的执行，并且返回一个错误消息；确保表中的每一行数据都有一个唯一值，这样可以确保每一个实体都可以唯一确认；

只能在可以保证实体完整性的列上创建唯一性索引。

复合索引

```
索引可以包含一个、两个或更多个列。两个或更多个列上的索引被称作复合索引
```

- 1

当创建复合索引时，应该考虑这些规则：

> （1）最多可以把16个列合并成一个单独的复合索引，构成复合索引的列的总长度不能超过900字节，也就是说复合列的长度不能太长；
>
> （2）在复合索引中，所有的列必须来自同一个表中，不能跨表建立复合列；
>
> （3）在复合索引中，列的排列顺序是非常重要的，因此要认真排列列的顺序，原则上，应该首先定义最唯一的列，例如在（COL1，COL2）上的索引与在（COL2，COL1）上的索引是不相同的，因为两个索引的列的顺序不同；
>
> （4）为了使查询优化器使用复合索引，查询语句中的WHERE子句必须参考复合索引中第一个列；
>
> （5）当表中有多个关键列时，复合索引是非常有用的；使用复合索引可以提高查询性能，减少在一个表中所创建的索引数量。

------

## 让or使用索引

https://blog.csdn.net/hguisu/article/details/7106159

1 .where 语句里面如果带有or条件, myisam表能用到索引， innodb不行。

1)myisam表：
CREATE TABLE IF NOT EXISTS `a` (
`id` int(1) NOT NULL AUTO_INCREMENT,
`uid` int(11) NOT NULL,
`aNum` char(20) DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `uid` (`uid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

mysql> explain select * from a where id=1 or uid =2;
+—-+————-+——-+————-+—————+————-+———+——+——+—————————————+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+—-+————-+——-+————-+—————+————-+———+——+——+—————————————+
| 1 | SIMPLE | a | index_merge | PRIMARY,uid | PRIMARY,uid | 4,4 | NULL | 2 | Using union(PRIMARY,uid); Using where |
+—-+————-+——-+————-+—————+————-+———+——+——+—————————————+
1 row in set (0.00 sec)

2)innodb表：

CREATE TABLE IF NOT EXISTS `a` (
`id` int(1) NOT NULL AUTO_INCREMENT,
`uid` int(11) NOT NULL,
`aNum` char(20) DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

mysql> explain select * from a where id=1 or uid =2;
+—-+————-+——-+——+—————+——+———+——+——+————-+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+—-+————-+——-+——+—————+——+———+——+——+————-+
| 1 | SIMPLE | a | ALL | PRIMARY,uid | NULL | NULL | NULL | 5 | Using where |
+—-+————-+——-+——+—————+——+———+——+——+————-+
1 row in set (0.00 sec)

2 .必须所有的or条件都必须是独立索引：
+——-+———————————————————————————————————————-
| Table | Create Table
+——-+———————————————————————————————————————-
| a | CREATE TABLE `a` (
`id` int(1) NOT NULL AUTO_INCREMENT,
`uid` int(11) NOT NULL,
`aNum` char(20) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 |
+——-+———————————————————————————————————————-
1 row in set (0.00 sec)

explain查看：
mysql> explain select * from a where id=1 or uid =2;
+—-+————-+——-+——+—————+——+———+——+——+————-+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+—-+————-+——-+——+—————+——+———+——+——+————-+
| 1 | SIMPLE | a | ALL | PRIMARY | NULL | NULL | NULL | 5 | Using where |
+—-+————-+——-+——+—————+——+———+——+——+————-+
1 row in set (0.00 sec)

全表扫描了。

\3. 用UNION替换OR (适用于索引列)
通常情况下, 用UNION替换WHERE子句中的OR将会起到较好的效果. 对索引列使用OR将造成全表扫描.
注意, 以上规则只针对多个索引列有效. 如果有column没有被索引, 查询效率可能会因为你没有选择OR而降低.

在下面的例子中, LOC_ID 和REGION上都建有索引.

```
//高效
select loc_id , loc_desc , region from location where loc_id = 10 
union 
select loc_id , loc_desc , region  from location where region = "melbourne" 
//低效
select loc_id , loc desc , region from location where loc_id = 10 or region = "melbourne"
```

如果你坚持要用OR, 那就需要返回记录最少的索引列写在最前面.

\4. 用in来替换or
这是一条简单易记的规则，但是实际的执行效果还须检验，在oracle8i下，两者的执行路径似乎是相同的．　

```
//低效: 
select…. from location where loc_id = 10 or loc_id = 20 or loc_id = 30 
//高效 
select… from location where loc_in  in (10,20,30);
```

------

## IN vs Exists

作者：IronM
链接：https://www.jianshu.com/p/f212527d76ff
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

```
select * from A where id in (select id from B);

select * from A where exists (select 1 from B where A.id=B.id);对于以上两种情况，in是在内存里遍历比较，而exists需要查询数据库，所以当B表数据量较大时，exists效率优于in。
```

1、IN()语句内部工作原理
IN()只执行一次，它查出B表中的所有id字段并缓存起来。之后，检查A表的id是否与B表中的id相等，如果相等则将A表的记录加入结果集中，直到遍历完A表的所有记录。
它的查询过程类似于以下过程：

```
List resultSet={};
Array A=(select * from A);
Array B=(select id from B);

for(int i=0;i<A.length;i++) {
  for(int j=0;j<B.length;j++) {
      if(A[i].id==B[j].id) {
        resultSet.add(A[i]);
        break;
      }
  }
}
return resultSet;
```

可以看出，当B表数据较大时不适合使用in()，因为它会B表数据全部遍历一次

2、EXISTS()语句内部工作原理
exists()会执行A.length次，它并不缓存exists()结果集，因为exists()结果集的内容并不重要，重要的是其内查询语句的结果集空或者非空，空则返回false，非空则返回true。
它的查询过程类似于以下过程：

```
List resultSet={};
Array A=(select * from A);

for(int i=0;i<A.length;i++) {
   if(exists(A[i].id) {  //执行select 1 from B where B.id=A.id是否有记录返回
       resultSet.add(A[i]);
   }
}
return resultSet;
```

当B表比A表数据大时适合使用exists()，因为它没有那么多遍历操作，只需要再执行一次查询就行。

> 例1：A表有10000条记录，B表有1000000条记录，那么exists()会执行10000次去判断A表中的id是否与B表中的id相等。
> 例2：A表有10000条记录，B表有100000000条记录，那么exists()还是执行10000次，因为它只执行A.length次，可见B表数据越多，越适合exists()发挥效果。
> 例3：A表有10000条记录，B表有100条记录，那么exists()还是执行10000次，还不如使用in()遍历10000*100次，因为in()是在内存里遍历比较，而exists()需要查询数据库，我们都知道查询数据库所消耗的性能更高，而内存比较很快。

结论：EXISTS()适合B表比A表数据大的情况

3、使用情况分析

当A表数据与B表数据一样大时，in与exists效率差不多，可任选一个使用。

在插入记录前，需要检查这条记录是否已经存在，只有当记录不存在时才执行插入操作，可以通过使用 EXISTS 条件句防止插入重复记录。

```
insert into A (name,age) select name,age from B where not exists (select 1 from A where A.id=B.id);
```

EXISTS与IN的使用效率的问题，通常情况下采用exists要比in效率高，因为IN不走索引。但要看实际情况具体使用：

> IN适合于外表大而内表小的情况；
> EXISTS适合于外表小而内表大的情况。

4、关于EXISTS：

EXISTS用于检查子查询是否至少会返回一行数据，该子查询实际上并不返回任何数据，而是返回值True或False。

EXISTS 指定一个子查询，检测行的存在。

EXISTS(包括 NOT EXISTS )子句的返回值是一个boolean值。 EXISTS内部有一个子查询语句(SELECT … FROM…),我将其称为EXIST的内查询语句。其内查询语句返回一个结果集, EXISTS子句根据其内查询语句的结果集空或者非空，返回一个布尔值。

一种通俗的可以理解为：将外查询表的每一行，代入内查询作为检验，如果内查询返回的结果取非空值，则EXISTS子句返回TRUE，这一行行可作为外查询的结果行，否则不能作为结果。

 