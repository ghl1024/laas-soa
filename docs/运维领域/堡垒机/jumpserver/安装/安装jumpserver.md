

# 安装jumpserver

服务器调优

修改系统设置如 最大打开文件数

```
$ vim /etc/security/limits.d/20-nproc.conf

*     soft   nofile    65535
*     hard   nofile    65535
*     soft   nproc     65535
*     hard   nproc     65535
root  soft   nproc     unlimited

$ reboot  # 重启服务器
```

参考文档: 参考文档\安装\极速部署 - JumpServer 文档.md

```
cd /opt
yum -y install wget
wget https://github.com/jumpserver/installer/releases/download/v2.6.1/jumpserver-installer-v2.6.1.tar.gz
tar -xf jumpserver-installer-v2.6.1.tar.gz
cd jumpserver-installer-v2.6.1
export DOCKER_IMAGE_PREFIX=docker.mirrors.ustc.edu.cn
cat config-example.txt
```

修改配置文件 `vi /opt/jumpserver-installer-v2.6.1/config-example.txt`

```
HTTP_PORT=80
HTTPS_PORT=443

DB_PASSWORD=<mysql_root_password>
REDIS_PASSWORD=<redis_auth>
MYSQL_ROOT_PASSWORD=<mysql_root_password>
```

配置镜像加速: 在安装完docker之后

```
vi /etc/docker/daemon.json
{
  "registry-mirrors": ["https://ibqko7t0.mirror.aliyuncs.com"],
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

安装jumpserver

```
./jmsctl.sh install
```

# 启动jumpserver

启动jumpserver

```
# 启动
./jmsctl.sh start

# 重启
$ ./jmsctl.sh restart

# 关闭, 不包含数据库
$ ./jmsctl.sh stop

# 关闭所有
$ ./jmsctl.sh down

# 备份数据库
$ ./jmsctl.sh backup_db

# 查看日志
$ ./jmsctl.sh tail
```

# 访问jumpserver

访问jumpserver:

http://<服务器ip>

建议配置一个域名



连接mysql

```
docker exec -it jms_mysql /bin/bash

echo $MYSQL_ROOT_PASSWORD

mysql -uroot -p
```

连接redis

```
docker exec -it jms_redis /bin/sh

echo $REDIS_PASSWORD

redis-cli -a <redis_auth>
```



默认登录账号/密码: admin/admin

登录之后建议修改账号密码

# 参考文档

https://jumpserver.readthedocs.io

https://docs.jumpserver.org/zh/master/