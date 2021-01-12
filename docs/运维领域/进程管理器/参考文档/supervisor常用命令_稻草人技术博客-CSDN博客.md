# supervisor常用命令

![img](supervisor常用命令_稻草人技术博客-CSDN博客.assets/original.png)

[Shower稻草人](https://sunzhy.blog.csdn.net/) 2018-10-11 15:12:25 ![img](supervisor常用命令_稻草人技术博客-CSDN博客.assets/articleReadEyes.png) 10322 ![img](supervisor常用命令_稻草人技术博客-CSDN博客.assets/tobarCollect.png) 收藏 7

分类专栏： [Linux](https://blog.csdn.net/u013474436/category_5783021.html)

版权

查看所有任务状态: `supervisorctl status`

```l
# supervisorctl status
nginx                           RUNNING   pid 18752, uptime 22:59:40
redis                            RUNNING   pid 14542, uptime 45 days, 19:18:08
123
```

第一列是服务名；
第二列是运行状态，RUNNING表示运行中，FATAL 表示运行失败，STARTING表示正在启动,STOPED表示任务已停止；　
第三/四列是进程号,最后是任务已经运行的时间。

查看单个任务状态: `supervisorctl status 服务名`

```l
# supervisorctl status nginx
nginx                      RUNNING   pid 26073, uptime 1 day, 23:12:10
12
```

启动任务:`supervisorctl start 服务名`

```l
# supervisorctl stop nginx
nginx: stopped
#supervisorctl status nginx
nginx                      STOPPED   Jan 05 01:59 PM
1234
```

停止任务:`supervisorctl stop 服务名`

```l
# supervisorctl start nginx
nginx: started
# supervisorctl status nginx
nginx                      RUNNING   pid 32207, uptime 0:00:05
1234
```

重启任务:`supervisorctl restart 服务名`

```l
# supervisorctl restart nginx
nginx: stopped
nginx: started
# supervisorctl status nginx
nginx                      RUNNING   pid 4952, uptime 0:00:03
12345
```

其他命令：
`supervisorctl help`：帮助命令
`supervisorctl update` ：配置文件修改后可以使用该命令加载新的配置
`supervisorctl reload`： 重新启动配置中的所有程序