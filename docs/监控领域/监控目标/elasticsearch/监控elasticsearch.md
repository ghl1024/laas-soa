192.168.2.15

# 数据采集

查看es是否可用

```
curl http://192.168.2.15:9200
```

部署

```
docker pull justwatch/elasticsearch_exporter:1.1.0

docker stop es_exporter && docker rm es_exporter
docker run -d --name es_exporter --restart=always -p 9114:9114 justwatch/elasticsearch_exporter:1.1.0 --es.uri=http://192.168.2.15:9200 --es.all --es.cluster_settings --es.indices --es.indices_settings --es.shards --es.snapshots
docker logs -f --tail 100 es_exporter
```

查看metrics信息: http://192.168.2.21:9114/metrics

# 数据抓取

修改prometheus配置文件

```
  - job_name: 'elasticsearch'
    scrape_interval: 60s
    static_configs:
    - targets: ['192.168.2.21:9114']
```

# 告警

参考 elasticsearch.rules文件

