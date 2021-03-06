DEVOPS

# 什么是 SRE（站点可靠性工程）？

站点可靠性工程（SRE）是 IT 运维的软件工程方案。SRE 团队使用软件作为工具，来管理系统、解决问题并实现运维任务[自动化](https://www.redhat.com/zh/topics/automation)。

SRE 执行的任务以前通常由运维团队手动执行，或者交给使用软件和自动化来解决问题和管理生产系统的工程师或运维团队来执行。 

在创建可扩展和高度可靠的软件系统时，SRE 是宝贵的实践。它可帮助您通过代码管理大型系统，对于管理成千上万台机器的系统管理员来说，代码更具可扩展性和可持续性。 

站点可靠性工程的概念由 Google 工程团队的 Ben Treynor Sloss 第一个提出。 

SRE 可以帮助团队在发布新功能和确保用户可靠性之间找到平衡。

标准化和自动化是 SRE 模型的两大重要部分。站点可靠性工程师应始终致力于增强和自动化运维任务。

这样一来，SRE 就能帮助提高现有系统的可靠性，同时优化体量逐渐庞大的系统。 

SRE 支持团队从传统 IT 运维方案迁移至[云原生](https://www.redhat.com/zh/topics/cloud-native-apps)方案。

## 站点可靠性工程师的工作是什么？

站点可靠性工程师是一个独特的岗位，要么必须是有运维经验的软件开发人员；要么必须是有软件开发技能的系统管理员或的 IT 运维人员。 

SRE 团队负责部署、配置和监控代码，以及生产服务的可用性、延迟、变更管理、应急响应和容量管理。

站点可靠性工程可帮助团队确定可以要启动哪些新功能，以及在何时根据服务水平协议（SLA）并利用服务水平指标（SLI）和服务水平目标（SLO）定义系统所需的可靠性。 

SLI 是针对提供的服务水平的特定方面所定义的测量指标。关键 SLI 包括请求延迟性、可用性、错误率和系统吞吐量。SLO 基于根据 SLI 而指定的服务水平的目标值或范围。

然后，根据认定为可接受的停机时间确定所需系统可靠性的 SLO。这个停机时间称为误差量，即出错和中断的最大允许阈值。 

SRE 并不是要实现 100% 可靠性，而是针对故障做好计划并妥善应对。 

开发团队在发布新功能时允许出现这一定量的误差。利用 SLO 和误差量，开发团队可确定产品或服务是否能够在可用误差量的基础上启动。

如果某个服务在运行时处于误差量以内，则开发团队可在任何时间发布它，但是，如果系统当前有太多错误或停机时间超过误差量的允许范围，则必须使错误数减少至误差量以内后才能发布。  

开发团队可执行自动化运维测试以验证可靠性。 

站点可靠性工程师的时间要均衡分配给运维任务和项目工作。根据 Google 的 SRE 最佳实践，站点可靠性工程师最多只能将一半的时间花在运维上，所以应该监控确保不会超过这个时间。 

剩余的时间应专注于开发任务上，比如创建新功能，扩展系统，以及实施自动化。

额外的运维工作和表现欠佳的服务应重新指定给开发团队，而不是让站点可靠性工程师将太多时间花在应用或服务的运维上。 

自动化是站点可靠性工程师的重要工作部分。如果他们要反复处理一个问题，就会努力实现解决方案自动化。这也有助于控制运维工作在他们工作中所占的比例。 

保持运维和开发工作之间的平衡是 SRE 的重要组成部分。 

## DevOps 和SRE

[DevOps](https://www.redhat.com/zh/topics/devops) 是指对企业文化、业务自动化和平台设计等方面进行全方位变革，从而实现迅捷、优质的服务交付，提升企业价值和响应能力。SRE 可视为 DevOps 的实施。

和 DevOps 一样，SRE 也与团队文化和关系密切相连。SRE 和 DevOps 都致力于搭建开发团队和运维团队之间的互通桥梁，以便加快交付服务。 

DevOps 和 SRE 实践都可以实现更快的应用开发生命周期、改进的服务质量和可靠性，以及缩短的 IT 应用开发时间等优势。

但 SRE 有所不同的是，它依赖于开发团队中的站点可靠性工程师，这些工程师也要有解决通信和工作流程问题的运维背景。

站点可靠性工程师本身要求职责重叠，兼具开发团队和运维团队的技能。 

DevOps 团队的开发人员常常疲于处理运维任务，需要拥有更专业运维技能，而 SRE 就能派上用场。 

在代码和新功能方面，DevOps 专注于有效通过开发流程，而 SRE 专注于通过创建新功能来平衡站点可靠性。 

基于容器技术、Kubernetes 和[微服务](https://www.redhat.com/zh/topics/microservices/what-are-microservices)的现代化应用平台是落实 DevOps 实践的关键所在，可帮助企业交付安全的创新软件服务。