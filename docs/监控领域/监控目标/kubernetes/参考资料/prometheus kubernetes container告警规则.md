# prometheus kubernetes container告警规则

作者: root007 分类: [prometheus](http://idcsec.com/category/kubernetes/prometheus/),[未分类](http://idcsec.com/category/uncategorized/) 发布时间: 2019-06-27 18:58

### Prometheus

#### 数据类型

Counter(计数器类型)

> Counter类型的指标的工作方式和计数器一样，只增不减(除非系统发生了重置),Counter一般用于累计值。

Gauges(仪表盘类型)

> Gauges是可增可减的指标类，可以用于反应当前应用的状态。比如在监控主机时，可用内存大小。

Histograms(直方图类型)

> 主要用于表示一段时间范围内对数据进行采样（通常是请求持续时间或响应大小），并能够对其指定区间以及总数进行统计,代表的是⼀种近似的百分⽐估算数值。举例说明: 如果你想监控用户的访问时间，将nginx日志的http_response_time列的数据全部采集下来，然后算一下总的平均值即可。但是这没有意义，如果只有一个用户请求特别慢，那么就会拉低总的平均值，而且你也发现不了小部分的问题。这时可以使用histogram来比较~=0.05秒的量有多少，0 ~ 0.05秒的有多少，>2秒的有多少，>10秒的有多少。

Summary(摘要类型)

> Summary 和 Histogram 类似,主要用于表示一段时间内数据采样结果（通常时请求持续时间或响应大小），它直接存储了quantile数据，而不是根据统计区间计算出来的。

#### 标签匹配运算符

- =：选择与提供的字符串完全相同的标签。
- !=：选择不等于提供的字符串的标签。
- =~：选择正则表达式匹配提供的字符串（或子字符串）的标签。
- !~：选择不与提供的字符串（或子字符串）匹配的标签。

**注释:** 标签名称的匹配可以使用如下方示例:

*(1)http_requests_total{environment=~”staging|testing|development”,method!=”GET”}*
*(2)http_requests_total{job=~”.+”,method!=”GET”}*
*(3)http_requests_total{job=~”.*“,method!=”GET”}*

#### 范围向量选择器

时间长度被追加在向量选择器尾部的方括号[]中，用以指定对于每个样本范围区间中的每个元素应该抓取的时间范围样本区间。

- s – seconds
- m – minutes
- h – hours
- d – days
- w – weeks
- y – years

**示例:** 取出过去5分钟内，度量指标名称为http_requests_total，标签为job=”prometheus”的时间序列数据
`http_requests_total{job="prometheus"}[5m]`

#### 位置修饰符

offset偏移修饰符，允许在查询中改变单个瞬时向量和范围向量中的时间偏移

**示例:** 取出相对于当前时间的前一周，过去五分钟的http_requests_total的速率：
`rate(http_requests_total[5m] offset 1w)`

#### 逻辑/集二元运算符（逻辑/集合二元操作符）

- and 交集
- or 并集
- unless 补集

vector1 and vector2 的逻辑/集合二元操作符，规则：vector1瞬时向量中的每个样本数据与vector2向量中的所有样本数据进行”标签”匹配，不匹配的，全部丢弃。运算结果是保留左边的度量指标名称和值。
**示例:**

```
公式:
node_cpu_seconds_total{job='test',cpu='1',mode=~"idle|system|user"}  and node_cpu_seconds_total{mode=~"system|user"}
返回的结果:
node_cpu_seconds_total{cpu="1",instance="gitlab:9100",job="test",mode="user"}
node_cpu_seconds_total{cpu="1",instance="gitlab:9100",job="test",mode="system"}
```

vector1 or vector2 的逻辑/集合二元操作符，规则：返回vector1中的所有元素和值,以及vector2中没有在vector1中匹配到的元素.
**示例:**

```
公式:
node_cpu_seconds_total{job='test',cpu='1',mode=~"user"} or node_cpu_seconds_total{cpu='1',job='test2',mode=~"system|user"}
返回的结果:
node_cpu_seconds_total{cpu="1",instance="gitlab:9100",job="test",mode="user"}   22.92
node_cpu_seconds_total{cpu="1",instance="gitlab:9100",job="test2",mode="system"}    54.14
node_cpu_seconds_total{cpu="1",instance="gitlab:9100",job="test2",mode="user"}   22.91
```

vector1 unless vector2的逻辑/集合二元操作符，又称差积。规则：包含在vector1中的元素，但是该元素不在vector2向量所有元素列表中，则写入到结果集中。
**示例:**

```
公式:
node_cpu_seconds_total{job='test',cpu='1',mode=~"user|system|idle"} unless node_cpu_seconds_total{mode=~"system|user"}
返回的结果:
node_cpu_seconds_total{cpu="1",instance="gitlab:9100",job="test",mode="idle"}
```

#### 聚合运算符:

Prometheus支持下面的内置聚合操作符。这些聚合操作符被用于聚合单个即时向量的所有时间序列列表，把聚合的结果值存入到新的向量中。

```
(1). sum (在所有的value上求和)
sum(node_cpu_seconds_total{job="test"})
(2). max (在所有的value求最大值)
max(node_cpu_seconds_total{job="test"})
(3). min (在所有的value求最小值)
min(node_cpu_seconds_total{job="test"})
(4). avg (在所有的value上求平均值)
avg(node_cpu_seconds_total{job="test"})
(5). stddev (求标准差)
(6). stdvar (求方差)
(7). count (统计向量元素的个数)
count(node_cpu_seconds_total{job="test"}) 
(8). count_values (统计相同数据值的元素数量)
count_values("tag",node_cpu_seconds_total{cpu="0",mode="nice"}) #tag是标签名
(9). bottomk (在维度上取几个最小值)
bottomk(3,node_cpu_seconds_total{instance="gitlab:9100",cpu="0",mode=~"idle|nice|softirq"})
(10). topk (在维度上取几个最大值)
topk(3,node_cpu_seconds_total{instance="gitlab:9100",cpu="0",mode=~"idle|nice|softirq"})
(11). quantile (统计分位数)
quantile(0.99,prometheus_http_request_duration_seconds_sum{handler!="/metrics"})   #值为0.38代表百分之99的请求都在0.38ms下。
(12). sort(排序)
(13). time(打印当前时间戳)
(14). sqrt(计算元素的平方根)
(15). timestamp(返回样本的时间戳(不是当前时间戳)）
```

#### 功能性函数说明

```
(1). increase()
increase(node_cpu_seconds_total{mode="idle"}[1m])    
#返回一个度量标准: last值-first值。取⼀段时间增量的总量  
(2). by()
count(node_cpu_seconds_total{mode="idle"}) by(cpu)   
#这个函数，可以把sum加合到⼀起的数值，按照指定的⼀个⽅式进⾏⼀层的拆分
(3). rate()  
#rate函数是专门搭配counter类型数据使⽤的函数它的功能是按照设置⼀个时间段，(last值-first值)/时间差s，取⼀段时间增量的平均每秒数量. 
(4). predict_limpar(预测函数)
predict_linear(node_filesystem_free_bytes{device="/dev/sda3",fstype="xfs",instance="jenkins:9100",job="test2",mountpoint="/"}[1m],300)
#根据磁盘1分钟内的变化，预测5分钟后的值
(5). abs()
#返回输入向量的所有样本的绝对值。
(6). absent()
#如果赋值给它的向量具有样本数据，则返回空向量；如果传递的瞬时向量参数没有样本数据，则返回不带度量指标名称且带有标签的样本值为1的结果,当监控度量指标时，如果获取到的样本数据是空的， 使用absent方法对告警是非常有用的.(有数据返回空，没数据返回1)
(7). ceil
#返回一个向上舍入为最接近的整数。
(8). changes()
changes(node_filesystem_free_bytes[1m])
#changes(v range-vector) 输入一个范围向量， 返回这个范围向量内每个样本数据值变化的次数。
(9). clamp_max()
#clamp_max(v instant-vector, max scalar)函数，输入一个瞬时向量和最大值，样本数据值若大于max，则改为max，否则不变
(10). clamp_min()
#输入一个瞬时向量和最大值，样本数据值小于min，则改为min。否则不变
(11). hour,minute,month,year,day_of_month(),day_of_week()，days_in_month()
#当前的小时，分钟，月，年，当天在这个月是第几天，当天在这个星期是第几天，这个月有多少天.
(12). delta()
delta(node_cpu_seconds_total{cpu="0",instance="gitlab:9100",job="test",mode="idle"}[1m])
#delta(v range-vector)函数，计算一个范围向量v的第一个元素和最后一个元素之间的差值。返回值：key:value=度量指标：差值
(13). floor()
#此函数，与ceil()函数相反。 4.3 为 4 。
(14). exp()
#输入一个瞬时向量, 返回各个样本值的e指数值，即为e^N次方，e=2.718281828,N=Value。
(15). idelta()
#idelta(v range-vector) 的参数是一个区间向量, 返回一个瞬时向量。它计算最新的 2 个样本值之间的差值。这个函数一般只用在 Gauge 类型的时间序列上。
(16). label_join()
label_join(up{instance="localhost:9091",job="pushgateway"},"foo", ",", "job","instance")
=》up{foo="pushgateway,localhost:9091",instance="localhost:9091",job="pushgateway"}
#函数可以将时间序列 v 中多个标签 src_label 的值，通过 separator作为连接符写入到一个新的标签 dst_label 中。可以有多个 src_label 标签。
(17). label_replace()
label_replace(up{instance="jenkins:9100",job="test2"},"port", "$2", "instance","(.*):(.*)")
=> up{instance="jenkins:9100",job="test2",port="9100"}
#label_replace 函数为时间序列添加额外的标签。该函数会依次对 v 中的每一条时间序列进行处理，通过 regex 匹配 src_label 的值，并将匹配部分 relacement 写入到 dst_label 标签中。
(18). round()
#round()函数与 ceil 和 floor 函数类似，返回向量中所有样本值的最接近的整数。
(19). vector()
#将标量返回s为没有标签的向量。
(20). irate（）
irate(node_load1[1m])
#irate(v range-vector)函数, 输入：范围向量，输出：key: value = 度量指标： (last值-last前一个值)/时间戳差值，它是基于最后两个数据点。
(21). <aggregation>_over_time()
#以下函数允许聚合给定范围向量的每个系列随时间的变化并返回具有每系列聚合结果的即时向量：
- avg_over_time(range-vector)：指定时间间隔内所有点的平均值。
avg_over_time(node_cpu_seconds_total{cpu="0",instance="gitlab:9100",job="test",mode="idle"}[1m])
- min_over_time(range-vector)：指定时间间隔内所有点的最小值。
- max_over_time(range-vector)：指定时间间隔内所有点的最大值。
- sum_over_time(range-vector)：指定时间间隔内所有值的总和。
- count_over_time(range-vector)：指定时间间隔内所有值的计数。
- quantile_over_time(scalar, range-vector)：指定间隔中的值的φ-分位数（0≤φ≤1）。
#中分位的计算方法:如果数字个数为奇数，中位值就是中间那个数，如果是偶数，则是中间两个数的平均数。
#90百分位数的计算方式: a=[1,2,3,4]
a. (n-1)*p=(4-1)*0.9=2.7  #则整数部分i=2，小数部分j=0.7,n=数字个数，p=90百分位数。
b. a[i]=3;a[i+1]=4
c. (1-0.7)*3+(0.7*4)=3.7
- stddev_over_time(range-vector) : 区间向量内每个度量指标的总体标准差。
#总体标准差计算方法:
步骤一、(每个样本数据 减去总体全部数据的平均值)。
步骤二、把步骤一所得的各个数值的平方相加。
步骤三、把步骤二的结果除以 n （“n”指总体数目）。
步骤四、从步骤三所得的数值之平方根就是总体的标准偏差。
- stdvar_over_time(range-vector) : #区间向量内每个度量指标的总体标准方差,计算方法相当于没有第四步的总体标准差方法。
 ### 容器内存使用率超过limit值80%,部分pod没有limit限制，所以值为+Inf，需要排除

- container_memory_usage_bytes{container_name!=""} / container_spec_memory_limit_bytes{container_name!=""}  *100 != +Inf > 80  
###container_memory_usage_bytes轻松跟踪内存利用率，但是，该指标还包括可以在内存压力下驱逐的缓存（认为是文件系统缓存）项。container_memory_usage_bytes == container_memory_rss + container_memory_cache + kernel memory更好的指标是container_memory_working_set_bytes,container_memory_working_set_bytes是容器真实使用的内存量，也是limit限制时的 oom 判断依据，kubectl top pod 得到的内存使用量，并不是cadvisor 中的container_memory_usage_bytes，而是container_memory_working_set_bytes，计算方式为：container_memory_working_set_bytes = container_memory_usage_bytes – total_inactive_file（未激活的匿名缓存页）
sum(container_memory_working_set_bytes{container_name!="",container_name!~"prometheus|fluent-bit"}) by (pod_name, namespace) / 
sum(label_join(container_memory_working_set_bytes, "pod_name", "", "pod")) by (pod_name, namespace) * 100 >80
#这里因为一个来自container_memory_working_set_bytes一个container_memory_working_set_bytes标签不一致所以使用label_join
#或者：(但是这会把相同的container_name累加)
sum(container_memory_working_set_bytes) by (container_name) / sum(label_join(kube_pod_container_resource_limits_memory_bytes,
    "container_name", "", "container")) by (container_name)
 ### 计算pod的内存使用情况,单位为MB，可以按需设定阈值，有两个表达式都可以实现
          - sum (container_memory_working_set_bytes{image!="",name=~"^k8s_.*"}) by (pod_name) /1024 /1024  #低版本pod_name改成kubernetes_pod_name
          - sort_desc(sum(container_memory_usage_bytes{image!=""}) by (io_kubernetes_container_name, image)) / 1024 / 1024   #通用


 ### 根据相同的pod_name来计算过去一分钟内pod 的 cpu使用率,metric名称版本不同也有些不一样：
          - sum by (pod_name)( rate(container_cpu_usage_seconds_total{image!=""}[1m] ) ) * 100 > 70  #高版本
(sum(rate(container_cpu_usage_seconds_total[3m])) BY (ip, name) * 100) > 80
          - sum by (kubernetes_pod_name)( rate(container_cpu_usage_seconds_total{image!=""}[1m] ) ) * 100 > 70  #低版本


### 计算pod的网络IO情况，单位为Mbps
# rx方向
- sort_desc(sum by (kubernetes_pod_name) (rate (container_network_receive_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 * 8 > 100 #低版本
 sort_desc(sum by (pod_name) (rate (container_network_receive_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 *8  > 100 #高版本
# tx方向
- sort_desc(sum by (kubernetes_pod_name) (rate (container_network_transmit_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 * 8 > 100 #低版本
- sort_desc(sum by (pod_name) (rate (container_network_transmit_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 *8  > 100 #高版本          
 ### 计算pod cpu使用：
- sum(sum by (io_kubernetes_container_name)( rate(container_cpu_usage_seconds_total{image!=""}[1m] ) )) / count(node_cpu{mode="system"}) * 100
- sum (rate (container_cpu_usage_seconds_total{id="/"}[1m])) / sum (machine_cpu_cores) * 100

node-exporter:
        ### 主要包含node相关的指标
        # url: http://$NODE_IP:31672/metrics
        metric expr:
          ### node磁盘使用率
          - (node_filesystem_size_bytes - node_filesystem_free_bytes) / node_filesystem_size_bytes * 100 > 80  
          ### node内存使用率
          - (node_memory_MemTotal_bytes - node_memory_MemFree_bytes) / node_memory_MemTotal_bytes  * 100 > 80  
##node内存使用剩余 < 10%
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes ))* 100 <10


# 集群cpu使用率
  - (sum(rate(node_cpu_seconds_total[1m])) - sum(rate(node_cpu_seconds_total{mode="idle"}[1m]))) / sum(rate(node_cpu_seconds_total[1m]))  * 100 > 80
#nodecpu负载
100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
 # 在老版本的exporter中`node_cpu_seconds_total`这个metric值叫`node_cpu`,因此老版本使用这个表达式：
- (sum(rate(node_cpu[1m])) - sum(rate(node_cpu{mode="idle"}[1m]))) / sum(rate(node_cpu[1m]))  * 100 > 80
# 集群node网络IO
rx方向
sort_desc(sum by (node) (rate (node_network_receive_bytes_total{device="eth0"}[2m]) )) /1024 /1024 /60 *8 >100
tx方向
sort_desc(sum by (node) (rate (node_network_transmit_bytes_total{device="eth0"}[2m]) )) /1024 /1024 /60 *8 >100
#磁盘读取数据 >50MB/s
 sum by (instance) (irate(node_disk_read_bytes_total[2m])) / 1024 / 1024 > 50
#磁盘写入数据 >50MB/s
sum by (instance) (irate(node_disk_written_bytes_total[2m])) / 1024 / 1024 > 50
磁盘空间不足/分区可用<10%
(1- node_filesystem_free_bytes{mountpoint ="/"} / node_filesystem_size_bytes{mountpoint ="/"}) * 100 < 10
    mysql-exporter:
        ### 主要包含mysql相关指标
        ## url: http://$Mysql_IP:9104/metrics
            # innodb各类型缓存缓存大小：
              - InnoDB Buffer Pool Data size : mysql_global_status_innodb_page_size * on (instance) mysql_global_status_buffer_pool_pages{state="data"}
              - InnoDB Log Buffer Size: mysql_global_variables_innodb_log_buffer_size
              - InnoDB Additional Memory Pool Size: mysql_global_variables_innodb_additional_mem_pool_size
              - InnoDB Dictionary Size: mysql_global_status_innodb_mem_dictionary
              - Key Buffer Size: mysql_global_variables_key_buffer_size
              - Query Cache Size: mysql_global_variables_query_cache_size
              - Adaptive Hash Index Size: mysql_global_status_innodb_mem_adaptive_hash


        metric expr:
          # 实例启动时间,单位s，三分钟内有重启记录则告警
          - mysql_global_status_uptime < 180  

          # 每秒查询次数指标
          - rate(mysql_global_status_questions[5m]) > 500

          # 连接数指标
          - rate(mysql_global_status_connections[5m]) > 200

          # mysql接收速率,单位Mbps
 - rate(mysql_global_status_bytes_received[3m]) * 1024 * 1024 * 8   > 50

# mysql传输速率,单位Mbps
- rate(mysql_global_status_bytes_sent[3m]) * 1024 * 1024 * 8   > 100

# 慢查询
- rate(mysql_global_status_slow_queries[30m]) > 3

# 死锁
- rate(mysql_global_status_innodb_deadlocks[3m]) > 1

 # 活跃线程小于30%
 - mysql_global_status_threads_running / mysql_global_status_threads_connected * 100 < 30


# innodb缓存占用缓存池大小超过80%
- (mysql_global_status_innodb_page_size * on (instance) mysql_global_status_buffer_pool_pages{state="data"} +  on (instance) mysql_global_variables_innodb_log_buffer_size +  on (instance) mysql_global_variables_innodb_additional_mem_pool_size + on (instance)  mysql_global_status_innodb_mem_dictionary + on (instance)  mysql_global_variables_key_buffer_size + on (instance)  mysql_global_variables_query_cache_size + on (instance) mysql_global_status_innodb_mem_adaptive_hash )  / on (instance) mysql_global_variables_innodb_buffer_pool_size * 100 > 80告警规则
```

配置告警规则

```
    - name: alert-rule
      rules:
      ### Node监控
      - alert: NodeFilesystemUsage-high
        expr: (node_filesystem_size_bytes - node_filesystem_free_bytes) / node_filesystem_size_bytes * 100 > 80 
        for: 2m
        labels:
          team: node
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: High Node Filesystem usage detected"
          description: "{{$labels.instance}}: Node Filesystem usage is above 80% ,(current value is: {{ $value }})"         
      - alert: NodeMemoryUsage
        expr: (node_memory_MemTotal_bytes - node_memory_MemFree_bytes) / node_memory_MemTotal_bytes  * 100 > 80
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: High Node Memory usage detected"
          description: "{{$labels.instance}}: Node Memory usage is above 80% ,(current value is: {{ $value }})"
      - alert: NodeCPUUsage
        expr: (sum(rate(node_cpu_seconds_total[1m])) - sum(rate(node_cpu_seconds_total{mode="idle"}[1m]))) / sum(rate(node_cpu_seconds_total[1m]))  * 100 > 80
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Node High CPU usage detected"
          description: "{{$labels.instance}}: Node CPU usage is above 80% ,(current value is: {{ $value }})"
      - alert: NodeCPUUsage_
        expr: (sum(rate(node_cpu[1m])) - sum(rate(node_cpu{mode="idle"}[1m]))) / sum(rate(node_cpu[1m]))  * 100 > 80
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Node High CPU usage detected"
          description: "{{$labels.instance}}: Node CPU usage is above 80% ,(current value is: {{ $value }})"   
       ### Pod监控
      - alert: PodMemUsage
        expr: container_memory_usage_bytes{container_name!=""} / container_spec_memory_limit_bytes{container_name!=""}  *100 != +Inf > 80
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High Mem usage detected"
          description: "{{$labels.instance}}: Pod Mem is above 80% ,(current value is: {{ $value }})"
      - alert: PodMemUsage_
        expr: container_memory_usage_bytes{kubernetes_container_name!=""} / container_spec_memory_limit_bytes{kubernetes_container_name!=""}  *100 != +Inf > 90
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High Mem usage detected"
          description: "{{$labels.instance}}: Pod Mem is above 80% ,(current value is: {{ $value }})"
      - alert: PodCpuUsage
        expr: sum by (pod_name)( rate(container_cpu_usage_seconds_total{image!=""}[1m] ) ) * 100 > 70
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High CPU usage detected"
          description: "{{$labels.instance}}: Pod CPU is above 80% ,(current value is: {{ $value }})"
      - alert: PodCpuUsage_
        expr: sum by (kubernetes_pod_name)( rate(container_cpu_usage_seconds_total{image!=""}[1m] ) ) * 100 > 70
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High CPU usage detected"
          description: "{{$labels.instance}}: Pod CPU is above 80% ,(current value is: {{ $value }})"
      - alert: NetI/O_RX
        expr: sort_desc(sum by (kubernetes_pod_name) (rate (container_network_receive_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 * 8 > 500
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High NetI/O_RX detected"
          description: "{{$labels.instance}}: Pod NetI/O_RX is more than 500Mbps ,(current value is: {{ $value }})"       
      - alert: NetI/O_RX_
        expr: sort_desc(sum by (pod_name) (rate (container_network_receive_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 *8  > 500
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High NetI/O_RX detected"
          description: "{{$labels.instance}}: Pod NetI/O_RX is more than 500Mbps ,(current value is: {{ $value }})"                
      - alert: NetI/O_TX
        expr: sort_desc(sum by (kubernetes_pod_name) (rate (container_network_transmit_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 * 8 > 500
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High NetI/O_TX detected"
          description: "{{$labels.instance}}: Pod NetI/O_TX is more than 100Mbps ,(current value is: {{ $value }})"      
      - alert: NetI/O_TX_
        expr: sort_desc(sum by (pod_name) (rate (container_network_transmit_bytes_total{name!=""}[1m]) )) /1024 /1024 /60 *8 > 500
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Pod High NetI/O_TX detected"
          description: "{{$labels.instance}}: Pod NetI/O_TX is more than 100Mbps ,(current value is: {{ $value }})"      
       ### Mysql监控
      - alert: Mysql_Instance_Reboot
        expr: mysql_global_status_uptime < 180 
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_Instance_Reboot detected"
          description: "{{$labels.instance}}: Mysql_Instance_Reboot in 3 minute (up to now is: {{ $value }} seconds"   
      - alert: Mysql_High_QPS
        expr: rate(mysql_global_status_questions[5m]) > 500 
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_High_QPS detected"
          description: "{{$labels.instance}}: Mysql opreation is more than 500 per second ,(current value is: {{ $value }})"  
      - alert: Mysql_Too_Many_Connections
        expr: rate(mysql_global_status_connections[5m]) > 100
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql Too Many Connections detected"
          description: "{{$labels.instance}}: Mysql Connections is more than 100 per second ,(current value is: {{ $value }})"  
      - alert: Mysql_High_Recv_Rate
        expr: rate(mysql_global_status_bytes_received[3m]) * 1024 * 1024 * 8   > 100
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_High_Recv_Rate detected"
          description: "{{$labels.instance}}: Mysql_Receive_Rate is more than 100Mbps ,(current value is: {{ $value }})"  
      - alert: Mysql_High_Send_Rate
        expr: rate(mysql_global_status_bytes_sent[3m]) * 1024 * 1024 * 8   > 100
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_High_Send_Rate detected"
          description: "{{$labels.instance}}: Mysql data Send Rate is more than 100Mbps ,(current value is: {{ $value }})"
      - alert: Mysql_Too_Many_Slow_Query
        expr: rate(mysql_global_status_slow_queries[30m]) > 3
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_Too_Many_Slow_Query detected"
          description: "{{$labels.instance}}: Mysql current Slow_Query Sql is more than 3 ,(current value is: {{ $value }})"
      - alert: Mysql_Deadlock
        expr: mysql_global_status_innodb_deadlocks > 0
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_Deadlock detected"
          description: "{{$labels.instance}}: Mysql Deadlock was found ,(current value is: {{ $value }})"          
      - alert: Mysql_Too_Many_sleep_threads
        expr: mysql_global_status_threads_running / mysql_global_status_threads_connected * 100 < 30
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_Too_Many_sleep_threads detected"
          description: "{{$labels.instance}}: Mysql_sleep_threads percent is more than {{ $value }}, please clean the sleeping threads"    
      - alert: Mysql_innodb_Cache_insufficient
        expr: (mysql_global_status_innodb_page_size * on (instance) mysql_global_status_buffer_pool_pages{state="data"} +  on (instance) mysql_global_variables_innodb_log_buffer_size +  on (instance) mysql_global_variables_innodb_additional_mem_pool_size + on (instance)  mysql_global_status_innodb_mem_dictionary + on (instance)  mysql_global_variables_key_buffer_size + on (instance)  mysql_global_variables_query_cache_size + on (instance) mysql_global_status_innodb_mem_adaptive_hash )  / on (instance) mysql_global_variables_innodb_buffer_pool_size * 100 > 80
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "{{$labels.instance}}: Mysql_innodb_Cache_insufficient detected"
          description: "{{$labels.instance}}: Mysql innodb_Cache was used more than 80% ,(current value is: {{ $value }})"
```

邮件告警目标

```
cat template/test.tmpl 
{{ define "email.default.html" }}
{{ range .Alerts }}
========start==========<br/>
告警程序: prometheus_alert<br/>
告警详情: {{ .Annotations.summary }}<br/>
告警级别: {{ .Labels.severity }}<br/>
告警类型: {{ .Labels.alertname }}<br/>
故障主机: {{ .Labels.instance }}<br/>
触发时间: {{ .StartsAt.Format "2006-01-02 15:04:05" }}<br/>
========end==========<br/>
{{ end }}
{{ end }}
```