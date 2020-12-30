# supervisor 进程管理工具

![img](supervisor 进程管理工具_鸟叔-CSDN博客.assets/original.png)

[IT界鸟叔](https://blog.csdn.net/kexiaoling) 2018-07-31 13:36:28 ![img](supervisor 进程管理工具_鸟叔-CSDN博客.assets/articleReadEyes.png) 649 ![img](supervisor 进程管理工具_鸟叔-CSDN博客.assets/tobarCollect.png) 收藏 1

分类专栏： [Linux](https://blog.csdn.net/kexiaoling/category_2408313.html)

版权

- **Supervisor 简介**

supervisor 是一个用python写的小工具， 目的是监控进程。

他以子进程的形式创建那些需要被监控的进程（在 supervisord.conf 中添加），

当子进程异常退出时， 他会重启该子进程；

注意这里必须时异常(throw new Exception)退出他才会重启，

如果是正常退出（return,  exit ）是不会重启的。

 

 

- **安装supervisor**

 

apt install supervisor

 

默认配置文件路径：

/etc/supervisor/supervisord.conf 

 

 

配置项保持默认即可， 不需要改动。

 

 

 

- **使用supervisor**

 

1. 添加需要被监控的进程

 

index.php :

 

**echo** **"Hello World"**;

*sleep*(10);

**throw new** \Exception(**"Hello World****”**);

 

 

在 /etc/supervisor/supervisord.conf 末尾加入

 

[program:hello]

command=php /wwwroot/bug.[3322.org/index.php](http://3322.org/index.php)

 

 

 

在index.php代码中故意抛出了异常， 查看supervisord.log日志就能发现进程异常退出， 然后又重启了。

 

 

1. 启动supervisord

 

supervisord -c /etc/supervisor/supervisord.conf 

 

-c : 指定配置文件路径

 

如果修改了配置， 无需重启进程，可通过下面的supervisorctl 来热更新配置文件

 

1. 进程管理工具supervisorctl

 

supervisorctl 可用于管理supervisord 以及其子进程

 

比如：

 

热更新supervisord进程的配置文件

 

supervisorctl update

 

启动所有子进程

 

 supervisorctl start all     

 

查看子进程的状态

 

 supervisorctl status

 

 

重启子进程

 

supervisorctl restart all

 

 

- **supervisor日志**

 

Supervisor 默认会生成3个日志文件：

 

/var/log/supervisor/hello-stderr---supervisor-S3lrCS.log  子进程的错误日志

 

/var/log/supervisor/hello-stdout---supervisor-t35eJP.log  子进程的输出日志

 

/var/log/supervisor/supervisord.log  子进程的启动/退出相关日志

 

- **事件监听**

 

事件监听目的是当监听到子进程异常退出时可以通知（邮件或其他）相关人员。

 

详细使用参考：

http://www.supervisord.org/events.html