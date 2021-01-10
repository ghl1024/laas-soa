# Loki迎来2.0重大更新，LogQL语法大幅增强！

[![云原生小白](Loki迎来2.0重大更新，LogQL语法大幅增强​！ - 知乎.assets/v2-9cc01b6fc1a07a56cb551b88fd485321_xs.jpg)](https://www.zhihu.com/people/miao-mi-ye-yao-wan-it)

[云原生小白](https://www.zhihu.com/people/miao-mi-ye-yao-wan-it)

关注他

2 人赞同了该文章

就在10月27日，Loki迎来至1.0版本以来的重要更新! 原以为这次Release会是1.7，没想到直接跳到2.0，看来Loki的应用和成熟度都有不少的提升，那么就看下本次重大更新包含哪些内容。

### **1. LogQL语法大增强**

本次LogQL已经将原先的`filter expression`更换为`log pipeline`，进一步增强了日志查询期间的管道功能，新的`log pipeline`包含了几大表达器。

**Line Filter Expression(行过滤表达式)**

原先`filter expression`大部分功能现在被行过滤表达式替换，功能上并没有太大的更新。

**Parser Expression（解析器表达式）**

解析器表达式可以解析和提取日志内容，并将他们作为新的标签。然后可以将新标签重新进行过滤或用于度量聚合。目前比较推荐的日志解析器格式为`json`、`logfmt`和`regexp`。

例如，我们的采集的XXX应用日志格式为json，内容如下

```text
{
    "protocol": "HTTP/2.0",
    "servers": ["129.0.1.1","10.2.1.3"],
    "request": {
        "time": "6.032",
        "method": "GET",
        "host": "foo.grafana.net",
        "size": "55",
    },
    "response": {
        "status": 401,
        "size": "228",
        "latency_seconds": "6.031"
    }
}
```

我们就可以使用json解析器语句重新构造日志成这样：

```text
"protocol" => "HTTP/2.0"
"request_time" => "6.032"
"request_method" => "GET"
"request_host" => "foo.grafana.net"
"request_size" => "55"
"response_status" => "401"
"response_size" => "228"
"response_size" => "228"
```

我们就可以用如下LogQL语句查询`response_status`等于401的日志了。

```text
{job="XXX"} | json | line_format "{{.response_status}}" |= "401"
```

`logfmt解析器`和`json解析器`功能差不多，这里不做过多演示。

关于`regexp解析器`，这个比较复杂，需要自己按照正则语法从日志里面提取内容，例如这条语句

```text
#日志内容
POST /api/prom/api/v1/query_range (200) 1.5s

# LogQL regexp解析器
{job="xxxx"} | regexp "(?P<method>\\w+) (?P<path>[\\w|/]+) \\((?P<status>\\d+?)\\) (?P<duration>.*)"
```

提取成如下标签

```text
"method" => "POST"
"path" => "/api/prom/api/v1/query_range"
"status" => "200"
"duration" => "1.5s"
```

> 小白有话说:日志解析器的推出，想必又让大家在日志格式化和规范化的道路上推进一把，这是天大的好事

**Label Filter Expression（标签过滤表达式）**

标签过滤器表达式可以支持使用日志的`原始`或者`新增`标签进行过滤。它可以通过操作符同时支持多个标签的比对。还是拿上述日志举例子，

```text
{job="xxxx"} | regexp "(?P<method>\\w+) (?P<path>[\\w|/]+) \\((?P<status>\\d+?)\\) (?P<duration>.*)" |
> | duration >= 20ms and status == "200"
```

> duration和status均为通过日志regexp解析器提出出来的新label，可参与管道的过滤计算

这样我们就可以过滤`状态为200`同时`请求时间大于20ms`的日志了.

**Format Expression（格式化表达式）**

格式化表达式里面包好了`Line Format Expression(行格式化表达式)`和`Labels Format Expression（标签格式化表达式）`。我把他们放一起介绍，主要是他们主要都是用于重新格式化日志标签和内容的输出，通常他们可以组合使用。

- **行格式化表达式** 主要用于重新格式化日志的输出行
- **标签格式化表达式**主要用于日志标签的增删改查

举个例子：

我们可以通过这条LogQL语句格式化成一个标准的模板输出：

```text
{cluster="ops-tools1", name="querier", namespace="loki-dev"}
  |= "metrics.go" != "loki-canary"
  | logfmt
  | query != ""
  | label_format query="{{ Replace .query \"\\n\" \"\" -1 }}"
  | line_format "{{ .ts}}\t{{.duration}}\ttraceID = {{.traceID}}\t{{ printf \"%-100.100s\" .query }} "
```

格式化前的日志

```text
level=info ts=2020-10-23T20:32:18.094668233Z caller=metrics.go:81 org_id=29 traceID=1980d41501b57b68 latency=fast query="{cluster=\"ops-tools1\", job=\"cortex-ops/query-frontend\"} |= \"query_range\"" query_type=filter range_type=range length=15m0s step=7s duration=650.22401ms status=200 throughput_mb=1.529717 total_bytes_mb=0.994659
level=info ts=2020-10-23T20:32:18.068866235Z caller=metrics.go:81 org_id=29 traceID=1980d41501b57b68 latency=fast query="{cluster=\"ops-tools1\", job=\"cortex-ops/query-frontend\"} |= \"query_range\"" query_type=filter range_type=range length=15m0s step=7s duration=624.008132ms status=200 throughput_mb=0.693449 total_bytes_mb=0.432718
```

格式化后的日志

```text
2020-10-23T20:32:18.094668233Z  650.22401ms     traceID = 1980d41501b57b68  {cluster="ops-tools1", job="cortex-ops/query-frontend"} |= "query_range"
2020-10-23T20:32:18.068866235Z  624.008132ms    traceID = 1980d41501b57b68  {cluster="ops-tools1", job="cortex-ops/query-frontend"} |= "query_range"
```

> 小白有话说: 这个日志格式化的功能略显复杂，需要花大量时间去做LogQL语句查询。这部分还不如让日志采集客户端做，甚至让研发通过SDK格式化输出日志

**Metrics（日志度量）**

日志度量方面支持了更高级的范围聚合查询`Unwrapped Range Aggregations`，它的主要作用在于根据过滤表达式提取一个时间区间内的值进行聚合查询。简单来说，以前LogQl这部分`只能对日志行`进行聚合查询，现在也能对`日志内容做聚合查询`了。它支持了如下的函数：

- sum_over_time(unwrapped-range)：指定时间间隔内所有值的总和。
- avg_over_time(unwrapped-range)：指定间隔内所有点的平均值。
- max_over_time(unwrapped-range)：指定间隔内所有点的最大值。
- min_over_time(unwrapped-range)：指定间隔中所有点的最小值
- stdvar_over_time(unwrapped-range)：指定间隔内值的总体标准方差。
- stddev_over_time(unwrapped-range)：指定间隔内值的总体标准偏差。
- quantile_over_time(scalar,unwrapped-range)：指定间隔内值的φ分位数（0≤φ≤1）

一个简单的演示例子：

这条聚合查询就可以算出日志里面的请求时间在1分钟内的TP99的数值

```text
quantile_over_time(0.99,
  {cluster="ops-tools1",container="ingress-nginx"}
    | json
    | __error__ = ""
    | unwrap request_time [1m])) by (path)
```

> 小白有话说: `Unwrapped Range Aggregations`的更新让loki彻底摆脱了只能聚合日志函数的尴尬，想想以前的蹩脚且简单的查询语句

### **2. 支持日志告警**

没错，原先以为会在Loki 1.7版本发布的功能直接在2.0里发布了。这部分可以参考小白之前的文章《Loki告警的正确姿势》，这部分内容基本没有新增变化。

### **3. 生产级别的boltdb-shipper支持**

`boltdb-shipper`一直作为Loki单机的默认kv存储引擎，在2.0版本也终于扶正了。不过`boltdb-shipper`的优势在于可以同时保存index和chunk。不过缺点也很明显，无法让loki实现分布式的部署，所以在要在生产环境里面使用Loki的同学，可以根据自己的使用场景和规模来选择存储的引擎。

在做loki升级到2.0版本时，要注意的是最好新增加一个storage schema来声明boltdb

```text
schema_config:
  configs:
    - from: 2018-04-15           
      store: boltdb              
      object_store: filesystem   
      schema: v11                
      index:
        prefix: index_           
        period: 168h             
    - from: 2020-10-24           
      store: boltdb-shipper
      object_store: filesystem   
      schema: v11
      index:
        prefix: index_
        period: 24h
```

### **4.小更新**

- loki的启动参数支持`verify-config`,用于检查配置文件是否合法，正常的返回码为`0`
- `results_cache.max_freshness`配置项迁移到`limits_config.max_cache_freshness_per_query`

### **总结**

本次Loki2.0的更新主要变化还是LogQL迎来全新的功能，这部分极大的扩展了Loki在日志查询领域的范围。虽然Loki不如ElasticSearch那样可以对日志单独做索引，但是借助LogQL V2的的日志管道表达式可以弥补相当大一部分索引功能。

另外值得一提的是Grafana Lab这家公司的`Observability宇宙`即将形成，届时云原生的可观察性产品都会以Grafana的形式展现出来，值得大家关注。