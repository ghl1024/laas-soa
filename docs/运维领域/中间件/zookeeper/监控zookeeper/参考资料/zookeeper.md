```
同事的内部分享, 个人觉得可以分享给大家，我很久前自己有个人部署和学习了解过zookeeper，但没太认真研究和思考，我知道，有机会，肯定还需要进一步学习zookeeper的
```

1. 序言
2. 目录规划
3. 安装步骤 3.1 下载和解压 3.3 日志格式 3.4 配置文件 3.5 部署Zookeeper Server服务标识
4. 启动和关闭
5. 进程维护 5.1 安装 supervisor 5.2 supervisor 的目录规划 5.3 supervisor 的配置示例
6. 主配置文件：$HOME/app/supervisor/supervisord.conf
7. zookeeper 配置文件：$HOME/app/supervisor/conf.d/zookeeper.conf 5.3 supervisor 的启动
8. 增加环境变量：
9. 启动服务
10. 服务监控 6.1 zookeeper server JVM 内存监控 6.2 zookeeper server 运行状态监控
11. 环境信息：envi
12. 固定设置：conf
13. 连接总览：cons
14. 状态概览：mntr 【监控首页】
15. Session 的 watch 统计：wchs、wchc、wchp 【可以通过 Session ID 关联到 cons 查看细节】

## 1. 序言

本手册是 zookeeper 安装的建议文档，zookeeper后续可搭配Kafka使用，Kafka本身也自带zookeeper，但是根据组件的封装性和隔离性建议单独部署。

## 2. 目录规划

以下是 zookeeper 的标准化安装时核心的目录/文件规划：

| 对象         | 目录/文件                        | 备注                                                         |
| ------------ | -------------------------------- | ------------------------------------------------------------ |
| 根目录       | $HOME/app/zookeeper【软链接】    | 真实目录会自带版本号，通过软链接建立没有版本号的路径，方便切换和回滚组件版本，例如: lrwxrwxrwx 1 storm storm 15 Aug 24 16:02 zookeeper -> zookeeper-3.4.6 drwxr-xr-x 16 storm storm 4096 Aug 25 17:16 zookeeper-3.4.6 |
| 配置目录     | $HOME/app/zookeeper/conf/zoo.cfg | zookeeper server 的主配置文件                                |
| 数据目录     | /home1/data/zookeeper/           | zookeeper server 的数据目录，存放这 zookeeper server 内存数据库在磁盘上产生的所有快照文件 |
| 事务日志目录 | /home1/data/zookeeper/datalog/   | zookeeper server 的事务日志目录，在对 zookeeper server 内存数据库执行磁盘快照前，先写事务日志，成功后再执行快照操作。 |
| 服务标识文件 | /home1/data/zookeeper/myid       | zookeeper server 启动时的唯一标识                            |
| 日志目录     | /home1/logs/zookeeper/           | zookeeper server 的日志存放目录，这些日志描述 zookeeper server 系统运行时产生的信息 |

注意：

> 一般情况下，建议是 data 和 datalog 分开磁盘存放的，这样可以避免事务日志和快照文件对同一个磁盘的资源竞争，这样对于 zookeeper server 的吞吐率有着关键性的影响(如果存在吞吐率瓶颈时，可以尝试分开)； 另外，经过测试，如果在大型 zookeeper server 集群中，当单个节点的事务日志或者快照文件损坏、丢失，故障的节点可以很快通过其他健康节点来恢复自身服务。

## 3. 安装步骤

### 3.1 下载和解压

官方直接给出二进制安装包，无需编译，直接解压使用即可：

下载地址：http://mirror.symnds.com/software/Apache/zookeeper/stable/

本文档编写时，stable 版本号为 3.4.6，因此下载链接为：http://mirror.symnds.com/software/Apache/zookeeper/stable/zookeeper-3.4.6.tar.gz

```
cd $HOME/pkgs
wget http://mirror.symnds.com/software/Apache/zookeeper/stable/zookeeper-3.4.6.tar.gz

tar -zxvf zookeeper-3.4.6.tar.gz -C $HOME/app/ 
cd $HOME/app && ln -snf $HOME/app/zookeeper-3.4.6.tar.gz $HOME/app/zookeeper
```

### 3.2 环境变量

建议直接使用官方自带的管理工具对 zookeeper server 进行管理，官方虽然直接给出二进制安装包，但是此二进制包在编译时使用的环境变量均是默认值，因此启动之前，有以下的环境变量需要被修改，以便适应标准化部署，这些环境变量将会被 zkEnv.sh、zkServer.sh 使用：

| 环境变量         | 配置内容                                               | 重要性 | 说明                                                         |
| ---------------- | ------------------------------------------------------ | ------ | ------------------------------------------------------------ |
| $ZOO_LOG_DIR     | /home1/logs/zookeeper/                                 | 中     | zookeeper server 自身运行时产生的系统日志目录                |
| $ZOO_LOG4J_PROP  | "INFO, ROLLINGFILE"                                    | 高     | zookeeper server 系统日志的运行级别和使用的 log4j Appender，否则日志会输出到 zookeeper.out，难以进行日志管理 |
| $JMXDISABLE      | NULL                                                   | 中     | 默认不配置任何内容时，启用 JMX 服务                          |
| $JMXLOCALONLY    | false                                                  | 中     | 默认为 falsely，运行 JMX 远程访问                            |
| $SERVER_JVMFLAGS | -Xms2048m -Xmx2048m -XX:MaxMetaspaceSize=512m          | 高     | 设置JVM的内存选项，默认没有限制，容易导致服务器物理内存不足时，系统崩溃，因此这里设置为2G Java 8 取消 Perm 区域，使用 MetaSpace 来存储加载的类数据结构 |
| $JVMFLAGS        | -Djava.net.preferIPv4Stack=true -XX:CICompilerCount=10 | 中     | 设置 zookeeper server 只允许在 IPV4 的网络，增加启动时的编译线程为10个 这里可以设置JVM的其他参数，例如：使用CMS算法、设定FGC执行时O区上限值、打印GC日志、设定JMX远程访问端口等等 |

编译 $HOME/.bash_profile 【注意：必须把变量进行export处理，Linux Shell派生的子进程才能获取这些变量值】

```
export ZOO_LOG_DIR=/home1/logs/zookeeper/logs
export ZOO_LOG4J_PROP="INFO, ROLLINGFILE"
export SERVER_JVMFLAGS="-Xms2048m -Xmx2048m -XX:MaxMetaspaceSize=512m"
export JVMFLAGS="-Djava.net.preferIPv4Stack=true -XX:CICompilerCount=10"
```

这样，通过在 zkServer.sh 在启动时，使用 zkEnv.sh 获取到相关的环境变量，程序的日志就会被重定向到 $HOME/logs/zookeeper 中，并且以日志文件的形式输出，启动时的内存也得到控制。

### 3.3 日志格式

zookeeper 自身的日志配置文件为：

```
$HOME/app/zookeeper/conf/log4j.properties
```

根据 LOG4J 的官方文档，日志可以按照大小和时间进行轮替，zookeeper 默认按照日志文件的大小进行轮替，这里给出2种标准化设定：

| 对象                                                | 内容                                                    | 备注                                                         | 使用场合 |
| --------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ | -------- |
| log4j.rootLogger                                    | INFO, ROLLINGFILE                                       | 日志输出的默认级别、输出对象，这里设定输出级别为INFO，输出的Appender为”ROLLINGFILE"日志级别有TRACE、DEBUG、INFO、WARN等，Appender对象是自定义的 | 通用     |
| log4j.appender.ROLLINGFILE                          | org.apache.log4j.RollingFileAppender                    | 设定一个 RollingFIleAppender，名称为 “ROLLINGFILE”，其他类型的Appender，例如：输出到终端：org.apache.log4j.ConsoleAppender 等 | 通用     |
| log4j.appender.ROLLINGFILE.Threshold                | INFO                                                    | 设定 ROLLINGFILE 的日志级别                                  | 通用     |
| log4j.appender.ROLLINGFILE.File                     | /home1/logs/zookeeper/zookeeper.log                     | 设定 ROLLINGFILE 的日志文件名称                              | 通用     |
| log4j.appender.ROLLINGFILE.layout                   | org.apache.log4j.PatternLayout                          | 设定 ROLLINGFILE 的日志输出格式类型                          | 通用     |
| log4j.appender.ROLLINGFILE.layout.ConversionPattern | %d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n | 设定ROLLINGFILE 的格式内容                                   | 通用     |

log4j.appender.ROLLINGFILE.MaxFileSize 10MB 设定 ROLLINGFILE 的日志文件达到10MB时，执行轮替 按照日志大小轮替时使用 【默认使用】 log4j.appender.ROLLINGFILE.MaxBackupIndex 10 设定 ROLLINGFILE 的日志文件轮替文件保留数量为10个，多于10个，执行删除操作 e.g.: zookeeper.1 zookeeper.2 ... 按照日志大小轮替时使用 【默认使用】

log4j.appender.ROLLINGFILE.DatePattern = '.'yyyy-MM-dd-HH '.'yyyy-MM-dd-HH 设定 ROLLINGFILE 的日志轮替周期为小时，每一小时轮替一次，如果想按照天来轮替： '.'yyyy-MM-dd 即可 e.g.: zookeeper.2015-09-06-17 zookeeper.2015-09-06-18 ... 按照时间轮替时使用

详细请看官方文档：https://logging.apache.org/log4j/1.2/manual.html

这里，根据日志大小进行轮替设定的示例配置文件： 【示例中安装用户是storm，只输出日志文件ROLLINGFILE，并且级别是INFO，CONSOLE(终端)和TRACE均有定义，但是不输出】

```
############################################################
# Define some default values that can be overridden by system properties
# root 
zookeeper.root.logger=INFO, ROLLINGFILE


# console threshold
zookeeper.console.threshold=DEBUG


# zookeeper.log
zookeeper.log.dir=/home1/logs/zookeeper/
zookeeper.log.file=zookeeper.log
zookeeper.log.threshold=INFO


# zookeeper_trace.log
zookeeper.tracelog.dir=/home1/logs/zookeeper/
zookeeper.tracelog.file=zookeeper_trace.log
############################################################


# DEFAULT: console appender only
log4j.rootLogger=${zookeeper.root.logger}


# Example with rolling log file
#log4j.rootLogger=DEBUG, CONSOLE, ROLLINGFILE


# Example with rolling log file and tracing
#log4j.rootLogger=TRACE, CONSOLE, ROLLINGFILE, TRACEFILE


# Log INFO level and above messages to the console
log4j.appender.CONSOLE=org.apache.log4j.ConsoleAppender
log4j.appender.CONSOLE.Threshold=${zookeeper.console.threshold}
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
log4j.appender.CONSOLE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n


# Add ROLLINGFILE to rootLogger to get log file output
# Log DEBUG level and above messages to a log file
log4j.appender.ROLLINGFILE=org.apache.log4j.RollingFileAppender
log4j.appender.ROLLINGFILE.Threshold=${zookeeper.log.threshold}
log4j.appender.ROLLINGFILE.File=${zookeeper.log.dir}/${zookeeper.log.file}


# Max log file size of 10MB
log4j.appender.ROLLINGFILE.MaxFileSize=10MB
# uncomment the next line to limit number of backup files
log4j.appender.ROLLINGFILE.MaxBackupIndex=10


log4j.appender.ROLLINGFILE.layout=org.apache.log4j.PatternLayout
log4j.appender.ROLLINGFILE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L] - %m%n


# Add TRACEFILE to rootLogger to get log file output
# Log DEBUG level and above messages to a log file
log4j.appender.TRACEFILE=org.apache.log4j.FileAppender
log4j.appender.TRACEFILE.Threshold=TRACE
log4j.appender.TRACEFILE.File=${zookeeper.tracelog.dir}/${zookeeper.tracelog.file}


log4j.appender.TRACEFILE.layout=org.apache.log4j.PatternLayout
# Notice we are including log4j's NDC here (%x)
log4j.appender.TRACEFILE.layout.ConversionPattern=%d{ISO8601} [myid:%X{myid}] - %-5p [%t:%C{1}@%L][%x] - %m%n
```

### 3.4 配置文件

zookeeper 主配置文件为：

```
$HOME/app/zookeeper/conf/zoo.cfg【cd $HOME/app/zookeeper/conf && cp -a zoo_sample.cfg zoo.cfg】
```

这里针对比较重要的参数进行了描述，详细可以查看官方文档：

| 对象                      | 内容                                                         | 备注                                                         |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| tickTime                  | 3000                                                         | 设定心跳周期为 3000 毫秒；zookeeper 服务器之间或客户端与服务器之间维持心跳的时间间隔，也就是每个 tickTime 时间就会发送一个心跳 |
| initLimit                 | 10                                                           | 设定心跳失败的次数为 10 次；zookeeper 的 Leader接受客户端（Follower）初始化连接时最长能忍受多少个心跳时间间隔数；当已经超过 10 个心跳的时间（也就是tickTime）长度后 zookeeper 服务器还没有收到客户端的返回信息，那么表明这个客户端连接失败。总的时间长度就是 10 * 3000 = 30 秒 |
| syncLimit                 | 5                                                            | 设定消息发送和接收的时间为 5 * 3000 = 15 秒；表示 Leader 与 Follower 之间发送消息时请求和应答时间长度，最长不能超过多少个tickTime 的时间长度，总的时间长度就是 5 * 3000 = 15 秒 |
| maxClientCnxns            | 60                                                           | 设定服务端能够同时处理的客户端连接数量为 60；默认关闭，允许在系统支撑条件的情况下，不限制客户端连接数量 |
| dataDir                   | /home1/data/zookeeper/                                       | 设定快照文件目录                                             |
| dataLogDir                | /home1/data/zookeeper/datalog/                               | 设定事务日志目录                                             |
| clientPort                | 2181                                                         | 设定客户端连接时使用的端口                                   |
| minSessionTimeout         | 6000                                                         | 设定客户端超时的最小时间为 6000 毫秒，默认 2 * tickTime      |
| maxSessionTimeout         | 180000                                                       | 设定客户端超时的最大时间为 180000 毫秒，默认 20 * tickTime   |
| autopurge.snapRetainCount | 30                                                           | 当启用自动清理时，设定快照文件的保留个数为 30，默认 3        |
| autopurge.purgeInterval   | 1                                                            | 设定启用自动清理，值为 1，默认 0，关闭自动清理快照和事务日志 |
| server.A=B:C:D            | 伪集群模式： server.1=100.84.73.76:30000:30001 server.2=100.84.73.76:30010:30011 server.3=100.84.76.76:30020:30021 正常模式： server.1=100.84.73.76:30000:30001 server.2=100.84.73.77:30000:30001 server.3=100.84.76.78:30000:30001 | A 设定为1，就是 zookeeper 服务端的在集群里面的标识，内容和 myid保持一致【$HOME/app/zookeeper/data/myid】； B 设定为 100.84.73.76，zookeeper 集群中服务端的 IP 或者内网域名； C 设定为 30000，zookeeper 集群中服务端和 Leader 交换信息的端口； D 设定为 30001，表示的是万一集群中的 Leader 服务器挂了，需要一个端口来重新进行选举，选出一个新的Leader，而这个端口就是用来执行选举时服务器相互通信的端口。如果是伪集群的配置方式，由于 B 都是一样，所以不同的 zookeeper 实例通信端口号不能一样，所以要给它们分配不同的端口号。 |

配置示例：

```
# The number of milliseconds of each tick
tickTime=3000


# The number of ticks that the initial synchronization phase can take
initLimit=10


# The number of ticks that can pass between sending a request and getting an acknowledgement
syncLimit=5


# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just example sakes.
dataDir=/home1/data/zookeeper/
dataLogDir=/home1/data/zookeeper/datalog/


# the port at which the clients will connect
clientPort=2181


# the minimum session timeout in milliseconds that the server will allow the client to negotiate.
# Default Value: 2 * tickTime
#minSessionTimeout=6000


# the maximum session timeout in milliseconds that the server will allow the client to negotiate.
# Default Value: 20 * tickTime
#maxSessionTimeout=180000


# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60


# Be sure to read the maintenance section of the administrator guide before turning on autopurge.
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance


# The number of snapshots to retain in dataDir
autopurge.snapRetainCount=30
# Purge task interval in hours
# Set to "0" to disable auto purge feature
autopurge.purgeInterval=1


# server configuration
server.1=10.34.161.39:30000:30001
server.2=10.34.161.41:30000:30001
server.3=10.34.166.113:30000:30001
```

这里提一下关于伪集群配置的问题：

zkServer.sh 启动时，默认读取 $HOME/app/zookeeper/conf/zoo.cfg 的配置文件，如果想通过单机运行多个实例进行伪集群的调试，可以指定配置文件：

```
zkServer.sh start zoo_1.cfg
zkServer.sh start zoo_2.cfg
zkServer.sh start zoo_3.cfg
```

这样，客户端启动时，可以通过 --server 指令来连接到不同的zkServer，例如： zoo_1.cfg 中指定 zkServer 的端口是 30000，那么zkCli.sh的命令为：zkCli.sh --server 127.0.0.1:30000 如果不是伪集群模式，直接输入zkCli.sh即可。

### 3.5 部署Zookeeper Server服务标识

在 3.4 的主配置文件中描述过，server.A=B:C:D 中的 A 为此 zookeeper server 实例在 zookeeper 集群中的标识，比如设定有：

server.1=10.34.161.39:30000:30001

那么在 dataDir(dataDir=/home/storm/data/zookeeper/) 中执行命令，创建 maid 文件，内容为 1，集群中的其他 zookeeper server 实例也如此类推：

cd /home1/data/zookeeper/ && echo 1 > myid

## 4. 启动和关闭

启动和关闭非常简单，推荐使用官方脚本 zkServer.sh

Usage: /home/storm/app/zookeeper/bin/zkServer.sh {start|start-foreground|stop|restart|status|upgrade|print-cmd} |zoo.cf

格式：zkServer.sh [指令] [配置文件]，配置文件可以不填写，默认 zoo.cfg，如果是其他名称或者是伪集群模式，则需要指定配置，例如配置文件为 zoo_1.cfg 时：zkServer 指令 zoo_1.cfg；

指令有以下类型：

指令 说明 start 以后台 daemon 的形式，启动 zookeeper 服务端 start-foreground 在前台终端上，启动 zookeeper 服务端 stop 关闭 zookeeper 服务端 restart 重新启动 zookeeper 服务端 status 获取当前 zookeeper 服务端的运行状态 upgrade 更新 zookeeper 的版本，重新恢复数据和日志，慎用！！ print-cmd 打印出当前环境变量下，zookeeper 服务端的启动命令，建议在启动前打印命令，观察是否正常，然后再启动

关于 upgrade 指令，是用于升级 zookeeper 的版本，需要停服更新，版本升级危险性非常高，慎用，以下是使用建议：

1. 停止 zookeeper 集群；
2. 备份数据目录和日志目录 和 ；
3. 执行 upgrade 指令：bin/zkServer.sh upgrade ；
4. 启动 zookeeper 集群；

配置为 zoo.cfg 时，启动命令如下：

```
# 检测启动命令
zkServer.sh print-cmd

# 确认无误后，启动进程
zkServer.sh start

# 检测状态
zkServer.sh status
```

按照操作，启动 zookeeper server 实例，随着实例的依次启动，检测 zkServer status 时，状态会从 "Error contacting service. It is probably not running." 到选举成功为止，改变为 "Mode: follower" 或者 “Mode: leader”。

另外，只有 “Mode: leader” 的 zookeeper server 实例才会启动服务端口，所有的 zookeeper server 实例均会启动 选举端口。

## 5. 进程维护

zookeeper server 的服务进程一般比较稳定，不太容易出异常崩溃或者退出的情况，但是基于 zookeeper 本身的快速失败(Fast Fail)原则，同时为了方便维护和管理，这里可以使用 supervisor 进行进程监视。

### 5.1 安装 supervisor

supervisor 的安装非常简单：

```
# 安装 supervisor
pip install supervisor [或者: easy_install supervisor]
```

### 5.2 supervisor 的目录规划

对象 目录/文件 配置根目录 $HOME/app/supervisor 主配置文件 $HOME/app/supervisor/supervisord.conf zookeeper 服务配置文件 $HOME/app/supervisor/conf.d/zookeeper.conf 日志目录 /home1/logs/supervisor/

### 5.3 supervisor 的配置示例

1. 主配置文件：$HOME/app/supervisor/supervisord.conf

```
[unix_http_server]
file=/tmp/supervisor.sock   ; (the path to the socket file)
;chmod=0700                 ; socket file mode (default 0700)
;chown=nobody:nogroup       ; socket file uid:gid owner
;username=user              ; (default is no username (open server))
;password=123               ; (default is no password (open server))


;[inet_http_server]         ; inet (TCP) server disabled by default
;port=127.0.0.1:9001        ; (ip_address:port specifier, *:port for all iface)
;username=user              ; (default is no username (open server))
;password=123               ; (default is no password (open server))


[supervisord]
logfile=/home1/logs/supervisor/supervisord.log    ; (main log file;default $CWD/supervisord.log)
logfile_maxbytes=50MB                       ; (max main logfile bytes b4 rotation;default 50MB)
logfile_backups=10                          ; (num of main logfile rotation backups;default 10)
loglevel=info                               ; (log level;default info; others: debug,warn,trace)
pidfile=/tmp/supervisord.pid                ; (supervisord pidfile;default supervisord.pid)
nodaemon=false                              ; (start in foreground if true;default false)
minfds=1024                                 ; (min. avail startup file descriptors;default 1024)
minprocs=200                                ; (min. avail process descriptors;default 200)               
;umask=022                                  ; (process file creation umask;default 022)
;user=chrism                                ; (default is current user, required if root)
;identifier=supervisor                      ; (supervisord identifier, default is 'supervisor')
;directory=/tmp                             ; (default is not to cd during start)
;nocleanup=true                             ; (don't clean up tempfiles at start;default false)
;childlogdir=/tmp                           ; ('AUTO' child log dir, default $TEMP)
;environment=KEY="value"                    ; (key value pairs to add to environment)
;strip_ansi=false                           ; (strip ansi escape codes in logs; def. false)


; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface


[supervisorctl]
serverurl=unix:///tmp/supervisor.sock      ; use a unix:// URL  for a unix socket
;serverurl=http://127.0.0.1:9001           ; use an http:// url to specify an inet socket
;username=chris                            ; should be same as http_username if set
;password=123                              ; should be same as http_password if set
;prompt=mysupervisor                       ; cmd line prompt (default "supervisor")
;history_file=~/.sc_history                ; use readline history if available


; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.


[include]
files = /home/storm/local/supervisor/conf.d/*.conf 
```

1. zookeeper 配置文件：$HOME/app/supervisor/conf.d/zookeeper.conf

```
[program:zookeeper]
command=zkServer.sh start-foreground
process_name=%(program_name)s
numprocs=1
;directory=/tmp
;umask=022
;priority=999
autostart=true
autorestart=true
startsecs=10
startretries=3
exitcodes=1
stopsignal=TERM
stopwaitsecs=10
;user=chrism
redirect_stderr=false
stdout_logfile=/home1/logs/supervisor/zookeeper_stdout.log
stdout_logfile_maxbytes=100MB
stdout_logfile_backups=10
;stdout_capture_maxbytes=1MB
stderr_logfile=/home1/logs/supervisor/zookeeper_stderr.log
stderr_logfile_maxbytes=100MB
stderr_logfile_backups=10
;stderr_capture_maxbytes=1MB
;environment=A="1",B="2"
;serverurl=AUTO
```

### 5.3 supervisor 的启动

1. 增加环境变量：

# supervisor Environment

alias supervisord="supervisord -c $HOME/app/supervisor/supervisord.conf" alias supervisorctl="supervisorctl -c $HOME/app/supervisor/supervisord.conf"

1. 启动服务

# supervisor cmd

启动进程：supervisord # autostart=true 时，服务随着 supervisor 进程启动 启动服务：supervisorctl start zookeeper # autostart=true 时，服务随着 supervisor 进程启动

检测状态：supervisorctl status 停止服务：supervisorctl stop zookeeper

## 6. 服务监控

对 zookeeper 进行服务监控，监控主要涉及3个方面：

1. zookeeper server JVM内存监控；
2. zookeeper server 运行状态监控；

### 6.1 zookeeper server JVM 内存监控

通过JMX 进行远程监控，用于非侵入式的JVM状态监控，后续细说。

### 6.2 zookeeper server 运行状态监控

运行状态信息，使用四字监控即可，在建立监控数据展示页面时，建议每一个 zookeeper server 为一个监控主页，里面根据以下的四字命令返回的信息来进行分 tab：

1. 环境信息：envi

属性 说明 zookeeper.version zookeeper 版本号 host.name 当前进程运行主机名称 java.version Java 版本 java.vendor JVM 制造厂商 java.home JRE 运行目录 os.name 操作系统 os.version 内核版本 user.name 运行用户 user.dir zookeeper server 根目录

```
# envi
[storm@st-ucgc221 ~]$ echo "envi" | nc localhost 2181
Environment:
zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
host.name=st-ucgc221
java.version=1.8.0_60
java.vendor=Oracle Corporation
java.home=/home/storm/local/jdk1.8.0_60/jre
...
user.dir=/home/storm/local/supervisor-3.1.3
```

1. 固定设置：conf 属性 说明 clientPort 客户端端口 dataDir 内存数据库快照存储目录 dataLogDir 内存数据库事务日志目录 tickTime 心跳时间 maxClientCnxns 单台 zookeeper server 可以处理的客户端的连接数上限 minSessionTimeout 客户端 Session 超时的最短时间 maxSessionTimeout 客户端 Session 超时的最长时间 serverId zookeeper server 集群标识 initLimit Follower 启动时同步所有数据信息的超时时间 syncLimit 运行过程中 Leader 和 Follower 之间心跳的超时时间 electionAlg 选举算法 electionPort 服务选举端口 quorumPort 数据服务端口 peerType zookeeper server 运行类型

```
# conf
[storm@st-ucgc221 ~]$ echo "conf" | nc localhost 2181
clientPort=2181
dataDir=/home/storm/data/zookeeper/version-2
dataLogDir=/home/storm/logs/zookeeper/version-2
...
quorumPort=30000
peerType=0
```

1. 连接总览：cons 属性 说明 10.34.166.113:59542 连接IP、端口 queued=0 请求等待队列长度 recved=1027857 接收数据 sent=1027858 发送数据 sid=0x2506ac05e870004 此连接的 Session ID lop=PING 最后的操作命令/指令 est=1445243451807 to=6000 lcxid=0x11 最后的创建事务 ID lzxid=0x100000072 最后的更新事务 ID lresp=1447299191099 最后的响应时间戳 llat=0 最后时延 minlat=0 最小时延 avglat=0 平均时延 maxlat=8 最大时延

```
# cons
[storm@st-ucgc221 ~]$ echo "cons" | nc localhost 2181
 /10.34.166.113:59542[1](queued=0,recved=993634,sent=993635,sid=0x2506ac05e870004,lop=PING,est=1445243451807,to=6000,lcxid=0x11,lzxid=0x100000070,lresp=1447230742970,llat=0,minlat=0,avglat=0,maxlat=8)
 /127.0.0.1:46797[0](queued=0,recved=1,sent=0)
 /10.34.161.41:60376[1](queued=0,recved=344909,sent=344914,sid=0x1506ac05e7f0000,lop=PING,est=1446540994814,to=6000,lcxid=0x39,lzxid=0x100000070,lresp=1447230742548,llat=0,minlat=0,avglat=0,maxlat=7)
```

1. 状态概览：mntr 【监控首页】 属性 说明 zk_version 版本信息【 详细 -> envi 以及 conf 】 zk_avg_latency 平均时延 zk_max_latency 最小时延 zk_min_latency 最大时延 zk_packets_received 接收数据的统计 zk_packets_sent 发送数据的统计 zk_num_alive_connections 当前连接数【 详细 -> cons 】 zk_outstanding_requests zk_server_state zookeeper server 的运行角色 zk_znode_count 节点数统计 zk_watch_count 被监听的节点数统计 zk_ephemerals_count 临时 Session 统计 zk_approximate_data_size zk_open_file_descriptor_count zookeeper server 目前使用的文件描述符统计 zk_max_file_descriptor_count zookeeper server 可以使用的文件描述符 zk_followers zookeeper 集群中 Follower 数量 【 Leader 仅有】 zk_synced_followers zookeeper 集群中正常同步的 Follower 数量【 Leader 仅有】 zk_pending_syncs zookeeper 集群中正在同步的 Follower 数量【 Leader 仅有】

```
# mntr
[storm@st-ucgc223 ~]$ echo "mntr" | nc 127.0.0.1 2181
zk_version      3.4.6-1569965, built on 02/20/2014 09:09 GMT
zk_avg_latency  0
zk_max_latency  8
zk_min_latency  0
zk_packets_received     2189794
zk_packets_sent 2189814
zk_num_alive_connections        3
zk_outstanding_requests 0
zk_server_state leader
zk_znode_count  24
zk_watch_count  13
zk_ephemerals_count     4
zk_approximate_data_size        820
zk_open_file_descriptor_count   35
zk_max_file_descriptor_count    65535
zk_followers    2
zk_synced_followers     2
zk_pending_syncs        0
```

1. Session 的 watch 统计：wchs、wchc、wchp 【可以通过 Session ID 关联到 cons 查看细节】

```
# watch 概览：wchs
[storm@st-ucgc221 ~]$  echo "wchs" | nc 127.0.0.1 2181
1 connections watching 2 paths
Total watches:2

# sessions watch 的 zk_zonde 统计：wchc
[storm@st-ucgc221 ~]$ echo "wchc" | nc 127.0.0.1 2181
0x150dafae8640000
        /controller
        /config/changes

# zk_zonde 被 watch 的 sessions 统计：wchp
[storm@st-ucgc221 ~]$ echo "wchp" | nc 127.0.0.1 2181
/controller
        0x150dafae8640000
/config/changes
        0x150dafae8640000
```