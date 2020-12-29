###### 整体分为ui、oap、es 三部分组成

192.168.2.20

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



# oap

安装

```
rm -rf /data/tristan/skywalking
mkdir -p /data/tristan/skywalking && chmod 777 /data/tristan/skywalking
docker run -d --name oap apache/skywalking-oap-server:8.3.0-es7
docker cp oap:/skywalking/config/ /data/tristan/skywalking/
sleep 10
ll /data/tristan/skywalking/config/
docker stop oap && docker rm oap

docker stop oap && docker rm oap

docker run -d \
  --name=oap \
  --restart=always \
  -p 11800:11800 -p 12800:12800 \
  -v /etc/localtime:/etc/localtime \
  -v /data/tristan/skywalking/config:/skywalking/config \
  -e SW_STORAGE=elasticsearch7 -e SW_STORAGE_ES_CLUSTER_NODES=192.168.5.5:9200 \
  apache/skywalking-oap-server:8.3.0-es7


docker logs -f --tail 100 oap
```



```
请谨慎使用influxdb, 因为可能你驾驭不住这个存储

docker run -d \
  --name=oap \
  --restart=always \
  -p 11800:11800 -p 12800:12800 \
  -v /etc/localtime:/etc/localtime \
  -v /data/tristan/skywalking/config:/skywalking/config \
  -e SW_STORAGE=influxdb -e SW_STORAGE_INFLUXDB_URL=http://192.168.5.5:8086 \
  apache/skywalking-oap-server:8.3.0-es7
```



修改nginx中原来skywalking对内访问地址, 实现oap替换, 充分验证

修改nginx中原来skywalking对外访问地址

# ui

安装

```
docker stop ui && docker rm ui

docker run --name ui -p 8080:8080 -v /etc/localtime:/etc/localtime --restart always -d -e SW_OAP_ADDRESS=192.168.2.20:12800 apache/skywalking-ui:8.3.0

docker logs -f --tail 100 ui
```



# nginx

使用nginx代理ui

nginx访问时进行用户名-密码认证

## 创建nginx用户名-密码登录文件

```
yum  -y install httpd-tools
htpasswd -c passwd admin
> 输入密码 两次
```

部署

```
rm -rf /data/tristan/nginx
mkdir -p /data/tristan/nginx

sudo cat >> /data/tristan/nginx/default.conf <<EOF
server {
    listen 80;
	
    auth_basic "Please input password";
    auth_basic_user_file /data/tristan/nginx/passwd;
    gzip on;
    gzip_vary on;
    gzip_disable "msie6";
    gzip_comp_level 6;
    gzip_min_length 1100;
    gzip_buffers 16 8k;
    gzip_proxied any;
    gzip_types
        text/plain
        text/css
        text/js
        text/xml
        text/javascript
        application/javascript
        application/x-javascript
        application/json
        application/xml
        application/xml+rss;


	location / {
        proxy_pass http://192.168.2.20:8080;
    }
}
EOF


docker stop nginx
docker rm   nginx


docker run -d \
  --name=nginx --restart=always \
  -p 80:80 \
  -v /data/tristan/nginx/default.conf:/etc/nginx/conf.d/default.conf \
  -v  /data/tristan/nginx/passwd:/data/tristan/nginx/passwd \
  nginx:1.19.6-alpine-perl

docker logs -f --tail 100 nginx
```

