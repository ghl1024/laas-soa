思路还是基于prometheus+grafana

是否继续使用prometheus operator? 还是直接使用prometheus?

先直接自己搭建吧

多个redis实例时使用,分隔

```
docker stop redis_exporter
docker rm   redis_exporter

docker run -d --name redis_exporter -p 9121:9121 oliver006/redis_exporter:v1.13.1-alpine --debug --redis.addr redis://192.168.90.235:7002,redis://192.168.90.235:7003,redis://192.168.90.235:7004

docker run -d --name redis_exporter -p 9121:9121 oliver006/redis_exporter:v1.13.1-alpine --redis.addr=192.168.90.235:7002,192.168.90.235:7003,192.168.90.235:7004

--redis.addr=172.17.0.5:6379,172.17.0.6:6379

docker run -d --name redis_exporter -p 9121:9121 oliver006/redis_exporter --redis.addr 192.168.90.235:7002,192.168.90.235:7003,192.168.90.235:7004


docker logs -f redis_exporter
```



修改prometheus数据挂载点

```
scrape_configs:
  - job_name: 'redis_exporter_targets'
    static_configs:
      - targets:
        - 192.168.90.235:7002
        - 192.168.90.235:7003
        - 192.168.90.235:7004
    metrics_path: /scrape
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 192.168.90.223:9121
  - job_name: 'redis_exporter'
    static_configs:
      - targets:
        - 192.168.90.223:9121
```

重启prometheu, 查看是否有修改错误

```
docker restart prometheus
docker logs -f prometheus
```

# 部署redis_exporter

```
docker stop redis_exporter
docker rm   redis_exporter

docker run -d --name redis_exporter -p 9121:9121 -e REDIS_EXPORTER_INCL_SYSTEM_METRICS="true" oliver006/redis_exporter:v1.13.1 --debug



docker run -d --name redis_exporter -p 9121:9121 -e REDIS_ADDR="redis://192.168.90.235:7002,redis://192.168.90.235:7003,redis://192.168.90.235:7004" oliver006/redis_exporter:v1.13.1 --debug

docker run -it -p 9121:9121 -e REDIS_ADDR="192.168.90.235:7002,192.168.90.235:7003,192.168.90.235:7004" oliver006/redis_exporter

docker run -it -p 9121:9121 -e REDIS_ADDR="redis://192.168.90.235:7002" oliver006/redis_exporter:v1.13.1 --debug

docker run -d --name redis_exporter -p 9121:9121 -e REDIS_ADDR="redis://192.168.90.235:7002" oliver006/redis_exporter:v1.13.1 --debug

docker logs -f redis_exporter
```



```
docker run -d --name redis_exporter -p 9121:9121 -e REDIS_EXPORTER_REDIS_ONLY_METRICS="false" -e REDIS_EXPORTER_LOG_FORMAT="json" -e REDIS_EXPORTER_INCL_SYSTEM_METRICS="true" oliver006/redis_exporter:v1.13.1 --debug
```



# 调整grafana

在grafana中添加dashboard

导入这个两个文件json

grafana_prometheus_redis_dashboard.json
grafana_prometheus_redis_dashboard_exporter_version_0.3x.json



目前发现使用 grafana_prometheus_redis_dashboard.json 有数据，比较好

# 监控什么

# 一些问题



oliver006/redis_exporter err: ERR unknown command 'SLOWLOG'"

