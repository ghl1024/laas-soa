创建监控专用用户

```
drop user exporter@'localhost';
CREATE USER 'exporter'@'%' IDENTIFIED BY 'XXXXXXXX' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';
```



运行

```
docker pull prom/mysqld-exporter:v0.12.1

docker stop mysql_exporter && docker rm mysql_exporter
docker run -d \
  --name mysql_exporter --restart=always \
  -p 9104:9104 \
  -e DATA_SOURCE_NAME="user:password@(hostname:3306)/" \
  prom/mysqld-exporter:v0.12.1

docker logs -f --tail 100 mysql_exporter
```



添加数据抓取点

```
  - job_name: 'mysql'
    scrape_interval: 60s
    static_configs:
    - targets: ['192.168.2.21:9104']
      labels:
        mysqlname: 'polardb业务库'
```



参考文档:

https://github.com/prometheus/mysqld_exporter