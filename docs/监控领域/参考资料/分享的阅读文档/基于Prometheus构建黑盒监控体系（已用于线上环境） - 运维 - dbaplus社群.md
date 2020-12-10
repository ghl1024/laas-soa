## 基于Prometheus构建黑盒监控体系（已用于线上环境）

罗辉 2020-04-25 11:22:00

 

**作者介绍**

**罗辉，**原荔枝FM运维工程师，现任北方激光研究院广西分公司运维总监。

 

**概述**

 

在监控体系里面，通常我们认为监控分为：白盒监控和黑盒监控。

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAUZSoHSQJkLB24UbWSug1MvpHJlurAAGgrxicFucR5VibMficGHWXfuUSg)

 

黑盒监控：主要关注的现象，一般都是正在发生的东西，例如出现一个告警，业务接口不正常，那么这种监控就是站在用户的角度能看到的监控，重点在于能对正在发生的故障进行告警。

 

白盒监控：主要关注的是原因，也就是系统内部暴露的一些指标，例如redis的info中显示redis slave down，这个就是redis info显示的一个内部的指标，重点在于原因，可能是在黑盒监控中看到redis down，而查看内部信息的时候，显示redis port is refused connection。

 

白盒监控：有很多种，有中间件，有存储，有web服务器例如redis可以使用info暴露内部的指标信息；例如mysql可以使用show variables暴露内部指标信息；例如nginx可以使用nginx_status来暴露内部信息，系统业务指标可以通过埋点或者命令进行采集。

 

**Blackbox Exporter**

 

在前面的知识中，我们介绍Prometheus下如何进行白盒监控，我们监控主机的资源用量、容器的运行状态、数据库中间件的运行数据，通过采集相关指标来预测我们的服务健康状态。

 

在黑盒健康方面。Blackbox Exporter是Prometheus社区提供的官方黑盒监控解决方案，其允许用户通过：HTTP、HTTPS、DNS、TCP以及ICMP的方式对网络进行探测，目前我司相关业务监控接口也是基于Blockbox来进行的，下面我们开始。

 

**Blackbox_exporter应用场景**

 

**1、HTTP 测试**

 

- 定义 Request Header 信息
- 判断 Http status / Http Respones Header / Http Body 内容

 

**2、TCP 测试**

 

- 业务组件端口状态监听
- 应用层协议定义与监听

 

**3、ICMP 测试**

 

- 主机探活机制

 

**4、POST 测试**

 

- 接口联通性

 

**5、SSL 证书过期时间**

 

**结合grafana生成的相关模板**

 

1、首先看下我们这边的相关图表，门户多项指标与ssl监控

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQA1eKLvEzv77GQS0k6zTgCLsSgRtYXIwTxzhr4U6l1z2JFAn6cicnJBLg)

 

2、机房线路监控

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAj6xySB3JS4WRSIBWmbM6ecHWmL4noHsuFT9POsJ7JPBuO0OCha0bKA)

 

3、接口状态监控

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAgK9kwNevzjicYBDrrrUXT1sfn46YBspFgzGoEoaibfOzftJBYS7VLzTw)

 

**Blackbox Exporter部署**

 

1、安装Exporter

 

 

[root@cinder1 src]# wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.16.0/blackbox_exporter-0.16.0.linux-amd64.tar.gz

[root@cinder1 src]#tar -zxvf blackbox_exporter-0.16.0.linux-amd64.tar.gz -C /usr/local

[root@cinder1 src]#mv /usr/local/blackbox_exporter-0.16.0.linux-amd64 /usr/local/blackbox_exporter

 

2、添加到启动项

 

 

[root@cinder1 src]# cat /etc/systemd/system/blackbox_exporter.service 

[Unit]

Description=blackbox_exporter

After=network.target 

 

[Service]

WorkingDirectory=/usr/local/blackbox

ExecStart=/usr/local/blackbox/blackbox_exporter \

​     --config.file=/usr/local/blackbox/blackbox.yml

[Install]

WantedBy=multi-user.target

 

3、检测是否正常启动

 

 

[root@cinder1 src]# ss -tunlp|grep 9115

tcp  LISTEN   0   128   :::9115         :::*          users:(("blackbox_export",pid=2517722,fd=3))

 

**icmp监控**

 

通过icmp 这个指标的采集，我们可以确认到对方的线路是否有问题。这个也是监控里面比较重要的一个环节。我们要了解全国各地到我们机房的线路有哪条有问题我们总结了两种方案：

 

- 全国各地各节点ping 和访问数据采集。这种类似听云运营商有提供这类服务，但是要花钱；
- 我现在用的方法就是：找各地测试ping 的节点，我们从机房主动ping 看是否到哪个线路有故障，下面我们开始。

 

1、prometheus 添加相关监控，Blackbox 使用默认配置启动即可

 

 

\- job_name: "icmp_ping"

  metrics_path: /probe

  params:

   module: [icmp] # 使用icmp模块

  file_sd_configs:

  \- refresh_interval: 10s

   files:

   \- "/home/prometheus/conf/ping_status*.yml" #具体的配置文件

  relabel_configs:

  \- source_labels: [__address__]

   regex: (.*)(:80)?

   target_label: __param_target

   replacement: ${1}

  \- source_labels: [__param_target]

   target_label: instance

  \- source_labels: [__param_target]

   regex: (.*)

   target_label: ping

   replacement: ${1}

  \- source_labels: []

   regex: .*

   target_label: __address__

   replacement: 192.168.1.14:9115

 

2、相关ping节点配置

 

 

[root@cinder1 conf]# cat ping_status.yml 

\- targets: ['220.181.38.150','14.215.177.39','180.101.49.12','14.215.177.39','180.101.49.11','14.215.177.38','14.215.177.38']

 labels:

  group: '一线城市-电信网络监控'

\- targets: ['112.80.248.75','163.177.151.109','61.135.169.125','163.177.151.110','180.101.49.11','61.135.169.121','180.101.49.11']

 labels:

  group: '一线城市-联通网络监控'

\- targets: ['183.232.231.172','36.152.44.95','182.61.200.6','36.152.44.96','220.181.38.149']

 labels:

  group: '一线城市-移动网络监控' 

 

这些数据是从全国各地ping 网站进行采集，大家可以从那些网站获取.

 

3、添加grafana 

 

这个grafana是自己定义的，看到网上没有就自己定义了一个。大家可以从github上下载，再看看效果，可以看到我们通过Ping 就获取到了全国各地的线路运行情况，可以有效的检测到我们线路异常问题：

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAj6xySB3JS4WRSIBWmbM6ecHWmL4noHsuFT9POsJ7JPBuO0OCha0bKA)

 

**http相关指标监控**

 

1、prometheus 配置http_get访问

 

 \- job_name: "blackbox"

  metrics_path: /probe

  params:

   module: [http_2xx] #使用http模块

  file_sd_configs: 

  \- refresh_interval: 1m

   files: 

   \- "/home/prometheus/conf/blackbox*.yml"

  relabel_configs:

  \- source_labels: [__address__]

   target_label: __param_target

  \- source_labels: [__param_target]

   target_label: instance

  \- target_label: __address__

   replacement: 192.168.1.14:9115

 

2、相关配置文件，类似举例如下

 

[root@cinder1 conf]# cat /home/prometheus/conf/blackbox-dis.yml 

\- targets:

 \- https://www.zhibo8.cc

 \- https://www.baidu.com

\#配置相关URL

 

3、添加grafana模板

 

可以选择模板的9965模板，这个模板我们也看到前面的，提供了相关的ssl 过期检测，这里以两个常见的网站为例。

 

**接口get请求检测**


1、prometheus 配置，其实跟我们之前的配置一样，我们直接看配置文件

 

 \- job_name: "check_get"

  metrics_path: /probe

  params:

   module: [http_2xx] # Look for a HTTP 200 response.

  file_sd_configs:

  \- refresh_interval: 1m

   files:

   \- "/home/prometheus/conf/service_get.yml"

  relabel_configs:

  \- source_labels: [__address__]

   target_label: __param_target

  \- source_labels: [__param_target]

   target_label: instance

  \- target_label: __address__

   replacement: 192.168.1.14:9115

 

2、相关接口配置参考

 

[root@cinder1 conf]# cat service_get.yml 

\- targets:

 \- http://10.10.1.123:10000/pmkb/atc_tcbi

 \- http://10.10.1.123:10000/pmkb/get_ship_lock_count

 \- http://10.10.1.123:10000/pmkb/get_terminal_count_by_city

 \- http://10.10.1.123:10000/pmkb/get_terminal_monitor?industry=1

 \- http://10.10.1.123:10000/pmkb/get_terminal_comparison?industry=1

 \- http://10.10.1.123:10000/pmkb/get_terminal_city_count_industry?industry=1

 \- http://10.10.1.123:10000/pmkb/industry_stat?industry=1

 \- http://10.10.1.123:10000/pmkb/get_company_car_count?industry=1

 \- http://10.10.1.123:10000/pmkb/get_terminal_month_countbyi?industry=1

 labels:

  group: 'service'

 

3、grafana 和前面一样自己订制的，可以从github上下载

 

**接口post请求状态检测**

 

1、这里首先我们要改一下post 相关接口的blackbox.yml配置，我们自己定义一个模块

 

[root@cinder1 blackbox]# cat blackbox.yml 

modules:

 http_2xx:

  prober: http

 http_post_2xx:  #这个模块名称可以自己定义

  prober: http

  http:

   method: POST

   headers:

​    Content-Type: application/json  #添加头部

   body: '{"username":"admin","password":"123456"}' #发送的相关数据，这里我们以登录接口为例

 

2、添加到prometheus

 

 \- job_name: "check_service"

  metrics_path: /probe

  params:

   module: [http_post_2xx] # 这里要对应配置文件里，定义的模块

  file_sd_configs: 

  \- refresh_interval: 1m

   files: 

   \- "/home/prometheus/conf/service_post.yml"

  relabel_configs:

  \- source_labels: [__address__]

   target_label: __param_target

  \- source_labels: [__param_target]

   target_label: instance

  \- target_label: __address__

   replacement: 192.168.1.14:9115

 

3、相关配置查看

 

[root@cinder1 conf]# cat service_post.yml 

\- targets:

 \- http://10.2.4.103:5000/devops/api/v1.0/login

 labels:

  group: 'service'

 

4、添加grafana相关配置，这个也是自己定义的，可以从github上下载

 

**tcp端口状态检测**


个人理解的是这个跟telnet差不多都是检测端口是否在线

 

1、prometheus 配置

 

 \- job_name: 'port_status'

  metrics_path: /probe

  params:

   module: [tcp_connect] #使用tcp模块

  static_configs:

   \- targets: ['10.10.1.35:8068','10.10.1.35:8069'] #对应主机接口

​    labels:

​     instance: 'port_status'

​     group: 'tcp'

  relabel_configs:

  \- source_labels: [__address__]

   target_label: __param_target 

  \- target_label: __address__

   replacement: 192.168.1.14:9115 

 

2、图表

 

图表可以集成到前面的grafana 9965模板。

 

**告警规则定义**

 

1、业务正常性

 

- icmp、tcp、http、post 监测是否正常可以观察probe_success 这一指标
- probe_success == 0 ##联通性异常
- probe_success == 1 ##联通性正常
- 告警也是判断这个指标是否等于0，如等于0 则触发异常报警

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAMU4WzaQVN7ky3ibw3ySc5xEug7BEv0Zpw6JD8U1BaibfTuJhbFkcFaGA)

 

2、通过http模块我们可以获取证书的过期时间，可以根据过期时间添加相关告警

 

probe_ssl_earliest_cert_expiry ：可以查询证书到期时间。

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAStyqj5HRZLCMEnSWr8uibTo1OZGt9vb8UUqpfqoibcghts50fdGibjfmg)

 

\#经过单位转换我们可以得到一下，按天来计算：(probe_ssl_earliest_cert_expiry - time())/86400 

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAuDBgzOL8SbhIERFKw0hbebRCOp3HfHgWny6UlF1W6mSzh9OzicjdWPg)

 

3、所以我们结合上面的配置可以定制如下告警规则

 

[root@cinder1 rules]# cat blackbox.yml 

groups:

\- name: blackbox_network_stats

 rules:

 \- alert: blackbox_network_stats

  expr: probe_success == 0

  for: 1m

  labels:

   severity: critical

  annotations:

   summary: "接口/主机/端口 {{ $labels.instance }} 无法联通"

   description: "请尽快检测"

 

\##ssl检测

 

[root@cinder1 rules]# cat ssl.yml 

groups:

\- name: check_ssl_status

 rules:

 \- alert: "ssl证书过期警告"

  expr: (probe_ssl_earliest_cert_expiry - time())/86400 <30

  for: 1h

  labels:

   severity: warn

  annotations:

   description: '域名{{$labels.instance}}的证书还有{{ printf "%.1f" $value }}天就过期了,请尽快更新证书'

   summary: "ssl证书过期警告"

 

4、重启完成之后我们可以登录web界面查看下

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAnxzacwkNqcZARqeFJnKibVzexuicUkHsibzWAr5VQ27ckTds2qQ3ibs6NA)

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQA1LpyUDFe67rgSNiaag65XybXP00gMY9Yibr35AISh2EHnqGURLv4tiaBA)

 

5、我们发现有个接口已经存在问题，这个时候我们也收到了一条相应的微信告警

 

![img](基于Prometheus构建黑盒监控体系（已用于线上环境） - 运维 - dbaplus社群.assets/tibrg3AoIJTs08vAt4tAjNibx16Nu1QDQAyocj2duMTZficsrwkbVE7twpu986rhibuSeKH7r1ibiaiaMMKgxPOibsEgicg)

 

**总结**

 

黑盒监控相较于白盒监控最大的不同在于黑盒监控是以故障为导向当故障发生时，黑盒监控能快速发现故障，所以我们监控时候以粒度比较细的，如端口、接口、线路等进行监控。

 

通过Prometheus Blackbox Exporter可以快速实现和定制我们很多相关策略，大家线上环境可以基于以上做配置即可。