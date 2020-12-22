部署

```
docker stop mssql-exporter && docker rm mssql-exporter
docker run -e SERVER=<ip> -e USERNAME=<username> -e PASSWORD=<password> -e DEBUG=app -p 4000:4000 --name mssql-exporter awaragi/prometheus-mssql-exporter:v0.4.1
docker logs -f --tail 100 mssql-exporter
```





添加数据抓取点

```
  - job_name: 'mssql'
    scrape_interval: 60s
    static_configs:
    - targets: ['172.30.1.153:4000']
      labels:
        name: 'oa'
```

