[Kubernetes 文档](https://kubernetes.io/zh/docs/)[任务](https://kubernetes.io/zh/docs/tasks/)[运行应用](https://kubernetes.io/zh/docs/tasks/run-application/)[Pod 水平自动扩缩](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/)

# Pod 水平自动扩缩

Pod 水平自动扩缩（Horizontal Pod Autoscaler） 可以基于 CPU 利用率自动扩缩 ReplicationController、Deployment、ReplicaSet 和 StatefulSet 中的 Pod 数量。 除了 CPU 利用率，也可以基于其他应程序提供的[自定义度量指标](https://git.k8s.io/community/contributors/design-proposals/instrumentation/custom-metrics-api.md) 来执行自动扩缩。 Pod 自动扩缩不适用于无法扩缩的对象，比如 DaemonSet。

Pod 水平自动扩缩特性由 Kubernetes API 资源和控制器实现。资源决定了控制器的行为。 控制器会周期性的调整副本控制器或 Deployment 中的副本数量，以使得 Pod 的平均 CPU 利用率与用户所设定的目标值匹配。

## Pod 水平自动扩缩工作机制

![水平自动扩缩示意图](Pod 水平自动扩缩  Kubernetes.assets/horizontal-pod-autoscaler.svg)

Pod 水平自动扩缩器的实现是一个控制回路，由控制器管理器的 `--horizontal-pod-autoscaler-sync-period` 参数指定周期（默认值为 15 秒）。

每个周期内，控制器管理器根据每个 HorizontalPodAutoscaler 定义中指定的指标查询资源利用率。 控制器管理器可以从资源度量指标 API（按 Pod 统计的资源用量）和自定义度量指标 API（其他指标）获取度量值。

- 对于按 Pod 统计的资源指标（如 CPU），控制器从资源指标 API 中获取每一个 HorizontalPodAutoscaler 指定的 Pod 的度量值，如果设置了目标使用率， 控制器获取每个 Pod 中的容器资源使用情况，并计算资源使用率。 如果设置了 target 值，将直接使用原始数据（不再计算百分比）。 接下来，控制器根据平均的资源使用率或原始值计算出扩缩的比例，进而计算出目标副本数。

  需要注意的是，如果 Pod 某些容器不支持资源采集，那么控制器将不会使用该 Pod 的 CPU 使用率。 下面的[算法细节](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details)章节将会介绍详细的算法。

- 如果 Pod 使用自定义指示，控制器机制与资源指标类似，区别在于自定义指标只使用 原始值，而不是使用率。

- 如果 Pod 使用对象指标和外部指标（每个指标描述一个对象信息）。 这个指标将直接根据目标设定值相比较，并生成一个上面提到的扩缩比例。 在 `autoscaling/v2beta2` 版本 API 中，这个指标也可以根据 Pod 数量平分后再计算。

通常情况下，控制器将从一系列的聚合 API（`metrics.k8s.io`、`custom.metrics.k8s.io` 和 `external.metrics.k8s.io`）中获取度量值。 `metrics.k8s.io` API 通常由 Metrics 服务器（需要额外启动）提供。 可以从 [metrics-server](https://kubernetes.io/zh/docs/tasks/debug-application-cluster/resource-metrics-pipeline/#metrics-server) 获取更多信息。 另外，控制器也可以直接从 Heapster 获取指标。

> **说明：**
>
> **FEATURE STATE:** `Kubernetes 1.11 [deprecated]`
>
> 自 Kubernetes 1.11 起，从 Heapster 获取指标特性已废弃。

关于指标 API 更多信息，请参考[度量值指标 API 的支持](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis)。

自动扩缩控制器使用 scale 子资源访问相应可支持扩缩的控制器（如副本控制器、 Deployment 和 ReplicaSet）。 `scale` 是一个可以动态设定副本数量和检查当前状态的接口。 关于 scale 子资源的更多信息，请参考[这里](https://git.k8s.io/community/contributors/design-proposals/autoscaling/horizontal-pod-autoscaler.md#scale-subresource).

### 算法细节

从最基本的角度来看，Pod 水平自动扩缩控制器根据当前指标和期望指标来计算扩缩比例。

```
期望副本数 = ceil[当前副本数 * (当前指标 / 期望指标)]
```

例如，当前度量值为 `200m`，目标设定值为 `100m`，那么由于 `200.0/100.0 == 2.0`， 副本数量将会翻倍。 如果当前指标为 `50m`，副本数量将会减半，因为`50.0/100.0 == 0.5`。 如果计算出的扩缩比例接近 1.0 （根据`--horizontal-pod-autoscaler-tolerance` 参数全局配置的容忍值，默认为 0.1）， 将会放弃本次扩缩。

如果 HorizontalPodAutoscaler 指定的是 `targetAverageValue` 或 `targetAverageUtilization`， 那么将会把指定 Pod 度量值的平均值做为 `currentMetricValue`。 然而，在检查容忍度和决定最终扩缩值前，我们仍然会把那些无法获取指标的 Pod 统计进去。

所有被标记了删除时间戳（Pod 正在关闭过程中）的 Pod 和失败的 Pod 都会被忽略。

如果某个 Pod 缺失度量值，它将会被搁置，只在最终确定扩缩数量时再考虑。

当使用 CPU 指标来扩缩时，任何还未就绪（例如还在初始化）状态的 Pod *或* 最近的指标 度量值采集于就绪状态前的 Pod，该 Pod 也会被搁置。

由于受技术限制，Pod 水平扩缩控制器无法准确的知道 Pod 什么时候就绪， 也就无法决定是否暂时搁置该 Pod。 `--horizontal-pod-autoscaler-initial-readiness-delay` 参数（默认为 30s）用于设置 Pod 准备时间， 在此时间内的 Pod 统统被认为未就绪。 `--horizontal-pod-autoscaler-cpu-initialization-period` 参数（默认为5分钟） 用于设置 Pod 的初始化时间， 在此时间内的 Pod，CPU 资源度量值将不会被采纳。

在排除掉被搁置的 Pod 后，扩缩比例就会根据 `currentMetricValue/desiredMetricValue` 计算出来。

如果缺失任何的度量值，我们会更保守地重新计算平均值， 在需要缩小时假设这些 Pod 消耗了目标值的 100%， 在需要放大时假设这些 Pod 消耗了 0% 目标值。 这可以在一定程度上抑制扩缩的幅度。

此外，如果存在任何尚未就绪的 Pod，我们可以在不考虑遗漏指标或尚未就绪的 Pod 的情况下进行扩缩， 我们保守地假设尚未就绪的 Pod 消耗了期望指标的 0%，从而进一步降低了扩缩的幅度。

在扩缩方向（缩小或放大）确定后，我们会把未就绪的 Pod 和缺少指标的 Pod 考虑进来再次计算使用率。 如果新的比率与扩缩方向相反，或者在容忍范围内，则跳过扩缩。 否则，我们使用新的扩缩比例。

注意，平均利用率的*原始*值会通过 HorizontalPodAutoscaler 的状态体现（ 即使使用了新的使用率，也不考虑未就绪 Pod 和 缺少指标的 Pod)。

如果创建 HorizontalPodAutoscaler 时指定了多个指标， 那么会按照每个指标分别计算扩缩副本数，取最大值进行扩缩。 如果任何一个指标无法顺利地计算出扩缩副本数（比如，通过 API 获取指标时出错）， 并且可获取的指标建议缩容，那么本次扩缩会被跳过。 这表示，如果一个或多个指标给出的 `desiredReplicas` 值大于当前值，HPA 仍然能实现扩容。

最后，在 HPA 控制器执行扩缩操作之前，会记录扩缩建议信息。 控制器会在操作时间窗口中考虑所有的建议信息，并从中选择得分最高的建议。 这个值可通过 `kube-controller-manager` 服务的启动参数 `--horizontal-pod-autoscaler-downscale-stabilization` 进行配置， 默认值为 5 分钟。 这个配置可以让系统更为平滑地进行缩容操作，从而消除短时间内指标值快速波动产生的影响。

## API 对象

HorizontalPodAutoscaler 是 Kubernetes `autoscaling` API 组的资源。 在当前稳定版本（`autoscaling/v1`）中只支持基于 CPU 指标的扩缩。

API 的 beta 版本（`autoscaling/v2beta2`）引入了基于内存和自定义指标的扩缩。 在 `autoscaling/v2beta2` 版本中新引入的字段在 `autoscaling/v1` 版本中以注解 的形式得以保留。

创建 HorizontalPodAutoscaler 对象时，需要确保所给的名称是一个合法的 [DNS 子域名](https://kubernetes.io/zh/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)。 有关 API 对象的更多信息，请查阅 [HorizontalPodAutoscaler 对象设计文档](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#horizontalpodautoscaler-v1-autoscaling)。

## kubectl 对 Horizontal Pod Autoscaler 的支持

与其他 API 资源类似，`kubectl` 以标准方式支持 HPA。 我们可以通过 `kubectl create` 命令创建一个 HPA 对象， 通过 `kubectl get hpa` 命令来获取所有 HPA 对象， 通过 `kubectl describe hpa` 命令来查看 HPA 对象的详细信息。 最后，可以使用 `kubectl delete hpa` 命令删除对象。

此外，还有个简便的命令 `kubectl autoscale` 来创建 HPA 对象。 例如，命令 `kubectl autoscale rs foo --min=2 --max=5 --cpu-percent=80` 将会为名 为 *foo* 的 ReplicationSet 创建一个 HPA 对象， 目标 CPU 使用率为 `80%`，副本数量配置为 2 到 5 之间。

## 滚动升级时扩缩

目前在 Kubernetes 中，可以针对 ReplicationController 或 Deployment 执行 滚动更新，它们会为你管理底层副本数。 Pod 水平扩缩只支持后一种：HPA 会被绑定到 Deployment 对象， HPA 设置副本数量时，Deployment 会设置底层副本数。

通过直接操控副本控制器执行滚动升级时，HPA 不能工作， 也就是说你不能将 HPA 绑定到某个 RC 再执行滚动升级。 HPA 不能工作的原因是它无法绑定到滚动更新时所新创建的副本控制器。

## 冷却/延迟支持

当使用 Horizontal Pod Autoscaler 管理一组副本扩缩时， 有可能因为指标动态的变化造成副本数量频繁的变化，有时这被称为 *抖动（Thrashing）*。

从 v1.6 版本起，集群操作员可以调节某些 `kube-controller-manager` 的全局参数来 缓解这个问题。

从 v1.12 开始，算法调整后，扩容操作时的延迟就不必设置了。

- `--horizontal-pod-autoscaler-downscale-stabilization`: `kube-controller-manager` 的这个参数表示缩容冷却时间。 即自从上次缩容执行结束后，多久可以再次执行缩容，默认时间是 5 分钟(`5m0s`)。

> **说明：** 当调整这些参数时，集群操作员需要明白其可能的影响。 如果延迟（冷却）时间设置的太长，Horizontal Pod Autoscaler 可能会不能很好的改变负载。 如果延迟（冷却）时间设置的太短，那么副本数量有可能跟以前一样出现抖动。

## 多指标支持

Kubernetes 1.6 开始支持基于多个度量值进行扩缩。 你可以使用 `autoscaling/v2beta2` API 来为 Horizontal Pod Autoscaler 指定多个指标。 Horizontal Pod Autoscaler 会根据每个指标计算，并生成一个扩缩建议。 幅度最大的扩缩建议会被采纳。

## 自定义指标支持

> **说明：** 在 Kubernetes 1.2 增加了支持基于使用特殊注解表达的、特定于具体应用的扩缩能力， 此能力处于 Alpha 阶段。 从 Kubernetes 1.6 起，由于新的 autoscaling API 的引入，这些 annotation 就被废弃了。 虽然收集自定义指标的旧方法仍然可用，Horizontal Pod Autoscaler 调度器将不会再使用这些度量值。 同时，Horizontal Pod Autoscaler 也不再使用之前用于指定用户自定义指标的注解。

自 Kubernetes 1.6 起，Horizontal Pod Autoscaler 支持使用自定义指标。 你可以使用 `autoscaling/v2beta2` API 为 Horizontal Pod Autoscaler 指定用户自定义指标。 Kubernetes 会通过用户自定义指标 API 来获取相应的指标。

关于指标 API 的要求，请参阅[对 Metrics API 的支持](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-metrics-apis)。

## 对 Metrics API 的支持

默认情况下，HorizontalPodAutoscaler 控制器会从一系列的 API 中检索度量值。 集群管理员需要确保下述条件，以保证 HPA 控制器能够访问这些 API：

- 启用了 [API 聚合层](https://kubernetes.io/zh/docs/tasks/extend-kubernetes/configure-aggregation-layer/)
- 相应的 API 已注册：
  - 对于资源指标，将使用 `metrics.k8s.io` API，一般由 [metrics-server](https://github.com/kubernetes-incubator/metrics-server) 提供。 它可以做为集群插件启动。
  - 对于自定义指标，将使用 `custom.metrics.k8s.io` API。 它由其他度量指标方案厂商的“适配器（Adapter）” API 服务器提供。 确认你的指标流水线，或者查看[已知方案列表](https://github.com/kubernetes/metrics/blob/master/IMPLEMENTATIONS.md#custom-metrics-api)。 如果你想自己编写，请从 [boilerplate](https://github.com/kubernetes-sigs/custommetrics-apiserver)开始。
  - 对于外部指标，将使用 `external.metrics.k8s.io` API。可能由上面的自定义指标适配器提供。
- `--horizontal-pod-autoscaler-use-rest-clients` 参数设置为 `true` 或者不设置。 如果设置为 false，则会切换到基于 Heapster 的自动扩缩，这个特性已经被弃用了。

关于指标来源以及其区别的更多信息，请参阅相关的设计文档， [the HPA V2](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/autoscaling/hpa-v2.md)、 [custom.metrics.k8s.io](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/custom-metrics-api.md) 和 [external.metrics.k8s.io](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/instrumentation/external-metrics-api.md)。

关于如何使用它们的示例，请参考 [使用自定义指标的教程](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics) 和[使用外部指标的教程](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-metrics-not-related-to-kubernetes-objects)。

## 支持可配置的扩缩

从 [v1.18](https://github.com/kubernetes/enhancements/blob/master/keps/sig-autoscaling/20190307-configurable-scale-velocity-for-hpa.md) 开始，`v2beta2` API 允许通过 HPA 的 `behavior` 字段配置扩缩行为。 在 `behavior` 字段中的 `scaleUp` 和 `scaleDown` 分别指定扩容和缩容行为。 可以两个方向指定一个稳定窗口，以防止扩缩目标中副本数量的波动。 类似地，指定扩缩策略可以控制扩缩时副本数的变化率。

### 扩缩策略

在 spec 字段的 `behavior` 部分可以指定一个或多个扩缩策略。 当指定多个策略时，默认选择允许更改最多的策略。 下面的例子展示了缩容时的行为:

```yaml
behavior:
  scaleDown:
    policies:
    - type: Pods
      value: 4
      periodSeconds: 60
    - type: Percent
      value: 10
      periodSeconds: 60
```

当 Pod 数量超过 40 个时，第二个策略将用于缩容。 例如，如果有 80 个副本，并且目标必须缩小到 10 个副本，那么在第一步中将减少 8 个副本。 在下一轮迭代中，当副本的数量为 72 时，10% 的 Pod 数为 7.2，但是这个数字向上取整为 8。 在 autoscaler 控制器的每个循环中，将根据当前副本的数量重新计算要更改的 Pod 数量。 当副本数量低于 40 时，应用第一个策略 *（Pods）* ，一次减少 4 个副本。

`periodSeconds` 表示策略的时间长度必须保证有效。 第一个策略允许在一分钟内最多缩小 4 个副本。 第二个策略最多允许在一分钟内缩小当前副本的 10%。

可以指定扩缩方向的 `selectPolicy` 字段来更改策略选择。 通过设置 `Min` 的值，它将选择副本数变化最小的策略。 将该值设置为 `Disabled` 将完全禁用该方向的缩放。

### 稳定窗口

当用于扩缩的指标持续抖动时，使用稳定窗口来限制副本数上下振动。 自动扩缩算法使用稳定窗口来考虑过去计算的期望状态，以防止扩缩。 在下面的例子中，稳定化窗口被指定为 `scaleDown`。

```yaml
scaleDown:
  stabilizationWindowSeconds: 300
```

当指标显示目标应该缩容时，自动扩缩算法查看之前计算的期望状态，并使用指定时间间隔内的最大值。 在上面的例子中，过去 5 分钟的所有期望状态都会被考虑。

### 默认行为

要使用自定义扩缩，不必指定所有字段。 只有需要自定义的字段才需要指定。 这些自定义值与默认值合并。 默认值与 HPA 算法中的现有行为匹配。

```yaml
behavior:
  scaleDown:
    stabilizationWindowSeconds: 300
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
  scaleUp:
    stabilizationWindowSeconds: 0
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
    - type: Pods
      value: 4
      periodSeconds: 15
    selectPolicy: Max
```

用于缩小稳定窗口的时间为 *300* 秒(或是 `--horizontal-pod-autoscaler-downscale-stabilization` 参数设定值)。 只有一种缩容的策略，允许 100% 删除当前运行的副本，这意味着扩缩目标可以缩小到允许的最小副本数。 对于扩容，没有稳定窗口。当指标显示目标应该扩容时，目标会立即扩容。 这里有两种策略，每 15 秒添加 4 个 Pod 或 100% 当前运行的副本数，直到 HPA 达到稳定状态。

### 示例：更改缩容稳定窗口

将下面的 behavior 配置添加到 HPA 中，可提供一个 1 分钟的自定义缩容稳定窗口：

```yaml
behavior:
  scaleDown:
    stabilizationWindowSeconds: 60
```

### 示例：限制缩容速率

将下面的 behavior 配置添加到 HPA 中，可限制 Pod 被 HPA 删除速率为每分钟 10%：

```yaml
behavior:
  scaleDown:
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
```

为了确保每分钟删除的 Pod 数不超过 5 个，可以添加第二个缩容策略，大小固定为 5，并将 `selectPolicy` 设置为最小值。 将 `selectPolicy` 设置为 `Min` 意味着 autoscaler 会选择影响 Pod 数量最小的策略:

```yaml
behavior:
  scaleDown:
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
    - type: Pods
      value: 5
      periodSeconds: 60
    selectPolicy: Min
```

### 示例：禁用缩容

`selectPolicy` 的值 `Disabled` 会关闭对给定方向的缩容。 因此使用以下策略，将会阻止缩容：

```yaml
behavior:
  scaleDown:
    selectPolicy: Disabled
```

## 隐式维护状态禁用

你可以在不必更改 HPA 配置的情况下隐式地为某个目标禁用 HPA。 如果此目标的期望副本个数被设置为 0，而 HPA 的最小副本个数大于 0， 则 HPA 会停止调整目标（并将其自身的 `ScalingActive` 状况设置为 `false`）， 直到你通过手动调整目标的期望副本个数或 HPA 的最小副本个数来重新激活。

## 接下来

- 设计文档：[Horizontal Pod Autoscaling](https://git.k8s.io/community/contributors/design-proposals/autoscaling/horizontal-pod-autoscaler.md)
- `kubectl autoscale` 命令：[kubectl autoscale](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#autoscale).
- 使用示例：[Horizontal Pod Autoscaler](https://kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/).