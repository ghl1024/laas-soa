整体分为ui、oap、es 三部分组成

192.168.2.35

# es

```
rm -rf /data/tristan/elasticsearch
mkdir -p /data/tristan/elasticsearch/data && chmod 777 /data/tristan/elasticsearch/data

grep vm.max_map_count /etc/sysctl.conf
sysctl -w vm.max_map_count=262144

docker stop elasticsearch && docker rm elasticsearch
docker run -d \
  --name=elasticsearch \
  --restart=always \
  -p 9200:9200 -p 9300:9300 \
  -v /data/tristan/elasticsearch/data:/usr/share/elasticsearch/data \
  -e "discovery.type=single-node" \
  -e "ES_JAVA_OPTS=-Xms8g -Xmx8g" \
  -e "bootstrap.memory_lock=true" --ulimit memlock=-1:-1 \
  --ulimit nofile=65535:65535 \
  docker.elastic.co/elasticsearch/elasticsearch:7.10.0

docker logs -f --tail 100 elasticsearch

curl -X GET "localhost:9200/_cat/nodes?v&pretty"
```



# oap

安装

```
docker stop oap && docker rm oap

docker run -d \
  --name=oap \
  --restart=always \
  -p 11800:11800 -p 12800:12800 \
  -v /etc/localtime:/etc/localtime \
  -e SW_STORAGE=elasticsearch7 -e SW_STORAGE_ES_CLUSTER_NODES=192.168.2.35:9200 \
  apache/skywalking-oap-server:8.3.0-es7

docker logs -f --tail 100 oap
```

修改nginx中原来skywalking对内访问地址, 实现oap替换, 充分验证

修改nginx中原来skywalking对外访问地址

# ui

安装

```
docker stop ui && docker rm ui

docker run --name ui -p 8081:8080 -v /etc/localtime:/etc/localtime --restart always -d -e SW_OAP_ADDRESS=192.168.2.35:12800 apache/skywalking-ui:8.3.0

docker logs -f --tail 100 ui
```







