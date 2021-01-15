# [Kubernetes 1.20：最优秀、美妙、酷的版本](https://segmentfault.com/a/1190000038423319)

[![img](Kubernetes 1.20：最优秀、美妙、酷的版本 - SegmentFault 思否.assets/241824629-5c132b13053fe_big64)**Donald**](https://segmentfault.com/u/donald_5c1216a7656d5)发布于 2020-12-09

![img](Kubernetes 1.20：最优秀、美妙、酷的版本 - SegmentFault 思否.assets/lg.php)

[你填了吗？2020年CNCF中国云原生问卷](http://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247494776&idx=1&sn=7716a4ad36c8afb46e2e71f634a7b4bd&chksm=ec9fe318dbe86a0e79fed42aa7894146ca4f2a5266af2e7ff2b635175d6aea9d6940c0f005d8&scene=21#wechat_redirect)

![Image](Kubernetes 1.20：最优秀、美妙、酷的版本 - SegmentFault 思否.assets/1460000038267183)

问卷链接（[https://www.wjx.cn/jq/9714648...](https://www.wjx.cn/jq/97146486.aspx)）

------

作者：[Kubernetes 1.20发布团队](https://github.com/kubernetes/sig-release/blob/master/releases/release-1.20/release_team.md)

我们很高兴地宣布Kubernetes 1.20的发布，这是我们在2020年发布的第三个也是最终的版本！这个版本包含了42个增强：11个增强已经稳定，15个增强进入beta，16个增强进入alpha。

在上一个扩展的发布周期之后，1.20的发布周期又回到了11周的正常节奏。这是一段时间以来功能最密集的版本之一：Kubernetes的创新周期仍呈上升趋势。这个版本更多的是alpha而不是稳定的增强，这表明在云原生生态系统中还有很多需要探索的地方。

**主题**

**卷快照操作趋于稳定**

该特性提供了一种触发卷快照操作的标准方法，并允许用户以可移植的方式在任何Kubernetes环境和支持的存储提供程序上合并快照操作。

此外，这些Kubernetes快照原语（primitive）充当基本构建块，解除了为Kubernetes开发高级、企业级存储管理特性（包括应用程序或集群级备份解决方案）的能力。

请注意，快照支持要求Kubernetes发行版绑定快照控制器、快照CRD和验证webhook。还必须在集群上部署支持快照功能的CSI驱动程序。

**Kubectl Debug升级到Beta**

kubectl alpha debug功能在1.20中升级到beta版，成为kubectl debug。该特性直接从kubectl提供了对常见调试工作流的支持。此版本kubectl支持的故障排除场景包括：

- 通过创建使用不同容器镜像或命令的pod副本来进行故障排除在启动时崩溃的工作负载。
- 通过在pod的新副本中添加带有调试工具的新容器或使用临时容器来进行故障排除无源（distroless）容器的故障。（临时容器是一个alpha特性，默认情况下不启用。）
- 通过创建在主机命名空间中运行并能够访问主机文件系统的容器来对节点进行故障排除。注意，作为一个新的内置命令，kubectl debug优先于任何名为“debug”的kubectl插件。你必须重命名受影响的插件。

使用kubectl alpha debug的调用现在被弃用，将在后续版本中删除。更新脚本以使用kubectl debug。有关kubectl debug的更多信息，请参见[调试运行的Pod](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-running-pod/)。

**Beta：API优先级和公平性**

在1.18中引入，Kubernetes 1.20现在默认支持API优先级和公平性（APF，API Priority and Fairness）。这允许kube-apiserver按优先级级别对传入请求进行分类。

**Alpha更新：IPV4/IPV6**

IPv4/IPv6双栈已经重新实现，以支持基于用户和社区反馈的双栈服务。这允许将IPv4和IPv6服务集群的IP地址分配给单个服务，也允许将一个服务从单个IP栈转换为双IP栈，反之亦然。

**GA：过程PID限制以提供稳定性**

进程ID（pid）是Linux主机上的基本资源。达到任务限制而不触及任何其他资源限制并导致主机不稳定是很简单的。

管理员需要一些机制来确保用户pod不会导致pid耗尽，从而阻止主机守护进程（运行时、kubelet等）运行。此外，务必确保在pod之间限制pid，以确保它们对节点上的其他工作负载的影响有限。在默认启用一年之后，SIG Node在SupportNodePidsLimit（pod到pod PID隔离）和SupportPodPidsLimit（限制每个pod PID的能力）上将PID限制转变为GA。

**Alpha：优雅关闭节点**

用户和集群管理员希望pod遵守预期的pod生命周期，包括pod终止。当前，当一个节点关闭时，pod没有遵循预期的pod终止生命周期，并且不能正常终止，这可能会导致一些工作负载问题。GracefulNodeShutdown特性现在是Alpha。GracefulNodeShutdown使kubelet能够意识到节点系统的关闭，从而在系统关闭期间能够优雅地终止pod。

**主要变化**

**Dockershim弃用**

Dockershim，用于Docker的容器运行时接口（CRI）垫片正在被弃用。对Docker的支持已被弃用，并将在未来的版本中删除。Docker生成的镜像将继续在兼容CRI的运行时在你的集群中工作，因为Docker镜像遵循Open Container Initiative（OCI）镜像规范。Kubernetes社区已经写了一篇[关于弃用的详细博客文章](http://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247495372&idx=1&sn=6d81a55241fbc8491a22478d88f38f3d&chksm=ec9fe1acdbe868ba2f9247523d8551c5eda6b1180112c4badd14bdc588738afb67fb9e67f1f4&scene=21#wechat_redirect)，并有[专门的FAQ页面](http://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247495499&idx=1&sn=e2392c79f2976918ef2b856fc91ffec2&chksm=ec9fe02bdbe8693d50de99ef80c588bee97cbb392823a1c947d44e4280df3f55c5d973eb64c5&scene=21#wechat_redirect)。

**执行探针超时处理**

一个长期存在的关于可能影响现有pod定义的执行探测超时的错误已经得到修复。在此修复之前，执行探测不考虑timeoutSeconds字段。相反，探测将无限期地运行，甚至超过配置的最后期限，直到返回结果为止。通过这个更改，如果没有指定一个值，将应用缺省值1秒，如果探测时间超过1秒，现有的pod定义可能不再足够。在此修复中添加了一个名为ExecProbeTimeout的特性gate，它使集群操作者能够恢复到以前的行为，但在后续版本中将锁定并删除该特性。为了恢复到以前的行为，集群操作人员应该将此特性门设置为false。

请查看关于[配置探针](https://kubernetes.io/blog/2020/12/08/kubernetes-1-20-release-announcement/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes)的更新文档以了解更多细节。

**其他的更新**

**升级到稳定**

- RuntimeClass
- Built-in API Types Defaults
- Add Pod-Startup Liveness-Probe Holdoff
- Support CRI-ContainerD On Windows
- SCTP Support for Services
- Adding AppProtocol To Services And Endpoints

**显著的特性更新**

- CronJobs

**发布说明**

你可以在[版本说明](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md)中查看1.20发行版的完整细节。

**下载**

Kubernetes 1.20可以在[GitHub上下载](https://github.com/kubernetes/kubernetes/releases/tag/v1.20.0)。有一些很好的资源可以帮助你开始使用Kubernetes。你可以在Kubernetes主站点上查看一些[交互式教程](https://kubernetes.io/docs/tutorials/)，或者使用带有[kind](https://kind.sigs.k8s.io/)的Docker容器在你的机器上运行一个本地集群。如果你想从头开始构建集群，请查看Kelsey Hightower编写的[Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)教程。

**发布团队**

这个版本是由一群非常敬业的个人组成的，他们在世界上发生了很多事情的时候聚集在一起组成了一个团队。非常感谢发布团队的领导Jeremy Rickard，以及发布团队中的每一个人对彼此的支持，以及为社区交付1.20发布版本所付出的努力。

**版本标志**

![Image](Kubernetes 1.20：最优秀、美妙、酷的版本 - SegmentFault 思否.assets/1460000038423322)

raddest：形容词，俚语。优秀；美妙；酷：

> The Kubernetes 1.20 Release has been the raddest release yet.
>
> Kubernetes 1.20版本是迄今为止最优秀、美妙、酷的版本。

2020年对我们很多人来说是充满挑战的一年，但是Kubernetes的贡献者在这个版本中提供了破纪录的增强。这是一个伟大的成就，所以发布团队的领导想用一点轻点来结束这一年，用一只名为Humphrey的“rad”猫来表达对[Kubernetes 1.14 - Caturnetes](https://github.com/kubernetes/sig-release/tree/master/releases/release-1.14)的敬意。

Humphrey是发布团队的领导的猫，有一个永久的[blep](https://www.inverse.com/article/42316-why-do-cats-blep-science-explains)。在20世纪90年代的美国，Rad是相当普遍的俚语，激光背景也是如此。Humphrey在一幅90年代风格的校园照片中，感觉像是一个有趣的方式来结束一年。希望Humphrey和他的blep能在2020年底给你带来一点快乐！

发行标志是由[Henry Hsu - @robotdancebattle](https://www.instagram.com/robotdancebattle/)设计的。

**用户亮点**

- 苹果在世界各地的数据中心运行着数千个节点的Kubernetes集群。观看[Alena Prokharchyk在北美KubeCon的主题演讲](https://youtu.be/Tx8qXC-U3KM)，了解更多关于他们的云原生之旅。

**项目速度**

[CNCF K8s DevStats项目](https://k8s.devstats.cncf.io/)聚集了许多与Kubernetes和各种子项目速度相关的有趣数据点。这包括了从个人贡献到参与贡献的公司数量的方方面面，这很好地说明了在进化这个生态系统方面所付出努力的深度和广度。

在为期11周的v1.20发布周期（9月25日至12月9日）中，我们看到来自26个国家的967家公司和1335名个人（其中44人做出了Kubernetes的第一份贡献）做出了贡献。

**生态系统更新**

- 北美KubeCon刚刚在三个星期前结束，是第二个这样的虚拟活动！所有的演讲现在可供点播！
- 今年6月，Kubernetes社区成立了一个新的工作小组，直接回应美国各地发生的“黑人的命也是命”抗议活动。WG Naming的目标是尽可能彻底地删除Kubernetes项目中有害的和不清楚的语言，并以可移植到其他CNCF项目的方式这样做。2020年北美KubeCon会议上有一场关于这项重要工作及其实施方式的精彩介绍性演讲，在v1.20版本中可以看到这项工作的最初影响。
- 先前于今年夏天宣布，Kubernetes安全认证专家（CKS）认证已在北美KubeCon期间发布，可以立即进行预约！遵循CKA和CKAD的模式，CKS是一个基于表现的考试，关注以安全为主题的能力和领域。这个考试针对的是当前的CKA持有者，特别是那些想要完善他们在云工作负载安全方面的基础知识的人（我们都是这样，对吗？）

**活动更新**

2021年欧洲KubeCon + CloudNativeCon将于2021年5月4 - 7日举行！报名将于1月11日开始。你可以在[这里](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)找到更多关于会议的信息。记住[CFP](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/program/cfp/)在12月13日星期日，太平洋标准时间晚上11：59关闭！

**即将举行的1.20版本网络研讨会**

请继续关注即将在一月份举行的1.20版本网络研讨会。

**参与**

如果你有兴趣为Kubernetes社区做出贡献，特殊兴趣组（SIG）是一个很好的起点。其中许多可能与你的兴趣一致！如果你想与社区分享一些东西，你可以参加每周的社区会议，或者使用以下任何渠道：

- 在新的[Kubernetes贡献者网站](https://www.kubernetes.dev/)找到更多关于为Kubernetes贡献的信息
- 关注我们的推特[@Kubernetesio](https://twitter.com/kubernetesio)，获取最新消息
- 在[Discuss](https://discuss.kubernetes.io/)上加入社区讨论
- 加入[Slack](http://slack.k8s.io/)的社区
- 分享你的Kubernetes的[故事](https://docs.google.com/a/linuxfoundation.org/forms/d/e/1FAIpQLScuI7Ye3VQHQTwBASrgkjQDSS5TP0g3AXfFhwSM9YpHgxRKFA/viewform)
- 在[博客](https://kubernetes.io/blog/)上阅读更多关于Kubernetes发生的事情
- 了解更多关于[Kubernetes发布团队](https://github.com/kubernetes/sig-release/tree/master/release-team)的信息

[点击阅读网站原文](https://kubernetes.io/blog/2020/12/08/kubernetes-1-20-release-announcement/)。

------

***CNCF (Cloud Native Computing Foundation)成立于2015年12月，隶属于Linux  Foundation，是非营利性组织。\***
***CNCF（云原生计算基金会）致力于培育和维护一个厂商中立的开源生态系统，来推广云原生技术。我们通过将最前沿的模式民主化，让这些创新为大众所用。扫描二维码关注CNCF微信公众号。\***
![image](Kubernetes 1.20：最优秀、美妙、酷的版本 - SegmentFault 思否.assets/bVbLRb6)

[容器](https://segmentfault.com/t/容器)[docker](https://segmentfault.com/t/docker)[kubernetes](https://segmentfault.com/t/kubernetes)[k8s](https://segmentfault.com/t/k8s)[cncf](https://segmentfault.com/t/cncf)