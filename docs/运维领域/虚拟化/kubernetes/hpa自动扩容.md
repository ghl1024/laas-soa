hpa扩容思路:

检测容器资源情况, 判断是否达到其他限制值的百分比量, 达到后根据最大副本量逐次添加



参数来自控制器管理器

默认15秒钟检查一次, 参数: `--horizontal-pod-autoscaler-sync-period` 

检查对象为启动5分钟之后的pod, 参数:   `--horizontal-pod-autoscaler-cpu-initialization-period` 

扩容最大数量被hpa编排文件中的maxReplicas限制, 最小数量被hpa编排文件中的minReplicas限制

扩容之后的pod在30秒钟之内不被记录扩容值中, 参数:  `--horizontal-pod-autoscaler-initial-readiness-delay` 

计算量判断误差为10%, 意味着总是会比实际期望量总是少一个副本, 也就是说不会因为流量的小幅度波动导致副本数量随意增加

需要注意: 扩容过程会忽略删除中和启动失败的pod, 导致一瞬间系统压力很大

滚动升级时不能自动扩缩容

自动扩缩容的最小数量将直接影响rc的副本数量(谨慎设置最小数量)

