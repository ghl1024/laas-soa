## 不要惊慌：Kubernetes和Docker

Kubernetes [CNCF](javascript:void(0);) *2020-12-03*

![图片](不要惊慌：Kubernetes和Docker.assets/640)：[来贡献几分钟提交：2020年CNCF中国云原生问卷](http://mp.weixin.qq.com/s?__biz=MzI5ODk5ODI4Nw==&mid=2247494776&idx=1&sn=7716a4ad36c8afb46e2e71f634a7b4bd&chksm=ec9fe318dbe86a0e79fed42aa7894146ca4f2a5266af2e7ff2b635175d6aea9d6940c0f005d8&scene=21#wechat_redirect)

![图片](不要惊慌：Kubernetes和Docker.assets/640)

问卷链接（https://www.wjx.cn/jq/97146486.aspx）



------



**作者：**Jorge Castro、Duffie Cooley、Kat Cosgrove、Justin Garrison、Noah Kantrowitz、Bob Killen、Rey Lejano、Dan "POP" Papandrea、Jeffrey Sica、Davanum "Dims" Srinivas





Kubernetes在1.20版本之后将弃用Docker作为容器运行时。

https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation



**你不需要惊慌。这并不像听起来那么戏剧化。**



简单来讲：Docker作为底层运行时正在被弃用，取而代之的是使用为Kubernetes创建的CRI（Container Runtime Interface，容器运行时接口）的运行时。Docker生成的镜像将继续在你的集群中与所有运行时一起工作，就像它们一直那样。

https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/



如果你是Kubernetes的最终用户，那么不会有太多的变化。这并不意味着Docker的消亡，也不意味着你不能或不应该再使用Docker作为开发工具。Docker仍然是构建容器的有用工具，运行Docker build产生的镜像仍然可以在Kubernetes集群中运行。



如果你正在使用像GKE或EKS这样的托管Kubernetes服务，那么在Kubernetes的未来版本中删除Docker支持之前，你需要确保你的工作节点使用的是受支持的容器运行时。如果你有节点自定义，则可能需要根据环境和运行时需求更新它们。请与你的服务提供商合作，以确保适当的升级测试和计划。



如果你在创建自己的集群，你还需要进行更改，以避免集群崩溃。在v1.20，你将收到Docker的弃用警告。当Docker运行时支持在Kubernetes的未来发行版（目前计划在2021年底的1.23发行版）中被移除时，它将不再受支持，你将需要切换到其他兼容的容器运行时，如containerd或CRI-O。只要确保你选择的运行时支持你当前使用的docker守护进程配置（例如日志）。



**那么，为什么会有这种困惑呢？每个人都在担心什么呢？**

我们在这里讨论的是两种不同的环境，这就造成了混淆。在Kubernetes集群中，有一个称为容器运行时的东西，它负责提取和运行容器镜像。Docker是该运行时的流行选择（其他常见选项包括containerd和CRI-O），但是Docker并不是被设计成嵌入到Kubernetes中，这就导致了一个问题。



你看，我们称为“Docker”的东西实际上并不只是一个东西--它是一个完整的技术堆栈，其中一部分是一个叫做“containerd”的东西，它本身是一个高级的容器运行时。Docker很酷，也很有用，因为它有很多UX增强，使得在我们进行开发工作时很容易与人交互，但是这些UX增强对Kubernetes来说不是必需的，因为它不是人。



由于有了这个对人友好的抽象层，你的Kubernetes集群必须使用另一个称为Dockershim的工具来获得它真正需要的东西，它包含在其中。这不太好，因为它给了我们另一个需要维护的东西，而且可能会损坏。这里实际发生的是，Dockershim最早将在v1.23版本就从Kubelet中删除了，从而取消了对Docker作为容器运行时的支持。你可能会想，如果containerd包含在Docker堆栈中，为什么Kubernetes需要Dockershim呢？



Docker与CRI（容器运行时接口）不兼容。如果是的话，我们就不需要垫片了，这就不成问题了。但这并不是世界末日，你也不必惊慌--你只需要将容器运行时从Docker更改为另一个受支持的容器运行时。

https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/



需要注意的一点是：如果你现在在集群中依赖底层docker socket（/var/run/docker.sock）作为工作流程的一部分，迁移到不同的运行时将会破坏你使用它的能力。这种模式通常称为Docker in Docker。对于这个特定的用例，有很多选择，包括kaniko、img和buildah。

https://github.com/GoogleContainerTools/kaniko

https://github.com/genuinetools/img

https://github.com/containers/buildah



**但是，这种变化对开发人员意味着什么呢？我们还在写Dockerfile吗？我们还用Docker构建东西吗？**

这一改变解决了一个与大多数人使用Docker进行交互的不同环境。你在开发中使用的Docker安装与Kubernetes集群中的Docker运行时无关。我知道这很令人困惑。作为一名开发人员，Docker仍然对你很有用，就像在这项更改宣布之前一样。Docker生成的镜像实际上并不是一个特定于Docker的镜像--它是一个OCI（Open Container Initiative）镜像。无论你使用什么工具构建它，任何符合OCI标准的镜像在Kubernetes看来都是一样的。containerd和CRI-O都知道如何提取这些镜像并运行它们。这就是为什么我们有一个容器应该是什么样的标准。

https://opencontainers.org/



所以，这种变化正在到来。这会给一些人带来问题，但这不是灾难性的，而且一般来说这是件好事。取决于你如何与Kubernetes交互，这可能对你毫无意义，也可能意味着需要进行一些工作。从长远来看，这会让事情变得更简单。如果这仍然让你感到困惑，那也没关系--这里发生了很多事情，Kubernetes有很多变动的部分，没有人是100%的专家。我们鼓励任何和所有的问题，无论经验水平或复杂性！我们的目标是确保每个人都尽可能多地了解即将到来的变化。我们希望这已经回答了你的大部分问题，缓解了你的一些焦虑！



点击【阅读原文】阅读网站原文。





![图片](https://mmbiz.qpic.cn/mmbiz_png/GpkQxibjhkJxyapkOjiazruKNQ7DZ6t8TSh0QSYM4DlI86xnXiayciayIgBUaG8q8lFZ3FsibPJiaeCqAahrKicB220aA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

扫描二维码联系我们！



------



***CNCF (Cloud Native Computing Foundation)成立于2015年12月，隶属于Linux  Foundation，是非营利性组织。\*** 

***\**\*CNCF\*\**\******（\******\**\*云原生计算基金会\*\**）致力于培育和维护一个厂商中立的开源生态系统，来推广云原生技术。我们通过将最前沿的模式民主化，让这些创新为大众所用。请长按以下二维码进行关注。\***

![图片](不要惊慌：Kubernetes和Docker.assets/640)