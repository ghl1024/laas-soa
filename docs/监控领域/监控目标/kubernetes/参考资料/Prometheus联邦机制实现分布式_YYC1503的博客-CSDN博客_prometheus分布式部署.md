# Prometheus联邦机制实现分布式

![img](Prometheus联邦机制实现分布式_YYC1503的博客-CSDN博客_prometheus分布式部署.assets/original.png)

[可耐的猪猪](https://blog.csdn.net/YYC1503) 2019-11-22 11:03:11 ![img](Prometheus联邦机制实现分布式_YYC1503的博客-CSDN博客_prometheus分布式部署.assets/articleReadEyes.png) 2882 ![img](Prometheus联邦机制实现分布式_YYC1503的博客-CSDN博客_prometheus分布式部署.assets/tobarCollect.png) 收藏 5

分类专栏： [linux监控](https://blog.csdn.net/yyc1503/category_9479976.html) 文章标签： [prometheus联邦机制](https://so.csdn.net/so/search/s.do?q=prometheus联邦机制&t=blog&o=vip&s=&l=&f=&viparticle=) [prometheus分布式](https://www.csdn.net/tags/MtjaUg0sNDg4MTktYmxvZwO0O0OO0O0O.html)

版权

## 总结

上文讲到了prometheus+grafana对于大数据集群的监控。但是随着集群规模越来越大，prometheus压力也随之增大，因为采取拉去方式，对于prometheus本身的压力比较大。那么程序本身有什么解决办法？其他监控采取什么方式解决的。

### 其他监控分布式

熟悉zabbix的朋友可能知道，zabbix中有主动模式和被动模式，主动模式可以实现agent节点自动向server节点汇报，这样就减轻了server端的压力。被动模式中也有一种添加代理节点方式实现分布式监控，实现跨机房异地监控目标。具体方法可以参考本人zabbix监控文章。

### prometheus联邦机制

prometheus的分布式类似于nginx的负载均衡模式，主节点配置文件可以配置从节点的地址池，主节点只要定时向从节点拉取数据即可，主节点的作用就是存贮实时数据，并提供给grafana 使用。而从节点作用就是分别从不同的各个采集端中抽取数据，可以实现分机器或者分角色。这种由一个中心的prometheus负则聚合多个prometheus数据中的监控模式，称为prometheus联邦集群。
例如：集群规模200台，两个从节点，可以每台机器监控100台，也可以每台机器监控200台，但是分别监控不同角色，第一个从节点监控hdfs，第二个节点监控hbase这种方式，反正想怎么监控就看个人配置了。

### 部署配置

分布式的部署就是找多台机器分别部署prometheus，部署方式都是一致，只有配置文件不同。
联邦集群核心在于每一个prometheus server都包含一个用于获取当前实例中监控样本的接口 /federate 。对于中心prometheus server无论是从其他prometheus实例还是node_exporter采集端获取数据，事实上没有任何差异的。

| 参数           | 作用                                                         |
| -------------- | ------------------------------------------------------------ |
| honor_labels   | 防止采集到监控指标冲突，配置true可以确保采集到指标冲突时自动忽略冲突指标；配置false会自动将冲突指标替换为exported_的形式。还可以添加标签区分不同监控目标 |
| metrics_path   | 联邦集群用于获取监控样本参数配置 /federate                   |
| match[ ]       | 指定需要获取的时间序列，个人认为也就是填写从节点的角色标签或者环境变量。可以填写job="zookeeper"或者__name__=~“instance.*”，模糊匹配可以使用通配符。将你想要展示的角色或者变量写入prometheus主节点才可以获取从节点上信息，否则无法获取 |
| static_configs | 在此填写从节点地址池即可                                     |

以下为主节点配置文件：

```bash
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
#  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

#    static_configs:
#    - targets: ['localhost:9090']


  - job_name: 'node_workers'
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]':
        - '{job="zookeeper"}'
        - '{job="hbase"}'
        - '{job="hdfs"}'
        - '{job="hive"}'
        - '{job="kafka"}'
        - '{job="linux_server"}'
        - '{job="spark"}'
        - '{job="yarn"}'
        - '{__name__=~"instance.*"}'
    static_configs:
      - targets:
        - '192.168.1.1:9090'
        - '192.168.1.2:9090'
```

从节点配置文件：
从节点1：

```bash
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']
  - job_name: 'linux_server'
    file_sd_configs:
     - files:
       - configs/linux.json
  - job_name: 'hdfs'
    file_sd_configs:
     - files:
       - configs/hdfs.json
  - job_name: 'hbase'
    file_sd_configs:
     - files:
       - configs/hbase.json
  - job_name: 'yarn'
    file_sd_configs:
     - files:
       - configs/yarn.json
```

从节点2：

```bash
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']
 - job_name: 'zookeeper'
    file_sd_configs:
     - files:
       - configs/zookeeper.json
  - job_name: 'hive'
    file_sd_configs:
     - files:
       - configs/hive.json
  - job_name: 'kafka'
    file_sd_configs:
     - files:
       - configs/kafka.json
  - job_name: 'spark'
    file_sd_configs:
     - files:
       - configs/spark.json
```

# 补充

prometheus默认是通过本地存贮方式的，这样可以减少管理的复杂性和异地存贮带来的网络带宽影响等。当然本地存储也带来了一些不好的地方，首先就是数据持久化的问题，特别是在像Kubernetes这样的动态集群环境下，如果Promthues的实例被重新调度，那所有历史监控数据都会丢失。 其次本地存储也意味着Prometheus不适合保存大量历史数据(一般Prometheus推荐只保留几周或者几个月的数据)。最后本地存储也导致Prometheus无法进行弹性扩展。为了适应这方面的需求，Prometheus提供了remote_write和remote_read的特性，支持将数据存储到远端和从远端读取数据。通过将监控样本采集和数据存储分离，解决Prometheus的持久化问题。