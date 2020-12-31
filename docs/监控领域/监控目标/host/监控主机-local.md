主机

```
192.168.90.182:9101
192.168.90.190:9101
192.168.90.220
192.168.90.237

192.168.90.201
```



如果主机上已经有9100则修改启动参数使用其他端口



```
vi /etc/systemd/system/node_exporter.service

--web.listen-address=0.0.0.0:9101

```



```
systemctl daemon-reload
systemctl restart  node_exporter
systemctl status node_exporter
systemctl enable node_exporter
```



