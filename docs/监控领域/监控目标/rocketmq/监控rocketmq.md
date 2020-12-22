# 部署exporter

构建

```
rocketmq:
  config:
    webTelemetryPath: /metrics
    rocketmqVersion: ${ROCKET_MQ_VERSION:4_2_0}
    namesrvAddr: ${NAMESRV_ADDR:127.0.0.1:9876}
    enableCollect: true
    enableACL: ${ENABLE_ACL:false} # if >=4.4.0
    accessKey: ${ACCESS_KEY:} # if >=4.4.0
    secretKey: ${SECRET_KEY:} # if >=4.4.0
```



```
FROM maven:3-alpine as builder
COPY . .
RUN  mvn clean package -DskipTests
FROM java:8
COPY --from=builder target/*.jar app.jar
EXPOSE 5557
ENTRYPOINT ["java","-jar","app.jar"]
```

部署

```
docker stop rocketmq_exporter && docker rm rocketmq_exporter
docker rmi tanshilindocker/rocketmq-exporter
docker run -d \
  --name rocketmq_exporter --restart=always \
  -p 5557:5557 \
  -e ROCKET_MQ_VERSION="4_7_0" \
  -e NAMESRV_ADDR="" \
  -e ENABLE_ACL="true" \
  -e ACCESS_KEY="" \
  -e SECRET_KEY="" \
  tanshilindocker/rocketmq-exporter
docker logs -f --tail 100 rocketmq_exporter
```

# 添加prometheus采集点

vi /data/tristan/prometheus/prometheus.yml

```
   - job_name: 'rocketmq_exporter'
     static_configs:
     - targets: ['192.168.2.20:5557']
```

# 添加告警规则

rockermq.rules

```
groups:
- name: GaleraAlerts
  rules:
  - alert: RocketMQClusterProduceHigh
    expr: sum(rocketmq_producer_tps) by (cluster) >= 10
    for: 3m
    labels:
      severity: warning
    annotations:
      description: '{{$labels.cluster}} Sending tps too high.'
      summary: cluster send tps too high
  - alert: RocketMQClusterProduceLow
    expr: sum(rocketmq_producer_tps) by (cluster) < 1
    for: 3m
    labels:
      severity: warning
    annotations:
      description: '{{$labels.cluster}} Sending tps too low.'
      summary: cluster send tps too low
  - alert: RocketMQClusterConsumeHigh
    expr: sum(rocketmq_consumer_tps) by (cluster) >= 10
    for: 3m
    labels:
      severity: warning
    annotations:
      description: '{{$labels.cluster}} consuming tps too high.'
      summary: cluster consume tps too high
  - alert: RocketMQClusterConsumeLow
    expr: sum(rocketmq_consumer_tps) by (cluster) < 1
    for: 3m
    labels:
      severity: warning
    annotations:
      description: '{{$labels.cluster}} consuming tps too low.'
      summary: cluster consume tps too low
  - alert: ConsumerFallingBehind
    expr: (sum(rocketmq_producer_offset) by (topic) - on(topic)  group_right  sum(rocketmq_consumer_offset) by (group,topic)) - ignoring(group) group_left sum (avg_over_time(rocketmq_producer_tps[5m])) by (topic)*5*60 > 0
    for: 3m
    labels:
      severity: warning
    annotations:
      description: 'consumer {{$labels.group}} on {{$labels.topic}} lag behind
        and is falling behind (behind value {{$value}}).'
      summary: consumer lag behind
  - alert: GroupGetLatencyByStoretime
    expr: rocketmq_group_get_latency_by_storetime > 1000
    for: 3m
    labels:
      severity: warning
    annotations:
      description: 'consumer {{$labels.group}} on {{$labels.broker}}, {{$labels.topic}} consume time lag behind message store time
        and (behind value is {{$value}}).'
      summary: message consumes time lag behind message store time too much 
```

