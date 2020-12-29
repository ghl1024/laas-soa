```
docker pull influxdb:1.8.3
```

部署

```
mkdir -p /data/tristan/influxdb/data && chmod 777 /data/tristan/influxdb/data
mkdir -p /data/tristan/influxdb/config && chmod 777 /data/tristan/influxdb/config

拷贝配置
docker run --rm influxdb:1.8.3 influxd config > /data/tristan/influxdb/config/influxdb.conf

docker stop influxdb && docker rm influxdb

docker run -d --name influxdb \
      -e INFLUXDB_ADMIN_USER=root \
      -e INFLUXDB_ADMIN_PASSWORD= \
      -e INFLUXDB_DB=skywalking \
      -p 8086:8086 \
      -v /data/tristan/influxdb/data:/var/lib/influxdb \
      -v /data/tristan/influxdb/config/influxdb.conf:/etc/influxdb/influxdb.conf:ro \
      influxdb:1.8.3
docker logs -f --tail 100 influxdb

```

