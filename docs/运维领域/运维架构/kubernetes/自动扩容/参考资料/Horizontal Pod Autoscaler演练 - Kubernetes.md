# Horizontal Pod Autoscaler演练

Horizontal Pod Autoscaler 可以根据CPU利用率自动伸缩 replication controller、deployment 或者 replica set 中的Pod数量 （也可以基于其他应用程序提供的度量指标，目前这一功能处于 beta 版本）。

本文将引导您了解如何为 php-apache 服务器配置和使用 Horizontal Pod Autoscaler。 更多 Horizontal Pod Autoscaler 的信息请参阅 [Horizontal Pod Autoscaler user guide](https://v1-16.docs.kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)。

- [准备开始](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#准备开始)
- [第一步：运行 php-apache 服务器并暴露服务](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#第一步-运行-php-apache-服务器并暴露服务)
- [创建 Horizontal Pod Autoscaler](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#创建-horizontal-pod-autoscaler)
- [增加负载](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#增加负载)
- [停止负载](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#停止负载)
- [基于多项度量指标和自定义度量指标自动伸缩](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#基于多项度量指标和自定义度量指标自动伸缩)
- [附录：Horizontal Pod Autoscaler状态条件](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#附录-horizontal-pod-autoscaler状态条件)
- [附录：Quantities](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#附录-quantities)
- [附录：其他可能的情况](https://v1-16.docs.kubernetes.io/zh/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#附录-其他可能的情况)

## 准备开始

本文示例需要一个1.2或者更高版本的可运行的 Kubernetes 集群以及 kubectl。 [metrics-server](https://github.com/kubernetes-incubator/metrics-server/) 也需要部署到集群中， 它可以通过 resource metrics API 对外提供度量数据，Horizontal Pod Autoscaler 正是根据此 API 来获取度量数据，部署方法请参考 [metrics-server](https://github.com/kubernetes-incubator/metrics-server/) 。 如果你正在使用GCE，按照 [getting started on GCE guide](https://v1-16.docs.kubernetes.io/docs/setup/production-environment/turnkey/gce/) 操作，metrics-server 会默认启动。

如果需要为 Horizontal Pod Autoscaler 指定多种资源度量指标，您的 Kubernetes 集群以及 kubectl 至少需要达到1.6版本。 此外，如果要使用自定义度量指标，您的Kubernetes 集群还必须能够与提供这些自定义指标的API服务器通信。 最后，如果要使用与 Kubernetes 对象无关的度量指标，则 Kubernetes 集群版本至少需要达到1.10版本，同样，需要保证集群能够与提供这些外部指标的API服务器通信。 更多详细信息，请参阅[Horizontal Pod Autoscaler user guide](https://v1-16.docs.kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-custom-metrics)。

## 第一步：运行 php-apache 服务器并暴露服务

为了演示 Horizontal Pod Autoscaler，我们将使用一个基于 php-apache 镜像的定制 Docker 镜像。 Dockerfile 内容如下：

```
FROM php:5-apache
ADD index.php /var/www/html/index.php
RUN chmod a+rx index.php
```

它定义一个 index.php 页面来执行一些 CPU 密集型计算：

```
<?php
  $x = 0.0001;
  for ($i = 0; $i <= 1000000; $i++) {
    $x += sqrt($x);
  }
  echo "OK!";
?>
```

首先，我们先启动一个 deployment 来运行这个镜像并暴露一个服务:

```shell
kubectl run php-apache --image=k8s.gcr.io/hpa-example --requests=cpu=200m --expose --port=80
service/php-apache created
deployment.apps/php-apache created
```

## 创建 Horizontal Pod Autoscaler

现在，php-apache服务器已经运行，我们将通过 [kubectl autoscale](https://v1-16.docs.kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale) 命令创建 Horizontal Pod Autoscaler。 以下命令将创建一个 Horizontal Pod Autoscaler 用于控制我们上一步骤中创建的 deployment，使 Pod 的副本数量在维持在1到10之间。 大致来说，HPA 将通过增加或者减少 Pod 副本的数量（通过 Deployment ）以保持所有 Pod 的平均CPU利用率在50%以内 （由于每个 Pod 通过 [kubectl run](https://github.com/kubernetes/kubernetes/blob/v1.16.15/docs/user-guide/kubectl/kubectl_run.md) 申请了200 milli-cores CPU，所以50%的 CPU 利用率意味着平均 CPU 利用率为100 milli-cores）。 相关算法的详情请参阅[here](https://git.k8s.io/community/contributors/design-proposals/autoscaling/horizontal-pod-autoscaler.md#autoscaling-algorithm)。

```shell
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
horizontalpodautoscaler.autoscaling/php-apache autoscaled
```

我们可以通过以下命令查看 autoscaler 的状态：

```shell
kubectl get hpa
NAME         REFERENCE                     TARGET    MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   0% / 50%  1         10        1          18s
```

请注意在上面的命令输出中，当前的CPU利用率是0%，这是由于我们尚未发送任何请求到服务器 （`CURRENT` 列显示了相应 deployment 所控制的所有 Pod 的平均 CPU 利用率）。

## 增加负载

现在，我们将看到 autoscaler 如何对增加负载作出反应。 我们将启动一个容器，并通过一个循环向 php-apache 服务器发送无限的查询请求（请在另一个终端中运行以下命令）：

```shell
kubectl run -i --tty load-generator --image=busybox /bin/sh

Hit enter for command prompt

while true; do wget -q -O- http://php-apache.default.svc.cluster.local; done
```

在几分钟时间内，通过以下命令，我们可以看到CPU负载升高了：

```shell
kubectl get hpa
NAME         REFERENCE                     TARGET      CURRENT   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   305% / 50%  305%      1         10        1          3m
```

这时，由于请求增多，CPU利用率已经升至305%。 可以看到，deployment 的副本数量已经增长到了7：

```shell
kubectl get deployment php-apache
NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
php-apache   7         7         7            7           19m
```

> **注意：** 有时最终副本的数量可能需要几分钟才能稳定下来。 由于环境的差异，不同环境中最终的副本数量可能与本示例中的数量不同。

## 停止负载

我们将通过停止负载来结束我们的示例。

在我们创建 busybox 容器的终端中，输入`<Ctrl> + C`来终止负载的产生。

然后我们可以再次查看负载状态（等待几分钟时间）：

```shell
kubectl get hpa
NAME         REFERENCE                     TARGET       MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   0% / 50%     1         10        1          11m
kubectl get deployment php-apache
NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
php-apache   1         1         1            1           27m
```

这时，CPU利用率已经降到0，所以 HPA 将自动缩减副本数量至1。

> **注意：** 自动伸缩完成副本数量的改变可能需要几分钟的时间。

## 基于多项度量指标和自定义度量指标自动伸缩

利用`autoscaling/v2beta2`API版本，您可以在自动伸缩 php-apache 这个 Deployment 时引入其他度量指标。

首先，获取`autoscaling/v2beta2`格式的 HorizontalPodAutoscaler 的YAML文件：

```shell
kubectl get hpa.v2beta2.autoscaling -o yaml > /tmp/hpa-v2.yaml
```

在编辑器中打开`/tmp/hpa-v2.yaml`：

```yaml
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
status:
  observedGeneration: 1
  lastScaleTime: <some-time>
  currentReplicas: 1
  desiredReplicas: 1
  currentMetrics:
  - type: Resource
    resource:
      name: cpu
      current:
        averageUtilization: 0
        averageValue: 0
```

需要注意的是，`targetCPUUtilizationPercentage` 字段已经被名为 `metrics` 的数组所取代。 CPU利用率这个度量指标是一个*resource metric*(资源度量指标)，因为它表示容器上指定资源的百分比。 除CPU外，您还可以指定其他资源度量指标。默认情况下，目前唯一支持的其他资源度量指标为内存。 只要`metrics.k8s.io` API存在，这些资源度量指标就是可用的，并且他们不会在不同的Kubernetes集群中改变名称。

您还可以指定资源度量指标使用绝对数值，而不是百分比，你需要将`target`类型`AverageUtilization`替换成`AverageValue`，同时 将`target.averageUtilization`替换成`target.averageValue`并设定相应的值。

还有两种其他类型的度量指标，他们被认为是*custom metrics*（自定义度量指标）： 即 Pod 度量指标和对象度量指标（pod metrics and object metrics）。 这些度量指标可能具有特定于集群的名称，并且需要更高级的集群监控设置。

第一种可选的度量指标类型是 Pod 度量指标。这些指标从某一方面描述了Pod，在不同Pod之间进行平均，并通过与一个目标值比对来确定副本的数量。 它们的工作方式与资源度量指标非常相像，差别是它们仅支持`target` 类型为`AverageValue`。

Pod 度量指标通过如下代码块定义：

```yaml
type: Pods
pods:
  metric:
    name: packets-per-second
  target:
    type: AverageValue
    averageValue: 1k
```

第二种可选的度量指标类型是对象度量指标。相对于描述 Pod，这些度量指标用于描述一个在相同名字空间(namespace)中的其他对象。 请注意这些度量指标用于描述这些对象，并非从对象中获取。 对象度量指标支持的`target`类型包括`Value`和`AverageValue`。如果是`Value`类型，target值将直接与API返回的度量指标比较， 而`AverageValue`类型，API返回的度量指标将按照 Pod 数量拆分，然后再与target值比较。 下面的 YAML 文件展示了一个表示`requests-per-second`的度量指标。

```yaml
type: Object
object:
  metric:
    name: requests-per-second
  describedObject:
    apiVersion: networking.k8s.io/v1beta1
    kind: Ingress
    name: main-route
  target:
    type: Value
    value: 2k
```

如果您指定了多个上述类型的度量指标，HorizontalPodAutoscaler 将会依次考量各个指标。 HorizontalPodAutoscaler 将会计算每一个指标所提议的副本数量，然后最终选择一个最高值。

比如，如果您的监控系统能够提供网络流量数据，您可以通过`kubectl edit`命令将上述 Horizontal Pod Autoscaler 的定义更改为：

```yaml
apiVersion: autoscaling/v2beta1
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: AverageUtilization
        averageUtilization: 50
  - type: Pods
    pods:
      metric:
        name: packets-per-second
      targetAverageValue: 1k
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1beta1
        kind: Ingress
        name: main-route
      target:
        kind: Value
        value: 10k
status:
  observedGeneration: 1
  lastScaleTime: <some-time>
  currentReplicas: 1
  desiredReplicas: 1
  currentMetrics:
  - type: Resource
    resource:
      name: cpu
    current:
      averageUtilization: 0
      averageValue: 0
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1beta1
        kind: Ingress
        name: main-route
      current:
        value: 10k
```

然后，您的 HorizontalPodAutoscaler 将会尝试确保每个Pod的CPU利用率在50%以内，每秒能够服务1000个数据包请求， 并确保所有在Ingress后的Pod每秒能够服务的请求总数达到10000个。

### 多个度量指标下伸缩

许多度量管道允许您通过名称或附加的_labels_来描述度量指标。对于所有非资源类型度量指标(pod、object和后面将介绍的external)， ，可以额外指定一个标签选择器。例如，如果你希望收集包含`verb`标签的`http_requests`度量指标， 你可以在 GET 请求中指定需要的度量指标，如下所示：

```yaml
type: Object
object:
  metric:
    name: `http_requests`
    selector: `verb=GET`
```

这个选择器使用与 Kubernetes 标签选择器相同的语法。 如果名称和标签选择器匹配到多个系列，监测管道会决定如何将多个系列合并成单个值。 选择器是附加的，它不会选择目标以外的对象（类型为`Pods`的目标和类型为`Object`的目标）。

### 基于Kubernetes以外的度量指标伸缩

运行在 Kubernetes 上的应用程序可能需要基于与 Kubernetes 集群中的任何对象没有明显关系的度量指标进行自动伸缩， 例如那些描述不在 Kubernetes 任何 namespaces 服务的度量指标。

使用外部的度量指标，需要了解你使用的监控系统，相关的设置与使用自定义试题指标类似。 External metrics 可以使用你的监控系统的任何指标来自动伸缩你的集群。你只需要在`metric`块中提供`name` 和 `selector`，同时将类型由`Object`改为`External`。 如果`metricSelector`匹配到多个度量指标，HorizontalPodAutoscaler 将会把它们加和。 External metrics 同时支持`Value`和`AverageValue`类型，这与`Object`类型的度量指标相同。

例如，如果你的应用程序处理主机上的消息队列， 为了让每30个任务有1个worker，你可以将下面的内容添加到 HorizontalPodAutoscaler 的配置中。

```yaml
- type: External
  external:
    metric:
      name: queue_messages_ready
      selector: "queue=worker_tasks"
    target:
      type: AverageValue
      averageValue: 30
```

如果可能，还是推荐 custom metric 而不是 external metrics，因为这便于让系统管理员加固 custom metrics API。 而 external metrics API 可以允许访问所有的度量指标，当暴露这些服务时，系统管理员需要仔细考虑这个问题。

## 附录：Horizontal Pod Autoscaler状态条件

当使用`autoscaling/v2beta2`格式的 HorizontalPodAutoscaler 时，您将可以看到 Kubernetes 为 HorizongtalPodAutoscaler 设置的状态条件（status conditions）。 这些状态条件可以显示当前 HorizontalPodAutoscaler 是否能够执行伸缩以及是否受到一定的限制。

`status.conditions`字段展示了这些状态条件。 可以通过`kubectl describe hpa`命令查看当前影响 HorizontalPodAutoscaler 的各种状态条件信息：

```shell
kubectl describe hpa cm-test
Name:                           cm-test
Namespace:                      prom
Labels:                         <none>
Annotations:                    <none>
CreationTimestamp:              Fri, 16 Jun 2017 18:09:22 +0000
Reference:                      ReplicationController/cm-test
Metrics:                        ( current / target )
  "http_requests" on pods:      66m / 500m
Min replicas:                   1
Max replicas:                   4
ReplicationController pods:     1 current / 1 desired
Conditions:
  Type                  Status  Reason                  Message
  ----                  ------  ------                  -------
  AbleToScale           True    ReadyForNewScale        the last scale time was sufficiently old as to warrant a new scale
  ScalingActive         True    ValidMetricFound        the HPA was able to successfully calculate a replica count from pods metric http_requests
  ScalingLimited        False   DesiredWithinRange      the desired replica count is within the acceptable range
Events:
```

对于上面展示的这个 HorizontalPodAutoscaler，我们可以看出有若干状态条件处于健康状态。 首先，`AbleToScale` 表明 HPA 是否可以获取和更新伸缩信息，以及是否存在阻止伸缩的各种回退条件。 其次，`ScalingActive` 表明HPA是否被启用（即目标的副本数量不为零） 以及是否能够完成伸缩计算。 当这一状态为 `False` 时，通常表明获取度量指标存在问题。 最后一个条件 `ScalingLimitted` 表明所需伸缩的值被 HorizontalPodAutoscaler 所定义的最大或者最小值所限制（即已经达到最大或者最小伸缩值）。 这通常表明您可能需要调整 HorizontalPodAutoscaler 所定义的最大或者最小副本数量的限制了。

## 附录：Quantities

HorizontalPodAutoscaler 和 metrics api 中的所有的度量指标使用 Kubernetes 中称为 *quantity* （）殊整数表示。 例如，数量`10500m`用十进制表示为`10.5`。 如果可能的话，metrics api 将返回没有后缀的整数，否则返回以千分单位的数量。 这意味着您可能会看到您的度量指标在`1`和`1500m`之间波动，或者在十进制记数法中的`1`和`1.5`。 更多信息，请参阅[度量术语](https://v1-16.docs.kubernetes.io/docs/reference/glossary?core-object=true#term-quantity)

## 附录：其他可能的情况

### 使用YAML文件创建 autoscaler

除了使用 `kubectl autoscale` 命令，也可以文件创建 HorizontalPodAutoscaler ：

| [`application/hpa/php-apache.yaml` ](https://raw.githubusercontent.com/kubernetes/website/master/content/zh/examples/application/hpa/php-apache.yaml)![Copy application/hpa/php-apache.yaml to clipboard](Horizontal Pod Autoscaler演练 - Kubernetes.assets/copycode.svg) |
| ------------------------------------------------------------ |
| `apiVersion: autoscaling/v1 kind: HorizontalPodAutoscaler metadata:  name: php-apache  namespace: default spec:  scaleTargetRef:    apiVersion: apps/v1    kind: Deployment    name: php-apache  minReplicas: 1  maxReplicas: 10  targetCPUUtilizationPercentage: 50 ` |

使用如下命令创建 autoscaler：

```shell
kubectl create -f https://k8s.io/examples/application/hpa/php-apache.yaml
horizontalpodautoscaler.autoscaling/php-apache created
```