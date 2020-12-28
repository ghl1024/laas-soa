# InfluxDB与ElasticSearch

[![img](InfluxDB与ElasticSearch - 简书.assets/12e8e919-ef5e-4f20-8f70-261d0b4a838e)](https://www.jianshu.com/u/ccbf26e472e0)

[andywangzhen](https://www.jianshu.com/u/ccbf26e472e0)关注

2020.02.24 12:45:35字数 641阅读 1,221

2020，开年就经历了疫情，这个年就过的有点长。随着春暖花开，全国各地都逐渐好转了，中国加油！

之前使用过InfluxDB做过SaaS服务，用于数据统计和展示；也使用过ES做时序数据的存储和数据统计。那么根据不同的情况，如何做出选择呢？

## 性能对比

提到数据服务，就不能不提读写性能。
我没有实际做过压测，我们就通过一篇官方文档，来了解一下：

> 在过去的几周中，我们着手比较了InfluxDB和Elasticsearch在时间序列工作负载方面的性能和功能，特别着眼于数据摄取率，磁盘上数据压缩率和查询性能。与Elastic的时间序列优化配置相比，InfluxDB在两项测试中均胜过Elasticsearch，写吞吐量提高了6.1 倍，而磁盘空间却减少了2.5倍。与来自Elasticsearch的缓存查询的响应时间相比，InfluxDB 对测试查询的响应时间缩短了 8.2倍。
> 原文：[InfluxDB与Elasticsearch的时间序列数据和指标基准](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.influxdata.com%2Fblog%2Finfluxdb-markedly-elasticsearch-in-time-series-data-metrics-benchmark%2F)

## 适用场景

InfluxDB，更适用于对数字类数据本身的计算和存储，支持数据统计函数，支持HttpAPI，支持Grafana；但它不支持全文检索，不支持Kibana；

ES，适合日志系统，也适合数字类数据本身的计算和存储，特别是坐标类数据，有独特的函数支持；支持HttpAPI，支持Kibana和Grafana。

总的来说，ES适用的场景多过InfluxDB，但也因此，其性能优势不大，磁盘存储成本也会相对高一些。

## 分布式与集群

两者都支持集群和分布式。
据说InfluxDB的最新版本，对集群功能已经不开源了，商业版本支持。开源版本，单机版稳定性优于集群。

ES的集群搭建，公司也尝试过，但运维成本和服务器成本都不理想，后改用阿里/腾讯的云套件。

## 个人倾向总结

如果搭建数据分析处理系统，倾向使用InfluxDB；日志系统，请使用ES。

部署更建议使用各大云平台的产品套件，其安全性、运维成本都是较低的。