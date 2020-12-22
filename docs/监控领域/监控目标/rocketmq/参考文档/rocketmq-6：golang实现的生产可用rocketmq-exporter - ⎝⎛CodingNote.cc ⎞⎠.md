### rocketmq-6：golang实现的生产可用rocketmq-exporter

-  2019 年 11 月 8 日
-  

-  [笔记](https://codingnote.cc/c/uncategorized/)

**目录**

**(1).概述与效果**

**(2).为何选择golang开发(附带不同语言开发的优劣对比)**

**1.开发语言选型**

**2.不同开发语言的资源占用对比**

**(3).代码组织结构与文件说明**

**1.包结构说明**

**2.不同开发语言的资源占用对比**

**(4).如何编译**

**1.安装go包依赖管理工具govendor**

**2.使用govendor下载包依赖**

**3.编译RocketmqExporter**

**(5).相关编译文件说明**

**(6).如何进行容器化部署**

**1.制作镜像**

**2.提供yaml范例**

**2.1.使用者需要注意&修改的label**

**2.2.使用者需要注意&修改的环境变量**

**3.容器化命令**

**(7).如何进行实体机部署**

**(8).如何结合prometheus与grafana**

**1.grafana/prometheus容器化**

**2.RocketmqExporter容器化**

**(9).其他相关文章**

**(1).概述与效果**

资源占用：K8S下，cpu占用0.01core, 内存占用10MB。

监控指标：消息堆积数，精确到进程粒度。

监控目的：实时掌控消息消费的健康程度。

数据来源：从rocketmq-console的http请求获取数据。也就是说RocketmqExporter必须依赖rocketmq-console。好吧，我承认我图省事儿了^_^。

为什么自己要重新实现： 官方exporter是java的，相对费资源；另外我们要求对消息堆积数有完备监控，且精确到进程级别。从topic, consumerGroup, broker,queueId, consumerClientIP, consumerClientPID等维度对消息堆积数进行聚合，如下图：

![img](https://ask.qcloudimg.com/http-save/6430377/ei3uvug3la.png)

效果图下载地址：

https://github.com/hepyu/k8s-app-config/blob/master/product/standard/grafana-prometheus-pro/exporter-mq-rocketmq/images/mesage-unconsumed-count.jpg

**(2).为何选择golang开发(附带不同语言开发的优劣对比)**

**1.开发语言选型**

golang是最适合的选择。常用选型不外乎java, python, golang。

| 语言   | 优势                                   | 劣势                                                         |
| :----- | :------------------------------------- | :----------------------------------------------------------- |
| java   | 写exporter真没啥优势。                 | 远比golang和python费资源，容器化下不可接受；相比golang费10倍。 |
| python | 比java省资源，但不如golang；开发简单。 | 镜像准备太麻烦；python版本差异太大(我受够了)，不是简单升级个版本就OK的，容器化下python栈可能要维护多批镜像。 |
| golang | 开发简单；占用资源很少；性能高。       | 写exporter真没啥劣势。                                       |

**2.不同开发语言的资源占用对比**

关于镜像大小与实际资源占用的生产对比。

| 语言   | K8S生产资源分配         | image大小 | 备注                                                         |
| :----- | :---------------------- | :-------- | :----------------------------------------------------------- |
| java   | cpu:100m, memory:1G。   | 过百兆    | 使用官方的rocketmq-exporter，java开发。                      |
| python | cpu:100m, memory:100m。 | 过百兆    | 笔者开发，依赖于rocketmq-console，位于：https://github.com/hepyu/hpy-rocketmq-exporter |
| golang | cpu:10m, memory:10m。   | 16MB      | 笔者开发，依赖于rocketmq-console，位于：https://github.com/hepyu/RocketmqExporter |

特别说明：

java很不适合开发exporter的重要原因有一点就是，“启动时内存和CPU耗费”与“运行时内存和CPU耗费差异太大”，这就导致容器资源分配时request和max有不小差值， 这个是很不好的，会留下隐患。

rocketmq实例不多还好，但是想象一下如果redis,mysql的exporter也是用java写，那这个差值就大了，放大到整个集群将成为潜在风险，我想这也是mysql-exporter, redis-exporter官方为什么用golang写的原因之一。

但是如果把request和max设置成一样，又很浪费。

综上所述，golang是最好的选择。

**(3).代码组织结构与文件说明**

**1.包结构说明**

| 包名     | 作用                                                         | 备注                                                         |
| :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| constant | 所有的常亮都定义在环境变量中，constant中定义方法取常量       | 由于要容器化，舍弃配置文件。                                 |
| model    | 存放所有struct结构体，定义要收集的metrics指标。              |                                                              |
| utils    | 封装工具类，主要是stringarray操作和http访问操作。            |                                                              |
| wrapper  | 封账从rocketmq-console或取的数据，并计算汇总成我们要的指标格式。 |                                                              |
| service  | 调用wrapper获取数据，计算汇总出消息堆积数的分类统计数据。    | 根据topic, consumerGroup, broker, clientIP, clientPID等进行分类汇总。 |

**2.重点文件说明**

| 主要代码                          | 作用                                                         | 备注 |
| :-------------------------------- | :----------------------------------------------------------- | :--- |
| Collector.go                      | prometheus的相关代码都在这里，使用prometheus-client将调用service返回的数据写入channel。 |      |
| RocketmqExporter.go               | 启动http-server，暴露metircs端口。                           |      |
| rocketmq_exporter.docker-build.sh | docker镜像制作脚本。                                         |      |
| env.default.config.backup         | 环境变量配置范例。                                           |      |

**(4).如何编译**

有点麻烦，我从开发(IDE用vim)到编译到image制作都是在linux服务器上，所以都是用的golang体系下原生命令进行操作的。

本工程目录下提供一个已经编译好的二进制文件：RocketmqExporter，可以直接使用。

**1.安装go包依赖管理工具govendor**

go get -u -v github.com/kardianos/govendor

**2.使用govendor下载包依赖**

配置环境变量(注意source生效)：export GOPATH=$HOME/go:$HOME/go-workspace

mkdir $HOME/go-workspace/src

然后将本工程clone到目录$HOME/go-workspace/src。

进入$HOME/go-workspace/src执行govendor命令列出工程依赖：govendor list

```javascript
m RocketmqExporter/constant    m RocketmqExporter/model    m RocketmqExporter/service    m RocketmqExporter/utils    m RocketmqExporter/wrapper    m github.com/go-kit/kit/log/level    m github.com/prometheus/client_golang/prometheus    m github.com/prometheus/client_golang/prometheus/promhttp    m github.com/prometheus/common/promlog    m github.com/prometheus/common/promlog/flag    m github.com/prometheus/common/version    m gopkg.in/alecthomas/kingpin.v2
```

然后执行govendor init,会生成一个vdendor目录和vendor.json，后边下载的包依赖都会放到这个目录下。

```javascript
vendor.json  {  "comment": "",  "ignore": "test",  "package": [],  "rootPath": "hpy-go-rocketmq-exporter"  }
```

下载包依赖到vendor目录，执行命令：govendor fetch +out，时间比较长(本工程下提供一个已经编译好的二进制文件：hpy-go-rocketmq-exporter，这个可以直接用于镜像制作)。

执行完成后，vendor目录下：

```javascript
github.com  golang.org  gopkg.in  RocketmqExporter  vendor.json  vendor.json内容：  {  "comment": "",  "ignore": "test",  "package": [  {  "path": "RocketmqExporter/constant",  "revision": ""  },  {  "path": "RocketmqExporter/model",  "revision": ""  },  {  "path": "RocketmqExporter/service",  "revision": ""  },  {  "path": "RocketmqExporter/utils",  "revision": ""  },  {  "path": "RocketmqExporter/wrapper",  "revision": ""  },  {  "checksumSHA1": "MXqUZAuWyiMWV7HC0X2krRinZoI=",  "path": "github.com/alecthomas/template",  "revision": "fb15b899a75114aa79cc930e33c46b577cc664b1",  "revisionTime": "2019-07-18T01:26:54Z"  },  {  "checksumSHA1": "3wt0pTXXeS+S93unwhGoLIyGX/Q=",  "path": "github.com/alecthomas/template/parse",  "revision": "fb15b899a75114aa79cc930e33c46b577cc664b1",  "revisionTime": "2019-07-18T01:26:54Z"  },  {  "checksumSHA1": "VT42paM42J+M52CXStvRwsc1v6g=",  "path": "github.com/alecthomas/units",  "revision": "f65c72e2690dc4b403c8bd637baf4611cd4c069b",  "revisionTime": "2019-09-24T02:57:48Z"  },  {  "checksumSHA1": "0rido7hYHQtfq3UJzVT5LClLAWc=",  "path": "github.com/beorn7/perks/quantile",  "revision": "37c8de3658fcb183f997c4e13e8337516ab753e6",  "revisionTime": "2019-07-31T12:00:54Z"  },  {  "path": "github.com/cespare/xxhash/v2",  "revision": ""  },  {  "checksumSHA1": "eVc+4p1fDrG3e49wZuztY6D2txA=",  "path": "github.com/go-kit/kit/log",  "revision": "9f5354e50d79d79d865f684fe139811cf309870f",  "revisionTime": "2019-10-18T12:22:45Z"  },  {  "checksumSHA1": "dyVQWAYHLspsCzhDwwfQjvkOtMk=",  "path": "github.com/go-kit/kit/log/level",  "revision": "9f5354e50d79d79d865f684fe139811cf309870f",  "revisionTime": "2019-10-18T12:22:45Z"  },  {  "checksumSHA1": "g8yM1TRZyIjXtopiqbslzgLqtM0=",  "path": "github.com/go-logfmt/logfmt",  "revision": "07c9b44f60d7ffdfb7d8efe1ad539965737836dc",  "revisionTime": "2018-11-22T01:56:15Z"  },  {  "checksumSHA1": "Q3FteGbNvRRUMJqbYbmrcBd2DMo=",  "path": "github.com/golang/protobuf/proto",  "revision": "ed6926b37a637426117ccab59282c3839528a700",  "revisionTime": "2019-10-22T19:55:53Z"  },  {  "checksumSHA1": "abKzFXAn0KDr5U+JON1ZgJ2lUtU=",  "path": "github.com/kr/logfmt",  "revision": "b84e30acd515aadc4b783ad4ff83aff3299bdfe0",  "revisionTime": "2014-02-26T03:06:59Z"  },  {  "checksumSHA1": "bKMZjd2wPw13VwoE7mBeSv5djFA=",  "path": "github.com/matttproud/golang_protobuf_extensions/pbutil",  "revision": "c182affec369e30f25d3eb8cd8a478dee585ae7d",  "revisionTime": "2018-12-31T17:19:20Z"  },  {  "checksumSHA1": "I7hloldMJZTqUx6hbVDp5nk9fZQ=",  "path": "github.com/pkg/errors",  "revision": "27936f6d90f9c8e1145f11ed52ffffbfdb9e0af7",  "revisionTime": "2019-02-27T00:00:51Z"  },  {  "checksumSHA1": "HquvlxEmpILGOdePiJzqL/zMvUY=",  "path": "github.com/prometheus/client_golang/prometheus",  "revision": "333f01cef0d61f9ef05ada3d94e00e69c8d5cdda",  "revisionTime": "2019-10-24T23:19:15Z"  },  {  "checksumSHA1": "UBqhkyjCz47+S19MVTigxJ2VjVQ=",  "path": "github.com/prometheus/client_golang/prometheus/internal",  "revision": "333f01cef0d61f9ef05ada3d94e00e69c8d5cdda",  "revisionTime": "2019-10-24T23:19:15Z"  },  {  "checksumSHA1": "UcahVbxaRZ35Wh58lM9AWEbUEts=",  "path": "github.com/prometheus/client_golang/prometheus/promhttp",  "revision": "333f01cef0d61f9ef05ada3d94e00e69c8d5cdda",  "revisionTime": "2019-10-24T23:19:15Z"  },  {  "checksumSHA1": "V8xkqgmP66sq2ZW4QO5wi9a4oZE=",  "path": "github.com/prometheus/client_model/go",  "revision": "14fe0d1b01d4d5fc031dd4bec1823bd3ebbe8016",  "revisionTime": "2019-08-12T15:41:04Z"  },  {  "checksumSHA1": "vA545Z9FkjGvIHBTAKQOE0nap/k=",  "path": "github.com/prometheus/common/expfmt",  "revision": "b5fe7d854c42dc7842e48d1ca58f60feae09d77b",  "revisionTime": "2019-10-17T12:25:55Z"  },  {  "checksumSHA1": "1Mhfofk+wGZ94M0+Bd98K8imPD4=",  "path": "github.com/prometheus/common/internal/bitbucket.org/ww/goautoneg",  "revision": "b5fe7d854c42dc7842e48d1ca58f60feae09d77b",  "revisionTime": "2019-10-17T12:25:55Z"  },  {  "checksumSHA1": "ccmMs+h9Jo8kE7izqsUkWShD4d0=",  "path": "github.com/prometheus/common/model",  "revision": "b5fe7d854c42dc7842e48d1ca58f60feae09d77b",  "revisionTime": "2019-10-17T12:25:55Z"  },  {  "checksumSHA1": "Pj64Wsr2ji1uTv5l49J89Rff0hY=",  "path": "github.com/prometheus/common/promlog",  "revision": "b5fe7d854c42dc7842e48d1ca58f60feae09d77b",  "revisionTime": "2019-10-17T12:25:55Z"  },  {  "checksumSHA1": "3tSd7cWrq75N2PaoaqAe79Wa+Fw=",  "path": "github.com/prometheus/common/promlog/flag",  "revision": "b5fe7d854c42dc7842e48d1ca58f60feae09d77b",  "revisionTime": "2019-10-17T12:25:55Z"  },  {  "checksumSHA1": "91KYK0SpvkaMJJA2+BcxbVnyRO0=",  "path": "github.com/prometheus/common/version",  "revision": "b5fe7d854c42dc7842e48d1ca58f60feae09d77b",  "revisionTime": "2019-10-17T12:25:55Z"  },  {  "checksumSHA1": "/otbR/D9hWawJC2jDEqxLdYkryk=",  "path": "github.com/prometheus/procfs",  "revision": "34c83637414974b5e7d4bd700b49de3c66631989",  "revisionTime": "2019-10-22T16:02:49Z"  },  {  "checksumSHA1": "ax1TLBC8m/zLs8u//UHHdFf80q4=",  "path": "github.com/prometheus/procfs/internal/fs",  "revision": "34c83637414974b5e7d4bd700b49de3c66631989",  "revisionTime": "2019-10-22T16:02:49Z"  },  {  "checksumSHA1": "sxRjp2SwHqonjR+sHIEXCkfBglI=",  "path": "github.com/prometheus/procfs/internal/util",  "revision": "34c83637414974b5e7d4bd700b49de3c66631989",  "revisionTime": "2019-10-22T16:02:49Z"  },  {  "path": "golang.org/x/sys/windows",  "revision": ""  },  {  "checksumSHA1": "sToCp8GThnMnsBzsHv+L/tBYQrQ=",  "path": "gopkg.in/alecthomas/kingpin.v2",  "revision": "947dcec5ba9c011838740e680966fd7087a71d0d",  "revisionTime": "2017-12-17T18:08:21Z"  }  ],  "rootPath": "hpy-go-rocketmq-exporter"  }
```

此时make会报错，找不到包github.com/cespare/xxhash/v2，这个是因为prometheus基于依赖于该包，而prometheus是基于gomod构建的，gomod支持能够识别xxhash后面的v2是指定的版本，常规方法无法下载，可以下载github.com/cespare/xxhash/，然后把该文件夹中的内容都copy到github.com/cespare/xxhash/v2目录下即可。

在vendor目录下执行：

git clone https://github.com/cespare/xxhash.git github.com/cespare/xxhash/v2

**3.编译RocketmqExporter**

执行 make 进行编译，打印信息如下：

```javascript
>> building binaries  GO111MODULE=on /root/go/bin/promu build --prefix /root/go-workspace/src/RocketmqExporter   >   RocketmqExporter  >> running all tests  GO111MODULE=on go test -race  -mod=vendor ./...  ?   RocketmqExporter[no test files]  ?   RocketmqExporter/constant[no test files]  ?   RocketmqExporter/model[no test files]  ?   RocketmqExporter/service[no test files]  ?   RocketmqExporter/utils[no test files]  ?   RocketmqExporter/wrapper[no test files]  >> vetting code  GO111MODULE=on go vet  -mod=vendor ./...
```

编译成功后，在目录下会生成一个二进制文件RocketmqExporter，可以直接执行：./RocketmqExporter，打印如下信息说明成功(不用关心报错，因为没有配置参数到环境变量，找不到rocketmq-console)：

```javascript
level=info ts=2019-11-01T09:19:57.879Z caller=RocketmqExporter.go:27 msg="Starting rocketmq_exporter" version="unsupported value type"  level=info ts=2019-11-01T09:19:57.879Z caller=RocketmqExporter.go:28 msg="Build contenxt" (gogo1.13.3,userroot@future,date111911090-09:17:41)=(MISSING)  level=info ts=2019-11-01T09:19:57.879Z caller=RocketmqExporter.go:34 msg=fmt.metricsPath:  panic: http: invalid pattern    goroutine 1 [running]:  net/http.(*ServeMux).Handle(0xd47080, 0x0, 0x0, 0x9f72c0, 0xc000091ec0)  /usr/local/go/src/net/http/server.go:2397 +0x33a  net/http.Handle(...)  /usr/local/go/src/net/http/server.go:2446  main.main()  /root/go-workspace/src/RocketmqExporter/RocketmqExporter.go:39 +0x720
```

**(5).相关编译文件说明**

| 文件名                          | 用途                                       | 备注                                                         |
| :------------------------------ | :----------------------------------------- | :----------------------------------------------------------- |
| Makefile                        | 定义构建规则的主文件。                     | copy from mysqld-exporter官方文件                            |
| Makefile.common                 | 详细定义构建规则的文件。                   | copy from mysqld-exporter官方文件                            |
| .golangci.yml                   | 代码静态检查。                             | 实际上我没有用他，在Makefile.common中注释掉了。              |
| .promu.yml                      | 定义RocketmqExporter的版本相关信息。       |                                                              |
| .travis.yml                     | 构建和测试的自动化工具。                   |                                                              |
| go.mod                          | 构建后文件，存放RocketmqExporter的依赖包。 | 执行go mod init RocketmqExporter后生成。包含go.mod文件的目录也被称为模块根，也就是说，go.mod 文件的出现定义了它所在的目录为一个模块。 |
| go.sum                          | go.sum 是记录所依赖的项目的版本的锁定。    | 执行go mod init RocketmqExporter后生成。                     |
| rocketmq_exporter.code-build.sh | go build .编译方式的执行脚本。             | 我实际上也不使用他，用的make编译方式。                       |

Makefile.common中的关键代码：

.PHONY: common-all

\#common-all: precheck style check_license lint unused build test

common-all: build test

上述代码指明了构建过程，可以看到我只开启了build和test两个构建命令，其余关闭。

| 文件名        | 用途                                                   | 备注 |
| :------------ | :----------------------------------------------------- | :--- |
| precheck      | 代码检查                                               |      |
| style         | 格式验证                                               |      |
| check_license | license验证                                            |      |
| lint          | Golint用于检查go代码中不够规范的地方                   |      |
| unused        | unused是用来检查Go代码未使用的常量，变量，函数和类型的 |      |
| build         | 编译                                                   |      |
| test          | 测试                                                   |      |

**(6).如何进行容器化部署**

**1.制作镜像**

直接在目录下执行：rocketmq_exporter.docker-build.sh

镜像名称为：hpy253215039/go-rocketmq-exporter，版本为：1.0.0。

镜像名称可以自己修改。

**2.提供yaml范例**

目录下的范例文件是：go-exporter-deployment-mq-rocketmq-c0.yaml

**2.1.使用者需要注意&修改的label**

| label                                        | 用途                                                         | 备注                        |
| :------------------------------------------- | :----------------------------------------------------------- | :-------------------------- |
| rocketClusterName: rocketmq-c0               | grafana中的一个下拉选择，标识监控的rocketmq集群的名称，必须配置。 |                             |
| namesrvAddr: rocketmq-c0-console-prod-server | grafana中的一个下拉选择，标识原始数据来自哪个rocketmq集群，必须配置。 | rocketmq-console的地址URL。 |

**2.2.使用者需要注意&修改的环境变量**

| 环境变量                 | 用途                                                         | 备注                                                         |
| :----------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| rocketmqConsoleIPAndPort | rocketmq-console的地址。                                     | 范例：rocketmq-c0-console-prod-server.coohua:8080            |
| ignoredTopics            | 配置不纳入监控的topic列表。rocketmq有一些默认topic，不需要监控；自己也可以额外加入别的topic。 | 建议值："RMQ_SYS_TRANS_HALF_TOPIC,BenchmarkTest,OFFSET_MOVED_EVENT,TBW102,SELF_TEST_TOPIC,DefaultCluster,broker-b,broker-a" |
| metricsPath              | 自定义uri名称。                                              | 建议值："/metrics"                                           |
| listenAddress            | 定义暴露的端口。                                             | 建议值：":9104"                                              |
| metricsPrefix            | metrics的名称前缀。                                          | 建议值："rocketmq"                                           |

**3.容器化命令**

直接执行: kubectl apply -f go-exporter-deployment-mq-rocketmq-c0.yaml

**(7).如何进行实体机部署**

将目录下env.default.config.backup中的内容拷贝到文件~/.bashrc中，然后执行 "source ~/.bashrc"使其生效。

然后运行目录下的RocketmqExporter二进制文件即可，注意最好使用supervisor进行守护。

golang如果想要获取自定义变量，必须把自定义变量放到这里定义：~/.bashrc ，放到/etc/profile中通过os.GetEnv是获取不到的。

注意环境变量含义，要根据自己的实例情况进行修改：

| 环境变量                 | 用途                                                         | 备注                                                         |
| :----------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| rocketmqConsoleIPAndPort | rocketmq-console的地址。                                     | 范例：rocketmq-c0-console-prod-server.coohua:8080            |
| ignoredTopics            | 配置不纳入监控的topic列表。rocketmq有一些默认topic，不需要监控；自己也可以额外加入别的topic。 | 建议值："RMQ_SYS_TRANS_HALF_TOPIC,BenchmarkTest,OFFSET_MOVED_EVENT,TBW102,SELF_TEST_TOPIC,DefaultCluster,broker-b,broker-a" |
| metricsPath              | 自定义uri名称。                                              | 建议值："/metrics"                                           |
| listenAddress            | 定义暴露的端口。                                             | 建议值：":9104"                                              |
| metricsPrefix            | metrics的名称前缀。                                          | 建议值："rocketmq"                                           |

**(8).如何结合prometheus与grafana**

笔者提供生产级容器化结合方式。

**1.grafana/prometheus容器化**

参照工程完成grafana/prometheus的容器化：

https://github.com/hepyu/k8s-app-config/tree/master/product/standard/grafana-prometheus-pro

上述工程包含消息堆积数的grafana的dashboard。

具体实施步骤和相关生产拓扑描述参见文章：

[grafana&prometheus生产级容器化监控-1：生产级容器化](https://mp.weixin.qq.com/s?__biz=Mzg4MDEzMDM4MA==&mid=2247484212&idx=1&sn=a544362016d88465b14897cd5ee5c2c5&chksm=cf78a317f80f2a01cf7636e223dd23cb04c15c3620ccab61972c4c8169d63994e16c3444daa8&scene=21#wechat_redirect)

主要资源位置：

grafana消息堆积数dashboard位于：

https://github.com/hepyu/k8s-app-config/tree/master/product/standard/grafana-prometheus-pro/grafana/provisioning/dashboards/mq-rocketmq

prometheus.yml配置的抓取规则位于：

https://github.com/hepyu/k8s-app-config/blob/master/product/standard/grafana-prometheus-pro/prometheus-mq-rocketmq/prometheus-mq-rocketmq-configmap.yaml

**2.RocketmqExporter容器化**

具体参见文章：

[grafana&prometheus生产级容器化监控-2：监控rocketmq](https://cloud.tencent.com/developer/article/1522408?from=10680)

**3.使用注意事项**

1.rocketmq-dashboard默认只显示堆积数大于1000的metric项，主要是为了避免显示太多而凌乱，可以自行修改。

2.当你使用broadcast模式发送消息时，消息堆积数是只增不减，因为consumer不会提交offset，所以你会看到这些topic的堆积数会很高，在做报警的时候要考虑过滤这类topic。

**(9).其他相关文章**

[rocketmq1:集群主要结构和监控，以及性能测试与成本控制](https://cloud.tencent.com/developer/article/1456379?from=10680)

[rocketmq-2：性能测试方案&压测&选型&结论](https://cloud.tencent.com/developer/article/1456397?from=10680)

[rocketmq-3：rocketmq流控/重试机制与应对](https://cloud.tencent.com/developer/article/1456404?from=10680)

[rocketmq-4：线上rocketmq slave节点的ECS宕机恢复实记](https://cloud.tencent.com/developer/article/1462205?from=10680)

[rocketmq-5：生产级rocketmq集群部署](https://cloud.tencent.com/developer/article/1509539?from=10680)

[golang实战-1：搭建vim-go开发环境](https://cloud.tencent.com/developer/article/1533830?from=10680)