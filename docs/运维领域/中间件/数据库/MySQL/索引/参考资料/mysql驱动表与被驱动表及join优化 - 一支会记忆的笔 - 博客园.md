# [mysql驱动表与被驱动表及join优化](https://www.cnblogs.com/JonaLin/p/11392613.html)

驱动表与被驱动表


先了解在join连接时哪个表是驱动表，哪个表是被驱动表：
1.当使用left join时，左表是驱动表，右表是被驱动表
2.当使用right join时，右表时驱动表，左表是驱动表
3.当使用join时，mysql会选择数据量比较小的表作为驱动表，大表作为被驱动表

join查询如何选择驱动表与被驱动表


　　在sql优化中，永远是以小表驱动大表。

例如: A是小表，B是大表
　　使用left join 时，则应该这样写select * from A a left join B b on a.code=b.code
　　A表时驱动表，B表是被驱动表

测试：A表140多条数据，B表20万左右的数据量
　　select * from A a left join B b on a.code=b.code
　　执行时间：7.5s

　　select * from B b left join A a on a.code=b.code
　　执行时间：19s

结论：小表驱动大表优于大表驱动小表

join查询在有索引条件下
　　驱动表有索引不会使用到索引
　　被驱动表建立索引会使用到索引

在以小表驱动大表的情况下，再给大表建立索引会大大提高执行速度

测试：给A表，B表建立索引
分析：EXPLAIN select * from A a left join B b on a.code=b.code

只有B表code使用到索引

如果只给A表的code建立索引会是什么情况？

在这种情况下，A表索引失效

结论：给被驱动表建立索引

驱动表的含义
MySQL 表关联的算法是 Nest Loop Join，是通过驱动表的结果集作为循环基础数据，然后一条一条地通过该结果集中的数据作为过滤条件到下一个表中查询数据
，然后合并结果。如果还有第三个参与Join，则再通过前两个表的Join结果集作为循环基础数据，再一次通过循环查询条件到第三个表中查询数据，如此往复。

例如：
小表驱动大表：
for(140条){
for(20万条){

}
}

大表驱动小表：
for(20万条){
for(140条){

}
}

大表驱动小表，要通过20万次的连接
小表驱动小表，只需要通过140多次的连接就可以了

所以也可以得出结论
如果A表，B表数据量差不多大的时候，那么选择谁作为驱动表也是无所谓了

忘了补充一句，也可以通过EXPLAIN分析来判断在sql中谁是驱动表，EXPLAIN语句分析出来的第一行的表即是驱动表

结论
1.以小表驱动大表
2.给被驱动表建立索引
————————————————
本文来源于：https://blog.csdn.net/qq_20891495/article/details/93744495