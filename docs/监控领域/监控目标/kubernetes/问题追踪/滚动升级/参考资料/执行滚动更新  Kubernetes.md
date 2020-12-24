[Kubernetes 文档](https://kubernetes.io/zh/docs/)[教程](https://kubernetes.io/zh/docs/tutorials/)[学习 Kubernetes 基础知识](https://kubernetes.io/zh/docs/tutorials/kubernetes-basics/)[更新你的应用](https://kubernetes.io/zh/docs/tutorials/kubernetes-basics/update/)[执行滚动更新](https://kubernetes.io/zh/docs/tutorials/kubernetes-basics/update/update-intro/)

# 执行滚动更新

### Objectives

- 使用 kubectl 执行滚动更新。

### 更新应用程序

用户希望应用程序始终可用，而开发人员则需要每天多次部署它们的新版本。在 Kubernetes 中，这些是通过滚动更新（Rolling Updates）完成的。 **滚动更新** 允许通过使用新的实例逐步更新 Pod 实例，零停机进行 Deployment 更新。新的 Pod 将在具有可用资源的节点上进行调度。

在前面的模块中，我们将应用程序扩展为运行多个实例。这是在不影响应用程序可用性的情况下执行更新的要求。默认情况下，更新期间不可用的 pod 的最大值和可以创建的新 pod 数都是 1。这两个选项都可以配置为（pod）数字或百分比。 在 Kubernetes 中，更新是经过版本控制的，任何 Deployment 更新都可以恢复到以前的（稳定）版本。

### 摘要：

- 更新应用

*滚动更新允许通过使用新的实例逐步更新 Pod 实例从而实现 Deployments 更新，停机时间为零。*



## 滚动更新概述

1. 
2. 
3. 
4. 

![img](执行滚动更新  Kubernetes.assets/module_06_rollingupdates3.svg)

[Previous](https://kubernetes.io/zh/docs/tutorials/kubernetes-basics/update/update-intro/#myCarousel)[Next](https://kubernetes.io/zh/docs/tutorials/kubernetes-basics/update/update-intro/#myCarousel)



与应用程序扩展类似，如果公开了 Deployment，服务将在更新期间仅对可用的 pod 进行负载均衡。可用 Pod 是应用程序用户可用的实例。

滚动更新允许以下操作：

- 将应用程序从一个环境提升到另一个环境（通过容器镜像更新）
- 回滚到以前的版本
- 持续集成和持续交付应用程序，无需停机

*如果 Deployment 是公开的，则服务将仅在更新期间对可用的 pod 进行负载均衡。*



在下面的交互式教程中，我们将应用程序更新为新版本，并执行回滚。