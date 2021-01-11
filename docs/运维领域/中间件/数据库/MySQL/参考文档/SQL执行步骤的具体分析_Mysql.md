 更新时间：2017年10月10日 16:23:59  作者：牧师-Panda  

这篇文章主要介绍了SQL执行步骤的具体分析的相关资料,希望通过本文能帮助到大家，让大家理解掌握SQL是如何执行的，需要的朋友可以参考下

**SQL执行步骤的具体分析**

先来看执行语句的顺序

```
(8)``select` `(9)``distinct` `A (1)``from` `Ta (3)``join` `Tb ``(2)``on` `XXX (4)``where` `XXX (5)``group` `by` `XXX (6)``with``{``cube``|roll up} (7)``having` `XXX (10)``order` `by` `XXX (11)limit XXX
```

 接着我们看一下具体分析查询处理的各个阶段：

1. FROM 对from子句中的左表和右表执行笛卡尔集，产生虚拟表VT1
2. ON 对虚拟表VT1进行on筛选，只有那些符合join condition的行才被插入虚拟表VT2中
3. JOIN 如果指定了outer join，那么保留表中未匹配的行作为外部行添加到虚拟表VT2中，产生虚拟表VT3。如果from子句包含两个以上的表，则对上一个连接生成的结果表中VT3和下一个表重复执行步骤1~步骤3，直到处理完所有的表为止。
4. WHERE 对虚拟表VT3进行where过滤条件，只有符合条件的才被插入到虚拟表VT4中。
5. GROUP BY 根据group by子句中的列，对VT4中的记录进行分组操作，产生VT5.
6. CUBE|ROLL UP 对表VT5进行CUBE或者ROLLUP操作，产生表VT6.
7. HAVING 对虚拟表VT6应用having过滤器，只有符合条件的记录才会被插入到虚拟表VT7中
8. SELECT 第二次执行select操作，选择指定的列，插入到虚拟表VT8中。
9. DISTINCT 去除重复数据，产生虚拟表VT9。
10. ORDER BY 将虚拟表VT9中的记录按照指定的要求进行排序操作，产生虚拟表VT10
11. LIMIT 取出指定行的记录，产生虚拟表VT11，并返回给查询用户