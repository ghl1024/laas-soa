# supervisor的使用简介

[![img](supervisor的使用简介-好记性不如烂笔头-51CTO博客.assets/wKioL1Tasy6SavnBAAAoAQuPrYw198_middle.jpg)](https://blog.51cto.com/nosmoking)

[pcnk](https://blog.51cto.com/nosmoking)关注0人评论[1411人阅读](javascript:;)[2014-12-24 15:54:32](javascript:;)

supervisor的使用简介

2017/12/26

```bash
1、安装
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
easy_install supervisor

或者
yum install python-pip
pip install supervisor


2、配置文件：
# echo_supervisord_conf > /etc/supervisord.conf \
&& mkdir /etc/supervisor.d \
&& /usr/bin/echo_supervisord_conf >/etc/supervisord.conf  \
&& echo -e '[include]\nfiles=/etc/supervisor.d/*.ini' >>/etc/supervisord.conf \
&& grep ^[^\;] /etc/supervisord.conf



3、启动supervisord服务：
# whereis supervisord
supervisord: /etc/supervisord.conf /usr/local/bin/supervisord
# /usr/local/bin/supervisord -c /etc/supervisord.conf

并增加到开机启动/etc/rc.local中
# echo '/usr/local/bin/supervisord -c /etc/supervisord.conf' >>/etc/rc.local

4、配置服务
# cd /etc/supervisor.d
# cat sshd.ini
[program:sshd]
command=/usr/sbin/sshd -D

# cat test.ini
[program:test]
command=/usr/bin/php  xxx.php
process_name=%(program_name)s_%(process_num)02d
numprocs=5
user=nobody

# cat uwsgi.ini
[program:uwsgi]
command=/usr/local/bin/uwsgi --http 127.0.0.1:8090 --chdir /opt/test-django/www --module www.wsgi >/var/log/nginx/uwsgi.log 2>&1

重新加载supervisord服务：
# supervisorctl reload
Restarted supervisord

验证
# supervisorctl status
uwsgi                            RUNNING   pid 15041, uptime 0:00:17
# ss -antp src :8090
State       Recv-Q Send-Q                     Local Address:Port                       Peer Address:Port
LISTEN      0      100                            127.0.0.1:8090                                  *:*      users:(("uwsgi",15041,4),("uwsgi",15042,4))

调整user1增加sudo的权限：
user1 ALL=NOPASSWD: /usr/bin/supervisorctl
然后通过这样的方式来管理：
$ sudo supervisorctl status|stop|start|restart


5、新增一个服务的正确姿势
总结下来就2个指令：
supervisorctl reread
supervisorctl update

实例：
[root@tvm001 supervisor.d]# pwd
/etc/supervisor.d

[root@tvm001 supervisor.d]# ls
gogogo.ini  uwsgi_asset.ini  uwsgi.ini

[root@tvm001 supervisor.d]# cat gogogo.ini
[program:gogogo]
command=/bin/cat
autostart=true
autorestart=true
stdout_logfile=/tmp/gogogo.stdout.log
stderr_logfile=/tmp/gogogo.stderr.log

[root@tvm001 supervisor.d]# supervisorctl status
uwsgi                            RUNNING   pid 26248, uptime 5:13:02
uwsgi_asset                      RUNNING   pid 26247, uptime 5:13:02
[root@tvm001 supervisor.d]# supervisorctl reread
gogogo: available
[root@tvm001 supervisor.d]# supervisorctl status
uwsgi                            RUNNING   pid 26248, uptime 5:13:12
uwsgi_asset                      RUNNING   pid 26247, uptime 5:13:12
[root@tvm001 supervisor.d]# supervisorctl update
gogogo: added process group
[root@tvm001 supervisor.d]# supervisorctl status
gogogo                           RUNNING   pid 27147, uptime 0:00:04
uwsgi                            RUNNING   pid 26248, uptime 5:13:25
uwsgi_asset                      RUNNING   pid 26247, uptime 5:13:25
[root@tvm001 supervisor.d]#


ZYXW、参考
1、doc
http://www.supervisord.org/running.html#supervisorctl-actions
```