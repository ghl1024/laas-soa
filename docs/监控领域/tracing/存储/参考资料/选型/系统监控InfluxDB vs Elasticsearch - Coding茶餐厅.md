# [系统监控:InfluxDB vs Elasticsearch](http://razil.cc/post/2017/10/influxdbvselasticsearch/)

By

 2017年10月19日

## 前言

译者: [Razil](http://razil.cc/post/2017/10/influxdbvselasticsearch/razil.cc)
本文译自: [System monitoring with InfluxDB vs Elasticsearch](http://www.spectory.com/blog/System monitoring with InfluxDB vs Elasticsearch)

系统的监控一直都扮演着重要角色。它能帮助我们了解系统的健康情况,发现问题甚至能预测问题。
如今，由于以下这些原因监控变得越来越重要:

- 云服务（存储价格的降低）使我们可以一直监控和存储几乎所有东西
- 系统变得越来越复杂。系统包含了各种各样的灵活部件比如虚拟机、docker、数据库和服务,应有尽有。
- 物联网的逐步普及使得大量的硬件设备需要我们去追踪和监测。
- 数据分析得以升级，让我们只需要通过关注系统的稳定性和健康状态，就能达到了解客户需求、掌握发展趋势、对客户进行分类等多种目的。

本文将对比两个流行的监控解决方案。两者有着不同的处理方法和实现方式，相比起来各有千秋。 首先是TICK框架中的InfluxDB，第二个是ELK框架中的Elasticsearch。

## 什么是监控？

监控由以下活动组成：

- 采集数据
- 保存数据
- 可视化数据
- 产生告警

## TICK

Tick框架:

- Telegraf - 用于在系统运行时从系统或者其他服务采集指标和数据
- InfluxDB - 高可用和高性能的时序数据库
- Chronograf - 数据可视化的web应用
- Kapacitor - 告警和数据处理引擎

本框架的而核心是时序数据库InfluxDB。时序数据库(Time series database TSDB)是一个为了处理时序数据(一系列由时间作为索引的数据)而特别优化的软件系统。例如，一段时间内锅炉里的水温或者一段时间内CPU的使用率。TSDB是一个NoSQL数据库，它支持增删改查操作和条件查询。与其他类型数据库最大的区别在于，它能在数据量庞大的情况下对时间索引维护的最优化。其他主要的时序数据库有 Graphite,Prometheus,OpenTSDB等等。我选择InfluxDB的真实原因是它是一个现代的数据库，用Go语言编写，非常容易安装和配置，而且性能出色。

### InfluxDB的数据模型

InfluxDB 是一种无模式数据库。我们可以任意添加series,measurements和tags。例如：

```
app_degrees, country=Canada, city=Toronto degree=77.5 1422568543702900257
```

相关术语（这里表述的还是比较抽象，括号是本人的理解）:

- Measurement - 一个数字值 (相当于关系型数据里的一个表)
- Series - 数据收集和分析的单位 (一个表里数据的系列,可以理解为多条曲线)
- Tag - Key/Value 键值对,可选,用于描述measurement (字符串型的键值对，用于描述这个点，可以用作索引)
- Timestamp - Measurement的确切时间点(微妙级时间戳)

这个模型是的我们可以高效而且便捷地插入Measurements。

### InfluxDB的读写

InfluxDB有支持许多语言例如Ruby、Go、Java、Node等等的HTTP API和客户端库。 InfluxDB支持通过API写入单条数据或从文件获取然后写入多行数据。 InfluxDB拥有非常近似SQL的查询语言。查询例子如下：

```
select degrees from app_degrees where country = ‘Canada’
```

它拥有以下查询描述: SELECT、WHERE、GROUP BY、ORDER BY、LIMIT 等等。这对于拥有SQL相关知识的开发者会 来说会觉得非常方便。
查询结构将以JSON结构展示。

### 数据可视化

“TICK”框架会通过Chronograf这款WEB应用进行对(InfluxDB中的)series的展示。它可以生成图像、表格仪表图等等。它有着非常容易上手的用户体验可以让你在短时间内构建一个仪表图。

### 其他特性

- Retention policy - 你可以配置是否自动删除过期数据
- Continues queries - 自动完成数据的聚合
- High availability - 高可用(商业版支持集群，社区办只能支持单机)

## ELK

ELK框架: + Elasticsearch - 一个基于Lucene的搜索引擎 + Logstash - 数据采集、整理和流水线传输。通过连接器与其他公共组件相连 + Kibana - 数据可视化平台

“Elastic”官方提供了一些补充的产品，为框架增加了丰富了许多功能，例如用于安全的”Shield”，用于告警的Wtercher”等等。 等。然而这些产品都并不开源，也不免费。

### Elasticsearch

Elasticsearch是一个基于apache Lucene的搜索引擎。本质上是一个为了全文搜索(例如谷歌搜索)而进行特别调整NoSQL数据库。 Elasticsearch支持分布式、可伸缩而且高可用。它非常容易去安全和配置。目前Elasticsearch非常流行，有着非常好的相关生态。 Elasticsearch也是无模式而且用JSON格式保存数据(就像MonogDB)的数据库。它为所有字段都建了索引，拥有许多能力，比如复杂的文本查询、文本高亮、联想、定位等等。 它也拥有许多restful API和多种语言的客户端。对于全文搜索能力，需要补充的是Elasticsearch也支持时序数据，这让他也成为系统监控的有优秀备选者。我们不仅可以进行系统监控还能对日志进行全文搜索。它能在不增加别的数据库情况下增加多些功能。

### Logstash

Logstash是一个数据采集器，基本上它用于：
\+ 从数据源获取数据 + 筛选数据，完善数据 + 将数据发送到目标

所有这些操作都在一个文件内配置。
Logstash有许多输入插件，可以让它从各种不同的数据源获取数据例如文件、HTTP、log4j、syslog等等。你只需要去配置数据源，Logstash就会帮你从数据源获取数据。
Logstash也拥有许多插件用于筛选和处理数据例如聚合、解析、转换甚至让你可以用Ruby来编程。
输出也同样，你可以将数据传输到许多输出接口，首选的当然就是Elasticsearch，但同样也有文件、Redis、Kafka甚至InfluxDB等等。如果有缺漏不支持的，有教程可以指导你编写出自己的插件。

### 数据可视化

Kibana相对于Chronograf来说会更复杂些。它拥有更多的功能例如各种各样的图表，地图的GEO定位等等。我想顺便也提一下Grafana，她也是一个非常出色可视化工具，可同样搭配Elasticsearch和InfluxDB。

## 哪一方更好？

两个解决方案都很棒，他们都是可伸缩、支持高可用、容易安装配置和维护。而且两者都是开源和免费。在性能测试上，InfluxData(开发InfluxDB的公司)表现更为出色。但Elasticsearch可以承受到目前为止一个常规系统能够承受巨大的负载。
Elasticsearch拥有一个超越InfluxDB的优点，就是全文搜索的能力。如果你想要保存日志(消息)和使用它们，这将会是一个非常有用的功能。为了让时序数据库比如InfluxDB的拥有这些功能，我们还需要增加其他支持这些功能的数据库。这会让系统更加复杂。为了实现监控我们将会不得不维护两个数据库，万一发生错误需要同步他们，可能增加一个消息队列例如RabbitMQ,所有的这些都会大大增加时间和金钱成本。
我想对于工具的选择还是要根据需求。如果监控系统仅仅需要监测时间段的数据，我会选择InfluxDB，因为它更适合这项工作。如果需要保存日志或者文本数据，为了简化工作，我会选择Elasticsearch。

## 引用

- https://en.wikipedia.org/wiki/Time_series_database
- https://www.influxdata.com/
- https://www.elastic.co/