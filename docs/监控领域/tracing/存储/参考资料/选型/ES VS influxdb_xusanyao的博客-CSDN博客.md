# ES VS influxdb

![img](ES VS influxdb_xusanyao的博客-CSDN博客.assets/original.png)

[_从头再来_](https://blog.csdn.net/sanyaoxu_2) 2020-05-27 22:59:15 ![img](ES VS influxdb_xusanyao的博客-CSDN博客.assets/articleReadEyes.png) 178 ![img](ES VS influxdb_xusanyao的博客-CSDN博客.assets/tobarCollect.png) 收藏

分类专栏： [数据库](https://blog.csdn.net/sanyaoxu_2/category_7368587.html)

版权

简介
最近一直在使用ES，之前也使用过influxdb。使用过程中两者在某些功能上有些类似。所以这里对两者一些区别和功能进行整理。已更好了解这两者工具。

ES和influxdb介绍
ES
是一个基于lucence的实时搜索服务器，本身是一个应用。
没有UI管理界面。
支持restful格式http接口来操作和展示界面，数据展示依靠Kibana。
influxdb
开源分布式时序、事件和指标数据库。使用 Go 语言编写，无需外部依赖。其设计目标是实现分布式和水平伸缩扩展。
自带管理界面，界面自带简单的图表

提供类似sql的查询语言。
展示图表可以使用grafana
**区别**
ES支持全文检索.
主要是针对term（关键字）。在时序数据的某些和处理上influxdb好于ES。
对于数字的一些监控，建议使用influxdb。而对于日志，文本可以使用ES。
两者都可以使用grafana做为展示。
es vs influxdb性能测试 ： the rates of data ingestion, on-disk data compression, and query performance. InfluxDB outperformed Elasticsearch in all three tests with 8x greater write throughput, while using 4x less disk space when compared against Elastic’s time series optimized configuration, and delivering 3.5x to 7.5x faster response times for tested queries.

写性能

 

查询性能

 

在这里顺便提一下Grafana和Kibana两个监控平台的数据展示界面
\- Kibana是和ES配套的数据展示工具。只支持ES。同时也有丰富的图表功能。因为与ES配套，所以Kibana更适合去分析日志。
\- Grafana是一个开源的支持包括ES和influxdb多种数据源，有用户权限验证功能。Grafana更适合展示数据。

influxdb实际案例

[美团-支付通话自动化运维](https://tech.meituan.com/2017/10/27/pay-paygw-automation-system.html)
 

参考
[es vs influxdb性能测试](https://www.influxdata.com/blog/influxdb-markedly-elasticsearch-in-time-series-data-metrics-benchmark/)
[开源influxdb 介绍](https://segmentfault.com/a/1190000000444617)
[玩转ElasticSearch- 降维打击！使用ElasticSearch作为时序数据库](https://yq.aliyun.com/articles/72749?t=t1)
里面介绍了使用ES作为时序数据库的原因。
原文地址：https://blog.csdn.net/a314773862/article/details/78446957