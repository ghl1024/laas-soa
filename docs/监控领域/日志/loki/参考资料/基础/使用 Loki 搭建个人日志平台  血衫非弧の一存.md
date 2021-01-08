# 使用 Loki 搭建个人日志平台

##### 2020-01-31   [ tech](https://blog.kelu.org/category/tech.html) [ log](https://blog.kelu.org/category/tags/log.html)

![img](使用 Loki 搭建个人日志平台  血衫非弧の一存.assets/loki.jpg)

# 背景

Loki的第一个稳定版本于2019年11月19日发布，是 Grafana Labs 团队最新的开源项目，是一个水平可扩展，高可用性，多租户的日志聚合系统。 Grafana 对 Loki 的描述如下：

> Loki: like Prometheus, but for logs. Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus. It is designed to be very cost effective and easy to operate. It does not index the contents of the logs, but rather a set of labels for each log stream.

简单说，Loki 是专门用于聚集日志数据，重点是高可用性和可伸缩性。与竞争对手不同的是，它确实易于安装且资源效率极高。

血衫目前运维大概上百个节点，虽然系统是统一的基线版本且使用docker运行应用，平时相安无事，但变更后的问题排查仍有点心有余悸。对一个火热的日志系统elk也有浅尝辄止，奈何对于非核心应用，多耗散一份算力意味着成本增加和利润的减少，elk对于小团队来说，还是过于笨重。趁着近日的疫情无法外出，调研后将 Loki 上线了生产，可以说是完美契合了中小团队对日志平台的需求。

# 介绍

与其他日志聚合系统相比，`Loki`具有下面的一些特性：

- 不对日志进行全文索引（vs ELK技）。通过存储压缩非结构化日志和仅索引元数据，Loki 操作起来会更简单，更省成本。
- 通过使用与 Prometheus 相同的标签记录流对日志进行索引和分组，这使得日志的扩展和操作效率更高。
- 特别适合储存 Kubernetes Pod 日志; 诸如 Pod 标签之类的元数据会被自动删除和编入索引。
- 受 Grafana 原生支持。

Loki 由以下3个部分组成：

- `loki`是主服务器，负责存储日志和处理查询。
- `promtail`是代理，负责收集日志并将其发送给 loki 。
- `Grafana`用于 UI 展示。

# 一、安装

Docker-compose.yml 可以参考`Loki`的[文档介绍](https://github.com/grafana/loki/tree/master/production)，开箱即用。

```
version: "3"

networks:
  loki:

services:
  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    networks:
      - loki

  promtail:
    image: grafana/promtail:latest
    volumes:
      - /var/log:/var/log
    command: -config.file=/etc/promtail/docker-config.yaml
    networks:
      - loki

  grafana:
    image: grafana/grafana:master
    ports:
      - "3000:3000"
    networks:
      - loki
```

然后直接使用 docker-compose 启动即可：

```
$ docker-compose up -d
```

# 二、使用

安装完成后，访问节点的 3000 端口访问 grafana，默认情况下使用(admin:admin)访问 -> 选择添加数据源：

![grafana-loki-dashsource](使用 Loki 搭建个人日志平台  血衫非弧の一存.assets/grafana-loki-dashsource.jpg)

在数据源列表中选择`Loki`，配置 Loki 源地址：

![grafana-loki-dashsource-config](使用 Loki 搭建个人日志平台  血衫非弧の一存.assets/grafana-loki-dashsource-config.jpg)grafana-loki-dashsource-config

源地址配置`http://loki:3100`即可，保存。

保存完成后，切换到 grafana 左侧区域的`Explore`，即可进入到`Loki`的页面，点击`Log labels`就可以把当前系统采集的日志标签给显示出来，可以根据这些标签进行日志的过滤查询：

![image-20200202180915479](使用 Loki 搭建个人日志平台  血衫非弧の一存.assets/image-20200202180915479.jpg)

图中显示的label是我自定义的 label，大家可以根据自己的业务需求定义自己的label。

# 三、配置

从上面的步骤已经可以一窥使用方法了，如果要使用起来，我们还需要了解如下信息：

### Loki 的配置

Loki的详细配置，可查看官方文档：https://github.com/grafana/loki/blob/master/docs/README.md

配置相关文档： https://github.com/grafana/loki/blob/v1.3.0/docs/configuration/README.md

我目前均保留了保留默认配置。

### promtail的配置

promtail 是 Loki 的官方支持的日志采集端，在需要采集日志的节点上运行采集日志，再统一发送到 Loki 进行处理。我们编写的大多是这一部分。

官方配置说明： https://github.com/grafana/loki/blob/v1.3.0/docs/clients/promtail/configuration.md

除了使用Promtail，社区还有很多采集日志的组件，比如fluentd、fluent bit等，都是比较优秀的。

这里是我的promtail配置，`bj1`是我的节点，在address等配置会域名解析成ip的方式。

```
server:
  http_listen_address: bj1
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /etc/promtail/positions.yaml
  sync_period: 10s

clients:
  - url: http://bj1:3100/loki/api/v1/push

scrape_configs:
- job_name: system
  static_configs:
  - targets:
      - localhost
    labels:
      job: system
      app: system
      node: bj1
      __path__: /var/log/*log
- job_name: cron
  static_configs:
  - targets:
      - localhost
    labels:
      job: cron
      app: cron
      node: bj1
      __path__: /var/local/log/cron/*log
```

# 四、选择器

对于查询表达式的标签部分，将其包装在花括号中`{}`，然后使用键值对的语法来选择标签，多个标签表达式用逗号分隔，比如：

```
{app="mysql",name="mysql-backup"}
```

目前支持以下标签匹配运算符：

- `=`等于
- `!=`不相等
- `=~`正则表达式匹配
- `!~`不匹配正则表达式

比如：

```
{name=~"mysql.+"}
{name!~"mysql.+"}
```

适用于`Prometheus`标签选择器规则同样也适用于`Loki`日志流选择器。

# 参考资料

- [Loki 设计初心](https://docs.google.com/document/d/11tjK_lvp1-SVsFZjgOTr1vV3-q6vBAsZYIQ5ZeYBkyM/view#)
- [Grafana 6.0 正式发布！新增查询工作流，全新独立 Gauge 面板](https://www.mayi888.com/archives/59170)