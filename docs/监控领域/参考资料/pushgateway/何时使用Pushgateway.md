# 何时使用Pushgateway

 浏览 0   扫码   分享   2019-12-11 17:48:17   [码农文档](http://www.coderdocument.com/)   [译文原文](http://www.coderdocument.com/docs/prometheus/v2.14/best_practices/when_to_use_push_gateway.html) [英文原文](https://prometheus.io/docs/practices/pushing/)

版权声明：本文为 [码农文档](http://www.coderdocument.com/) 原创译文，遵循 [CC 4.0 BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

公告：如果您也想加入翻译队伍，或者您有相关中文文档想要贡献给大家，请联系[coderdocument@163.com](mailto:coderdocument@163.com) ，谢谢！

Pushgateway是一种中间服务，它允许你从不能被抓取的作业中推送指标。有关详细信息，请参见[推送指标](http://www.coderdocument.com/docs/prometheus/v2.14/instrumenting/pushing_metrics.html)。

## 我应该使用Pushgateway吗？

**我们只建议在某些有限的情况下使用Pushgateway。**当盲目地使用Pushgateway而不是Prometheus通常的拉取模型来收集指标时，会有如下问题：

- 当通过一个Pushgateway监控多个实例时，Pushgateway就变成了一个单一的故障点和一个潜在的瓶颈。
- 你失去了Prometheus通过 `up` 指标（在每次抓取时产生）实现的自动实例健康监控。
- Pushgateway永远不会遗漏推送给它的时间序列，除非通过推送网关的API手动删除这些时间序列，否则Pushgateway会永远将这些时间序列暴露给Prometheus。

当一个作业的多个实例通过一个类似`instance`的标签区分它们在Pushgateway中的指标时，最后一点尤其相关。结果就是，即使初始实例被重命名或删除，实例的指标仍将保留在Pushgateway中。这是因为作为指标缓存的Pushgateway的生命周期与向其推送指标的进程的生命周期是完全独立的。与Prometheus通常的拉取监控模式不同：当一个实例删除时，它的指标将自动随之消失。在使用Pushgateway时，情况并非如此，你现在必须手动删除相关指标，或者自己同步其生命周期。

**通常，推送网关唯一有效的使用场景是捕获服务级别的批处理作业的结果。**“服务级别”批处理作业在语义上与特定机器或作业实例无关（例如，删除整个服务的多个用户）。引类作业的指标不应该包含机器或实例标签，以将特定机器或实例的生命周期与推送的指标解耦。这减少了Pushgateway中管理过时指标的负担。请参阅[监控批量作业的最佳实践](http://www.coderdocument.com/docs/prometheus/v2.14/best_practices/instrumentation.html#pichulizuoye)。

## 备用策略

如果入口防火墙或NAT阻止你抓取指标，那么也可以考虑将Prometheus服务器移到网络屏障后端。我们通常建议在与被监控实例相同的网络上运行Prometheus服务器。

对于与机器相关的批处理作业（例如自动安全更新cronjob或配置管理客户端），请使用[节点导出器](https://github.com/prometheus/node_exporter)的textfile模块而不是使用Pushgateway暴露指标。