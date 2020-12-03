目标主机:

192.168.2.240:2181,192.168.3.100:2181,192.168.4.195:2181

调试zk监控数据

开启mntr

```
# 安装nc
yum install -y nc

echo mntr| nc 127.0.0.1 2181

# 如果出现以下内容则需要调整配置文件
mntr is not executed because it is not in the whitelist.

find / |grep zoo.cfg
vi /data/apache-zookeeper-3.5.6-bin/conf/zoo.cfg

4lw.commands.whitelist=mntr,ruok
或者
4lw.commands.whitelist=stat, ruok, conf, isro
或者
4lw.commands.whitelist=*


cd /data/apache-zookeeper-3.5.6-bin

bin/zkServer.sh status


密切关注zookeeper运行日志
cat bin/zkEnv.sh |grep ZOO_LOG_DIR
ll logs

tail -f -n 100 logs/zookeeper-root-server-redis02.out
tail -f -n 100 logs/zookeeper-root-server-reids03.out
tail -f -n 100 logs/zookeeper-root-server-redis01.out

./bin/zkServer.sh  restart
```



安装

```
docker stop zk_exporter
docker rm   zk_exporter

docker run -d --name zk_exporter -p 9141:9141 dabealu/zookeeper-exporter:v0.1.10 --zk-hosts="192.168.2.240:2181,192.168.3.100:2181,192.168.4.195:2181" --timeout=5

docker logs -f --tail 100 zk_exporter
```



添加数据抓取点到prometheus

```
  - job_name: 'zookeeper'
    scrape_interval: 60s
    static_configs:
    - targets: ['192.168.2.21:9141']
```

添加dashboard

https://grafana.com/grafana/dashboards/11442



测试访问：

http://192.168.2.21:9141/metrics