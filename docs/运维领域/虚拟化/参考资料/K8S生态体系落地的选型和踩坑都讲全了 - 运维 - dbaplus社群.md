## K8S生态体系落地的选型和踩坑都讲全了

刘俊杰 2020-03-27 11:59:12

**作者介绍**

**刘俊杰，**某上市互联网公司容器化落地项目开发工程师。

 

开源节流，是企业提升利润的两大方向；中台战略或基础结构体系常常肩负了节流的重任。无论大小企业，容器化都被认为可以大幅度地提升效率，增加运维标准化和资源利用率。但是此类事情一旦做不好很容易造成花了大量成本而效果得不到认可的尴尬结果。本次分享从团队的实际经验出发，聊一下容器化生态体系落地中的一些事情。

 

**监控**

 

容器环境一般是提供一整套解决方案的，监控可以分为三种：指标监控、业务监控、调用链监控。

 

业务监控和调用链监控更多的取决于业务开发部门的选型，如skywalking等。

 

容器环境下，指标监控非Prometheus莫属，通过Service Discovery机制中的Kubernetes plugin获得scrape路径，之后的链路就比较通畅了。

 

使用Prometheus过程中一个绕不开的问题是持久化存储，WAL中保存的数据不宜过多，否则内存和加载速度都会产生很大问题，官方支持的remote read/write列表中，我们考查了InfluxDB和TiDB这两个，实践中两者占用的内存都非常大，建议在集群外的物理机中进行部署，如果使用InfluxDB，如果集群中Pod创建频繁（例如使用了cronjob）可能会触发key数量限制。

 

**日志**

 

日志分为两种：std系列日志和文件日志，它们的区别主要在于收集方式不同，一般来说，收集上来的日志都会并进入ELK体系，后面的处理就都差不多了。

 

std系列日志因其属于Linux模型，可以统一从Docker数据目录中予以收集，一种部署方式是使用DaemonSet部署Fluentd并挂载hostPath。

 

文件形态的日志略显复杂，NFS/CephFS等分布式存储肯定不适合存放日志，我们通过emptyDir形式实现目录共享，然后新增filebeat sidecar对共享目录中的日志文件进行收集，入ELK体系。

 

**如何与持续交付对接**

 

这里我们关注持续交付部署部分的方案，Kubernetes的部署本质上就是不同类型的资源对象以yaml格式应用，在自研与使用开源方案之间，我们选用了Helm作为部署阶段中，持续交付与Kubernetes的沟通桥梁。通过Helm我们可以把部署配置变成一个JSON对象，辅以标准化的部署模版，实现部署的标准化，同时自带了资源状态监测，应用管理等功能。

 

作为一个toB性质的服务，我们不应该只关注服务本身的可用性和性能，更应该从最终用户体验维度进行自查改进。例如Kubernetes官方的Benchmark工具中提到Pod平均启动时间，但是对项目来说更加关注的是Pod平均ready时间，而探针的结果是受到项目依赖，数据库等因素的影响的。对于特定项目，很多数值是稳定的，我们可以在报警系统中进行一些统计学方面的处理。

 

**如何正确地添加Sidecar**

 

刚刚的日志章节，提到了使用Filebeat Sidecar来收集日志，持续交付对接过程中提到了使用模版来生成项目的yaml文件。这就意味着，日志Sidecar容器必须在项目部署配置中予以体现，与项目进行耦合。这带来了很大的复杂度，也令日志系统的配置变更流程非常复杂。毕竟稳定的项目一般不会去更新部署配置，日志系统要一直兼容老版本的规则文件。因而需要一种手段，把日志配置和项目配置进行隔离。

 

我们找到的办法是Kubernetes的动态准入控制（Mutating Admission Webhook）来实现sidecar injection。通过这一机制，所有的资源在操作（增删改）同步到etcd前，都会请求Webhook，Webhook可以通过或否决（allow/reject），也可以响应一个JSON Patch，修改对象的部分资源。

 

事实上，常常会发现我们定义的Pod中会被默认注入default service account，就是Kubernetes中内置Admission的作用产物，现在非常火的Istio，其劫持流量的原理为修改每个Pod的网络规则，也是通过这种机制注入init-container，从而在Pod中修改iptables来实现。

 

通过这一机制，还可以针对诸如hostPort，hostPath，探针规范作出安全审计，可以说提供了相当丰富的想象空间。风险点是Webhook必须稳定可靠，延时较长不是问题，1.14+提供了timeoutSeconds，但如果返回一个不能被apply的patch，会导致资源创建失败。

 

在日志应用场合，我们注册了Pod对象的Create动作，项目只需要通过annotation传入几个简单配置，就可以自动生成一个自定义的Filebeat Sidecar，非常干净和方便。

 

**如何实现自定义PodIP**

 

Kubernetes中每次Pod的创建都会分配一个新的IP，社区的目的是希望用户使用Service+DNS的机制实现通信，但实际上，在一些基础组件的容器化过程中，由于软件兼容性，我们会希望某些业务容器的IP固化，不因重启而变更。

 

这里以Redis举例要用到稳定的IP的场景：

 

在Redis集群模式中，“cluster meet”命令只支持IP格式，不支持域名解析配置，社区中有人提出过这个issue结果被拒了。虽说Redis集群中任意一个节点的IP变更都可以在Redis集群内自动识别（因为Instance ID不变），但是如果因为意外情况导致所有Redis集群节点同时发生重启，集群内节点两两无法发现彼此，那就只能由运维人工介入，重新让节点发现彼此，此外IP的变更也会导致有缓存的Redis客户端产生错误。

 

在Kubernetes中，Service相关资源由kube-proxy负责，主要体现在iptables或IPVS规则中，而PodIP是由CNI负责分配，具体体现在eth-pair和路由表中。我们选用了Calico作为CNI插件，通过cni.projectcalico.org/ipAddrs这个annotation将预期的IP传递给Calico。

 

相对于对CNI进行二次开发自行实现IPAM来说，这种方法的开发成本较小。

 

在具体实现上：由于Pod是通过上级对象资源的模版创建，无法在模版中为每个Pod自定义annotation，所以我们同样通过动态准入机制实现，例如在sts资源中自定义一个annotation并传递一组IP，随后劫持Pod的创建，根据序号依次为Pod新增annotation，以激活Calico的指定PodIP功能。

 

这里注意的一点是，我们在实现IP固化功能后，一些微服务团队也希望使用这个功能。他们想要解决的痛点是容器发版之后，注册中心仍然保有旧的PodIP的问题。这里不适合去做IP固化：

 

- 原因一：Web项目大都使用deployment发布，在rs和Pod阶段，podName会添加随机字符串，无法甄别排序；事实上，我们只对sts资源开放了固化IP的方案；
- 原因二：微服务应用应当实现对SIGINT，SIGTERM等信号的监听，在pod terminationGracePeriodSeconds中自行实现注册中心的反注册。

 

**任务调度**

 

我们有一些祖传的业务员仍然使用PHP，PHP在进程管理上比较欠缺，物理机环境下很多调度工作要借助于cronjob来完成。我们一些PHP项目一开始上容器的时候，采用的就是Kubernetes提供的cronjob机制，使用下来有这么几个问题：

 

- Pod执行日志通过ELK体系收集后展示不直观；
- 更新代码后Pod在节点的首次启动会因为pull代码而不准时；
- 无法手动执行启动；
- 间隔时间较短的cron大幅度提高了集群Pod总数，增加管理节点的压力。

 

最后我们选择使用开源的goCron方案，为项目单独部署任务专用deployment，通过gRPC的方式进行任务的启停和日志传输。

 

值得注意的是，在开源goCron方案中，由Server角色向Node角色发起请求，但是我们不可能为每一个Node容器都配备Ingress或者NodePort暴露。

 

在有关二次开发中，我们为gRPC proto参数中新增了target字段。即Server角色中心化部署，每个容器编排集群部署一个Agent角色作为中转，最终通过SVC达到Node角色。

 

**集群事件监控**

 

我们排查问题的时候第一件事一般都是describe一下相关资源，然后查看event，但是事实上，event默认只能存在1小时；kube-apiserver中有一个参数定义了事件在etcd中的保留时间：event-ttl Amount of time to retain events. (default 1h0m0s)。

 

这个1h主要是考虑到大规模集群中etcd的性能瓶颈；但即使是小集群，这个值也不建议调整到24h以上。这意味着，如果半夜中集群中发生事件，到了白天上班只能看到restart计数器+1或者对象存活时间清零，而找不到任何相关信息。

 

所以我们经过二次开发，在所有集群内部署了一个事件收集中间件，监听所有ns中的ev，发送至ES，并进行一些简单的聚合，以metrics的形式暴露给prom。这一工具深受运维团队好评，并且逐渐成为了集群健康的重要晴雨表。

 

**容器内时间模拟及系统参数模拟**

 

容器化和虚拟化相比，最大的区别在于容器和物理机共享了内核，内核实现了进程调度、网络、io，等等功能，并通过Namespace和CGroup实现隔离。但是在这些隔离中，时间、CPU、内存等信息不在隔离范围内，从而带来了问题。

 

首先我们看一下CPU和内存，在容器中，如果我们打印/proc/cpuinfo或是/proc/meminfo，取到的是物理机的核数和内存大小，但实际上容器必然是会有资源限制的，这会误导容器环境中的进程，使得一些预期中的优化变成了负优化。如线程数、GC的默认设置。

 

针对此问题的解决方案有三个：

 

- Java/Golang/Node启动时手动参数传入资源最大限制；
- Java 8u131+和Java 9+添加-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap；Java 8u191+和Java 10+默认开启UseContainerSupport，无需操作；但是这些手段无法修正进程内直接读取/proc下或者调用top、free -m、uptime等命令输出的内容；
- 改写相关内核参数，对任意程序都有效果。

 

前两种方案，侵入性较高，我们选择使用第三种方案，改写相关内核参数，使用LXCFS实现，yaml中使用hostPath装载。

 

关于LXCFS，这里只提供一个关键词，大家可以去搜索相关信息。

 

与CPU/内存相类似的还有Uptime、diskStats、Swaps等信息，改写后容器内top、free -m、uptime等命令都会显示正确。

 

值得注意的是CPU的限制，容器中所谓的CPU限制，并不是绑定独占核，而是限制使用时间。举个例子：一台4核的物理机，能并行4个线程；而一台32核的宿主机上起一个限制为4核的容器，它仍然能并行32个线程，只不过每个核只能占用1/8的时间片。

 

关于容器内时间的模拟，我们使用了libfaketime，进程启动时添加LD_PRELOAD和FAKETIME环境变量。

 

最后聊一下Kubernetes的基础，etcd。当api-server不可用的时候，直接读取etcd中的数据将成为最后的救命稻草。然而etcd中存放的数据在某个版本之后已经变成了Protobuf编译过的二进制数据。get出来之后肉眼无法识别。

 

我平时会使用Auger这个开源项目，通过管道的形式将etcd中的内容还原成yaml文本。

 

我认知中的Kubernetes，它是一个容器编排体系，是一套云原生的微服务架构。

 

**>>>>**

 

**Q&A**

 

**Q1：**落地过程必然涉及到之前开发、测试和运维流程的变更，组织和相关人员都会面临调整，这部分工作贵公司是如何推进的，踩了哪些坑，如何解决的？

 

A：这个一言难尽啊，人的问题是最难解决的，能用技术解决的都不是问题，要是说回答的话，初期打通公司各个关节，让大boss认可这件事，行政命令强推，很重要。不然做出来也没人用，就是白忙活，在用户中找小白鼠迭代，而不是自己弄个自以为完美的推出去。

 

**Q2：**Java容器瞬间拉起的过程，整个集群都会被CPU用尽，如何解决Java CPU启动时候CPU资源互争的情况？

 

A：这个问题我们也遇到过，后来把内核升级到4.19后就不再发生了，很多内存耗尽，CPU爆炸的问题我们都通过内核升级解决了。

 

**Q3：**日志平台怎么解决没法像grep -C查找上下文，日志平台怎么标准化日志格式？

 

A：这个得看日志平台具体开发是怎么实现的了，一般来说这不是问题

日志格式的标准化，得和业务合作。事实上日志平台一般是中台部门的单独的系统，它要单独开发。

 

**Q4：**容器化落地怎么协调开发的需求？比如开发学习成本，比如本地调试和现场保留复现问题，排查问题的方法方式对开发友好。

 

A：这还是人的问题，很多业务开发不愿意学习，不接受新事物，一叶障目否定容器，这真的没办法。还是从人身上寻求妥协吧。每个人的精力都是有限的，这种事情陷进去很难拔出来；公开培训，讲座，驻场支持，培养业务部门懂的人。

 

**Q5：**线上Kubernetes集群采用什么方式部署，二进制还是kubeadm等，部署架构是怎么样的？

 

A：如果了解证书制作和Kubernetes各个组件的作用，建议从二进制文件入手，企业环境可以自己写Ansible等脚本。kubeadm维护一般不适用于线上环境。

 

**Q6：**我是一名Java工程师，有7年经验，想转行到容器相关领域，请问成为容器开发工程师需要哪些条件？

 

A：对Linux要非常了解，脱离JVM看一些系统方面的知识。此外容器的语言基本上都是Go，微服务那套和Java没啥区别，熟悉Protobuf。

 

**Q7：**如何保证日志Sidecar的存活与否不会影响到业务容器？

 

A：Sidecar和业务容器本来就是互相隔离的，现在1.10+的Kubernetes在Pod内只会共享网络，不会默认共享pid了，应该不会有啥影响。

 

**Q8：**Sidecar方式收集日志会出现延时，特别是丢失问题，这个如何解决？

 

A：减少Filebeat的采集时间，这个我感觉无解。或者在gracefultime上做文章，让Filebeat多活一会。

 

作者丨刘俊杰

来源丨分布式实验室（ID：dockerone）

dbaplus社群欢迎广大技术人员投稿，投稿邮箱：editor@dbaplus.cn