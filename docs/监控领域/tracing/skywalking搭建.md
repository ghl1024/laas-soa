整体分为ui、oap、es 三部分组成

# oap

安装

```
docker stop oap && docker rm oap
docker run --name oap -p 11800:11800 -p 12800:12800 -v /etc/localtime:/etc/localtime --restart always -d apache/skywalking-oap-server:8.3.0-es7

docker logs -f --tail 100 oap
```

# ui

安装

```
docker stop ui && docker rm ui

docker run --name ui -p 8081:8080 -v /etc/localtime:/etc/localtime --restart always -d -e SW_OAP_ADDRESS=<oap_ip>:12800 apache/skywalking-ui:8.3.0

docker logs -f --tail 100 ui
```



