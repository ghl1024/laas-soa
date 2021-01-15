[XniLe](https://blog.dianduidian.com/)

[首页](https://blog.dianduidian.com/)[归档](https://blog.dianduidian.com/post/)[标签](https://blog.dianduidian.com/tags/)[分类](https://blog.dianduidian.com/categories/)[About](https://blog.dianduidian.com/about/)

# Kubernetes Deployment滚动更新原理解析

2020-04-07 

[ kubernetes](https://blog.dianduidian.com/categories/kubernetes/)

## 文章目录

[控制器相关的配置项](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#控制器相关的配置项)[Watch GVK](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#watch-gvk)[Event Handler](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#event-handler)[Run函数](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#run函数)[核心逻辑syncDeployment](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#核心逻辑syncdeployment)[Rolling Update](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#rolling-update)[Scale up的逻辑](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#scale-up的逻辑)[Scale down的逻辑](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#scale-down的逻辑)[Deployment 删除](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#deployment-删除)[同一个Deployment先后触发滚动更新会如何处理？](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#同一个deployment先后触发滚动更新会如何处理)[pause和resume](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#pause和resume)[minReadySeconds的作用](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#minreadyseconds的作用)[Scale down过程中被kill Pod的优先级](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#scale-down过程中被kill-pod的优先级)[调试](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#调试)[总结](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#总结)[参考](https://blog.dianduidian.com/post/kubernetes-deployment滚动更新原理分析/#参考)

> 分析基于kubernetes-1.15.5源码。

`Deployment`是新一代用于`Pod`管理的对象，除了继承了`Replication`的全部功能外，还在此基础上提供了更加完善的功能，特别是提供了滚动更新的功能，这对服务平滑升级简直太友好了。关于`Rolling Update`它有几个重要的参数用来控制滚动更新的动作：

- `.spec.minReadySeconds`
- `.spec.strategy.rollingUpdate.maxSurge`
- `.spec.strategy.rollingUpdate.maxUnavailable`

为了更好的理解这几个参数的作用，有必要深入分析一下`Deployment Controller`的处理逻辑。

## 控制器相关的配置项

- `--concurrent-deployment-syncs` int32 Default: 5 The number of deployment objects that are allowed to sync concurrently. Larger number = more responsive deployments, but more CPU (and network) load
- `--deployment-controller-sync-period` duration Default: 30s Period for syncing the deployments.

## Watch GVK

| ` 1 2 3 4 5 6 7 8 9 10 ` | `func startDeploymentController(ctx ControllerContext) (http.Handler, bool, error) { // ... dc, err := deployment.NewDeploymentController( 	ctx.InformerFactory.Apps().V1().Deployments(), 	ctx.InformerFactory.Apps().V1().ReplicaSets(), 	ctx.InformerFactory.Core().V1().Pods(), 	ctx.ClientBuilder.ClientOrDie("deployment-controller"), ) // ... }` |
| ------------------------ | ------------------------------------------------------------ |
|                          |                                                              |

- Apps/V1/Deployments
- Apps.V1.ReplicaSets
- Core.V1.Pods。

## Event Handler

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ` | `// NewDeploymentController creates a new DeploymentController. func NewDeploymentController(dInformer appsinformers.DeploymentInformer, rsInformer appsinformers.ReplicaSetInformer, podInformer coreinformers.PodInformer, client clientset.Interface) (*DeploymentController, error) {    //...     dInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{        AddFunc:    dc.addDeployment,        UpdateFunc: dc.updateDeployment,        // This will enter the sync loop and no-op, because the deployment has been deleted from the store.        DeleteFunc: dc.deleteDeployment,    })    rsInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{        AddFunc:    dc.addReplicaSet,        UpdateFunc: dc.updateReplicaSet,        DeleteFunc: dc.deleteReplicaSet,    })    podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{        DeleteFunc: dc.deletePod,    })        // ... }` |
| --------------------------------------------------------- | ------------------------------------------------------------ |
|                                                           |                                                              |

## Run函数

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ` | `// Run begins watching and syncing. func (dc *DeploymentController) Run(workers int, stopCh <-chan struct{}) { 	// ... 	// @xnile 等待informer cache同步完成 if !controller.WaitForCacheSync("deployment", stopCh, dc.dListerSynced, dc.rsListerSynced, dc.podListerSynced) { 	return } 	for i := 0; i < workers; i++ { 	go wait.Until(dc.worker, time.Second, stopCh) } 	<-stopCh }` |
| ------------------------------------------ | ------------------------------------------------------------ |
|                                            |                                                              |

- 等待本地`Informer cache`同步完成
- 开启workers(workers由`--concurrent-deployment-syncs`参数指定，默认为5)个协程从任务队列中消费任务然后交给`syncHandler`处理，`syncHandler`的逻辑在`syncDeployment`函数,`Deployment Controller`的关键函数。

## 核心逻辑syncDeployment

`Deployment Controller`核心逻辑`syncDeployment`函数

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 ` | `func (dc *DeploymentController) syncDeployment(key string) error {        // ... 省略     //@xnile 从informer cache中获取deployment对象    deployment, err := dc.dLister.Deployments(namespace).Get(name)     // ...省略     // Deep-copy otherwise we are mutating our cache.    // TODO: Deep-copy only when needed.    // @xnile Deep-copy 每一次syncloop独立,每个goroutine独立    d := deployment.DeepCopy()     // @xnile 获取deployment管理的rs    rsList, err := dc.getReplicaSetsForDeployment(d)    if err != nil {        return err    }     // ... 省略     // @xnile 判断deployment是否已经被删除，只有当删除策略为“Foreground”时才会出现    if d.DeletionTimestamp != nil {        return dc.syncStatusOnly(d, rsList)        // @xnile 后续GC Controller会负责清理rs、pods    }     // @xnile 是否处于暂停状态,更新Conditions,目的是在暂停的这段时间内不记时，防止触发spec.progressDeadlineSeconds,    if err = dc.checkPausedConditions(d); err != nil {        return err    }    if d.Spec.Paused {        return dc.sync(d, rsList)    }     // @xnile 通过检测 .spec.rollbackTo 信息判断是否需要回退    // @xnile 通过yaml文件指定或使用kubectl rollout undo命令    if getRollbackTo(d) != nil {        return dc.rollback(d, rsList)    }     // @xnile 是否需要scale    // @xnile 如果更新的同时并修改了replicas,先scale完了再Rolling Update    scalingEvent, err := dc.isScalingEvent(d, rsList)    if err != nil {        return err    }    if scalingEvent {        return dc.sync(d, rsList)    }     // @xnile 更新    switch d.Spec.Strategy.Type {    case apps.RecreateDeploymentStrategyType:        return dc.rolloutRecreate(d, rsList, podMap)    case apps.RollingUpdateDeploymentStrategyType:        // @xnile 滚动更新        return dc.rolloutRolling(d, rsList)    }    return fmt.Errorf("unexpected deployment strategy type: %s", d.Spec.Strategy.Type) }` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

- 从`Informer cache`中获取`deployment`对象
- 获取`deployment`关联的`rs`
- 判断`deployment`是否已经被删除，只有当删除策略为`Foreground`时才会出现
- 判断是否处于暂停状态，更新`Conditions`,目的是在暂停的这段时间内不记时，防止触发`spec.progressDeadlineSeconds`,
- 通过检测 `.spec.rollbackTo` 信息判断是否需要回退
- 判断是否需要`scale`，如果更新的同时并修改了`replicas`,先`scale`完了再更新。
- 更新。根据`.spec.strategy.type`指定的更新策略选择不同的处理逻辑。

## Rolling Update

**`Deployment`滚动更新是靠新旧`rs`交接棒完成的，更新过程分成两步：`Scale up`和`Scale down`。**

- **`Scale up`负责将新`rs`的`replicas`朝着`deployment.Spec.Replicas`指定的数据递加。**
- **`Scale down`负责将旧的`replicas`朝着0的目标递减。**

**一次完整的滚动更新需要经过很多轮`Scale up`和`Scale down`的过程，这对理解`pause`和`resume`很重要。**

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ` | `//@ xnile 一次完整的滚动更新需要执行多次 rolloutRolling func (dc *DeploymentController) rolloutRolling(d *apps.Deployment, rsList []*apps.ReplicaSet) error { // @xnile 获取新旧rs，如果是首次rolling out因为new rs还不存在则会创建new rs newRS, oldRSs, err := dc.getAllReplicaSetsAndSyncRevision(d, rsList, true) if err != nil { 	return err } allRSs := append(oldRSs, newRS) 	// Scale up, if we can. scaledUp, err := dc.reconcileNewReplicaSet(allRSs, newRS, d) if err != nil { 	return err } if scaledUp { 	// Update DeploymentStatus 	return dc.syncRolloutStatus(allRSs, newRS, d) } 	// Scale down, if we can. scaledDown, err := dc.reconcileOldReplicaSets(allRSs, controller.FilterActiveReplicaSets(oldRSs), newRS, d) if err != nil { 	return err } if scaledDown { 	// Update DeploymentStatus 	return dc.syncRolloutStatus(allRSs, newRS, d) } 	// @xnile 更新已完成 // @xnile TODO 为什么还要先判断是否已经完成？不scale up也不scale down的情况是？ if deploymentutil.DeploymentComplete(d, &d.Status) { 	// @xnile 清理历史rs, 最多只保留最 d.Spec.RevisionHistoryLimit 个历史版本 	if err := dc.cleanupDeployment(oldRSs, d); err != nil { 		return err 	} } 	// Sync deployment status return dc.syncRolloutStatus(allRSs, newRS, d) }` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

- 获取新旧`rs`，如果是首次滚动更新因为`New rs`还不存在则会创建`New rs`

- 调用`dc.reconcileNewReplicaSet`方法判断是否能`Scale up`

- 调用`dc.reconcileOldReplicaSets`方法判断是否能`Scale down`

- 如果更新已经完成则清理历史`rs`,最多只保留`.spec.RevisionHistoryLimit`个历史版本

- 更新`deployment`状态，通过`kubectl describe`可以看到下面信息

  | `1 2 3 4 5 6 7 ` | `Events: Type    Reason             Age                  From                   Message ----    ------             ----                 ----                   ------- Normal  ScalingReplicaSet  61s (x2 over 8h)     deployment-controller  Scaled up replica set my-nginx-79cb8c4647 to 1 Normal  ScalingReplicaSet  49s (x2 over 8h)     deployment-controller  Scaled up replica set my-nginx-79cb8c4647 to 2 Normal  ScalingReplicaSet  49s                  deployment-controller  Scaled down replica set my-nginx-9f4d8c9d5 to 3 Normal  ScalingReplicaSet  37s (x2 over 8h)     deployment-controller  Scaled up ` |
  | ---------------- | ------------------------------------------------------------ |
  |                  |                                                              |

### Scale up的逻辑

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ` | `func (dc *DeploymentController) reconcileNewReplicaSet(allRSs []*apps.ReplicaSet, newRS *apps.ReplicaSet, deployment *apps.Deployment) (bool, error) { if *(newRS.Spec.Replicas) == *(deployment.Spec.Replicas) { 	// Scaling not required. 	return false, nil } // @xnile TODO 什么情况下会出现? if *(newRS.Spec.Replicas) > *(deployment.Spec.Replicas) { 	// Scale down. 	scaled, _, err := dc.scaleReplicaSetAndRecordEvent(newRS, *(deployment.Spec.Replicas), deployment) 	return scaled, err } // @xnile 获取能scale up的数量 newReplicasCount, err := deploymentutil.NewRSNewReplicas(deployment, allRSs, newRS) if err != nil { 	return false, err } // @xnile 调用api更新rs的replicas,然后rs controller会负责pod的创建 scaled, _, err := dc.scaleReplicaSetAndRecordEvent(newRS, newReplicasCount, deployment) return scaled, err }` |
| ------------------------------------------------------ | ------------------------------------------------------------ |
|                                                        |                                                              |

- 判断是否能`Scale up`
- 判断是否需要先`Scale down`（什么情况会出现？）。
- 调用`deploymentutil.NewRSNewReplicas`获取能`Scale up`的数量
- 调用api更新`rs`的`replicas`,然后`rs controller`会负责`pod`的创建

继续来看下`deploymentutil.NewRSNewReplicas`方法，`.spec.strategy.rollingUpdate.maxSurge`参数的作用也就在于此。

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ` | `func NewRSNewReplicas(deployment *apps.Deployment, allRSs []*apps.ReplicaSet, newRS *apps.ReplicaSet) (int32, error) { switch deployment.Spec.Strategy.Type { case apps.RollingUpdateDeploymentStrategyType: 	// Check if we can scale up. 	maxSurge, err := intstrutil.GetValueFromIntOrPercent(deployment.Spec.Strategy.RollingUpdate.MaxSurge, int(*(deployment.Spec.Replicas)), true) 	if err != nil { 		return 0, err 	} 	// Find the total number of pods 	currentPodCount := GetReplicaCountForReplicaSets(allRSs) 	maxTotalPods := *(deployment.Spec.Replicas) + int32(maxSurge) 	if currentPodCount >= maxTotalPods { 		// Cannot scale up. 		return *(newRS.Spec.Replicas), nil 	} 	// Scale up. 	scaleUpCount := maxTotalPods - currentPodCount 	// Do not exceed the number of desired replicas. 	scaleUpCount = int32(integer.IntMin(int(scaleUpCount), int(*(deployment.Spec.Replicas)-*(newRS.Spec.Replicas)))) 	return *(newRS.Spec.Replicas) + scaleUpCount, nil case apps.RecreateDeploymentStrategyType: 	return *(deployment.Spec.Replicas), nil default: 	return 0, fmt.Errorf("deployment type %v isn't supported", deployment.Spec.Strategy.Type) } }` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

函数逻辑比较简单，从中我们能看出的`.spec.strategy.rollingUpdate.maxSurge`的作用:

> 在scale up的时候所有pod不能超过`deployment.Spec.Replicas`+`.spec.strategy.rollingUpdate.maxSurge`相加之和，`.spec.strategy.rollingUpdate.maxSurge`可以是整数或百分比，是百分比时需要向上取整(如0.1就限1)。

### Scale down的逻辑

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ` | `func (dc *DeploymentController) reconcileOldReplicaSets(allRSs []*apps.ReplicaSet, oldRSs []*apps.ReplicaSet, newRS *apps.ReplicaSet, deployment *apps.Deployment) (bool, error) {    oldPodsCount := deploymentutil.GetReplicaCountForReplicaSets(oldRSs)    if oldPodsCount == 0 {        // Can't scale down further        return false, nil    }     allPodsCount := deploymentutil.GetReplicaCountForReplicaSets(allRSs)    klog.V(4).Infof("New replica set %s/%s has %d available pods.", newRS.Namespace, newRS.Name, newRS.Status.AvailableReplicas)    maxUnavailable := deploymentutil.MaxUnavailable(*deployment)     minAvailable := *(deployment.Spec.Replicas) - maxUnavailable    newRSUnavailablePodCount := *(newRS.Spec.Replicas) - newRS.Status.AvailableReplicas    // @xnile 这里为什么不用readyPodCount - minAvailable    // @xnile allPodsCount、minAvailable 两值都是静态的，但newRSUnavailablePodCount是动态的。    // @xnile 考虑一种情况，滚动更新后新创建的Pod因为某种原因一直不能ready。这时不能再scale down，这时我查找到原因了修复了，再滚动一次，发现readyPodCount - minAvailable=0 会卡住    maxScaledDown := allPodsCount - minAvailable - newRSUnavailablePodCount    if maxScaledDown <= 0 {        return false, nil    }     // Clean up unhealthy replicas first, otherwise unhealthy replicas will block deployment    // and cause timeout. See https://github.com/kubernetes/kubernetes/issues/16737    oldRSs, cleanupCount, err := dc.cleanupUnhealthyReplicas(oldRSs, deployment, maxScaledDown)    if err != nil {        return false, nil    }    klog.V(4).Infof("Cleaned up unhealthy replicas from old RSes by %d", cleanupCount)     // Scale down old replica sets, need check maxUnavailable to ensure we can scale down    allRSs = append(oldRSs, newRS)    scaledDownCount, err := dc.scaleDownOldReplicaSetsForRollingUpdate(allRSs, oldRSs, deployment)    if err != nil {        return false, nil    }    klog.V(4).Infof("Scaled down old RSes of deployment %s by %d", deployment.Name, scaledDownCount)     totalScaledDown := cleanupCount + scaledDownCount    return totalScaledDown > 0, nil }` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

其中`minAvailable := *(deployment.Spec.Replicas) - maxUnavailable` 一句比较关键，

> 在scale down的过程中必须保证当前可用pod不能少于`deployment.Spec.Replicas` - `.spec.strategy.rollingUpdate.maxUnavailable`。`.spec.strategy.rollingUpdate.maxUnavailable`可以是整数或百分比，如果百分比就向下取整（如1.7就是1）

**PS：这里一开始我在看源码时对`maxScaledDown := allPodsCount - minAvailable - newRSUnavailablePodCount`这行代码有个疑问，为什么不直接用`readyPodCount - minAvailable`计算出能scale down的pod数量呢？后来根据这个[Issue](https://github.com/kubernetes/kubernetes/issues/16737)，发现在之前确实使用过`totalScaleDownCount := readyPodCount - minAvailable`，也因此引入了一个Bug，如果新起的pod因为某种原因一直不能ready,会卡住后续的更新，想回滚也不行，想了解细节的同学可以看下那个Issue。**

## Deployment 删除

从源码中我们可以看到`Deployment Controller`中没有`deployment`的删除逻辑，其实`deployment`的删除及关联的`rs`、`Pod`的删除是在`GC Controller`中处理的，以后有机会再分析下`GC Controller`的逻辑。

## 同一个Deployment先后触发滚动更新会如何处理？

如果上一次滚动更新还未完成马上接着又对此`deployment`执行了一次滚动更新，控制器又会如何处理呢？`Scale up`的流程参加上边分析的过程会创建`New rs`，但`Scale down`会如何处理呢，是`Scale down`上一次滚动更新刚创建的`rs`还是更老的`rs`的呢?

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ` | `func (dc *DeploymentController) scaleDownOldReplicaSetsForRollingUpdate(allRSs []*apps.ReplicaSet, oldRSs []*apps.ReplicaSet, deployment *apps.Deployment) (int32, error) { maxUnavailable := deploymentutil.MaxUnavailable(*deployment) 	//... 	// @xnile 根据创建时间排序，即先Scale down最早创建的rs sort.Sort(controller.ReplicaSetsByCreationTimestamp(oldRSs)) 	totalScaledDown := int32(0) totalScaleDownCount := availablePodCount - minAvailable for _, targetRS := range oldRSs { 	//... } 	return totalScaledDown, nil }` |
| ------------------------------------------ | ------------------------------------------------------------ |
|                                            |                                                              |

答案是先`scale down`最老的`rs`，然后再`Scale down`上次更新时创建的`rs`.

## pause和resume

如果`deployment`还在滚动更新中我们执行了`kubectl rollout pause` 命令，控制器又会如何处理?

在`Rolling Update`章节我们已经提到过一次完成的滚动更新需要经过多轮`Scale up`和`Scale down`的过程，当执行暂停操作只会影响下一轮的`Scale up`或`Scale down`而不会影响本轮的操作。是不是也侧面说明了`kubernetes`操作都是声明式的而非命令式的。

## minReadySeconds的作用

`.spec.minReadySeconds`的作用是在Scale up的过程中新创建的pod在本身ready的基础上会再等上minReadySeconds才会认为pod已经是可用状态，然后才会接着开始scale down，相当于一个观察期的作用，防止新起的pod发生crash，进而影响服务的可用性，保证集群在更新过程的稳定性。

在测试过程中可以适当增加这个值，人为减慢滚动更新的进度，方便我们使用`kubectl get rs -w`观察滚动更新的过程。

## Scale down过程中被kill Pod的优先级

在滚动更新`Scale down`阶段需要杀掉老的`pod`,这些需要被杀掉的`pod`是如何被筛选出来的呢？

| ` 1 2 3 4 5 6 7 8 9 10 11 12 ` | `func getPodsToDelete(filteredPods []*v1.Pod, diff int) []*v1.Pod { // No need to sort pods if we are about to delete all of them. // diff will always be <= len(filteredPods), so not need to handle > case. if diff < len(filteredPods) { 	// Sort the pods in the order such that not-ready < ready, unscheduled 	// < scheduled, and pending < running. This ensures that we delete pods 	// in the earlier stages whenever possible. 	// @xnile 尽可能删除较早的pod 	sort.Sort(controller.ActivePods(filteredPods)) } return filteredPods[:diff] }` |
| ------------------------------ | ------------------------------------------------------------ |
|                                |                                                              |

| ` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ` | `func (s ActivePods) Less(i, j int) bool { // 1. Unassigned < assigned // If only one of the pods is unassigned, the unassigned one is smaller if s[i].Spec.NodeName != s[j].Spec.NodeName && (len(s[i].Spec.NodeName) == 0 || len(s[j].Spec.NodeName) == 0) { 	return len(s[i].Spec.NodeName) == 0 } // 2. PodPending < PodUnknown < PodRunning m := map[v1.PodPhase]int{v1.PodPending: 0, v1.PodUnknown: 1, v1.PodRunning: 2} if m[s[i].Status.Phase] != m[s[j].Status.Phase] { 	return m[s[i].Status.Phase] < m[s[j].Status.Phase] } // 3. Not ready < ready // If only one of the pods is not ready, the not ready one is smaller if podutil.IsPodReady(s[i]) != podutil.IsPodReady(s[j]) { 	return !podutil.IsPodReady(s[i]) } // TODO: take availability into account when we push minReadySeconds information from deployment into pods, //       see https://github.com/kubernetes/kubernetes/issues/22065 // 4. Been ready for empty time < less time < more time // If both pods are ready, the latest ready one is smaller if podutil.IsPodReady(s[i]) && podutil.IsPodReady(s[j]) && !podReadyTime(s[i]).Equal(podReadyTime(s[j])) { 	return afterOrZero(podReadyTime(s[i]), podReadyTime(s[j])) } // 5. Pods with containers with higher restart counts < lower restart counts if maxContainerRestarts(s[i]) != maxContainerRestarts(s[j]) { 	return maxContainerRestarts(s[i]) > maxContainerRestarts(s[j]) } // 6. Empty creation time pods < newer pods < older pods if !s[i].CreationTimestamp.Equal(&s[j].CreationTimestamp) { 	return afterOrZero(&s[i].CreationTimestamp, &s[j].CreationTimestamp) } return false }` |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

注释已经解释的比较清楚了，就不赘述了。

## 调试

- `kubectl get rs -w` watch rs 的变化
- `kubectl describe deploy <name>` 查看`deployment`的更新状态

## 总结

`Kubernetes Deployment`滚动更新是靠新老`RS`交接棒完成的，新的`RS` scale up->老的`RS` scale down->新的`RS` scale up的…… 一直循环直到新的`RS` `repliacs`的数量达到期望值。在滚动更新的过程中会遵循：

- 总pod数不能超过`deployment.Spec.Replicas`+`.spec.strategy.rollingUpdate.maxSurge`
- 保证当前ready的pod不能少于`deployment.Spec.Replicas` - `.spec.strategy.rollingUpdate.maxUnavailable`

在生产环境实际操作中默认`25%`对`replicas`基数很大的服务是不合适的，因为在滚动更新的一瞬间`maxSurge`可能突破你集群资源的上限，`maxUnavailable`也可能会击穿你服务性能水平的下限，因此一定要根据自己服务的情况做相应调整。

## 参考

https://github.com/kubernetes/kubernetes/issues/22065

https://github.com/kubernetes/kubernetes/pull/20368/commits/86aea1d59c42de15afbff5e2388e4b764bd134fc

https://github.com/kubernetes/kubernetes/pull/20368

文章作者 XniLe

上次更新 2020-04-07