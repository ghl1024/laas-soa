# es

假如你下载镜像特别慢:

```
docker save -o elasticsearch.tar dock
scp elasticsearch.tar root@192.168.2.20:/root
docker import  elasticsearch.tar docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```



```
docker pull elasticsearch:7.9.3
```

安装

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
  -v /usr/share/zoneinfo/Asia/Shanghai:/etc/localtime \
  -v /data/tristan/elasticsearch/data:/usr/share/elasticsearch/data \
  -e "discovery.type=single-node" \
  -e "ES_JAVA_OPTS=-Xms4g -Xmx4g" \
  -e "bootstrap.memory_lock=true" --ulimit memlock=-1:-1 \
  --ulimit nofile=65535:65535 \
  docker.elastic.co/elasticsearch/elasticsearch:7.10.0

docker logs -f --tail 100 elasticsearch

curl -X GET "localhost:9200/_cat/nodes?v&pretty"
```

调优

```
curl -XGET localhost:9200/_cluster/allocation/explain?pretty

curl -X PUT localhost:9200/_cluster/settings -H "Content-Type: application/json" -d '{ "persistent": { "cluster.max_shards_per_node": "4000" } }'
```

