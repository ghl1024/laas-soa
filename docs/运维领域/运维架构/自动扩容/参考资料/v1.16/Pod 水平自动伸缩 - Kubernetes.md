# Pod 水平自动伸缩

Pod 水平自动伸缩（Horizontal Pod Autoscaler）特性， 可以基于CPU利用率自动伸缩 replication controller、deployment和 replica set 中的 pod 数量，（除了 CPU 利用率）也可以 基于其他应程序提供的度量指标[custom metrics](https://git.k8s.io/community/contributors/design-proposals/instrumentation/custom-metrics-api.md)。 pod 自动缩放不适用于无法缩放的对象，比如 DaemonSets。

Pod 水平自动伸缩特性由 Kubernetes API 资源和控制器实现。资源决定了控制器的行为。 控制器会周期性的获取平均 CPU 利用率，并与目标值相比较后来调整 replication controller 或 deployment 中的副本数量。

- [Pod 水平自动伸缩工作机制](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#pod-水平自动伸缩工作机制)
- [API 对象](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#api-对象)
- [使用 kubectl 操作 Horizontal Pod Autoscaler](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#使用-kubectl-操作-horizontal-pod-autoscaler)
- [滚动升级时缩放](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#滚动升级时缩放)
- [冷却/延迟](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#冷却-延迟)
- [多指标支持](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#多指标支持)
- [自定义指标支持](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#自定义指标支持)
- [指标 API](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#指标-api)
- [接下来](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#接下来)

## Pod 水平自动伸缩工作机制

![水平自动伸缩示意图](Pod 水平自动伸缩 - Kubernetes.assets/horizontal-pod-autoscaler.svg)

Pod 水平自动伸缩的实现是一个控制循环，由 controller manager 的 `--horizontal-pod-autoscaler-sync-period` 参数 指定周期（默认值为15秒）。

每个周期内，controller manager 根据每个 HorizontalPodAutoscaler 定义中指定的指标查询资源利用率。 controller manager 可以从 resource metrics API（每个pod 资源指标）和 custom metrics API（其他指标）获取指标。

- 对于每个 pod 的资源指标（如 CPU），控制器从资源指标 API 中获取每一个 HorizontalPodAutoscaler 指定 的 pod 的指标，然后，如果设置了目标使用率，控制器获取每个 pod 中的容器资源使用情况，并计算资源使用率。 如果使用原始值，将直接使用原始数据（不再计算百分比）。 然后，控制器根据平均的资源使用率或原始值计算出缩放的比例，进而计算出目标副本数。

需要注意的是，如果 pod 某些容器不支持资源采集，那么控制器将不会使用该 pod 的 CPU 使用率。 下面的[算法细节](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details)章节将会介绍详细的算法。

- 如果 pod 使用自定义指示，控制器机制与资源指标类似，区别在于自定义指标只使用原始值，而不是使用率。

- 如果pod 使用对象指标和外部指标（每个指标描述一个对象信息）。 这个指标将直接跟据目标设定值相比较，并生成一个上面提到的缩放比例。在 `autoscaling/v2beta2` 版本API中， 这个指标也可以根据 pod 数量平分后再计算。

通常情况下，控制器将从一系列的聚合 API（`metrics.k8s.io`、`custom.metrics.k8s.io`和`external.metrics.k8s.io`） 中获取指标数据。 `metrics.k8s.io` API 通常由 metrics-server（需要额外启动）提供。 可以从[metrics-server](https://v1-16.docs.kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/#metrics-server) 获取更多信息。 另外，控制器也可以直接从 Heapster 获取指标。

> **注意：**
>
> **FEATURE STATE:** `Kubernetes 1.11` [废弃](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#)
>
> 自 Kubernetes 1.11起，从 Heapster 获取指标特性已废弃。

关于指标 API 更多信息，请参考[Support for metrics APIs](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis)。

自动缩放控制器使用 scale sub-resource 访问相应可支持缩放的控制器（如replication controllers、deployments 和 replica sets）。 `scale` 是一个可以动态设定副本数量和检查当前状态的接口。 更多关于 scale sub-resource 的信息，请参考[这里](https://git.k8s.io/community/contributors/design-proposals/autoscaling/horizontal-pod-autoscaler.md#scale-subresource).

### 算法细节

从最基本的角度来看，pod 水平自动缩放控制器跟据当前指标和期望指标来计算缩放比例。

```
期望副本数 = ceil[当前副本数 * ( 当前指标 / 期望指标 )]
```

例如，当前指标为`200m`，目标设定值为`100m`,那么由于`200.0 / 100.0 == 2.0`， 副本数量将会翻倍。 如果当前指标为`50m`，副本数量将会减半，因为`50.0 / 100.0 == 0.5`。 如果计算出的缩放比例接近1.0（跟据`--horizontal-pod-autoscaler-tolerance` 参数全局配置的容忍值，默认为0.1）， 将会放弃本次缩放。

如果 HorizontalPodAutoscaler 指定的是`targetAverageValue` 或 `targetAverageUtilization`， 那么将会把指定pod的平均指标做为`currentMetricValue`。 然而，在检查容忍度和决定最终缩放值前，我们仍然会把那些无法获取指标的pod统计进去。

所有被标记了删除时间戳(Pod正在关闭过程中)的 pod 和 失败的 pod 都会被忽略。

如果某个 pod 缺失指标信息，它将会被搁置，只在最终确定缩值时再考虑。

当使用 CPU 指标来缩放时，任何还未就绪（例如还在初始化）状态的 pod *或* 最近的指标为就绪状态前的 pod， 也会被搁置

由于受技术限制，pod 水平缩放控制器无法准确的知道 pod 什么时候就绪， 也就无法决定是否暂时搁置该 pod。 `--horizontal-pod-autoscaler-initial-readiness-delay` 参数（默认为30s），用于设置 pod 准备时间， 在此时间内的 pod 统统被认为未就绪。 `--horizontal-pod-autoscaler-cpu-initialization-period`参数（默认为5分钟），用于设置 pod 的初始化时间， 在此时间内的 pod，CPU 资源指标将不会被采纳。

在排除掉被搁置的 pod 后，缩放比例就会跟据`currentMetricValue / desiredMetricValue`计算出来。

如果有任何 pod 的指标缺失，我们会更保守地重新计算平均值， 在需要缩小时假设这些 pod 消耗了目标值的 100%， 在需要放大时假设这些 pod 消耗了0%目标值。 这可以在一定程度上抑制伸缩的幅度。

此外，如果存在任何尚未就绪的pod，我们可以在不考虑遗漏指标或尚未就绪的pods的情况下进行伸缩， 我们保守地假设尚未就绪的pods消耗了试题指标的0%，从而进一步降低了伸缩的幅度。

在缩放方向（缩小或放大）确定后，我们会把未就绪的 pod 和缺少指标的 pod 考虑进来再次计算使用率。 如果新的比率与缩放方向相反，或者在容忍范围内，则跳过缩放。 否则，我们使用新的缩放比例。

注意，平均利用率的*原始*值会通过 HorizontalPodAutoscaler 的状态体现（ 即使使用了新的使用率，也不考虑未就绪 pod 和 缺少指标的 pod)。

如果创建 HorizontalPodAutoscaler 时指定了多个指标， 那么会按照每个指标分别计算缩放副本数，取最大的进行缩放。 如果任何一个指标无法顺利的计算出缩放副本数（比如，通过 API 获取指标时出错）， 那么本次缩放会被跳过。

最后，在 HPA 控制器执行缩放操作之前，会记录缩放建议信息（scale recommendation）。 控制器会在操作时间窗口中考虑所有的建议信息，并从中选择得分最高的建议。 这个值可通过 kube-controller-manager 服务的启动参数 `--horizontal-pod-autoscaler-downscale-stabilization` 进行配置， 默认值为 5min。 这个配置可以让系统更为平滑地进行缩容操作，从而消除短时间内指标值快速波动产生的影响。

## API 对象

HorizontalPodAutoscaler 是 Kubernetes `autoscaling` API 组的资源。 在当前稳定版本（`autoscaling/v1`）中只支持基于CPU指标的缩放。

在 beta 版本（`autoscaling/v2beta2`），引入了基于内存和自定义指标的缩放。 在`autoscaling/v2beta2`版本中新引入的字段在`autoscaling/v1`版本中基于 annotation 实现。

更多有关 API 对象的信息，请查阅[HorizontalPodAutoscaler Object](https://git.k8s.io/community/contributors/design-proposals/autoscaling/horizontal-pod-autoscaler.md#horizontalpodautoscaler-object)。

## 使用 kubectl 操作 Horizontal Pod Autoscaler

与其他 API 资源类似，`kubectl` 也标准支持 Pod 自动伸缩。 我们可以通过 `kubectl create` 命令创建一个自动伸缩对象， 通过 `kubectl get hpa` 命令来获取所有自动伸缩对象， 通过 `kubectl describe hpa` 命令来查看自动伸缩对象的详细信息。 最后，可以使用 `kubectl delete hpa` 命令删除对象。

此外，还有个简便的命令 `kubectl autoscale` 来创建自动伸缩对象。 例如，命令 `kubectl autoscale rs foo --min=2 --max=5 --cpu-percent=80` 将会为名 为 *foo* 的 replication set 创建一个自动伸缩对象， 对象目标CPU使用率为 `80%`，副本数量配置为 2 到 5 之间。

## 滚动升级时缩放

目前在 Kubernetes 中，可以针对 replication controllers 或 deployment 执行 滚动升级[rolling update](https://v1-16.docs.kubernetes.io/docs/tasks/run-application/rolling-update-replication-controller/)，他们会为你管理底层副本数。 Pod 水平缩放只支持后一种：Horizontal Pod Autoscaler 会被绑定到 deployment 对象中，Horizontal Pod Autoscaler 设置副本数量时， deployment 会设置底层副本数。

当使用 replication controllers 执行滚动升级时， Horizontal Pod Autoscaler 不能工作， 也就是说你不能将 Horizontal Pod Autoscaler 绑定到某个 replication controller 再执行滚动升级（例如使用 `kubectl rolling-update` 命令）。 Horizontal Pod Autoscaler 不能工作的原因是，Horizontal Pod Autoscaler 无法绑定到滚动升级时创建的新副本。

## 冷却/延迟

当使用 Horizontal Pod Autoscaler 管理一组副本缩放时， 有可能因为指标动态的变化造成副本数量频繁的变化，有时这被称为 *抖动*。

从 v1.6 版本起，集群操作员可以开启某些 `kube-controller-manager` 全局的参数来缓和这个问题。

从 v1.12 开始，算法调整后，就不用这么做了。

- `--horizontal-pod-autoscaler-downscale-stabilization`: 这个 `kube-controller-manager` 的参数表示缩容冷却时间。 即自从上次缩容执行结束后，多久可以再次执行缩容，默认时间是5分钟(`5m0s`)。

> **注意：**
>
> 当启用这个参数时，集群操作员需要明白其可能的影响。 如果延迟（冷却）时间设置的太长，那么 Horizontal Pod Autoscaler 可能会不能很好的改变负载。 如果延迟（冷却）时间设备的太短，那么副本数量有可能跟以前一样抖动。

## 多指标支持

在 Kubernetes 1.6 支持了基于多个指标进行缩放。 你可以使用 `autoscaling/v2beta2` API 来为 Horizontal Pod Autoscaler 指定多个指标。 Horizontal Pod Autoscaler 会跟据每个指标计算，并生成一个缩放建议。 幅度最大的缩放建议会被采纳。

## 自定义指标支持

> **注意：**
>
> 在 Kubernetes 1.2 增加的 alpha 的缩放支持基于特定的 annotation。 自从 Kubernetes 1.6 起，由于缩放 API 的引入，这些 annotation 就不再支持了。 虽然收集自定义指标的旧方法仍然可用，但是 Horizontal Pod Autoscaler 调度器将不会再使用这些指标， 同时，Horizontal Pod Autoscaler 也不再使用之前的用于指定用户自定义指标的 annotation 了。

自 Kubernetes 1.6 起，Horizontal Pod Autoscaler 支持使用自定义指标。 你可以使用 `autoscaling/v2beta2` API 为 Horizontal Pod Autoscaler 指定用户自定义指标。 Kubernetes 会通过用户自定义指标 API 来获取相应的指标。

关于指标 API 的要求，请查阅 [Support for metrics APIs](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis)。

## 指标 API

默认情况下，HorizontalPodAutoscaler 控制器会从一系列的 API 中请求指标数据。 集群管理员需要确保下述条件，以保证这些 API 可以访问：

- [API aggregation layer](https://v1-16.docs.kubernetes.io/docs/tasks/access-kubernetes-api/configure-aggregation-layer/) 已开启

- 相应的 API 已注册：
  - 资源指标会使用 `metrics.k8s.io` API，一般由 [metrics-server](https://github.com/kubernetes-incubator/metrics-server) 提供。 它可以做为集群组件启动。
  - 用户指标会使用 `custom.metrics.k8s.io` API。 它由其他厂商的“适配器”API 服务器提供。 确认你的指标管道，或者查看 [list of known solutions](https://github.com/kubernetes/metrics/blob/master/IMPLEMENTATIONS.md#custom-metrics-api)。
  - 外部指标会使用 `external.metrics.k8s.io` API。可能由上面的用户指标适配器提供。

- `--horizontal-pod-autoscaler-use-rest-clients` 参数设置为 `true` 或者不设置。 如果设置为 false，则会切换到基于 Heapster 的自动缩放，这个特性已经被弃用了。

更多关于指标来源以及其区别，请参阅相关的设计文档， [the HPA V2](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/hpa-v2.md)、 [custom.metrics.k8s.io](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md)和 [external.metrics.k8s.io](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/external-metrics-api.md)。

如何使用它们的示例，请参考 [the walkthrough for using custom metrics](https://v1-16.docs.kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics) 和 [the walkthrough for using external metrics](https://v1-16.docs.kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-metrics-not-related-to-kubernetes-objects)。

## 接下来

- 设计文档：[Horizontal Pod Autoscaling](https://git.k8s.io/community/contributors/design-proposals/autoscaling/horizontal-pod-autoscaler.md).
- kubectl 自动缩放命令： [kubectl autoscale](https://v1-16.docs.kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#autoscale).
- 使用示例：[Horizontal Pod Autoscaler](https://v1-16.docs.kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/).