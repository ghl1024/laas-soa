# Loki QL查询语句

![img](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[等风来也chen](https://blog.csdn.net/weixin_44267608) 2020-04-02 10:53:57 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes.png) 2075 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect.png) 收藏 1

分类专栏： [Loki](https://blog.csdn.net/weixin_44267608/category_8817489.html) 文章标签： [loki](https://www.csdn.net/tags/MtzaMg0sODczMzYtYmxvZwO0O0OO0O0O.html) [QL](https://so.csdn.net/so/search/s.do?q=QL&t=blog&o=vip&s=&l=&f=&viparticle=) [查询语句](https://www.csdn.net/tags/MtTaEg0sMTc5MzMtYmxvZwO0O0OO0O0O.html)

版权

## LogQL：日志查询语言

基本的LogQL查询由两部分组成：log stream selector、filter expression

## Log stream selector

它由一个或多个键值对组成，每个键是一个日志标签，值的话是标签的值，例如

```c
{app="mysql",name="mysql-backup"}
1
```

在这个例子中，记录具有的标签流app，其值是mysql 和的一个标签name，它的值mysql-backup将被包括在查询结果。注意，这将匹配其标签至少 包含mysql-backup其名称标签的任何日志流；如果有多个包含该标签的流，则所有匹配流的日志将显示在结果中。

支持以下标签匹配运算符：

- =：完全相等。
- !=：不相等。
- =~：正则表达式匹配。
- !~：正则表达式不匹配。

适用于Prometheus标签选择器的相同规则也适用 于Loki日志流选择器。

## Filter expression

写入日志流选择器后，可以使用搜索表达式进一步过滤生成的日志集。搜索表达式可以只是文本或正则表达式：

- {job=“mysql”} |= “error”
- {name=“kafka”} |~ “tsdb-ops.*io:2003”
- {instance=~“kafka-[23]”,name=“kafka”} !=
  kafka.server:type=ReplicaManager

运算符说明

- |=：日志行包含字符串。
- !=：日志行不包含字符串。
- |~：日志行匹配正则表达式。
- !~：日志行与正则表达式不匹配。

## 指标查询

### 范围向量

LogQL 与Prometheus 具有相同的范围向量概念，不同之处在于所选的样本范围包括每个日志条目的值1。可以在所选范围内应用聚合，以将其转换为实例向量。

**注：对于此种查询，需要添加数据源，选择promethes，但是地址为loki的地址，并在最后添加/loki即可**

当前支持的操作功能为：

- rate：计算每秒的条目数
- count_over_time：计算给定范围内每个日志流的条目。

//对fluent-bit作业在最近五分钟内的所有日志行进行计数。

```c
count_over_time({job="fluent-bit"}[5m])    
1
```

获取fluent-bit作业在过去十秒内所有非超时错误的每秒速率。

```c
rate({job="fluent-bit"} |= "error" != "timeout" [10s]  
1
```

### 集合运算符

与PromQL一样，LogQL支持内置聚合运算符的一个子集，可用于聚合单个向量的元素，从而产生具有更少元素但具有集合值的新向量：

- sum：计算标签上的总和
- min：选择最少的标签
- max：选择标签上方的最大值
- avg：计算标签上的平均值
- stddev：计算标签上的总体标准差
- stdvar：计算标签上的总体标准方差
- count：计算向量中元素的数量
- bottomk：通过样本值选择最小的k个元素
- topk：通过样本值选择最大的k个元素

可以通过包含a without或 by子句，使用聚合运算符聚合所有标签值或一组不同的标签值：

```c
<aggr-op>([parameter,] <vector expression>) [without|by (<label list>)]
1
```

举例：

统计最高日志吞吐量按container排序前十的应用程序

```c
topk(10,sum(rate({job="fluent-bit"}[5m])) by(container))
1
```

获取最近五分钟内的日志计数，按级别分组

```c
sum(count_over_time({job="fluent-bit"}[5m])) by (level)
1
```

更多内容请参考：https://github.com/grafana/loki/blob/master/docs/logql.md