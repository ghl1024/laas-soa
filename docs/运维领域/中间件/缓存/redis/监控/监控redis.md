安装

```
docker stop redis_exporter
docker rm   redis_exporter

docker run -d --name redis_exporter -p 9121:9121 --env REDIS_ADDR=redis://192.168.3.100:7001 --env REDIS_EXPORTER_INCL_SYSTEM_METRICS=true oliver006/redis_exporter:v1.13.1 --debug

docker logs -f --tail 100 redis_exporter
```



```
mkdir -p /data/tristan/redis_exporter && chmod 777 /data/tristan/redis_exporter
cd /data/tristan/redis_exporter
wget https://github.com/oliver006/redis_exporter/releases/download/v1.13.1/redis_exporter-v1.13.1.linux-amd64.tar.gz

tar -zvxf redis_exporter-v1.3.5.linux-amd64.tar.gz
cd redis_exporter-v1.3.5.linux-amd64

./redis_exporter -redis.addr=redis://192.168.3.100:7001 -include-system-metrics=true -count-keys=db0=*:* -debug
./redis_exporter -redis.addr=redis://192.168.3.100:7001 -include-system-metrics=true -debug

nohup ./redis_exporter -redis.addr redis://192.168.3.100:7001 >redis_exporter.log 2>&1 &
```





修改prometheus数据挂载点

```
scrape_configs:
  - job_name: 'redis_exporter_targets'
    static_configs:
      - targets:
        - redis://192.168.2.240:7001
        - redis://192.168.3.100:7001
        - redis://192.168.4.195:7001
    metrics_path: /scrape
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 192.168.2.21:9121
  - job_name: 'redis_exporter'
    static_configs:
      - targets:
        - 192.168.2.21:9121
```

重启prometheu, 查看是否有修改错误

```
curl -X POST http://localhost:9090/-/reload
docker logs -f --tail 100 prometheus
```

# 告警

redis.rules

```
groups:
  - name: redis
    rules:
      - alert: RedisDown
        expr: redis_up == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Redis down (instance {{ $labels.instance }})"
          description: "Redis instance is down\n  VALUE = {{ $value }}\n  LABELS: {{ $labels }}"
      - alert: RedisOutOfMemory
        expr: redis_memory_used_bytes / redis_total_system_memory_bytes * 100 > 90
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Redis out of memory (instance {{ $labels.instance }})"
          description: "Redis is running out of memory (> 90%)\n  VALUE = {{ $value }}\n  LABELS: {{ $labels }}"
      - alert: RedisTooManyConnections
        expr: redis_connected_clients > 100
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Redis too many connections (instance {{ $labels.instance }})"
          description: "Redis instance has too many connections\n  VALUE = {{ $value }}\n  LABELS: {{ $labels }}"
```

