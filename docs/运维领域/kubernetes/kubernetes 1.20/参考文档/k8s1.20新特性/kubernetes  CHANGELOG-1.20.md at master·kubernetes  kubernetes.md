- v1.20.1
  - v1.20.1的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries)
  - [自v1.20.0起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200)
  - 种类变化
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed)
- v1.20.0
  - v1.20.0下载
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-1)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-1)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-1)
  - [自v1.19.0起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1190)
  - 新增功能（主要主题）
    - [Dockershim弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#dockershim-deprecation)
    - [外部凭证供应商](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#external-credential-provider-for-client-go)
    - [通过功能门可以使用CronJob控制器v2](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#cronjob-controller-v2-is-available-through-feature-gate)
    - [PID将毕业生限制为一般可用性](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#pid-limits-graduates-to-general-availability)
    - [API优先级和公平性毕业于Beta](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-priority-and-fairness-graduates-to-beta)
    - [IPv4 / IPv6运行](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#ipv4ipv6-run)
    - [go1.15.5](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#go1155)
    - [CSI卷快照升级为通用版本](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#csi-volume-snapshot-graduates-to-general-availability)
    - [非递归卷所有权（FSGroup）毕业生进入Beta](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#non-recursive-volume-ownership-fsgroup-graduates-to-beta)
    - [FSGroup毕业生使用Beta版的CSIDriver策略](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#csidriver-policy-for-fsgroup-graduates-to-beta)
    - [CSI驱动程序的安全性改进（Alpha）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#security-improvements-for-csi-drivers-alpha)
    - [引入优美的节点关闭功能（Alpha）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#introducing-graceful-node-shutdown-alpha)
    - [运行时日志卫生](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#runtime-log-sanitation)
    - [Pod资源指标](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#pod-resource-metrics)
    - [简介 `RootCAConfigMap`](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#introducing-rootcaconfigmap)
    - [`kubectl debug` 毕业于Beta](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#kubectl-debug-graduates-to-beta)
    - [在Kubeadm中删除不推荐使用的标志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removing-deprecated-flags-in-kubeadm)
    - [FQDN毕业于Beta的Pod主机名](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#pod-hostname-as-fqdn-graduates-to-beta)
    - [`TokenRequest`/`TokenRequestProjection`应届毕业生](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#tokenrequest--tokenrequestprojection-graduates-to-general-availability)
    - [RuntimeClass使毕业生可以使用“一般可用性”。](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#runtimeclass-feature-graduates-to-general-availability)
    - [Cloud Provider现在由Cloud Provider独家提供](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#cloud-controller-manager-now-exclusively-shipped-by-cloud-provider)
  - 已知的问题
    - [kubelet中的摘要API没有加速器指标](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#summary-api-in-kubelet-doesnt-have-accelerator-metrics)
  - 紧急升级说明
    - [（不，实际上，您必须在升级之前阅读此内容）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#no-really-you-must-read-this-before-you-upgrade)
  - 种类变化
    - [弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation)
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature)
    - [文献资料](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#documentation)
    - [测试失败](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#failing-test)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-1)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-1)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-1)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-1)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-2)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-2)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-2)
- v1.20.0-rc.0
  - v1.20.0-rc.0的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-1)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-2)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-2)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-2)
  - [自v1.20.0-beta.2起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-beta2)
  - 种类变化
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-1)
    - [测试失败](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#failing-test-1)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-2)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-3)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-3)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-3)
- v1.20.0-beta.2
  - v1.20.0-beta.2的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-2)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-3)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-3)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-3)
  - [自v1.20.0-beta.1起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-beta1)
  - 紧急升级说明
    - [（不，实际上，您必须在升级之前阅读此内容）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#no-really-you-must-read-this-before-you-upgrade-1)
  - 种类变化
    - [弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation-1)
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-1)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-2)
    - [文献资料](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#documentation-1)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-3)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake-1)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-4)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-4)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-4)
- v1.20.0-beta.1
  - v1.20.0-beta.1的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-3)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-4)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-4)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-4)
  - [从v1.20.0-beta.0开始的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-beta0)
  - 种类变化
    - [弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation-2)
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-2)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-3)
    - [文献资料](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#documentation-2)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-4)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake-2)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-5)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-5)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-5)
- v1.20.0-beta.0
  - v1.20.0-beta.0的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-4)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-5)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-5)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-5)
  - [自v1.20.0-alpha.3起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-alpha3)
  - 紧急升级说明
    - [（不，实际上，您必须在升级之前阅读此内容）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#no-really-you-must-read-this-before-you-upgrade-2)
  - 种类变化
    - [弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation-3)
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-3)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-4)
    - [文献资料](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#documentation-3)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-5)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake-3)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-6)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-6)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-6)
- v1.20.0-alpha.3
  - v1.20.0-alpha.3的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-5)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-6)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-6)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-6)
  - [自v1.20.0-alpha.2起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-alpha2)
  - 种类变化
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-4)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-5)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-6)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake-4)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-7)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-7)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-7)
- v1.20.0-alpha.2
  - v1.20.0-alpha.2的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-6)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-7)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-7)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-7)
  - [自v1.20.0-alpha.1起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-alpha1)
  - 种类变化
    - [弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation-4)
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-5)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-6)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-7)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake-5)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-8)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-8)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-8)
- v1.20.0-alpha.1
  - v1.20.0-alpha.1的下载
    - [源代码](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#source-code-7)
    - [客户二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries-8)
    - [服务器二进制文件](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#server-binaries-8)
    - [节点二进制](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#node-binaries-8)
  - [自v1.20.0-alpha.0起的变更日志](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changelog-since-v1200-alpha0)
  - 紧急升级说明
    - [（不，实际上，您必须在升级之前阅读此内容）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#no-really-you-must-read-this-before-you-upgrade-3)
  - 种类变化
    - [弃用](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#deprecation-5)
    - [API变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#api-change-6)
    - [特征](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#feature-7)
    - [文献资料](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#documentation-4)
    - [测试失败](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#failing-test-2)
    - [错误或回归](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#bug-or-regression-8)
    - [其他（清理或片状）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#other-cleanup-or-flake-6)
  - 依存关系
    - [添加](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#added-9)
    - [已变更](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#changed-9)
    - [已移除](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#removed-9)

# v1.20.1

## v1.20.1的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes.tar.gz) | 154929ba535dcb564610d7c0f80906917b431ddd67bd462e7a82e889de54a86e8fe6960c8f2e88d76d877c0809083e76720ee7bbb204dcdd1eedff1aad3d8134 |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-src.tar.gz) | 6031392d46b677439549a342c17a07eb33de3f5964b8b476fcb0dbf150bc80a995e4f4eaf8f07f25392bb1f920dc7a849998819c4dd84cf1006cbd2bf7739ce2 |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-darwin-amd64.tar.gz) | f5280e35b65059f02cc242ec25235036d67fa49bdfdf82174aa8131b8ac8d6423a56615ffe89f5503b8388a41df223e2e50079f5bf14e39cab37d7dcc2190d67 |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-linux-386.tar.gz) | 0d50f018ec0ad46ecd2c89d282e57d6b3bda6eb71be19184f0565e77537fbfeddf5e4e5dab3c59bd5dc1e237a499956fc7f3411dbf6ccb9927c7c36a701ddf12 |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-linux-amd64.tar.gz) | a07146819c2777583875f1761807bca509404d7f1842d1bdcf1cb1247938dc14caf3aa1dce2ac470e5ec8baffd47b8240508268b435465d5541c63035fde4898 |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-linux-arm.tar.gz) | 1be85ece9f0ec319417a0d0f3217d285e90565300bfad2a6dd35e496b1bdca6fd13ae6b397f3c212776ebe87703356e9828ab9954751ca184c5901fdaa14c120 |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-linux-arm64.tar.gz) | a1e78fde3169b9da98edddfb1581798b743c8978ac6dd08d68dcea66b0c6e32049d8ff6e1b00e49219b2edc90decd4a637dfbfd6d1bd30b98f23c7f393df71f7 |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-linux-ppc64le.tar.gz) | 74a943773da29acd250c3c20089ba1d196148fa23ea01cd8a9810209cb8eadf719bc369468b8b759126d96c75a44e7d45ca75ad8442276cc4e1f03b7cbfd0df3 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-linux-s390x.tar.gz) | bba2f76ac2c778b3e1b5cc1c0f72eb56942caba059736676dc688254b78f6fd8e1cce8bc25d5fc67d9ec940bbd97e36cce03e72816f22a395a3753cb4e478c01 |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-windows-386.tar.gz) | aa0017c720cbd1a88b363a52668e196eb590f0403dc78c635841eb5749d190d3bd8cd0e9e34aa11a2f15bcd74d1be80892ed3cf4dfd9958405bfa3dfdfb941bc |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-client-windows-amd64.tar.gz) | 67413fc5a262cd02094863cde26a099ccadbfaa66daa8e62a82d657f222eb2ed1eaf5a39033fbac64c647fbfb68ed00eda342d8ddb4a38d5cc12da2f202d8831 |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-server-linux-amd64.tar.gz) | 0a5ff7082b9bd54592697ec9c4ea75e1be80de712823e5b76687a5a110c392e3e8cd88adbc5715cc39537143e7656b40a3f36e550183c8fa7215dc882d2bf61a |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-server-linux-arm.tar.gz) | ea27b814cca68851d20b50ce25f3e81d22a1aff7333dc77e3e9d6a48bcb3cc5253a7226f4d7916aeca909e908a54b69635a3287e2d7861068f5cebceb91d5580 |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-server-linux-arm64.tar.gz) | b93857e8c38e433f3edd1ea5727c64b79e1898bcfb8b31a823024c06c2dc66b047482f28d8e89db5c1aae99532a7820dc0212b2aa5a51de3b9c94aa88514b372 |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-server-linux-ppc64le.tar.gz) | 5f952f48a3b0abccf5117f4d2b2f826a7d191f0f49d3a1a7726246bf276f1747dad96f068f601c2cda42a77304f68644ef1a2244b0f5095a1ba692eb264cf1a4 |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-server-linux-s390x.tar.gz) | 166ca5d1a96ddba55d6a75b8bd0fe5e833e771fc07460457e90afd3ab15b588d04164ebe76faebd31196314166bd0079e59988fb277740ed338de81b79abd6fe |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-node-linux-amd64.tar.gz) | 6a3d406bd48a3fbeec48d40bd2fc6e38bf189f07731c7c7a7222355a816bcc4887b9683605cfc071deeace38b2fe813574307ec0cafeb052d744a4ad0567228c |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-node-linux-arm.tar.gz) | 518cf973bd8daa47e64c3cfa8d5e6f2d13f142d85517ea506ed61472a43fc6558b384c765068ea6fcc84751db03bc561050cfe2f47ceaf83268487d86a327368 |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-node-linux-arm64.tar.gz) | 4f3f695de1690a48470d76e0ad12713b30c5a48a754533ccd83464ca7eba33892f5ada57359f1cf577d912428041633f9fc5b5b788bb158c287a10cecf9b083a |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-node-linux-ppc64le.tar.gz) | 61344e120a07ba2925d3e1117ece76bd8b1fa58cb45ddabc49ef0dcb7553650cb3d4ea4b8e4543b350fff47b1e612eb796a0c604a2e2e4e53f6e4e9e449d7dbd |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-node-linux-s390x.tar.gz) | 1494481817de129b52e7d7ba1046fe0fd73abdd918c85ef3327f9221c0c14213ca6273222aea10529612d6b6af26dfff25a7d1b04bfbfcd7ce88fa3cccc715e2 |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.1/kubernetes-node-windows-amd64.tar.gz) | 2180bf72bc7948fcec27940dbcff88892d2b37b1690f2398c1c6f0a8f48dc7a0aec46f9e9f521727b8e71d7f3af52af296221f4bb46ada356f204ea56f8e5d56 |

## 自v1.20.0起的变更日志

## 种类变化

### 错误或回归

- 使用cri_stats_provider时，在kubelet的摘要API中将提供AcceleratorStats。（[＃97018](https://github.com/kubernetes/kubernetes/pull/97018)，[@ ](https://github.com/ruiwen-zhao)[ruiwen ](https://github.com/kubernetes/kubernetes/pull/97018)[-zhao](https://github.com/ruiwen-zhao)）[SIG节点]
- 修复了FibreChannel卷插件在分离多路径卷时损坏文件系统的问题。（[＃97013](https://github.com/kubernetes/kubernetes/pull/97013)，[@jsafrane](https://github.com/jsafrane)）[SIG存储]
- 修复了kubelet中的错误，该错误将在容器重新启动后饱和CPU利用率。（[＃97175](https://github.com/kubernetes/kubernetes/pull/97175)，[@hanlins](https://github.com/hanlins)）[SIG节点]
- 现在，当使用v1.19（[＃97284](https://github.com/kubernetes/kubernetes/pull/97284)，[@pacoxu](https://github.com/pacoxu)）创建集群时，Kubeadm将安装etcd的3.4.13版本（SIG集群生命周期）
- Kubeadm：修复了一个kubeadm升级错误，该错误可能导致自定义CoreDNS配置被默认值替换。（[＃97016](https://github.com/kubernetes/kubernetes/pull/97016)，[@rajansandeep](https://github.com/rajansandeep)）[SIG集群生命周期]

## 依存关系

### 添加

*什么也没有变。*

### 已变更

- github.com/google/cadvisor：[v0.38.5→v0.38.6](https://github.com/google/cadvisor/compare/v0.38.5...v0.38.6)

### 已移除

*什么也没有变。*

# v1.20.0

[文献资料](https://docs.k8s.io/)

## v1.20.0下载

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes.tar.gz) | `ebfe49552bbda02807034488967b3b62bf9e3e507d56245e298c4c19090387136572c1fca789e772a5e8a19535531d01dcedb61980e42ca7b0461d3864df2c14` |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-src.tar.gz) | `bcbd67ed0bb77840828c08c6118ad0c9bf2bcda16763afaafd8731fd6ce735be654feef61e554bcc34c77c65b02a25dae565adc5e1dc49a2daaa0d115bf1efe6` |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-darwin-amd64.tar.gz) | `3609f6483f4244676162232b3294d7a2dc40ae5bdd86a842a05aa768f5223b8f50e1d6420fd8afb2d0ce19de06e1d38e5e5b10154ba0cb71a74233e6dc94d5a0` |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-linux-386.tar.gz) | `e06c08016a08137d39804383fdc33a40bb2567aa77d88a5c3fd5b9d93f5b581c635b2c4faaa718ed3bb2d120cb14fe91649ed4469ba72c3a3dda1e343db545ed` |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-linux-amd64.tar.gz) | `081472833601aa4fa78e79239f67833aa4efcb4efe714426cd01d4ddf6f36fbf304ef7e1f5373bff0fdff44a845f7560165c093c108bd359b5ab4189f36b1f2f` |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-linux-arm.tar.gz) | `037f84a2f29fe62d266cab38ac5600d058cce12cbc4851bcf062fafba796c1fbe23a0c2939cd15784854ca7cd92383e5b96a11474fc71fb614b47dbf98a477d9` |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-linux-arm64.tar.gz) | `275727e1796791ca3cbe52aaa713a2660404eab6209466fdc1cfa8559c9b361fe55c64c6bcecbdeba536b6d56213ddf726e58adc60f959b6f77e4017834c5622` |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-linux-ppc64le.tar.gz) | `7a9965293029e9fcdb2b7387467f022d2026953b8461e6c84182abf35c28b7822d2389a6d8e4d8e532d2ea5d5d67c6fee5fb6c351363cb44c599dc8800649b04` |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-linux-s390x.tar.gz) | `85fc449ce1980f5f030cc32e8c8e2198c1cc91a448e04b15d27debc3ca56aa85d283f44b4f4e5fed26ac96904cc12808fa3e9af3d8bf823fc928befb9950d6f5` |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-windows-386.tar.gz) | `4c0a27dba1077aaee943e0eb7a787239dd697e1d968e78d1933c1e60b02d5d233d58541d5beec59807a4ffe3351d5152359e11da120bf64cacb3ee29fbc242e6` |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-client-windows-amd64.tar.gz) | `29336faf7c596539b8329afbbdceeddc843162501de4afee44a40616278fa1f284d8fc48c241fc7d52c65dab70f76280cc33cec419c8c5dbc2625d9175534af8` |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-server-linux-amd64.tar.gz) | `fb56486a55dbf7dbacb53b1aaa690bae18d33d244c72a1e2dc95fb0fcce45108c44ba79f8fa04f12383801c46813dc33d2d0eb2203035cdce1078871595e446e` |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-server-linux-arm.tar.gz) | `735ed9993071fe35b292bf06930ee3c0f889e3c7edb983195b1c8e4d7113047c12c0f8281fe71879fc2fcd871e1ee587f03b695a03c8512c873abad444997a19` |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-server-linux-arm64.tar.gz) | `ffab155531d5a9b82487ee1abf4f6ef49626ea58b2de340656a762e46cf3e0f470bdbe7821210901fe1114224957c44c1d9cc1e32efb5ee24e51fe63990785b2` |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-server-linux-ppc64le.tar.gz) | `9d5730d35c4ddfb4c5483173629fe55df35d1e535d96f02459468220ac2c97dc01b995f577432a6e4d1548b6edbfdc90828dc9c1f7cf7464481af6ae10aaf118` |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-server-linux-s390x.tar.gz) | `6e4c165306940e8b99dd6e590f8542e31aed23d2c7a6808af0357fa425cec1a57016dd66169cf2a95f8eb8ef70e1f29e2d500533aae889e2e3d9290d04ab8721` |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-node-linux-amd64.tar.gz) | `3e6c90561dd1c27fa1dff6953c503251c36001f7e0f8eff3ec918c74ae2d9aa25917d8ac87d5b4224b8229f620b1830442e6dce3b2a497043f8497eee3705696` |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-node-linux-arm.tar.gz) | `26db385d9ae9a97a1051a638e7e3de22c4bbff389d5a419fe40d5893f9e4fa85c8b60a2bd1d370fd381b60c3ca33c5d72d4767c90898caa9dbd4df6bd116a247` |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-node-linux-arm64.tar.gz) | `5b8b63f617e248432b7eb913285a8ef8ba028255216332c05db949666c3f9e9cb9f4c393bbd68d00369bda77abf9bfa2da254a5c9fe0d79ffdad855a77a9d8ed` |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-node-linux-ppc64le.tar.gz) | `60da7715996b4865e390640525d6e98593ba3cd45c6caeea763aa5355a7f989926da54f58cc5f657f614c8134f97cd3894b899f8b467d100dca48bc22dd4ff63` |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-node-linux-s390x.tar.gz) | `9407dc55412bd04633f84fcefe3a1074f3eaa772a7cb9302242b8768d6189b75d37677a959f91130e8ad9dc590f9ba8408ba6700a0ceff6827315226dd5ee1e6` |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0/kubernetes-node-windows-amd64.tar.gz) | `9d4261af343cc330e6359582f80dbd6efb57d41f882747a94bbf47b4f93292d43dd19a86214d4944d268941622dfbc96847585e6fec15fddc4dbd93d17015fa8` |

## 自v1.19.0起的变更日志

## 新增功能（主要主题）

### Dockershim弃用

不推荐使用Docker作为底层运行时。Docker生成的映像将一如既往地在所有运行时中继续在您的集群中工作。Kubernetes社区[已经写了一篇有关此](https://blog.k8s.io/2020/12/02/dont-panic-kubernetes-and-docker/)[问题](https://blog.k8s.io/2020/12/02/dockershim-faq/)[的博客文章，](https://blog.k8s.io/2020/12/02/dont-panic-kubernetes-and-docker/)其中[包含专门的FAQ页面](https://blog.k8s.io/2020/12/02/dockershim-faq/)。

### 外部凭证供应商

现在，可以通过`KUBERNETES_EXEC_INFO`环境变量在当前群集信息中传递“客户访问凭证”插件。在[客户端凭证插件文档中](https://docs.k8s.io/reference/access-authn-authz/authentication/#client-go-credential-plugins/)了解有关此内容的更多信息。

### 通过功能门可以使用CronJob控制器v2

该版本中的`CronJob`控制器的替代实现现已作为alpha功能提供，该功能通过使用告示程序而不是轮询来提高实验性能。虽然这将是将来的默认行为，但您可以[在此版本中通过功能选通尝试它们](https://docs.k8s.io/concepts/workloads/controllers/cron-jobs/)。

### PID将毕业生限制为一般可用性

在默认情况下在一年内处于Beta阶段启用之后，PID限制功能现在在`SupportNodePidsLimit`（节点到容器的PID隔离）和`SupportPodPidsLimit`（限制每个容器的PID的能力）上普遍可用。

### API优先级和公平性毕业于Beta

Kubernetes 1.20最初在1.18中引入，现在默认情况下启用API优先级和公平性（APF）。这允许[按优先级](https://docs.k8s.io/concepts/cluster-administration/flow-control/)`kube-apiserver`对[传入的请求](https://docs.k8s.io/concepts/cluster-administration/flow-control/)进行[分类](https://docs.k8s.io/concepts/cluster-administration/flow-control/)。

### IPv4 / IPv6运行

IPv4 / IPv6双协议栈已针对1.20重新实现，以基于用户和社区反馈支持双协议栈服务。如果您的群集启用了双堆栈，则可以创建可以使用IPv4，IPv6或同时使用这两种服务，并且可以为现有服务更改此设置。有关详细信息，请参见更新的[IPv4 / IPv6双协议栈文档](https://docs.k8s.io/concepts/services-networking/dual-stack/)，其中涵盖了各种细微差别的选项。

我们希望该实现在即将发布的版本中从alpha升级到beta和GA，因此我们希望您对[＃k8s-dual-stack](https://kubernetes.slack.com/messages/k8s-dual-stack)或[增强功能＃563中](https://features.k8s.io/563)的双栈体验发表评论。

### go1.15.5

从此版本开始，go1.15.5已集成到Kubernetes项目中，[包括有关此工作的其他与基础架构有关的更新](https://github.com/kubernetes/kubernetes/pull/95776)。

### CSI卷快照升级为通用版本

CSI卷快照在1.20版中移至GA。此功能提供了一种在Kubernetes中触发卷快照操作的标准方法，并允许Kubernetes用户以可移植的方式在任何Kubernetes环境中合并快照操作，而无需支持底层存储提供程序。此外，这些Kubernetes快照原语是基本的构建块，可释放为Kubernetes开发高级企业级存储管理功能的能力：包括应用程序或集群级备份解决方案。请注意，快照支持将需要Kubernetes发行商捆绑Snapshot控制器，Snapshot CRD和验证Webhook。此外，还必须在群集上部署支持快照功能的CSI驱动程序。

### 非递归卷所有权（FSGroup）毕业生进入Beta

默认情况下，该`fsgroup`设置（如果指定）将以递归方式更新每个装载中卷中每个文件的权限。如果卷中有许多文件，这会使挂载和Pod启动非常慢。此设置使pod可以指定一个`PodFSGroupChangePolicy`，指示仅当根目录的权限和所有权与卷上的预期权限不匹配时，才更改卷的所有权和权限。

### FSGroup毕业生使用Beta版的CSIDriver策略

FSGroup的CSIDriver策略现在在1.20中为beta版。这使CSIDriver可以通过明确指示是否希望Kubernetes管理其卷的权限和所有权`fsgroup`。

### CSI驱动程序的安全性改进（Alpha）

在1.20中，我们引入了一个新的alpha功能`CSIServiceAccountToken`。此功能使CSI驱动程序可以模拟为其安装卷的Pod。这改善了安装过程中的安全状态，在该过程中，将卷在Pod的服务帐户上进行ACL加密，而无需将不必要的权限分配给CSI驱动程序的服务帐户。此功能对于秘密处理CSI驱动程序（例如secrets-store-csi驱动程序）特别重要。由于这些令牌可以循环使用并且寿命很短，因此此功能还为CSI驱动程序提供了一个旋钮，以使其可以`NodePublishVolume`定期使用新令牌接收RPC调用。当卷寿命短（例如证书）时，此旋钮也很有用。

### 引入优美的节点关闭功能（Alpha）

该`GracefulNodeShutdown`功能现在位于Alpha中。这使kubelet可以知道节点系统已关闭，从而在系统关闭期间正常终止Pod。可以[通过功能门启用](https://docs.k8s.io/concepts/architecture/nodes/#graceful-node-shutdown)此功能。

### 运行时日志卫生

现在可以将日志配置为使用运行时保护，以防止敏感数据泄漏。[有关此实验功能的详细信息，请参见文档](https://docs.k8s.io/concepts/cluster-administration/system-logs/#log-sanitization)。

### Pod资源指标

现在可以通过进行按需指标计算`/metrics/resources`。[启用后](https://docs.k8s.io/concepts/cluster-administration/system-metrics#kube-scheduler-metrics)，端点将报告所有正在运行的Pod的请求资源和所需限制。

### 简介 `RootCAConfigMap`

`RootCAConfigMap`毕业于Beta，与分开`BoundServiceAccountTokenVolume`。该`kube-root-ca.crt`ConfigMap现在提供给每一个命名空间，默认情况下。它包含用于验证kube-apiserver连接的证书颁发机构捆绑包。

### `kubectl debug` 毕业于Beta

`kubectl alpha debug`从1.20的alpha到beta毕业，成为`kubectl debug`。 `kubectl debug`直接从kubectl提供对常见调试工作流的支持。此版本的发行版中支持的故障排除方案`kubectl`包括：通过创建使用其他容器映像或命令的Pod副本，对在启动时崩溃的工作负载进行故障排除。通过在调试容器的新副本中或使用临时容器添加带有调试工具的新容器来解决Distroless容器的故障。（临时容器是默认情况下未启用的alpha功能。）通过在主机名称空间中运行并具有对主机文件系统访问权限的容器来对节点进行故障排除。请注意，作为新的内置命令，`kubectl debug`其优先级高于任何内置命令。`kubectl`名为“ debug”的插件。您将需要重命名受影响的插件。`kubectl alpha debug`现在不建议使用调用，并将在后续发行版中将其删除。更新您的脚本以`kubectl debug`代替使用`kubectl alpha debug`！有关kubectl调试的更多信息，请参见Kubernetes网站上的Debugging Running Pod（调试运行中的Pod），kubectl帮助调试，或通过访问＃sig-cli或对[增强功能进行](https://features.k8s.io/1441)注释[＃1441](https://features.k8s.io/1441)来访问SIG CLI 。

### 在Kubeadm中删除不推荐使用的标志

`kubeadm`在此版本中应用了许多弃用和删除的弃用功能。有关更多详细信息，请参见“紧急升级说明”和“种类/弃用”部分。

### FQDN毕业于Beta的Pod主机名

以前在功能门后面的1.19中引入，`SetHostnameAsFQDN`现在默认情况下启用。有关[服务和Pod的DNS文档中](https://docs.k8s.io/concepts/services-networking/dns-pod-service/#pod-sethostnameasfqdn-field)提供了有关此行为的更多详细信息

### `TokenRequest`/`TokenRequestProjection`应届毕业生

绑定到pod的服务帐户令牌现在是一个稳定的功能。功能门将在1.21版本中删除。有关更多信息，请参阅以下更改日志中的注释。

### RuntimeClass使毕业生可以使用“一般可用性”。

该`node.k8s.io`API组从推动`v1beta1`到`v1`。`v1beta1`现在已弃用，并将在以后的版本中删除，请开始使用`v1`。（[＃95718](https://github.com/kubernetes/kubernetes/pull/95718)，[@SergeyKanzhelev](https://github.com/SergeyKanzhelev)）[SIG应用，[身份](https://github.com/SergeyKanzhelev)验证，节点，计划和测试]

### Cloud Provider现在由Cloud Provider独家提供

Kubernetes将不再交付Cloud Controller Manager二进制文件的实例。每个云提供商都应交付自己的二进制文件实例。对于云提供商建立这样一个二元的实例详细信息下可以找到[这里](https://github.com/kubernetes/kubernetes/tree/master/staging/src/k8s.io/cloud-provider/sample)。任何对构建Cloud Controller Manager存有疑问的人都应该与SIG Cloud Provider联系。有关Managed Kubernetes解决方案上的Cloud Controller Manager的问题应转到相关的Cloud Provider。可以通过SIG Cloud Provider提出有关非托管解决方案上的Cloud Controller Manager的问题。

## 已知的问题

### kubelet中的摘要API没有加速器指标

当前，cadvisor_stats_provider提供AcceleratorStats，而cri_stats_provider不提供。结果，当使用cri_stats_provider时，kubelet的摘要API没有加速器指标。[有一个正在进行的工作正在解决此问题](https://github.com/kubernetes/kubernetes/pull/96873)。

## 紧急升级说明

### （不，实际上，您必须在升级之前阅读此内容）

- 在kubelet中修复了一个错误，该错误中不遵守exec探测超时的问题。这可能会导致意外行为，因为默认超时（如果未指定）`1s`对于某些exec探针可能太小。确保依赖此行为的Pod已更新，以正确处理探测超时。有关更多详细信息，请参见文档的“[配置探针”](https://docs.k8s.io/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes)部分。
  - 对于某些群集，此行为更改可能是意外的，并且可以通过关闭`ExecProbeTimeout`功能门来禁用。此门将在以后的版本中锁定和删除，因此始终遵守exec探测超时。（[＃94115](https://github.com/kubernetes/kubernetes/pull/94115)，[@andrewsykim](https://github.com/andrewsykim)）[SIG节点和测试]
- RuntimeClass使毕业生可以使用“一般可用性”。将`node.k8s.io`API组从`v1beta1`升级为`v1`。`v1beta1`现在已弃用，并将在以后的版本中删除，请开始使用`v1`。（[＃95718](https://github.com/kubernetes/kubernetes/pull/95718)，[@SergeyKanzhelev](https://github.com/SergeyKanzhelev)）[SIG应用，[身份](https://github.com/SergeyKanzhelev)验证，节点，计划和测试]
- API优先级和公平性逐步升至Beta版。启用APF的1.19服务器不应在具有1.20+服务器的多服务器群集中运行。（[＃96527](https://github.com/kubernetes/kubernetes/pull/96527)，[@adtac](https://github.com/adtac)）[SIG API机械和测试]
- 对于CSI驱动程序，kubelet不再根据CSI规范为NodePublishVolume创建target_path。Kubelet也不再检查登台路径和目标路径是否已装入或已损坏。CSI驱动程序需要是幂等的，并执行任何必要的安装验证。（[＃88759](https://github.com/kubernetes/kubernetes/pull/88759)，[@andyzhangx](https://github.com/andyzhangx)）[SIG存储]
- Kubeadm：[http](http://git.k8s.io/enhancements/keps/sig-cluster-lifecycle/kubeadm/2067-rename-master-label-taint/README.md) ://git.k8s.io/enhancements/keps/sig-cluster-lifecycle/kubeadm/2067-rename-master-label-taint/README.md （[＃95382](https://github.com/kubernetes/kubernetes/pull/95382)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]
  - 现在已弃用了应用于控制平面节点的标签“ node-role.kubernetes.io/master”，并将在GA弃用期过后的将来版本中将其删除。
  - 引入一个新标签“ node-role.kubernetes.io/control-plane”，该标签将与“ node-role.kubernetes.io/master”并行应用，直到删除“ node-role.kubernetes.io/master”为止“ 标签。
  - 使“ kubeadm升级适用”在升级过程中仅具有“ node-role.kubernetes.io/master”标签的现有节点上添加“ node-role.kubernetes.io/control-plane”标签。
  - 请调整您在kubeadm之上构建的工具，以使用“ node-role.kubernetes.io/control-plane”标签。
  - 现在已弃用了应用于控制平面节点“ node-role.kubernetes.io/master:NoSchedule”的污点，并将在GA弃用期过后的将来版本中将其删除。
  - 对kubeadm CoreDNS / kube-dns托管清单的新的，将来的污点“ node-role.kubernetes.io/control-plane:NoSchedule”应用公差。请注意，此污点尚未应用于kubeadm控制平面节点。
  - 请调整您的工作负载以抢先忍受相同的未来污点。
- Kubeadm：改进serviceSubnet和podSubnet的验证。由于实现细节，必须限制ServiceSubnet的大小，并且掩码不能分配超过20位。PodSubnet针对kube-controller-manager的相应群集“ --node-cidr-mask-size”进行验证，如果值不兼容，它将失败。kubeadm不再在IPv6部署上自动设置节点掩码，您必须检查您的IPv6服务子网掩码是否与默认节点掩码/ 64兼容或正确设置。以前，对于IPv6，如果podSubnet的掩码小于/ 112，则kubeadm计算出的节点掩码为8的倍数，并拆分可用位以最大化用于节点的数量。（[＃95723](https://github.com/kubernetes/kubernetes/pull/95723)，[@aojea](https://github.com/aojea)）[SIG集群生命周期]
- 现在已从kubeadm命令中删除了已弃用的标志--experimental-kustomize。请改用--experimental-patches，这是1.19中引入的。--exprimental-patches的--help说明中提供了迁移信息。（[＃94871](https://github.com/kubernetes/kubernetes/pull/94871)，[@ neolit123](https://github.com/neolit123)）
- Windows hyper-v容器功能门在1.20中已弃用，在1.21中将被删除（[＃95505](https://github.com/kubernetes/kubernetes/pull/95505)，[@ wawa0210](https://github.com/wawa0210)）[SIG节点和Windows]
- 自v1.10起不推荐使用的在不安全端口上服务的kube-apiserver功能已被删除。不安全的位置标志`--address`，并`--insecure-bind-address`在KUBE-API服务器没有影响，在V1.24被删除。不安全的端口标志`--port`，`--insecure-port`只能设置为0，并将在v1.24中删除。（[＃95856](https://github.com/kubernetes/kubernetes/pull/95856)，[@ knight42](https://github.com/knight42)，[SIG API机械，节点，测试]）
- 添加双栈服务（alpha）。这是对alpha API的重大更改。它将双栈API wrt服务从单个ipFamily字段更改为3个字段：ipFamilyPolicy（SingleStack，PreferDualStack，RequireDualStack），ipFamily（分配的族列表）和clusterIP（包括clusterIP）。大多数用户根本不需要设置任何东西，默认情况下会为他们处理。服务是单栈的，除非用户要求双栈。所有这些都由“ IPv6DualStack”功能门控制。（[＃](https://github.com/kubernetes/kubernetes/pull/91824)[91824](https://github.com/khenidak)，[@khenidak](https://github.com/khenidak)）[SIG API机械，应用程序，CLI，网络，节点，计划和测试]
- `TokenRequest`并且`TokenRequestProjection`现在是GA功能。API服务器需要以下标志：
  - `--service-account-issuer`，应设置为一个URL，以标识在群集生存期内将保持稳定的API服务器。
  - `--service-account-key-file`，设置为一个或多个文件，其中包含一个或多个用于验证令牌的公共密钥。
  - `--service-account-signing-key-file`，设置为包含用于签署服务帐户令牌的私钥的文件。可以给同一个文件`kube-controller-manager`用`--service-account-private-key-file`。（[＃95896](https://github.com/kubernetes/kubernetes/pull/95896)，[@zshihang](https://github.com/zshihang)）[SIG API机械，[身份](https://github.com/zshihang)验证，集群生命周期]
- kubeadm：使命令“ kubeadm alpha kubeconfig用户”接受“ --config”标志，并删除以下标志：
  - apiserver-advertise-address / apiserver-bind-port：使用InitConfiguration中的localAPIEndpoint或ClusterConfiguration中的controlPlaneEndpoint。
  - cluster-name：使用ClusterConfiguration中的clusterName
  - cert-dir：使用ClusterConfiguration中的certificateDir（[＃94879](https://github.com/kubernetes/kubernetes/pull/94879)，[@ knight42](https://github.com/knight42)）[SIG群集生命周期]
- 当遇到拥有不正确数据的ownerReferences时，解决垃圾收集控制器的不确定行为。`OwnerRefInvalidNamespace`当检测到子对象和所有者对象之间的名称空间不匹配时，将记录原因为的事件。该[kubectl检查-ownerreferences](https://github.com/kubernetes-sigs/kubectl-check-ownerreferences)工具可以在升级之前运行，以查找与无效ownerReferences现有对象。
  - 现在，将具有ownerReference引用命名空间类型的uid（该命名空间不存在于同一命名空间中）的命名空间对象统一视为该所有者不存在，并且删除子对象。
  - 现在可以一致地对待具有ownerReference引用命名空间类型的uid的群集范围内的对象，就像该所有者是不可解析的一样，并且垃圾回收器将忽略子对象。（[＃92743](https://github.com/kubernetes/kubernetes/pull/92743)，[@liggitt](https://github.com/liggitt)）[SIG API机械，应用和测试]

## 种类变化

### 弃用

- kubelet中的Docker支持现已弃用，并将在以后的版本中删除。Kubelet使用名为“ dockershim”的模块，该模块实现了对Docker的CRI支持，并且在Kubernetes社区中看到了维护问题。我们鼓励您评估向容器运行时的迁移，该运行时是CRI（符合v1alpha1或v1）的完整实现。（[＃94624](https://github.com/kubernetes/kubernetes/pull/94624)，[@dims](https://github.com/dims)）[SIG节点]
- Kubeadm：不赞成使用自托管支持。实验命令“ kubeadm alpha自托管”现已弃用，并将在以后的版本中删除。（[＃95125](https://github.com/kubernetes/kubernetes/pull/95125)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]
- Kubeadm：将“ kubeadm alpha certs”命令升级为父命令“ kubeadm certs”。命令“ kubeadm alpha certs”已被弃用，在以后的版本中将被删除。请迁移。（[＃94938](https://github.com/kubernetes/kubernetes/pull/94938)，[@yagonobre](https://github.com/yagonobre)）[SIG群集生命周期]
- Kubeadm：删除不推荐使用的“ kubeadm alpha kubelet config enable-dynamic”命令。要继续使用该功能，请参考k8s.io上的“动态Kubelet配置”指南。此更改还删除了父命令“ kubeadm alpha kubelet”，因为暂时没有下面的子命令。（[＃94668](https://github.com/kubernetes/kubernetes/pull/94668)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]
- Kubeadm：删除命令“ kubeadm升级节点”（[＃94869](https://github.com/kubernetes/kubernetes/pull/94869)，[@ neolit123](https://github.com/neolit123)）弃用的--kubelet-config标志[SIG集群生命周期]
- Kubectl：弃用--delete-local-data（[＃95076](https://github.com/kubernetes/kubernetes/pull/95076)，[@dougsland](https://github.com/dougsland)）[SIG CLI，云提供程序和可伸缩性]
- Kubelet不推荐使用的端点`metrics/resource/v1alpha1`已被删除，请采用`metrics/resource`。（[＃](https://github.com/kubernetes/kubernetes/pull/94272)[94272](https://github.com/RainbowMango)，[@RainbowMango](https://github.com/RainbowMango)）[SIG仪器和节点]
- 删除不推荐使用的调度程序指标DeprecatedSchedulingDuration，DeprecatedSchedulingAlgorithmPredicateEvaluationSecondsDuration，DeprecatedSchedulingAlgorithmPriorityEvaluationSecondsDuration（[＃94884](https://github.com/kubernetes/kubernetes/pull/94884)，[@ arghya88](https://github.com/arghya88)）[SIG仪器和调度]
- 不建议使用调度程序Alpha指标binding_duration_seconds和schedule_algorithm_preemption_evaluation_seconds，这两个指标现在都作为framework_extension_point_duration_seconds的一部分涵盖，前者作为PostFilter，后者作为PostFilter，而Bind插件。该计划是在1.21（[＃95001](https://github.com/kubernetes/kubernetes/pull/95001)，[@ arghya88](https://github.com/arghya88)）中同时删除两者[SIG仪表和计划]
- 在EgressSelectorConfiguration API中支持将“ controlplane”作为有效的EgressSelection类型。“ Master”已弃用，并将在v1.22中删除。（[＃](https://github.com/kubernetes/kubernetes/pull/95235)[95235](https://github.com/andrewsykim)，[@andrewsykim](https://github.com/andrewsykim)）[SIG API机械]
- v1alpha1 PodPreset API和准入插件已被删除，没有内置替代。准入网络挂钩可用于在创建时修改pod。（[＃94090](https://github.com/kubernetes/kubernetes/pull/94090)，[@ deads2k](https://github.com/deads2k)）[SIG API机械，应用程序，CLI，云提供程序，可伸缩性和测试]

### API变更

- ```
  TokenRequest
  ```

  并且

  ```
  TokenRequestProjection
  ```

  功能已升级到通用航空。此功能允许生成在“秘密”对象中不可见并且与Pod对象的生存期相关的服务帐户令牌。有关配置和使用此功能的详细信息，请参见

  https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection

  。该

  ```
  TokenRequest
  ```

  和

  ```
  TokenRequestProjection
  ```

  功能大门将在V1.21被删除。

  - kubeadm的kube-apiserver Pod清单现在默认包含以下标志：“-service-account-key-file”，“-service-account-signing-key-file”，“-service-account-issuer”。（[＃93258](https://github.com/kubernetes/kubernetes/pull/93258)，[@zshihang](https://github.com/zshihang)）[SIG API机械，[身份](https://github.com/zshihang)验证，群集生命周期，存储和测试]

- `nofuzz`现在，新的go build标签将禁用gofuzz支持。发布二进制文件可启用此功能。（[＃92491](https://github.com/kubernetes/kubernetes/pull/92491)，[@BenTheElder](https://github.com/BenTheElder)）[SIG API机械]

- 将WindowsContainerResources和注释添加到CRI-API UpdateContainerResourcesRequest（[＃95741](https://github.com/kubernetes/kubernetes/pull/95741)，[@katiewasnothere](https://github.com/katiewasnothere)）[SIG节点]

- 向EndpointSlice API添加`serving`和`terminating`条件。 `serving`跟踪端点的就绪状态，无论其终止状态如何。这与之不同，`ready`因为`ready`只有当Pod没有终止时才如此。 `terminating`当端点终止时为true。对于Pod，这是带有删除时间戳记的任何端点。（[＃92968](https://github.com/kubernetes/kubernetes/pull/92968)，[@andrewsykim](https://github.com/andrewsykim)）[SIG应用和网络]

- 添加双栈服务（alpha）。这是对alpha API的重大更改。它将双栈API wrt服务从单个ipFamily字段更改为3个字段：ipFamilyPolicy（SingleStack，PreferDualStack，RequireDualStack），ipFamily（分配的族列表）和clusterIP（包括clusterIP）。大多数用户根本不需要设置任何东西，默认情况下会为他们处理。服务是单栈的，除非用户要求双栈。所有这些都由“ IPv6DualStack”功能门控制。（[＃](https://github.com/kubernetes/kubernetes/pull/91824)[91824](https://github.com/khenidak)，[@khenidak](https://github.com/khenidak)）[SIG API机械，应用程序，CLI，网络，节点，计划和测试]

- 向向下的API（[＃86102](https://github.com/kubernetes/kubernetes/pull/86102)，[@derekwaynecarr](https://github.com/derekwaynecarr)）添加对大页面的支持[SIG API机械，应用程序，CLI，网络，节点，计划和测试]

- 添加了kubelet alpha功能，`GracefulNodeShutdown`该功能使kubelet知道节点系统已关闭，并导致在系统关闭期间正常终止Pod。（[＃96129](https://github.com/kubernetes/kubernetes/pull/96129)，[@bobbypage](https://github.com/bobbypage)）[SIG节点]

- AppProtocol现在是用于端点和服务的GA。ServiceAppProtocol功能闸将在1.21中弃用。（[＃96327](https://github.com/kubernetes/kubernetes/pull/96327)，[@robscott](https://github.com/robscott)）[SIG应用和网络]

- 现在，可以通过设置（新）参数Service.spec.allocateLoadBalancerNodePorts = false来禁用为LoadBalancer类型的服务自动分配NodePorts。默认情况是为类型为LoadBalancer的服务分配NodePorts，这是现有行为。（[＃92744](https://github.com/kubernetes/kubernetes/pull/92744)，[@uablrek](https://github.com/uablrek)）[SIG应用和网络]

- 将服务更改为`type`不需要这些字段的模式时，将自动清除Service对象上的某些字段。例如，从type = LoadBalancer更改为type = ClusterIP将清除NodePort分配，而不是强制用户清除它们。（[＃95196](https://github.com/kubernetes/kubernetes/pull/95196)，[@thockin](https://github.com/thockin)）[SIG API机械，应用程序，网络和测试]

- 记录需要使用ServiceTopology功能`service.spec.topologyKeys`。（[＃96528](https://github.com/kubernetes/kubernetes/pull/96528)，[@andrewsykim](https://github.com/andrewsykim)）[SIG应用]

- EndpointSlice具有一个新的NodeName字段，该字段由EndpointSliceNodeName功能门保护。

  - 在即将发布的版本中，将不建议使用EndpointSlice拓扑字段。
  - 在Kubernetes 1.17中弃用EndpointSlice“ IP”地址类型后，该地址类型被正式删除。
  - Discovery.k8s.io/v1alpha1 API已过时，将在Kubernetes 1.21中删除。（[＃96440](https://github.com/kubernetes/kubernetes/pull/96440)，[@robscott](https://github.com/robscott)）[SIG API机械，应用程序和网络]

- 面向外部的API podresources现在可以在k8s.io/kubelet/pkg/apis/下获得（[＃92632](https://github.com/kubernetes/kubernetes/pull/92632)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）[SIG节点和测试]

- 列举了更少的候选人来抢占来提高大型集群的性能。（[＃94814](https://github.com/kubernetes/kubernetes/pull/94814)，[@adtac](https://github.com/adtac)）

- 修复自定义指标的转化。（[＃94481](https://github.com/kubernetes/kubernetes/pull/94481)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94481)[-t](https://github.com/wojtek-t)）[SIG API机械和仪器]

- 默认情况下，现在禁用kubelet提供的GPU指标。（[＃95184](https://github.com/kubernetes/kubernetes/pull/95184)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）

- 如果启用了BoundServiceAccountTokenVolume，则群集管理员可以使用指标`serviceaccount_stale_tokens_total`来监视依赖于扩展令牌的工作负载。如果没有此类工作负载，请通过`kube-apiserver`以标志`--service-account-extend-token-expiration=false`（[＃96273](https://github.com/kubernetes/kubernetes/pull/96273)，[@zshihang](https://github.com/zshihang)）开头关闭扩展令牌。[SIG API机械与认证]

- 在kubelet中引入对基于exec的容器注册表凭据提供程序插件的alpha支持。（[＃94196](https://github.com/kubernetes/kubernetes/pull/94196)，[@andrewsykim](https://github.com/andrewsykim)）[SIG节点和发行版]

- 引入了HPA的度量标准源，该度量标准源允许根据容器资源的使用量进行扩展。（[＃](https://github.com/kubernetes/kubernetes/pull/90691)[90691](https://github.com/arjunrn)，[@arjunrn](https://github.com/arjunrn)）[SIG API机械，应用程序，自动[缩放](https://github.com/arjunrn)和CLI]

- Kube-apiserver现在删除过期的kube-apiserver租赁对象：

  - 该功能位于功能门下`APIServerIdentity`。
  - 将标记添加到kube-apiserver：`identity-lease-garbage-collection-check-period-seconds`（[＃95895](https://github.com/kubernetes/kubernetes/pull/95895)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械，应用程序，[身份](https://github.com/roycaihw)验证和测试]

- Kube-controller-manager：可以限制批量插件通过设置来联系本地和环回地址`--volume-host-allow-local-loopback=false`，或者通过设置来限制联系特定的CIDR范围`--volume-host-cidr-denylist`（例如，`--volume-host-cidr-denylist=127.0.0.1/28,feed::/16`）（[＃91785](https://github.com/kubernetes/kubernetes/pull/91785)，[@mattcary](https://github.com/mattcary)）[SIG API机械，应用程序，[身份](https://github.com/mattcary)验证，CLI ，网络，节点，存储和测试]

- 迁移调度程序，控制器-管理器和云控制器-管理器以使用LeaseLock（[＃94603](https://github.com/kubernetes/kubernetes/pull/94603)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94603)[-t](https://github.com/wojtek-t)）[SIG API机械，应用程序，云提供程序和调度]

- 修改DNS-1123错误消息以指示未完全遵循RFC 1123（[＃94182](https://github.com/kubernetes/kubernetes/pull/94182)，[@mattfenwick](https://github.com/mattfenwick)）[SIG API机械，应用程序，[身份](https://github.com/mattfenwick)验证，网络和节点]

- 将Pod的可配置fsgroup更改策略移至Beta（[＃96376](https://github.com/kubernetes/kubernetes/pull/96376)，[@ gnufied](https://github.com/gnufied)）[SIG应用和存储]

- 引入了新标记，即--topology-manager-scope = container | pod。默认值为“容器”范围。（[＃92967](https://github.com/kubernetes/kubernetes/pull/92967)，[@cezaryzukowski](https://github.com/cezaryzukowski)）[SIG仪器，节点和测试]

- 新的参数`defaultingType`为`PodTopologySpread`插件允许使用限定的或用户提供的默认约束K8S（[＃95048](https://github.com/kubernetes/kubernetes/pull/95048)，[@alculquicondor](https://github.com/alculquicondor)）[SIG调度]

- 可以使用AddedAffinity配置NodeAffinity插件。（[＃96202](https://github.com/kubernetes/kubernetes/pull/96202)，[@alculquicondor](https://github.com/alculquicondor)）[SIG节点，计划和测试]

- 将RuntimeClass功能升级为GA。将node.k8s.io API组从v1beta1升级到v1。（[＃95718](https://github.com/kubernetes/kubernetes/pull/95718)，[@SergeyKanzhelev](https://github.com/SergeyKanzhelev)）[SIG应用，[身份](https://github.com/SergeyKanzhelev)验证，节点，计划和测试]

- 提醒：不赞成使用标签“ failure-domain.beta.kubernetes.io/zone”和“ failure-domain.beta.kubernetes.io/region”，而应使用“ topology.kubernetes.io/zone”和“ topology.kubernetes” .io / region”。“ failure-domain.beta ...”标签的所有用户都应切换到“ topology ...”等效项。（[＃96033](https://github.com/kubernetes/kubernetes/pull/96033)，[@thockin](https://github.com/thockin)）[SIG API机械，应用程序，CLI，云提供程序，网络，节点，计划，存储和测试]

- 现在，服务器端应用将LabelSelector字段视为原子字段（意味着整个选择器由单个编写者管理并一起更新），因为它们包含相互关联且不可分割的字段，这些字段无法以直观的方式合并。（[＃93901](https://github.com/kubernetes/kubernetes/pull/93901)，[@jpbetz](https://github.com/jpbetz)）[SIG API机制，Auth，CLI，云提供程序，群集生命周期，检测，网络，节点，存储和测试]

- 服务现在将具有一个`clusterIPs`领域`clusterIP`。 `clusterIPs[0]`是的同义词`clusterIP`，将在创建和更新操作时同步化。（[＃95894](https://github.com/kubernetes/kubernetes/pull/95894)，[@thockin](https://github.com/thockin)）[SIG网络]

- ServiceAccountIssuerDiscovery功能闸现在为Beta，默认情况下已启用。（[＃91921](https://github.com/kubernetes/kubernetes/pull/91921)，[@mtaufen](https://github.com/mtaufen)）[SIG[身份](https://github.com/mtaufen)验证]

- 现在，不带“ preserveUnknownFields：false”的v1beta1 CRD的状态显示为“ spec.preserveUnknownFields：无效值：true：必须为false”。（[＃93078](https://github.com/kubernetes/kubernetes/pull/93078)，[@vareti](https://github.com/vareti)）

- 如果启用了新功能Gate MixedProtocolLBService，则可以在同一LoadBalancer服务中使用混合协议值。默认情况下，功能门是禁用的。用户必须为API服务器启用它。（[＃94028](https://github.com/kubernetes/kubernetes/pull/94028)，[@janosi](https://github.com/janosi)）[SIG API机械和应用程序]

- 此PR将引入一个功能门CSIServiceAccountToken以及中的两个附加字段`CSIDriverSpec`。（[＃93130](https://github.com/kubernetes/kubernetes/pull/93130)，[@zshihang](https://github.com/zshihang)）[SIG API机械，应用程序，[身份](https://github.com/zshihang)验证，CLI，网络，节点，存储和测试]

- 用户可以使用功能门尝试cronjob控制器v2。这将是将来版本中的默认控制器。（[＃93370](https://github.com/kubernetes/kubernetes/pull/93370)，[@ alaypatel07](https://github.com/alaypatel07)）[SIG API机械，应用程序，[身份](https://github.com/alaypatel07)验证和测试]

- VolumeSnapshotDataSource在1.20版（[＃95282](https://github.com/kubernetes/kubernetes/pull/95282)，[@ xing-yang](https://github.com/xing-yang)）中移至GA [SIG Apps]

- WinOverlay功能已升级到Beta版（[＃94807](https://github.com/kubernetes/kubernetes/pull/94807)，[@ksubrmnn](https://github.com/ksubrmnn)）[SIG Windows]

### 特征

- `apiserver_request_filter_duration_seconds`引入了新的度量标准，以秒为单位度量请求过滤器的延迟。（[＃95207](https://github.com/kubernetes/kubernetes/pull/95207)，[@tkashem](https://github.com/tkashem)）[SIG API机械和仪器]

- Kubernetes调度程序在`/metrics/resources`端点下报告了一组新的Alpha指标，使管理员可以轻松查看资源消耗（Pod上所有资源的请求和限制），并将其与Pod的实际使用量或节点容量进行比较。（[＃94866](https://github.com/kubernetes/kubernetes/pull/94866)，[@smarterclayton](https://github.com/smarterclayton)）[SIG API机械，工具，节点和调度]

- 添加--experimental-logging-sanitization标志，启用运行时保护，以免泄露日志中的敏感数据（[＃96370](https://github.com/kubernetes/kubernetes/pull/96370)，[@serathius](https://github.com/serathius)）[SIG API机械，集群生命周期和检测]

- 添加一个StorageVersionAPI功能闸，使API服务器在处理某些写入请求之前更新storageversions。此功能使存储迁移器可以管理内置资源的存储迁移。要启用此功能，需要启用internal.apiserver.k8s.io/v1alpha1 API和APIServerIdentity功能门。（[＃93873](https://github.com/kubernetes/kubernetes/pull/93873)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械，认证和测试]

- 添加用于执行递归权限更改所花费时间的度量标准（[＃95866](https://github.com/kubernetes/kubernetes/pull/95866)，[@JornShen](https://github.com/JornShen)）[SIG仪表和存储]

- 添加新`vSphere`指标：`cloudprovider_vsphere_vcenter_versions`。它的内容显示`vCenter`主机名以及相关的服务器版本。（[＃94526](https://github.com/kubernetes/kubernetes/pull/94526)，[@ Danil-Grigorev](https://github.com/Danil-Grigorev)）[SIG云提供程序和工具]

- 添加一个新标志来设置Windows节点上kubelet的优先级，以使工作负载不会通过破坏kubelet进程淹没那里的节点。（[＃96051](https://github.com/kubernetes/kubernetes/pull/96051)，[@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)）[SIG节点和Windows]

- 将功能添加到大小支持内存的卷（[＃94444](https://github.com/kubernetes/kubernetes/pull/94444)，[@ derekwaynecarr](https://github.com/derekwaynecarr)）中[SIG存储和测试]

- 使用新`kubectl delete foreground|background|orphan`选项将前景级联删除添加到kubectl 。（[＃93384](https://github.com/kubernetes/kubernetes/pull/93384)，[@ zhouya0](https://github.com/zhouya0)）

- 添加Azure服务操作（路由和负载平衡器）的指标。（[＃94124](https://github.com/kubernetes/kubernetes/pull/94124)，[@ nilo19](https://github.com/nilo19)）[SIG Cloud Provider and Instrumentation]

- 在Azure帐户创建中添加网络规则支持。（[＃94239](https://github.com/kubernetes/kubernetes/pull/94239)，[@andyzhangx](https://github.com/andyzhangx)）

- 添加node_authorizer_actions_duration_seconds指标，该指标可用于估计节点授权者的负载。（[＃92466](https://github.com/kubernetes/kubernetes/pull/92466)，[@mborsz](https://github.com/mborsz)）[SIG API机械，认证和检测]

- 将基于pod_的CPU和内存指标添加到Kubelet的/ metrics / resource端点（[＃95839](https://github.com/kubernetes/kubernetes/pull/95839)，[@egernst](https://github.com/egernst)）[SIG仪器，节点和测试]

- 已将`get-users`和添加`delete-user`到`kubectl config`子命令（[＃89840](https://github.com/kubernetes/kubernetes/pull/89840)，[@eddiezane](https://github.com/eddiezane)）[SIG CLI]

- 添加了计数器指标“ apiserver_request_self”以对带有动词，资源和子资源标签的API服务器自我请求进行计数。（[＃94288](https://github.com/kubernetes/kubernetes/pull/94288)，[@LogicalShark](https://github.com/LogicalShark)）[SIG API机械，[身份](https://github.com/LogicalShark)验证，检测和调度]

- 添加了新的k8s.io/component-helpers存储库，为（核心）组件提供了共享的帮助程序代码。（[＃92507](https://github.com/kubernetes/kubernetes/pull/92507)，[@ingvagabund](https://github.com/ingvagabund)）[SIG应用，节点，发行和计划]

- 将`create ingress`命令添加到`kubectl`（[＃78153](https://github.com/kubernetes/kubernetes/pull/78153)，[@amimof](https://github.com/amimof)）[SIG CLI和网络]

- 在node-local-cache插件上添加无头服务。（[＃88412](https://github.com/kubernetes/kubernetes/pull/88412)，[@stafot](https://github.com/stafot)）[SIG云提供商和网络]

- 允许在不同平台上交叉编译kubernetes。（[＃94403](https://github.com/kubernetes/kubernetes/pull/94403)，[@bnrjee](https://github.com/bnrjee)）[SIG版本]

- Azure：支持共享一个IP地址的多个服务（[＃94991](https://github.com/kubernetes/kubernetes/pull/94991)，[@ nilo19](https://github.com/nilo19)）[SIG云提供程序]

- CRD：对于结构模式，现在将删除不可为空的null映射字段，并且如果有默认值，则默认为默认值。列表中的空项目将继续保留，如果不能为空，则验证失败。（[＃95423](https://github.com/kubernetes/kubernetes/pull/95423)，[@apelisse](https://github.com/apelisse)）[SIG API机械]

- 更改：将默认的“ Accept：*/* ”标头添加到HTTP探针。见https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#http-probes（https://github.com/kubernetes/website/pull/24756） （[＃95641](https://github.com/kubernetes/kubernetes/pull/95641)，[@ fonsecas72](https://github.com/fonsecas72)）[SIG网络和节点]

- 现在，可以通过KUBERNETES_EXEC_INFO环境变量在当前群集信息中传递客户端证书凭据插件。（[＃95489](https://github.com/kubernetes/kubernetes/pull/95489)，[@ankeesler](https://github.com/ankeesler)）[SIG API机械和认证]

- 命令来启动网络代理更改自'KUBE_ENABLE_EGRESS_VIA_KONNECTIVITY_SERVICE ./cluster/kube-up.sh'到'KUBE_ENABLE_KONNECTIVITY_SERVICE =真./hack/kube-up.sh'（[＃92669](https://github.com/kubernetes/kubernetes/pull/92669)，[@Jefftree](https://github.com/Jefftree)）[SIG云供应商]

- 通过服务注释配置AWS LoadBalancer运行状况检查协议。（[＃94546](https://github.com/kubernetes/kubernetes/pull/94546)，[@kishorj](https://github.com/kishorj)）

- DefaultPodTopologySpread升级到Beta。默认情况下，功能门处于启用状态。（[＃95631](https://github.com/kubernetes/kubernetes/pull/95631)，[@alculquicondor](https://github.com/alculquicondor)）[SIG计划和测试]

- PodFsGroupChangePolicy的E2e测试（[＃96247](https://github.com/kubernetes/kubernetes/pull/96247)，[@ saikat-royc](https://github.com/saikat-royc)）[SIG存储和测试]

- 临时容器现在应用与[initContainers](https://github.com/kubernetes/kubernetes/pull/94896)和容器相同的API默认值（[＃94896](https://github.com/kubernetes/kubernetes/pull/94896)，[@ wawa0210](https://github.com/wawa0210)）[SIG Apps和CLI]

- 将Pod Resources API升级到GA引入了pod_resources_endpoint_requests_total指标，该指标跟踪对pod资源API的请求总数（[＃92165](https://github.com/kubernetes/kubernetes/pull/92165)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）[SIG仪器，节点和测试]

- 现在，在双栈裸机集群中，您可以将双栈IP传递给`kubelet --node-ip`。例如：`kubelet --node-ip 10.1.0.5,fd01::0005`。非裸金属群集尚不支持此功能。

  在节点具有双栈地址的双栈群集中，hostNetwork Pod现在将获得双栈PodIP。（[＃95239](https://github.com/kubernetes/kubernetes/pull/95239)，[@danwinship](https://github.com/danwinship)）[SIG网络和节点]

- 介绍api-extensions类别，该类别将返回：例如，当在kubectl get中使用时，对入场配置进行突变，验证入场配置，CRD和APIService。（[＃95603](https://github.com/kubernetes/kubernetes/pull/95603)，[@soltysh](https://github.com/soltysh)）[SIG API机械]

- 引入了一个新的GCE特定集群创建变量KUBE_PROXY_DISABLE。设置为true时，这将跳过kube-proxy（守护程序集或静态pod）的创建。这可以用来独立于节点的生命周期来控制kube-proxy的生命周期。（[＃91977](https://github.com/kubernetes/kubernetes/pull/91977)，[@varunmar](https://github.com/varunmar)）[SIG云提供商]

- Kube-apiserver现在维护一个Lease对象来标识自己：

  - 该功能位于功能门下`APIServerIdentity`。
  - 向kube-apiserver添加了两个标志：`identity-lease-duration-seconds`，`identity-lease-renew-interval-seconds`（[＃95533](https://github.com/kubernetes/kubernetes/pull/95533)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械]

- Kube-apiserver：现在可以使用来配置对etcd进行运行状况检查时使用的超时`--etcd-healthcheck-timeout`。默认超时为2秒，与以前的行为匹配。（[＃93244](https://github.com/kubernetes/kubernetes/pull/93244)，[@ Sh4d1](https://github.com/Sh4d1)）[SIG API机械]

- Kube-apiserver：添加了对使用`--audit-log-compress`（[＃94066](https://github.com/kubernetes/kubernetes/pull/94066)，[@lojies](https://github.com/lojies)）压缩旋转审核日志文件的支持[SIG API的机制和认证]

- 如果当前系统时间在已加载证书的NotBefore和NotAfter范围之外，则Kubeadm现在将显示警告而不是抛出错误。（[＃94504](https://github.com/kubernetes/kubernetes/pull/94504)，[@ neolit123](https://github.com/neolit123)）

- Kubeadm：添加飞行前检查，以确保控制平面节点至少具有1700MB RAM（[＃93275](https://github.com/kubernetes/kubernetes/pull/93275)，[@ xlgao-zju](https://github.com/xlgao-zju)）[SIG集群生命周期]

- Kubeadm：将“ --cluster-name”标志添加到“ kubeadm alpha kubeconfig用户”，以允许在生成的kubeconfig文件中配置集群名称（[＃93992](https://github.com/kubernetes/kubernetes/pull/93992)，[@ prabhu43](https://github.com/prabhu43)）[SIG集群生命周期]

- Kubeadm：将“ --kubeconfig”标志添加到“ kubeadm init phase upload-certs”命令，以允许用户传递kubeconfig文件的自定义位置。（[＃94765](https://github.com/kubernetes/kubernetes/pull/94765)，[@ zhanw15](https://github.com/zhanw15)）[SIG集群生命周期]

- Kubeadm：默认情况下，使etcd pod请求100m CPU，100Mi内存和100Mi ephemeral_storage（[＃94479](https://github.com/kubernetes/kubernetes/pull/94479)，[@ knight42](https://github.com/knight42)）[SIG集群生命周期]

- Kubeadm：使命令“ kubeadm alpha kubeconfig用户”接受“ --config”标志，并删除以下标志：

  - apiserver-advertise-address / apiserver-bind-port：使用InitConfiguration中的localAPIEndpoint或ClusterConfiguration中的controlPlaneEndpoint。
  - cluster-name：使用ClusterConfiguration中的clusterName
  - cert-dir：使用ClusterConfiguration中的certificateDir（[＃94879](https://github.com/kubernetes/kubernetes/pull/94879)，[@ knight42](https://github.com/knight42)）[SIG群集生命周期]

- Kubectl create现在支持创建入口对象。（[＃94327](https://github.com/kubernetes/kubernetes/pull/94327)，[@rikatz](https://github.com/rikatz)）[SIG CLI和网络]

- Kubectl推出历史记录sts / sts-name --revision = some-revision将开始显示该指定修订版（[＃86506](https://github.com/kubernetes/kubernetes/pull/86506)，[@dineshba](https://github.com/dineshba)）上sts的详细视图[SIG CLI]

- Kubectl：以前，用户无法通过KUBECTL_EXTERNAL_DIFF env向外部差异工具提供参数。现在，此版本允许用户为KUBECTL_EXTERNAL_DIFF env指定args。（[＃95292](https://github.com/kubernetes/kubernetes/pull/95292)，[@dougsland](https://github.com/dougsland)）[SIG CLI]

- Kubemark现在在单个群集中同时支持实节点和空心节点。（[＃93201](https://github.com/kubernetes/kubernetes/pull/93201)，[@ellistarn](https://github.com/ellistarn)）[SIG可伸缩性]

- Kubernetes E2E测试映像清单清单现在包含Windows映像。（[＃77398](https://github.com/kubernetes/kubernetes/pull/77398)，[@claudiubelu](https://github.com/claudiubelu)）[SIG测试和Windows]

- Kubernetes现在使用go1.15.2构建

  - 版本：更新至k/repo-infra@v0.1.1（支持go1.15.2）

  - 构建：使用go-runner：buster-v2.0.1（使用go1.15.1构建）

  - bazel：用Starlark构建设置标志替换--features

  - hack / lib / util.sh：一些bash清理

    - 切换了一个位置以使用kube :: logging
    - make kube :: util :: find-binary在找不到任何内容时会返回错误，从而使hack脚本快速失败，而不是出现“二进制未找到”错误。
    - 这需要删除一些genfeddoc内容。自从我们删除了federation /之后，该二进制文件就不再存在于k / k存储库中，而且我也没有在[https://github.com/kubernetes-sigs/kubefed/中](https://github.com/kubernetes-sigs/kubefed/)看到它。我假设它已经一去不复返了。

  - bazel：直接从go_binary_conditional_pure输出go_binary规则

    来自：[@mikedanese](https://github.com/mikedanese)：而不是别名。别名以多种方式令人烦恼。现在，这特别困扰我，因为它们使操作图更难以以编程方式进行分析。通过在此处使用别名，我们将需要处理可能别名的go_binary目标并取消对有效目标的引用。

    该注释引用了一个问题，`pure = select(...)`考虑到现在的版本，该问题似乎已解决。

  - 使kube :: util :: find-binary不依赖于bazel-out /结构

    实现一个方面，输出用于go二进制文件的go_build_mode元数据，并在二进制选择期间使用它。（[＃94449](https://github.com/kubernetes/kubernetes/pull/94449)，[@justaugustus](https://github.com/justaugustus)）[SIG体系结构，CLI，群集生命周期，节点，发布和测试]

- Kubernetes现在使用go1.15.5构建

  - 版本：更新至k/repo-infra@v0.1.2（支持go1.15.5）（[＃95776](https://github.com/kubernetes/kubernetes/pull/95776)，[@justaugustus](https://github.com/justaugustus)）[SIG云提供程序，规范，发布和测试]

- 当使用污点和节点相似性时，新的默认调度插件顺序减少了调度和抢占延迟（[＃95539](https://github.com/kubernetes/kubernetes/pull/95539)，[@soulxu](https://github.com/soulxu)）[SIG调度]

- 仅在附加/分离时更新Azure数据磁盘（[＃94265](https://github.com/kubernetes/kubernetes/pull/94265)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 将SupportNodePidsLimit升级为GA，以提供节点到容器的PID隔离。推广SupportPodPidsLimited to GA以提供限制每个Pod的PID的功能。（[＃94140](https://github.com/kubernetes/kubernetes/pull/94140)，[@derekwaynecarr](https://github.com/derekwaynecarr)）

- API对象（Pod，Service，NetworkPolicy）中的SCTP支持现在为GA。请注意，这对是否在内核级别的节点上启用SCTP没有影响，并且请注意，某些云平台和网络插件不支持SCTP通信。（[＃95566](https://github.com/kubernetes/kubernetes/pull/95566)，[@danwinship](https://github.com/danwinship)）[SIG应用和网络]

- 如果新旧Pod的resourceVersion相同，则Scheduler现在将忽略Pod更新事件。（[＃96071](https://github.com/kubernetes/kubernetes/pull/96071)，[@ Huang-Wei](https://github.com/Huang-Wei)）[SIG调度]

- 计划框架：将Run [Pre] ScorePlugins函数公开给PreemptionHandle，可在PostFilter扩展点中使用。（[＃93534](https://github.com/kubernetes/kubernetes/pull/93534)，[@everpeace](https://github.com/everpeace)）[SIG计划和测试]

- 当启用DefaultPodTopologySpread功能（[＃95448](https://github.com/kubernetes/kubernetes/pull/95448)，[@alculquicondor](https://github.com/alculquicondor)）时，SelectorSpreadPriority映射到PodTopologySpread插件[SIG计划]

- 将GCE节点启动脚本日志发送到控制台和日志。（[＃95311](https://github.com/kubernetes/kubernetes/pull/95311)，[@karan](https://github.com/karan)）

- SetHostnameAsFQDN已升级为Beta，因此默认情况下已启用。（[＃95267](https://github.com/kubernetes/kubernetes/pull/95267)，[@javidiaz](https://github.com/javidiaz)）[SIG节点]

- 支持[service.beta.kubernetes.io/azure-pip-ip-tags]批注，以允许客户指定ip标签以影响Azure中的公共IP创建[Tag1 = Value1，Tag2 = Value2等]（[＃94114](https://github.com/kubernetes/kubernetes/pull/94114)，[@MarcPow](https://github.com/MarcPow)）[SIG云提供商]

- 支持针对云提供商托管资源的自定义标签（[＃96450](https://github.com/kubernetes/kubernetes/pull/96450)，[@ nilo19](https://github.com/nilo19)）[SIG云提供商]

- 支持自定义负载平衡器运行状况探测协议和请求路径（[＃96338](https://github.com/kubernetes/kubernetes/pull/96338)，[@ nilo19](https://github.com/nilo19)）[SIG云提供程序]

- 增加了对Windows容器映像（操作系统版本：1809、1903、1909、2004）的支持：pause：3.4映像。（[＃](https://github.com/kubernetes/kubernetes/pull/91452)[91452](https://github.com/claudiubelu)，[@claudiubelu](https://github.com/claudiubelu)）[SIG节点，版本和Windows]

- 在一个群集中支持多个标准负载均衡器（[＃96111](https://github.com/kubernetes/kubernetes/pull/96111)，[@ nilo19](https://github.com/nilo19)）[SIG Cloud Provider]

- Beta`RootCAConfigMap`功能门默认情况下处于启用状态，并导致kube-controller-manager向每个名称空间发布“ kube-root-ca.crt” ConfigMap。此ConfigMap包含一个CA捆绑包，用于验证与kube-apiserver的连接。（[＃](https://github.com/kubernetes/kubernetes/pull/96197)[96197](https://github.com/zshihang)，[@zshihang](https://github.com/zshihang)）[SIG API机械，应用程序，[身份](https://github.com/zshihang)验证和测试]

- kubelet_runtime_operations_duration_seconds度量标准存储桶设置为0.005 0.0125 0.03125 0.078125 0.1953125 0.48828125 1.220703125 3.0517578125 7.62939453125 19.073486328125 47.6837158203125 119.20928955078125 298.0232238769531和745.0580596923828秒（[＃96054](https://github.com/kubernetes/kubernetes/pull/96054)，[@alvaroman](https://github.com/alvaroaleman)）

- 有一个新的pv_collector_total_pv_count度量标准，该度量标准通过卷插件名称和卷模式对持久卷进行计数。（[＃95719](https://github.com/kubernetes/kubernetes/pull/95719)，[@tsmetana](https://github.com/tsmetana)）[SIG应用，仪器，存储和测试]

- 卷快照e2e测试，用于验证PVC和VolumeSnapshotContent终结器（[＃95863](https://github.com/kubernetes/kubernetes/pull/95863)，[@ RaunakShah](https://github.com/RaunakShah)）[SIG云提供程序，存储和测试]

- 在执行kubectl apply / diff到当前正在删除的资源时警告用户。（[＃95544](https://github.com/kubernetes/kubernetes/pull/95544)，[@SaiHarshaK](https://github.com/SaiHarshaK)）[SIG CLI]

- `kubectl alpha debug`已毕业到beta版了`kubectl debug`。（[＃96138](https://github.com/kubernetes/kubernetes/pull/96138)，[@verb](https://github.com/verb)）[SIG CLI和测试]

- `kubectl debug`在复制用于调试的Pod时获得更改容器映像的支持，类似于`kubectl set image`工作原理。请参阅`kubectl help debug`以获取更多信息。（[＃96058](https://github.com/kubernetes/kubernetes/pull/96058)，[@verb](https://github.com/verb)）[SIG CLI]

### 文献资料

- 伪造的动态客户端：List不会在UnstructuredList中保留TypeMeta的文档（[＃95117](https://github.com/kubernetes/kubernetes/pull/95117)，[@andrewsykim](https://github.com/andrewsykim)）[SIG API机制]
- Kubelet：删除CNI标志的alpha警告。（[＃94508](https://github.com/kubernetes/kubernetes/pull/94508)，[@andrewsykim](https://github.com/andrewsykim)）[SIG网络和节点]
- 更新有关外部云提供商的云提供商InstancesV2和Zones接口的文档和指南：
  - 删除InstancesV2的实验性警告
  - 文档说明InstancesV2的实现将禁用对区域的调用
  - 赞成使用InstancesV2（[＃96397](https://github.com/kubernetes/kubernetes/pull/96397)，[@andrewsykim](https://github.com/andrewsykim)）弃用区域[SIG云提供程序]

### 测试失败

- 解决了在群集上运行Ingress一致性测试的问题，该群集使用Ingress对象的终结器来管理释放的负载均衡器资源（[＃96742](https://github.com/kubernetes/kubernetes/pull/96742)，[@ spencerhance](https://github.com/spencerhance)）[SIG网络和测试]
- 一致性测试“验证具有相同hostPort但不同hostIP和协议的Pod之间没有冲突”现在除了功能之外，还验证了与每个hostPort的连接性。（[＃96627](https://github.com/kubernetes/kubernetes/pull/96627)，[@aojea](https://github.com/aojea)）[SIG计划和测试]

### 错误或回归

- 添加kubectl wait --ignore-not-found标志（[＃90969](https://github.com/kubernetes/kubernetes/pull/90969)，[@ zhouya0](https://github.com/zhouya0)）[SIG CLI]

- 通过Windows上的直接服务器返回（DSR）负载平衡器，为kube-proxy添加了对externalTrafficPolicy = Local设置的支持。（[＃93166](https://github.com/kubernetes/kubernetes/pull/93166)，[@ elweb9858](https://github.com/elweb9858)）[SIG网络]

- 使用pvc（[＃95635](https://github.com/kubernetes/kubernetes/pull/95635)，[@RaunakShah](https://github.com/RaunakShah)）更改措辞来描述[广告](https://github.com/kubernetes/kubernetes/pull/95635)[连播](https://github.com/RaunakShah)[SIG CLI]

- 现在，解决了`volume.kubernetes.io/storage-resizer`当PVC StorageClass已更新为树外配置程序时，阻止卷扩展控制器注释PVC的问题。（[＃94489](https://github.com/kubernetes/kubernetes/pull/94489)，[@ialidzhikov](https://github.com/ialidzhikov)）[SIG API机械，应用程序和存储]

- Azure ARM客户端：不要对空响应和http错误（[＃94078](https://github.com/kubernetes/kubernetes/pull/94078)，[@bpineau](https://github.com/bpineau)）进行[隔离](https://github.com/bpineau)（SIG Cloud Provider）

- Azure armclient退避步骤默认为1（不重试）。（[＃94180](https://github.com/kubernetes/kubernetes/pull/94180)，[@feiskyer](https://github.com/feiskyer)）

- Azure：修复了一个错误，如果配置了错误的Azure VMSS名称，kube-controller-manager将会恐慌（[＃94306](https://github.com/kubernetes/kubernetes/pull/94306)，[@ knight42](https://github.com/knight42)）[SIG云提供程序]

- 审核事件的apiserver_request_duration_seconds指标和RequestReceivedTimestamp字段现在都考虑了请求在apiserver请求过滤器中花费的时间。（[＃94903](https://github.com/kubernetes/kubernetes/pull/94903)，[@tkashem](https://github.com/tkashem)）

- 构建/库/发行版：在构建服务器映像时明确使用“ --platform”

  当我们切换到go-runner来构建apiserver，controller-manager和Scheduler服务器组件时，我们不再在映像名称中引用各个体系结构，尤其是在服务器映像Dockerfile的'FROM'指令中。

  结果，非amd64映像的服务器映像将以go-runner amd64二进制文件而不是与该体系结构匹配的go-runner复制。

  该提交显式设置了“ --platform = linux / $ {arch}”，以确保我们从清单列表中提取正确的go-runner拱。

  之前： `FROM ${base_image}`

  之后： `FROM --platform=linux/${arch} ${base_image}`（[＃94552](https://github.com/kubernetes/kubernetes/pull/94552)，[@justaugustus](https://github.com/justaugustus)）[SIG发行]

- 将节点问题检测器版本升级到v0.8.5，以使用Linux内核5.1+（[＃96716](https://github.com/kubernetes/kubernetes/pull/96716)，[@ tosi3k](https://github.com/tosi3k)）修复OOM检测[SIG云提供程序，可伸缩性和测试]

- 可以在卷附件期间部署CSIDriver对象。（[＃93710](https://github.com/kubernetes/kubernetes/pull/93710)，[@ Jiawei0227](https://github.com/Jiawei0227)）[SIG应用，节点，存储和测试]

- 即使未提供ceph.conf，Ceph RBD卷扩展现在也可以工作。（[＃92027](https://github.com/kubernetes/kubernetes/pull/92027)，[@juliantaylor](https://github.com/juliantaylor)）

- 在csi和flexvolume的fsgroupapplymetrics中更改插件名称，以区分不同的驱动程序（[＃95892](https://github.com/kubernetes/kubernetes/pull/95892)，[@JornShen](https://github.com/JornShen)）[SIG仪表，存储和测试]

- 更改吊舱UID的计算，以使静态吊舱获得唯一值-在就地升级后，将导致所有容器被杀死并重新创建。（[＃87461](https://github.com/kubernetes/kubernetes/pull/87461)，[@bboreham](https://github.com/bboreham)）[SIG节点]

- 将挂载方式从systemd更改为普通挂载，但ceph和glusterfs intree-volume除外。（[＃94916](https://github.com/kubernetes/kubernetes/pull/94916)，[@smileusd](https://github.com/smileusd)）[SIG应用，云提供商，网络，节点，存储和测试]

- 已恢复对1.20.0-beta.2中超时参数处理的更改，以避免破坏与现有客户端的向后兼容性。（[＃96727](https://github.com/kubernetes/kubernetes/pull/96727)，[@liggitt](https://github.com/liggitt)）[SIG API机械和测试]

- 使用nodeport（[＃71573](https://github.com/kubernetes/kubernetes/pull/71573)，[@JacobTanenbaum](https://github.com/JacobTanenbaum)）时，清除端点更改上的UDP conntrack条目[SIG网络]

- 云节点控制器：处理来自getProviderID（[＃95342](https://github.com/kubernetes/kubernetes/pull/95342)，[@nicolehanjing](https://github.com/nicolehanjing)）的空providerID [SIG Cloud Provider]

- 禁用事件的监视缓存（[＃96052](https://github.com/kubernetes/kubernetes/pull/96052)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/96052)[-t](https://github.com/wojtek-t)）[SIG API机械]

- `LocalStorageCapacityIsolation`在计划期间将禁用禁用功能门。（[＃96092](https://github.com/kubernetes/kubernetes/pull/96092)，[@ Huang-Wei](https://github.com/Huang-Wei)）[SIG调度]

- 不要对空元素进行排序。（[＃94666](https://github.com/kubernetes/kubernetes/pull/94666)，[@soltysh](https://github.com/soltysh)）[SIG CLI]

- 双堆栈：默认情况下启用双堆栈功能门（[＃90439](https://github.com/kubernetes/kubernetes/pull/90439)，[@SataQiu](https://github.com/SataQiu)）时，使nodeipam与现有的单堆栈群集兼容[SIG API Machinery]

- 现在，API服务器会删除创建/更新/补丁请求中重复的所有者引用条目。现在，发送请求的客户端会在API响应中收到警告标头。客户应停止发送具有重复所有者引用的请求。API服务器可能最早于1.24拒绝此类请求。（[＃96185](https://github.com/kubernetes/kubernetes/pull/96185)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械和测试]

- 端点切片控制器现在将父级的服务标签镜像到其相应的端点切片。（[＃94443](https://github.com/kubernetes/kubernetes/pull/94443)，[@aojea](https://github.com/aojea)）

- 确保当Azure VMSS的网络接口为null（[＃94355](https://github.com/kubernetes/kubernetes/pull/94355)，[@feiskyer](https://github.com/feiskyer)）[SIG云提供程序]时，getPrimaryInterfaceID不会发生混乱。

- 公开并设置DelegatingAuthorizationOptions（[＃95725](https://github.com/kubernetes/kubernetes/pull/95725)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）的SubjectAccessReview客户端的默认超时[SIG API机械和云提供商]

- 公开并为TokenReview客户端设置DelegatingAuthenticationOptions（[＃96217](https://github.com/kubernetes/kubernetes/pull/96217)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）的默认超时[SIG API机械和云提供商]

- 修复了CVE-2020-8555的Quobyte客户端连接。（[＃95206](https://github.com/kubernetes/kubernetes/pull/95206)，[@misterikkit](https://github.com/misterikkit)）[SIG存储]

- 修复UDP和TCP数据包的IP碎片不支持LoadBalancer规则（[＃96464](https://github.com/kubernetes/kubernetes/pull/96464)，[@ nilo19](https://github.com/nilo19)）上的问题[SIG Cloud Provider]

- 修复了使用（旧式）调度程序策略时DefaultPreemption插件被禁用的错误。（[＃96439](https://github.com/kubernetes/kubernetes/pull/96439)，[@ Huang-Wei](https://github.com/Huang-Wei)）[SIG计划和测试]

- 修复了由于缺少资源组而导致负载均衡器删除卡住的错误。（[＃93962](https://github.com/kubernetes/kubernetes/pull/93962)，[@ phiphi282](https://github.com/phiphi282)）

- 修复kubelet中的并发映射写入错误（[＃93773](https://github.com/kubernetes/kubernetes/pull/93773)，[@ knight42](https://github.com/knight42)）[SIG节点]

- 修正`kubectl debug`Pod有多个init或临时容器的情况。（[＃94580](https://github.com/kubernetes/kubernetes/pull/94580)，[@ kiyoshim55](https://github.com/kiyoshim55)）

- 修复了向“ kubeadm升级计划”命令（[＃94421](https://github.com/kubernetes/kubernetes/pull/94421)，[@rosti](https://github.com/rosti)）提供可选版本命令行参数时kubeadm因致命错误而失败的回归问题（SIG集群生命周期）

- 修复了大于4TB的磁盘的azure磁盘附加故障（[＃95463](https://github.com/kubernetes/kubernetes/pull/95463)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 修复了卸载磁盘（[＃95456](https://github.com/kubernetes/kubernetes/pull/95456)，[@andyzhangx](https://github.com/andyzhangx)）时Windows上的天蓝色磁盘数据丢失问题[SIG云提供程序和存储]

- 修复azure文件迁移恐慌（[＃94853](https://github.com/kubernetes/kubernetes/pull/94853)，[@andyzhangx](https://github.com/andyzhangx)）[SIG Cloud Provider]

- 修复JSON路径解析器中的错误，该错误在范围为空时发生错误（[＃95933](https://github.com/kubernetes/kubernetes/pull/95933)，[@brianpursley](https://github.com/brianpursley)）[SIG API机械]

- 修复客户端通用方法，以正确显示在某些环境中访问的API路径。（[＃74363](https://github.com/kubernetes/kubernetes/pull/74363)，[@aanm](https://github.com/aanm)）[SIG API机械]

- 修复了[虚拟机](https://github.com/kubernetes/kubernetes/pull/95177)不存在时分离天蓝色磁盘的问题（[＃95177](https://github.com/kubernetes/kubernetes/pull/95177)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 修复kube-apiserver（[＃94773](https://github.com/kubernetes/kubernetes/pull/94773)，[@tkashem](https://github.com/tkashem)）报告的etcd_object_counts指标[SIG API机械]

- 修复针对CRD对象的kube-apiserver指标错误报告的动词（[＃93523](https://github.com/kubernetes/kubernetes/pull/93523)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/93523)[-t](https://github.com/wojtek-t)）[SIG API机械和工具]

- 修复k8s.io/apimachinery/pkg/api/meta.SetStatusCondition以更新ObservedGeneration（[＃95961](https://github.com/kubernetes/kubernetes/pull/95961)，[@KnicKnic](https://github.com/KnicKnic)）[SIG API机械]

- 在数组类型上使用x-kubernetes-preserve-unknown-fields修复具有模式的CRD上的kubectl SchemaError。（[＃94888](https://github.com/kubernetes/kubernetes/pull/94888)，[@sttts](https://github.com/sttts)）[SIG API机械]

- 修复基础时间来回切换时kube-apiserver中的内存泄漏。（[＃96266](https://github.com/kubernetes/kubernetes/pull/96266)，[@ chenyw1990](https://github.com/chenyw1990)）[SIG API机械]

- 修复并行csinode更新期间节点上缺少的csi注释。（[＃94389](https://github.com/kubernetes/kubernetes/pull/94389)，[@pacoxu](https://github.com/pacoxu)）[SIG存储]

- 修复了针对Endpoints / EndpointSlice删除的network_programming_latency指标报告，在该报告中我们没有正确的时间戳（[＃95363](https://github.com/kubernetes/kubernetes/pull/95363)，[@ wojtek-t](https://github.com/wojtek-t)）[SIG网络和可伸缩性]

- 修复了Azure API使用非空的nextLink（[＃96211](https://github.com/kubernetes/kubernetes/pull/96211)，[@feiskyer](https://github.com/feiskyer)）返回空值时的分页问题[SIG Cloud Provider]

- 使用Azure管理身份（[＃96355](https://github.com/kubernetes/kubernetes/pull/96355)，[@andyzhangx](https://github.com/andyzhangx)）修复来自多个[ACR的](https://github.com/kubernetes/kubernetes/pull/96355)拉取图像错误[SIG Cloud Provider]

- 将竞态条件固定在timeCache锁上。（[＃94751](https://github.com/kubernetes/kubernetes/pull/94751)，[@auxten](https://github.com/auxten)）

- 修复了`kubectl portforward`何时在同一端口上配置TCP和UCP服务的回归问题。（[＃94728](https://github.com/kubernetes/kubernetes/pull/94728)，[@amorenoz](https://github.com/amorenoz)）

- 当节点在其[Pod](https://github.com/kubernetes/kubernetes/pull/95130)（[＃95130](https://github.com/kubernetes/kubernetes/pull/95130)，[@alculquicondor](https://github.com/alculquicondor)）之前被删除时，修复调度程序缓存快照[SIG调度]

- 修复`cloudprovider_azure_api_request_duration_seconds`指标存储桶以正确捕获延迟指标。以前，大多数调用将属于“ + Inf”存储桶。（[＃94873](https://github.com/kubernetes/kubernetes/pull/94873)，[@marwanad](https://github.com/marwanad)）[SIG云提供程序和工具]

- 修复可能错误地附加到错误节点的vSphere卷（[＃96224](https://github.com/kubernetes/kubernetes/pull/96224)，[@ gnufied](https://github.com/gnufied)）[SIG云提供程序和存储]

- 修复kube-apiserver指标的动词和范围报告（列表报告而不是GET）（[＃95562](https://github.com/kubernetes/kubernetes/pull/95562)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/95562)[-t](https://github.com/wojtek-t)）[SIG API机械和测试]

- 修复静态PV的vsphere分离失败（[＃95447](https://github.com/kubernetes/kubernetes/pull/95447)，[@ gnufied](https://github.com/gnufied)）[SIG云提供程序和存储]

- 修复：如果源不存在，请[执行“](https://github.com/andyzhangx)天蓝色磁盘调整大小”错误（[＃93011](https://github.com/kubernetes/kubernetes/pull/93011)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 修复：分离在Azure Stack（[＃94885](https://github.com/kubernetes/kubernetes/pull/94885)，[@andyzhangx](https://github.com/andyzhangx)）上损坏的azure磁盘[SIG Cloud Provider]

- 修复：处于连接状态时调整Azure磁盘大小的问题（[＃96705](https://github.com/kubernetes/kubernetes/pull/96705)，[@andyzhangx](https://github.com/andyzhangx)）[SIG Cloud Provider]

- 修复：smb有效路径错误（[＃95583](https://github.com/kubernetes/kubernetes/pull/95583)，[@andyzhangx](https://github.com/andyzhangx)）[SIG存储]

- 修复：在Windows挂载上使用sensitiveOptions（[＃94126](https://github.com/kubernetes/kubernetes/pull/94126)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序和存储]

- 修复了导致格式错误的错误`kubectl describe ingress`。（[＃94985](https://github.com/kubernetes/kubernetes/pull/94985)，[@howardjohn](https://github.com/howardjohn)）[SIG CLI和网络]

- 修正了在客户端去一臭虫，与新客户定制的`Dial`，`Proxy`，`GetCert`配置可能会过时的HTTP传输。（[＃95427](https://github.com/kubernetes/kubernetes/pull/95427)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械]

- 修复了阻止kubectl使用对象字段的x-kubernetes-preserve-unknown-fields验证带有模式的CRD的错误。（[＃96369](https://github.com/kubernetes/kubernetes/pull/96369)，[@gautierdelorme](https://github.com/gautierdelorme)）[SIG API机械和测试]

- 修复了一个错误，该错误阻止在存在经过验证的准入网络挂钩的情况下使用临时容器。（[＃94685](https://github.com/kubernetes/kubernetes/pull/94685)，[@verb](https://github.com/verb)）[SIG节点和测试]

- 修复了报告已删除apiservices的aggregator_unavailable_apiservice指标的错误。（[＃96421](https://github.com/kubernetes/kubernetes/pull/96421)，[@dgrisonnet](https://github.com/dgrisonnet)）[SIG API机械和仪器]

- 修复了以下错误：端点的不正确存储和比较导致端点控制器（[＃94112](https://github.com/kubernetes/kubernetes/pull/94112)，[@damemi](https://github.com/damemi)）的API[流](https://github.com/kubernetes/kubernetes/pull/94112)[量过大](https://github.com/damemi)[SIG应用，网络和测试]

- 修复了以下回归问题：`docker/default`如果存在允许`runtime/default`seccomp配置文件的PodSecurityPolicy ，则会阻止在1.19中创建带有seccomp批注的容器。（[＃95985](https://github.com/kubernetes/kubernetes/pull/95985)，[@saschagrunert](https://github.com/saschagrunert)）[SIG[身份](https://github.com/saschagrunert)验证]

- 修复了反射器中无法从API服务器1.17.0-1.18.5（[＃94316](https://github.com/kubernetes/kubernetes/pull/94316)，[@janeczku](https://github.com/janeczku)）的“资源太大版本”错误中恢复的错误[SIG API机械]

- 修复了当--sort-by和--containers标志一起使用时（[＃93692](https://github.com/kubernetes/kubernetes/pull/93692)，[@brianpursley](https://github.com/brianpursley)）不对kubectl顶部容器输出进行排序的错误（SIG CLI）

- 修复了kubelet在所有容器成功之后（[＃92614](https://github.com/kubernetes/kubernetes/pull/92614)，[@tnqn](https://github.com/tnqn)）为带有RestartPolicyOnFailure的pod创建额外的沙箱的问题[SIG节点和测试]

- 解决了在不指定端口（[＃94834](https://github.com/kubernetes/kubernetes/pull/94834)，[@liggitt](https://github.com/liggitt)）的情况下代理ipv6 pod的问题[SIG API机械和网络]

- 修复了非命名空间创建子资源假客户端测试的代码生成。（[＃96586](https://github.com/kubernetes/kubernetes/pull/96586)，[@Doude](https://github.com/Doude)）[SIG API机械]

- 修复了kubectl消耗（[＃95260](https://github.com/kubernetes/kubernetes/pull/95260)，[@amandahla](https://github.com/amandahla)）中的高CPU使用率[SIG CLI]

- 对于vSphere Cloud Provider，如果删除了工作节点的VM，则节点控制器（[＃92608](https://github.com/kubernetes/kubernetes/pull/92608)，[@lubronzhan](https://github.com/lubronzhan)）也将删除该节点[SIG Cloud Provider]

- 当其父级比例集丢失（[＃95289](https://github.com/kubernetes/kubernetes/pull/95289)，[@bpineau](https://github.com/bpineau)）时，优雅地删除节点[SIG Cloud Provider]

- 默认情况下，所有Kubernetes客户端都启用HTTP / 2连接运行状况检查。该功能应立即可用。如果需要，用户可以通过HTTP2_READ_IDLE_TIMEOUT_SECONDS和HTTP2_PING_TIMEOUT_SECONDS环境变量来调整功能。如果HTTP2_READ_IDLE_TIMEOUT_SECONDS设置为0，则该功能被禁用。（[＃95981](https://github.com/kubernetes/kubernetes/pull/95981)，[@caesarxuchao](https://github.com/caesarxuchao)）[SIG API机制，CLI，云提供程序，群集生命周期，检测和节点]

- 如果用户在请求URL中指定了无效的超时，则该请求将使用HTTP 400终止。

  - 如果用户在请求URL中指定的超时时间超过了apiserver允许的最大请求期限，则该请求将使用HTTP 400终止。（[＃96061](https://github.com/kubernetes/kubernetes/pull/96061)，[@tkashem](https://github.com/tkashem)）[SIG API机械，网络和测试]

- 如果我们在scaleUp行为或scaleDown行为上设置SelectPolicy MinPolicySelect，则Horizontal Pod Autoscaler不会自动正确缩放Pod的数量（[＃95647](https://github.com/kubernetes/kubernetes/pull/95647)，[@JoshuaAndrew](https://github.com/JoshuaAndrew)）[SIG Apps and Autoscaling]

- 忽略非Linux操作系统（[＃93220](https://github.com/kubernetes/kubernetes/pull/93220)，[@ wawa0210](https://github.com/wawa0210)）的apparmor [SIG节点和Windows]

- Windows pod启动时忽略root用户检查（[＃92355](https://github.com/kubernetes/kubernetes/pull/92355)，[@ wawa0210](https://github.com/wawa0210)）[SIG节点和Windows]

- 改进与nodePort端点更改conntrack条目清除相关的错误消息。（[＃96251](https://github.com/kubernetes/kubernetes/pull/96251)，[@ravens](https://github.com/ravens)）[SIG网络]

- 在双堆栈群集中，kubelet现在将同时设置IPv4和IPv6 iptables规则，这可能会解决某些问题，例如HostPorts。（[＃94474](https://github.com/kubernetes/kubernetes/pull/94474)，[@danwinship](https://github.com/danwinship)）[SIG网络和节点]

- 将AWS EBS io1卷的最大IOPS增加到当前的最大值（64,000）。（[＃](https://github.com/kubernetes/kubernetes/pull/90014)[90014](https://github.com/jacobmarble)，[@jacobmarble](https://github.com/jacobmarble)）

- ipvs：确保已加载选定的调度程序内核模块（[＃93040](https://github.com/kubernetes/kubernetes/pull/93040)，[@cmluciano](https://github.com/cmluciano)）[SIG网络]

- K8s.io/apimachinery：runtime.DefaultUnstructuredConverter.FromUnstructured现在可处理将整数字段转换为类型化的浮点值（[＃93250](https://github.com/kubernetes/kubernetes/pull/93250)，[@liggitt](https://github.com/liggitt)）[SIG API机械]

- 现在，Kube-proxy会修剪在loadBalancerSourceRanges中找到的多余空间以匹配服务验证。（[＃94107](https://github.com/kubernetes/kubernetes/pull/94107)，[@robscott](https://github.com/robscott)）[SIG网络]

- Kubeadm确保“ kubeadm reset”不会卸载根“ / var / lib / kubelet”目录（如果用户已将其挂载）。（[＃93702](https://github.com/kubernetes/kubernetes/pull/93702)，[@thtanaka](https://github.com/thtanaka)）

- Kubeadm现在确保即使没有更改etcd的版本，也可以在升级时重新生成etcd清单（[＃94395](https://github.com/kubernetes/kubernetes/pull/94395)，[@ rosti](https://github.com/rosti)）[SIG集群生命周期]

- 现在，如果用户提供了所有证书，密钥和kubeconfig，则在“ kubeadm join --control-plane”期间，Kubeadm会针对根CA，前代理CA和etcd CA丢失“ ca.key”文件（而不是错误提示）发出警告需要使用给定CA密钥签名的文件。（[＃94988](https://github.com/kubernetes/kubernetes/pull/94988)，[@ neolit123](https://github.com/neolit123)）

- Kubeadm：将丢失的“ --experimental-patches”标志添加到“ kubeadm init相位控制平面”（[＃95786](https://github.com/kubernetes/kubernetes/pull/95786)，[@ Sh4d1](https://github.com/Sh4d1)）[SIG集群生命周期]

- Kubeadm：确定升级期间是否支持运行版本的CoreDNS时避免恐慌（[＃94299](https://github.com/kubernetes/kubernetes/pull/94299)，[@zouyee](https://github.com/zouyee)）[SIG集群生命周期]

- Kubeadm：确保在控制平面初始化和加入过程中以0700权限创建etcd数据目录（[＃94102](https://github.com/kubernetes/kubernetes/pull/94102)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]

- Kubeadm：在kubeadm升级过程中有新的默认配置（[＃96907](https://github.com/kubernetes/kubernetes/pull/96907)，[@pacoxu](https://github.com/pacoxu)）时，应该触发修复coredns迁移[SIG集群生命周期]

- Kubeadm：修复了即使CRI套接字用于另一个CR（[＃94555](https://github.com/kubernetes/kubernetes/pull/94555)，[@SataQiu](https://github.com/SataQiu)），kubeadm仍尝试调用“ docker info”的错误[SIG集群生命周期]

- Kubeadm：对于Docker作为容器运行时，请在删除容器之前使“ kubeadm reset”命令停止容器（[＃94586](https://github.com/kubernetes/kubernetes/pull/94586)，[@BedivereZero](https://github.com/BedivereZero)）[SIG集群生命周期]

- Kubeadm：使kube-controller-manager和kube-scheduler的kubeconfig文件使用LocalAPIEndpoint而不是ControlPlaneEndpoint。这使kubeadm群集在不可变升级期间更能解决版本倾斜问题：[https](https://kubernetes.io/docs/setup/release/version-skew-policy/#kube-controller-manager-kube-scheduler-and-cloud-controller-manager) ://kubernetes.io/docs/setup/release/version-skew-policy/#kube-controller-manager-kube-scheduler-and-cloud-controller [-manager](https://kubernetes.io/docs/setup/release/version-skew-policy/#kube-controller-manager-kube-scheduler-and-cloud-controller-manager)（[＃94398](https://github.com/kubernetes/kubernetes/pull/94398)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]

- Kubeadm：放松对kubeconfig服务器URL的验证。允许用户定义自定义kubeconfig服务器URL，而无需在验证现有kubeconfig文件的过程中出错（例如，使用外部CA模式时）。（[＃94816](https://github.com/kubernetes/kubernetes/pull/94816)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]

- Kubectl：如果用户将标志放在插件名称之前（[＃92343](https://github.com/kubernetes/kubernetes/pull/92343)，[@ knight42](https://github.com/knight42)），[则会](https://github.com/knight42)出现打印错误[SIG CLI]

- Kubelet：假定`/proc/swaps`不存在时禁用交换功能（[＃93931](https://github.com/kubernetes/kubernetes/pull/93931)，[@SataQiu](https://github.com/SataQiu)）[SIG节点]

- 现在，新的Azure实例类型确实具有正确的最大数据磁盘计数信息。（[＃94340](https://github.com/kubernetes/kubernetes/pull/94340)，[@ialidzhikov](https://github.com/ialidzhikov)）[SIG云提供程序和存储]

- 端口映射现在允许将`containerPort`不同容器中的相同容器更改为不同容器，`hostPort`而无需显式命名该映射。（[＃94494](https://github.com/kubernetes/kubernetes/pull/94494)，[@SergeyKanzhelev](https://github.com/SergeyKanzhelev)）

- 在-v = 4而不是-v = 2（[＃94663](https://github.com/kubernetes/kubernetes/pull/94663)，[@soltysh](https://github.com/soltysh)）上打印go堆栈跟踪信息[SIG CLI]

- 在快速创建服务时重新创建EndpointSlices。（[＃94730](https://github.com/kubernetes/kubernetes/pull/94730)，[@robscott](https://github.com/robscott)）

- 减少vSphere卷的卷名长度（[＃96533](https://github.com/kubernetes/kubernetes/pull/96533)，[@gnufied](https://github.com/gnufied)）[SIG存储]

- 在emptyDir卷TearDown期间，删除就绪文件及其目录（在卷设置期间创建）。（[＃95770](https://github.com/kubernetes/kubernetes/pull/95770)，[@ jingxu97](https://github.com/jingxu97)）[SIG存储]

- 重组了iptables规则以解决性能问题（[＃95252](https://github.com/kubernetes/kubernetes/pull/95252)，[@tssurya](https://github.com/tssurya)）[SIG网络]

- 如果在kubelet配置中设置了非默认的cpuCFSQuotaPeriod，则需要功能部件标志CustomCPUCFSQuotaPeriod。（[＃94687](https://github.com/kubernetes/kubernetes/pull/94687)，[@karan](https://github.com/karan)）[SIG节点]

- 解决了1.19+版本中的回归问题，目标为已弃用的beta os / arch标签的工作负载在节点启动时陷入了NodeAffinity状态。（[＃96810](https://github.com/kubernetes/kubernetes/pull/96810)，[@liggitt](https://github.com/liggitt)）[SIG节点]

- 当遇到拥有不正确数据的ownerReferences时，解决垃圾收集控制器的不确定行为。`OwnerRefInvalidNamespace`当检测到子对象和所有者对象之间的名称空间不匹配时，将记录原因为的事件。该[kubectl检查-ownerreferences](https://github.com/kubernetes-sigs/kubectl-check-ownerreferences)工具可以在升级之前运行，以查找与无效ownerReferences现有对象。

  - 现在，将具有ownerReference引用命名空间类型的uid（该命名空间不存在于同一命名空间中）的命名空间对象统一视为该所有者不存在，并且删除子对象。
  - 现在可以一致地对待具有ownerReference引用命名空间类型的uid的群集范围内的对象，就像该所有者是不可解析的一样，并且垃圾回收器将忽略子对象。（[＃92743](https://github.com/kubernetes/kubernetes/pull/92743)，[@liggitt](https://github.com/liggitt)）[SIG API机械，应用和测试]

- 跳过[k8s.io/kubernetes@v1.19.0/test/e2e/storage/testsuites/base.go:162]：驱动程序azure磁盘不支持快照类型DynamicSnapshot-跳过跳过[k8s.io/kubernetes@v1 .19.0 / test / e2e / storage / testsuites / base.go：185]：驱动程序azure-disk不支持[ntfs-](https://github.com/kubernetes/kubernetes/pull/96144)跳过（[＃96144](https://github.com/kubernetes/kubernetes/pull/96144)，[@qinpingli](https://github.com/qinpingli)）[SIG存储和测试]

- StatefulSet Controller现在在创建Pod之前等待PersistentVolumeClaim删除。（[＃93457](https://github.com/kubernetes/kubernetes/pull/93457)，[@ ymmt2005](https://github.com/ymmt2005)）

- StreamWatcher现在以适当的顺序调用HandleCrash。（[＃93108](https://github.com/kubernetes/kubernetes/pull/93108)，[@ lixiaobing1](https://github.com/lixiaobing1)）

- 支持节点标签`node.kubernetes.io/exclude-from-external-load-balancers`（[＃95542](https://github.com/kubernetes/kubernetes/pull/95542)，[@ nilo19](https://github.com/nilo19)）[SIG Cloud Provider]

- 现在可以在服务创建期间指定AWS网络负载平衡器属性（[＃95247](https://github.com/kubernetes/kubernetes/pull/95247)，[@kishorj](https://github.com/kishorj)）[SIG Cloud Provider]

- `/debug/api_priority_and_fairness/dump_requests`apiserver上的路径将不再为每个免税优先级级别返回幻像行。（[＃93406](https://github.com/kubernetes/kubernetes/pull/93406)，[@MikeSpreitzer](https://github.com/MikeSpreitzer)）[SIG API机械]

- kube-apiserver将不再提供应在GA非alpha级中删除的API。Alpha级别将继续服务于已删除的API，以便CI不会立即中断。（[＃96525](https://github.com/kubernetes/kubernetes/pull/96525)，[@ deads2k](https://github.com/deads2k)）[SIG API机械]

- kubelet识别--containerd-namespace标志以配置cadvisor使用的命名空间。（[＃87054](https://github.com/kubernetes/kubernetes/pull/87054)，[@changyaowei](https://github.com/changyaowei)）[SIG节点]

- 如果有足够的健康豆荚，则可以成功驱逐PDB覆盖的不健康豆荚。（[＃94381](https://github.com/kubernetes/kubernetes/pull/94381)，[@michaelgugino](https://github.com/michaelgugino)）[SIG应用]

- 将Calico更新到v3.15.2（[＃94241](https://github.com/kubernetes/kubernetes/pull/94241)，[@lmm](https://github.com/lmm)）[SIG Cloud Provider]

- 将默认的etcd服务器版本更新为3.4.13（[＃94287](https://github.com/kubernetes/kubernetes/pull/94287)，[@jingyih](https://github.com/jingyih)）[SIG API机械，云提供程序，集群生命周期和测试]

- 更新max azure数据磁盘计数图（[＃96308](https://github.com/kubernetes/kubernetes/pull/96308)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序和存储]

- 在LB更新期间不处于成功置备状态的PIP时进行更新。（[＃95748](https://github.com/kubernetes/kubernetes/pull/95748)，[@ nilo19](https://github.com/nilo19)）[SIG云提供商]

- `pipName`更改服务的批注（[＃95813](https://github.com/kubernetes/kubernetes/pull/95813)，[@ nilo19](https://github.com/nilo19)）时更新前端IP配置[SIG Cloud Provider]

- 在路由协调循环（[＃96545](https://github.com/kubernetes/kubernetes/pull/96545)，[@ nilo19](https://github.com/nilo19)）中更新路由表标记[SIG Cloud Provider]

- 在运行状况检查SG规则（[＃93515](https://github.com/kubernetes/kubernetes/pull/93515)，[@ t0rr3sp3dr0](https://github.com/t0rr3sp3dr0)）中使用NLB子网CIDR代替VPC CIDR [SIG云提供程序]

- 用户将看到删除Pod的时间增加，并保证从api服务器中删除Pod将意味着从容器运行时删除所有资源。（[＃92817](https://github.com/kubernetes/kubernetes/pull/92817)，[@kmala](https://github.com/kmala)）[SIG节点]

- 现在可以`kubectl patch`使用该`--patch-file`标志指定很大的补丁，而不是直接在命令行中包含它们。在`--patch`和`--patch-file`标志是互斥的。（[＃93548](https://github.com/kubernetes/kubernetes/pull/93548)，[@smarterclayton](https://github.com/smarterclayton)）[SIG CLI]

- 卷绑定：未找到绑定的PV时，报告UnschedulableAndUnresolvable状态而不是错误（[＃95541](https://github.com/kubernetes/kubernetes/pull/95541)，[@cofyc](https://github.com/cofyc)）[SIG Apps，计划和存储]

- 通过kubectl（[＃92492](https://github.com/kubernetes/kubernetes/pull/92492)，[@eddiezane](https://github.com/eddiezane)）使用自定义动词创建Roles和ClusterRoles时发出警告而不是失败[SIG CLI]

- 当创建具有已设置volume.beta.kubernetes.io/storage-provisioner注释的PVC时，PV控制器可能会错误地删除新配置的PV，而不是将其绑定到PVC，具体取决于时间和系统负载。（[＃95909](https://github.com/kubernetes/kubernetes/pull/95909)，[@pohly](https://github.com/pohly)）[SIG应用和存储]

- [kubectl]当本地源文件不存在时失败（[＃90333](https://github.com/kubernetes/kubernetes/pull/90333)，[@bamarni](https://github.com/bamarni)）[SIG CLI]

### 其他（清理或片状）

- 处理cronjob控制器v2中的慢速cronjob lister并改善内存占用。（[＃96443](https://github.com/kubernetes/kubernetes/pull/96443)，[@ alaypatel07](https://github.com/alaypatel07)）[SIG应用]
- --redirect-container-streaming不再起作用。该标志将在v1.22中删除（[＃95935](https://github.com/kubernetes/kubernetes/pull/95935)，[@tallclair](https://github.com/tallclair)）[SIG节点]
- 一个新的指标`requestAbortsTotal`已引入中止计数为每个请求`group`，`version`，`verb`，`resource`，`subresource`和`scope`。（[＃95002](https://github.com/kubernetes/kubernetes/pull/95002)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）[SIG API机械，云提供程序，检测和调度]
- API优先级和公平性指标在标签名称中使用snake_case（[＃96236](https://github.com/kubernetes/kubernetes/pull/96236)，[@adtac](https://github.com/adtac)）[SIG API机械，集群生命周期，检测和测试]
- 在Pod内部一致性测试中添加细粒度的调试，以在运行一致性测试或声浮标测试时对潜在不健康节点的网络问题进行故障排除。（[＃93837](https://github.com/kubernetes/kubernetes/pull/93837)，[@ jayunit100](https://github.com/jayunit100)）
- 添加以下指标：
  - network_plugin_operations_total
  - network_plugin_operations_errors_total（[＃93066](https://github.com/kubernetes/kubernetes/pull/93066)，[@AnishShah](https://github.com/AnishShah)）
- 为/ metrics，/ livez / *，/ readyz /*和/ healthz /-端点添加自举ClusterRole，ClusterRoleBinding和组。（[＃93311](https://github.com/kubernetes/kubernetes/pull/93311)，[@logicalhan](https://github.com/logicalhan)）[SIG API机械，[身份](https://github.com/logicalhan)验证，云提供程序和工具]
- 现在，为创建命名空间API对象而发送的AdmissionReview对象`namespace`始终填充属性（以前`namespace`通过POST请求创建命名空间时该属性为空，而通过服务器端应用PATCH请求创建的命名空间中该属性为空）（[＃95012](https://github.com/kubernetes/kubernetes/pull/95012)，[@nodo](https://github.com/nodo)）[ SIG API机械和测试]
- 将翻译应用于所有命令描述（[＃95439](https://github.com/kubernetes/kubernetes/pull/95439)，[@HerrNaN](https://github.com/HerrNaN)）[SIG CLI]
- 基本映像：更新为debian-iptables：buster-v1.3.0
  - 使用iptables 1.8.5
  - base-images：更新至debian-base：buster-v1.2.0
  - cluster / images / etcd：构建etcd：3.4.13-1映像
    - 使用debian-base：buster-v1.2.0（[＃94733](https://github.com/kubernetes/kubernetes/pull/94733)，[@justaugustus](https://github.com/justaugustus)）[SIG API机制，发布和测试]
- 更改：从HTTP探针中删除了默认的“ Accept-Encoding”标头。见https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#http-probes（[＃96127](https://github.com/kubernetes/kubernetes/pull/96127)，[@ fonsecas72](https://github.com/fonsecas72)）[SIG网络和节点]
- 现在，Client-go标头日志记录（详细级别> = 9）掩盖了`Authorization`标头内容（[＃95316](https://github.com/kubernetes/kubernetes/pull/95316)，[@sfowl](https://github.com/sfowl)）[SIG API Machinery]
- 在设置configmap / secret的卷所有权时，降低警告消息的频率。（[＃92878](https://github.com/kubernetes/kubernetes/pull/92878)，[@jvanz](https://github.com/jvanz)）
- 增强verifyRunAsNonRoot的日志信息，添加容器，容器信息（[＃94911](https://github.com/kubernetes/kubernetes/pull/94911)，[@ wawa0210](https://github.com/wawa0210)）[SIG节点]
- 修复功能名称NewCreateCreateDeploymentOptions（[＃91931](https://github.com/kubernetes/kubernetes/pull/91931)，[@ lixiaobing1](https://github.com/lixiaobing1)）[SIG CLI]
- 修复kubelet以在启动容器时正确记录日志。以前，kubelet可能会记录该容器已死并在首次实际启动时已重新启动。此行为仅发生在具有initContainers和常规容器的容器上。（[＃91469](https://github.com/kubernetes/kubernetes/pull/91469)，[@rata](https://github.com/rata)）
- 修复了有关调度程序中的指标无身份验证的消息。（[＃94035](https://github.com/kubernetes/kubernetes/pull/94035)，[@ zhouya0](https://github.com/zhouya0)）[SIG调度]
- 服务的生成器已从kubectl（[＃95256](https://github.com/kubernetes/kubernetes/pull/95256)，[@ Git-Jiro](https://github.com/Git-Jiro)）中删除[SIG CLI]
- 介绍kubectl-convert插件。（[＃96190](https://github.com/kubernetes/kubernetes/pull/96190)，[@soltysh](https://github.com/soltysh)）[SIG CLI和测试]
- 现在，Kube-scheduler在启动时记录已处理的组件配置（[＃96426](https://github.com/kubernetes/kubernetes/pull/96426)，[@damemi](https://github.com/damemi)）[SIG计划]
- Kubeadm：日志消息中单独的参数键/值（[＃94016](https://github.com/kubernetes/kubernetes/pull/94016)，[@mrueg](https://github.com/mrueg)）[SIG集群生命周期]
- Kubeadm：应用插件时删除CoreDNS检查以获取已知图像摘要（[＃94506](https://github.com/kubernetes/kubernetes/pull/94506)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]
- Kubeadm：在Windows上将默认的暂停图像版本更新为1.4.0。通过此更新，该映像支持Windows版本1809（2019LTS），[1903、1909、2004](https://github.com/kubernetes/kubernetes/pull/95419)（[＃95419](https://github.com/kubernetes/kubernetes/pull/95419)，[@jsturtevant](https://github.com/jsturtevant)）[SIG群集生命周期和Windows]
- Kubectl：已弃用该`generator`标志，`kubectl autoscale`并且该标志无效，它将在功能版本中删除（[＃92998](https://github.com/kubernetes/kubernetes/pull/92998)，[@SataQiu](https://github.com/SataQiu)）[SIG CLI]
- 将ExternalPolicyForExternalIP锁定为默认值，此功能门将在1.22中删除。（[＃94581](https://github.com/kubernetes/kubernetes/pull/94581)，[@knabben](https://github.com/knabben)）[SIG网络]
- 屏蔽ceph RBD admin当logLevel> = 4时在日志中[保密](https://github.com/kubernetes/kubernetes/pull/95245)（[＃95245](https://github.com/kubernetes/kubernetes/pull/95245)，[@sfowl](https://github.com/sfowl)）
- 从kubectl cluster-info命令中删除令人反感的单词。（[＃95202](https://github.com/kubernetes/kubernetes/pull/95202)，[@rikatz](https://github.com/rikatz)）
- 删除kubeadm中对“ ci / k8s-master”版本标签的支持，改用“ ci / latest”。参见[kubernetes / test-infra＃18517](https://github.com/kubernetes/test-infra/pull/18517)。（[＃93626](https://github.com/kubernetes/kubernetes/pull/93626)，[@vikkyomkar](https://github.com/vikkyomkar)）
- 删除apiserver / cloud-provider / controller-manager上csi-translation-lib模块的依赖项（[＃95543](https://github.com/kubernetes/kubernetes/pull/95543)，[@ wawa0210](https://github.com/wawa0210)）[SIG发行版]
- 调度程序框架接口从pkg / scheduler / framework / v1alpha移至pkg / scheduler / framework（[＃95069](https://github.com/kubernetes/kubernetes/pull/95069)，[@farah](https://github.com/farah)）[SIG调度，存储和测试]
- Service.beta.kubernetes.io/azure-load-balancer-disable-tcp-reset已删除。所有标准负载平衡器将始终启用tcp重置。（[＃94297](https://github.com/kubernetes/kubernetes/pull/94297)，[@MarcPow](https://github.com/MarcPow)）[SIG云提供商]
- 在kube-apiserver（[＃94397](https://github.com/kubernetes/kubernetes/pull/94397)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94397)[-t](https://github.com/wojtek-t)）中停止传播SelfLink（在1.16版中已弃用）[SIG API机械与测试]
- 在Windows上剥离不必要的安全上下文（[＃93475](https://github.com/kubernetes/kubernetes/pull/93475)，[@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)）[SIG节点，测试和Windows]
- 为了确保代码坚固，请为GetAddressAndDialer添加单元测试（[＃93180](https://github.com/kubernetes/kubernetes/pull/93180)，[@ FreeZhang61](https://github.com/FreeZhang61)）[SIG节点]
- UDP和SCTP协议可能会留下需要清除的陈旧连接，以避免服务中断，但是它们可能会导致难以调试的问题。使用大于或等于4的日志级别的Kubernetes组件将记录conntrack操作及其输出，以显示已删除的条目。（[＃95694](https://github.com/kubernetes/kubernetes/pull/95694)，[@aojea](https://github.com/aojea)）[SIG网络]
- 将CNI插件更新到v0.8.7（[＃94367](https://github.com/kubernetes/kubernetes/pull/94367)，[@justaugustus](https://github.com/justaugustus)）[SIG云提供程序，网络，节点，版本和测试]
- 将cri-tools更新到[v1.19.0](https://github.com/kubernetes-sigs/cri-tools/releases/tag/v1.19.0)（[＃94307](https://github.com/kubernetes/kubernetes/pull/94307)，[@xmudrii](https://github.com/xmudrii)）[SIG Cloud Provider]
- 将etcd客户端更新为v3.4.13（[＃94259](https://github.com/kubernetes/kubernetes/pull/94259)，[@jingyih](https://github.com/jingyih)）[SIG API机械和云提供商]
- 用户现在将能够配置AWS NLB运行状况检查间隔的所有受支持的值以及新资源的阈值。（[＃96312](https://github.com/kubernetes/kubernetes/pull/96312)，[@kishorj](https://github.com/kishorj)）[SIG云提供商]
- V1helpers.MatchNodeSelectorTerms现在仅接受节点和条款列表（[＃95871](https://github.com/kubernetes/kubernetes/pull/95871)，[@damemi](https://github.com/damemi)）[SIG应用，计划和存储]
- vSphere：改善节点缓存刷新事件（[＃95236](https://github.com/kubernetes/kubernetes/pull/95236)，[@andrewsykim](https://github.com/andrewsykim)）上的日志记录消息[SIG Cloud Provider]
- `MatchNodeSelectorTerms`函数移至`k8s.io/component-helpers`（[＃95531](https://github.com/kubernetes/kubernetes/pull/95531)，[@damemi](https://github.com/damemi)）[SIG应用，计划和存储]
- `kubectl api-resources`现在可以打印API版本（作为“ API组/版本”，与的输出相同`kubectl api-versions`）。APIGROUP列现在为APIVERSION（[＃95253](https://github.com/kubernetes/kubernetes/pull/95253)，[@sallyom](https://github.com/sallyom)）[SIG CLI]
- `kubectl get ingress`现在更喜欢`networking.k8s.io/v1`过`extensions/v1beta1`（因为V1.14不建议使用）。要明确请求不推荐使用的版本，请使用`kubectl get ingress.v1beta1.extensions`。（[＃94309](https://github.com/kubernetes/kubernetes/pull/94309)，[@liggitt](https://github.com/liggitt)）[SIG API机械和CLI]

## 依存关系

### 添加

- cloud.google.com/go/firestore：v1.1.0
- github.com/Azure/go-autorest：[v14.2.0 +兼容](https://github.com/Azure/go-autorest/tree/v14.2.0)
- github.com/armon/go-metrics：[f0300d1](https://github.com/armon/go-metrics/tree/f0300d1)
- github.com/armon/go-radix：[7fddfc3](https://github.com/armon/go-radix/tree/7fddfc3)
- github.com/bketelsen/crypt：[5cbc8cc](https://github.com/bketelsen/crypt/tree/5cbc8cc)
- github.com/form3tech-oss/jwt-go：[V3.2.2 +不兼容](https://github.com/form3tech-oss/jwt-go/tree/v3.2.2)
- github.com/fvbommel/sortorder：[V1.0.1](https://github.com/fvbommel/sortorder/tree/v1.0.1)
- github.com/hashicorp/consul/api：[V1.1.0](https://github.com/hashicorp/consul/api/tree/v1.1.0)
- github.com/hashicorp/consul/sdk：[v0.1.1](https://github.com/hashicorp/consul/sdk/tree/v0.1.1)
- github.com/hashicorp/errwrap：[V1.0.0](https://github.com/hashicorp/errwrap/tree/v1.0.0)
- github.com/hashicorp/go-cleanhttp：[v0.5.1](https://github.com/hashicorp/go-cleanhttp/tree/v0.5.1)
- github.com/hashicorp/go-immutable-radix：[V1.0.0](https://github.com/hashicorp/go-immutable-radix/tree/v1.0.0)
- github.com/hashicorp/go-msgpack：[v0.5.3](https://github.com/hashicorp/go-msgpack/tree/v0.5.3)
- github.com/hashicorp/go-multierror：[V1.0.0](https://github.com/hashicorp/go-multierror/tree/v1.0.0)
- github.com/hashicorp/go-rootcerts：[V1.0.0](https://github.com/hashicorp/go-rootcerts/tree/v1.0.0)
- github.com/hashicorp/go-sockaddr：[V1.0.0](https://github.com/hashicorp/go-sockaddr/tree/v1.0.0)
- github.com/hashicorp/go-uuid：[V1.0.1](https://github.com/hashicorp/go-uuid/tree/v1.0.1)
- github.com/hashicorp/go.net：[v0.0.1](https://github.com/hashicorp/go.net/tree/v0.0.1)
- github.com/hashicorp/logutils：[V1.0.0](https://github.com/hashicorp/logutils/tree/v1.0.0)
- github.com/hashicorp/mdns：[V1.0.0](https://github.com/hashicorp/mdns/tree/v1.0.0)
- github.com/hashicorp/memberlist：[v0.1.3](https://github.com/hashicorp/memberlist/tree/v0.1.3)
- github.com/hashicorp/serf：[v0.8.2](https://github.com/hashicorp/serf/tree/v0.8.2)
- github.com/jmespath/go-jmespath/internal/testify：[V1.5.1](https://github.com/jmespath/go-jmespath/internal/testify/tree/v1.5.1)
- github.com/mitchellh/cli：[V1.0.0](https://github.com/mitchellh/cli/tree/v1.0.0)
- github.com/mitchellh/go-testing-interface：[V1.0.0](https://github.com/mitchellh/go-testing-interface/tree/v1.0.0)
- github.com/mitchellh/gox：[V0.4.0](https://github.com/mitchellh/gox/tree/v0.4.0)
- github.com/mitchellh/iochan：[V1.0.0](https://github.com/mitchellh/iochan/tree/v1.0.0)
- github.com/pascaldekloe/goe：[57f6aae](https://github.com/pascaldekloe/goe/tree/57f6aae)
- github.com/posener/complete：[V1.1.1](https://github.com/posener/complete/tree/v1.1.1)
- github.com/ryanuber/columnize：[9b3edd6](https://github.com/ryanuber/columnize/tree/9b3edd6)
- github.com/sean-/seed：[e2103e2](https://github.com/sean-/seed/tree/e2103e2)
- github.com/subosito/gotenv：[V1.2.0](https://github.com/subosito/gotenv/tree/v1.2.0)
- github.com/willf/bitset：[d5bec33](https://github.com/willf/bitset/tree/d5bec33)
- gopkg.in/ini.v1：v1.51.0
- gopkg.in/yaml.v3：9f266ea
- rsc.io/quote/v3：v3.1.0
- rsc.io/sampler：v1.3.0

### 已变更

- cloud.google.com/go/bigquery：v1.0.1→v1.4.0
- cloud.google.com/go/datastore：v1.0.0→v1.1.0
- cloud.google.com/go/pubsub：v1.0.1→v1.2.0
- cloud.google.com/go/storage：v1.0.0→v1.6.0
- cloud.google.com/go：v0.51.0→v0.54.0
- github.com/Azure/go-autorest/autorest/adal：[v0.8.2→v0.9.5](https://github.com/Azure/go-autorest/autorest/adal/compare/v0.8.2...v0.9.5)
- github.com/Azure/go-autorest/autorest/date：[v0.2.0→v0.3.0](https://github.com/Azure/go-autorest/autorest/date/compare/v0.2.0...v0.3.0)
- github.com/Azure/go-autorest/autorest/mocks：[v0.3.0→v0.4.1](https://github.com/Azure/go-autorest/autorest/mocks/compare/v0.3.0...v0.4.1)
- github.com/Azure/go-autorest/autorest：[v0.9.6→v0.11.1](https://github.com/Azure/go-autorest/autorest/compare/v0.9.6...v0.11.1)
- github.com/Azure/go-autorest/logger：[v0.1.0→v0.2.0](https://github.com/Azure/go-autorest/logger/compare/v0.1.0...v0.2.0)
- github.com/Azure/go-autorest/tracing：[v0.5.0→v0.6.0](https://github.com/Azure/go-autorest/tracing/compare/v0.5.0...v0.6.0)
- github.com/Microsoft/go-winio：[fc70bd9→v0.4.15](https://github.com/Microsoft/go-winio/compare/fc70bd9...v0.4.15)
- github.com/aws/aws-sdk-go：[v1.28.2→v1.35.24](https://github.com/aws/aws-sdk-go/compare/v1.28.2...v1.35.24)
- github.com/blang/semver：v3.5.0 [+不兼容→v3.5.1 +不兼容](https://github.com/blang/semver/compare/v3.5.0...v3.5.1)
- github.com/checkpoint-restore/go-criu/v4：[V4.0.2→V4.1.0](https://github.com/checkpoint-restore/go-criu/v4/compare/v4.0.2...v4.1.0)
- github.com/containerd/containerd：[V1.3.3→V1.4.1](https://github.com/containerd/containerd/compare/v1.3.3...v1.4.1)
- github.com/containerd/ttrpc：[V1.0.0→V1.0.2](https://github.com/containerd/ttrpc/compare/v1.0.0...v1.0.2)
- github.com/containerd/typeurl：[V1.0.0→V1.0.1](https://github.com/containerd/typeurl/compare/v1.0.0...v1.0.1)
- github.com/coreos/etcd：v3.3.10 [+不兼容→v3.3.13 +不兼容](https://github.com/coreos/etcd/compare/v3.3.10...v3.3.13)
- github.com/docker/docker：[aa6a989→bd33bbf](https://github.com/docker/docker/compare/aa6a989...bd33bbf)
- github.com/go-gl/glfw/v3.3/glfw：[12ad95a→6f7a984](https://github.com/go-gl/glfw/v3.3/glfw/compare/12ad95a...6f7a984)
- github.com/golang/groupcache：[215e871→8c9f03a](https://github.com/golang/groupcache/compare/215e871...8c9f03a)
- github.com/golang/mock：[V1.3.1→V1.4.1](https://github.com/golang/mock/compare/v1.3.1...v1.4.1)
- github.com/golang/protobuf：[5.0上→1.4.3](https://github.com/golang/protobuf/compare/v1.4.2...v1.4.3)
- github.com/google/cadvisor：[v0.37.0→v0.38.5](https://github.com/google/cadvisor/compare/v0.37.0...v0.38.5)
- github.com/google/go-cmp：[V0.4.0→v0.5.2](https://github.com/google/go-cmp/compare/v0.4.0...v0.5.2)
- github.com/google/pprof：[d4f498a→1ebb73c](https://github.com/google/pprof/compare/d4f498a...1ebb73c)
- github.com/google/uuid：[V1.1.1→V1.1.2](https://github.com/google/uuid/compare/v1.1.1...v1.1.2)
- github.com/gorilla/mux：[v1.7.3→v1.8.0](https://github.com/gorilla/mux/compare/v1.7.3...v1.8.0)
- github.com/gorilla/websocket：[V1.4.0→5.0上](https://github.com/gorilla/websocket/compare/v1.4.0...v1.4.2)
- github.com/jmespath/go-jmespath：[c2b33e8→V0.4.0](https://github.com/jmespath/go-jmespath/compare/c2b33e8...v0.4.0)
- github.com/karrick/godirwalk：[v1.7.5→v1.16.1](https://github.com/karrick/godirwalk/compare/v1.7.5...v1.16.1)
- github.com/opencontainers/go-digest：[V1.0.0-RC1→V1.0.0](https://github.com/opencontainers/go-digest/compare/v1.0.0-rc1...v1.0.0)
- github.com/opencontainers/runc：[819fcc6→V1.0.0-rc92](https://github.com/opencontainers/runc/compare/819fcc6...v1.0.0-rc92)
- github.com/opencontainers/runtime-spec：[237cc4f→4d89ac9](https://github.com/opencontainers/runtime-spec/compare/237cc4f...4d89ac9)
- github.com/opencontainers/selinux：[V1.5.2→V1.6.0](https://github.com/opencontainers/selinux/compare/v1.5.2...v1.6.0)
- github.com/prometheus/procfs：[v0.1.3→v0.2.0](https://github.com/prometheus/procfs/compare/v0.1.3...v0.2.0)
- github.com/quobyte/api：[v0.1.2→v0.1.8](https://github.com/quobyte/api/compare/v0.1.2...v0.1.8)
- github.com/spf13/cobra：[V1.0.0→V1.1.1](https://github.com/spf13/cobra/compare/v1.0.0...v1.1.1)
- github.com/spf13/viper：[V1.4.0→V1.7.0](https://github.com/spf13/viper/compare/v1.4.0...v1.7.0)
- github.com/storageos/go-api：[343b3ef→V2.2.0 +不兼容](https://github.com/storageos/go-api/compare/343b3ef...v2.2.0)
- github.com/stretchr/testify：[V1.4.0→V1.6.1](https://github.com/stretchr/testify/compare/v1.4.0...v1.6.1)
- github.com/vishvananda/netns：[52d707b→db3c7e5](https://github.com/vishvananda/netns/compare/52d707b...db3c7e5)
- go.etcd.io/etcd：17cef6e→dd1b699
- go.opencensus.io：v0.22.2→v0.22.3
- golang.org/x/crypto：75b2880→7f63de1
- golang.org/x/exp：da58074→6cc2880
- golang.org/x/lint：fdd1cda→738671d
- golang.org/x/net：ab34263→69a7880
- golang.org/x/oauth2：858c2ad→bf48bf1
- golang.org/x/sys：ed371f2→5cba982
- golang.org/x/text：v0.3.3→v0.3.4
- golang.org/x/time：555d28b→3af7569
- golang.org/x/xerrors：9bdfabe→5ec99f8
- google.golang.org/api：v0.15.1→v0.20.0
- google.golang.org/genproto：cb27e3a→8816d57
- google.golang.org/grpc：v1.27.0→v1.27.1
- google.golang.org/protobuf：v1.24.0→v1.25.0
- honnef.co/go/tools：v0.0.1-2019.2.3→v0.0.1-2020.1.3
- k8s.io/gengo：8167cfd→83324d8
- k8s.io/klog/v2：v2.2.0→v2.4.0
- k8s.io/kube-openapi：6aeccd4→d219536
- k8s.io/system-validators：v1.1.2→v1.2.0
- k8s.io/utils：d5654de→67b214c
- sigs.k8s.io/apiserver-network-proxy/konnectivity-client：v0.0.9→v0.0.14
- sigs.k8s.io/structured-merge-diff/v4：v4.0.1→v4.0.2

### 已移除

- github.com/armon/consul-api：[eb2c6b5](https://github.com/armon/consul-api/tree/eb2c6b5)
- github.com/go-ini/ini：[v1.9.0](https://github.com/go-ini/ini/tree/v1.9.0)
- github.com/ugorji/go：[V1.1.4](https://github.com/ugorji/go/tree/v1.1.4)
- github.com/xlab/handysort：[fb3537e](https://github.com/xlab/handysort/tree/fb3537e)
- github.com/xordataexchange/crypt：[b2862e3](https://github.com/xordataexchange/crypt/tree/b2862e3)
- vbom.ml/util：db5cfe1

## 依存关系

### 添加

- cloud.google.com/go/firestore：v1.1.0
- github.com/Azure/go-autorest：[v14.2.0 +兼容](https://github.com/Azure/go-autorest/tree/v14.2.0)
- github.com/armon/go-metrics：[f0300d1](https://github.com/armon/go-metrics/tree/f0300d1)
- github.com/armon/go-radix：[7fddfc3](https://github.com/armon/go-radix/tree/7fddfc3)
- github.com/bketelsen/crypt：[5cbc8cc](https://github.com/bketelsen/crypt/tree/5cbc8cc)
- github.com/form3tech-oss/jwt-go：[V3.2.2 +不兼容](https://github.com/form3tech-oss/jwt-go/tree/v3.2.2)
- github.com/fvbommel/sortorder：[V1.0.1](https://github.com/fvbommel/sortorder/tree/v1.0.1)
- github.com/hashicorp/consul/api：[V1.1.0](https://github.com/hashicorp/consul/api/tree/v1.1.0)
- github.com/hashicorp/consul/sdk：[v0.1.1](https://github.com/hashicorp/consul/sdk/tree/v0.1.1)
- github.com/hashicorp/errwrap：[V1.0.0](https://github.com/hashicorp/errwrap/tree/v1.0.0)
- github.com/hashicorp/go-cleanhttp：[v0.5.1](https://github.com/hashicorp/go-cleanhttp/tree/v0.5.1)
- github.com/hashicorp/go-immutable-radix：[V1.0.0](https://github.com/hashicorp/go-immutable-radix/tree/v1.0.0)
- github.com/hashicorp/go-msgpack：[v0.5.3](https://github.com/hashicorp/go-msgpack/tree/v0.5.3)
- github.com/hashicorp/go-multierror：[V1.0.0](https://github.com/hashicorp/go-multierror/tree/v1.0.0)
- github.com/hashicorp/go-rootcerts：[V1.0.0](https://github.com/hashicorp/go-rootcerts/tree/v1.0.0)
- github.com/hashicorp/go-sockaddr：[V1.0.0](https://github.com/hashicorp/go-sockaddr/tree/v1.0.0)
- github.com/hashicorp/go-uuid：[V1.0.1](https://github.com/hashicorp/go-uuid/tree/v1.0.1)
- github.com/hashicorp/go.net：[v0.0.1](https://github.com/hashicorp/go.net/tree/v0.0.1)
- github.com/hashicorp/logutils：[V1.0.0](https://github.com/hashicorp/logutils/tree/v1.0.0)
- github.com/hashicorp/mdns：[V1.0.0](https://github.com/hashicorp/mdns/tree/v1.0.0)
- github.com/hashicorp/memberlist：[v0.1.3](https://github.com/hashicorp/memberlist/tree/v0.1.3)
- github.com/hashicorp/serf：[v0.8.2](https://github.com/hashicorp/serf/tree/v0.8.2)
- github.com/jmespath/go-jmespath/internal/testify：[V1.5.1](https://github.com/jmespath/go-jmespath/internal/testify/tree/v1.5.1)
- github.com/mitchellh/cli：[V1.0.0](https://github.com/mitchellh/cli/tree/v1.0.0)
- github.com/mitchellh/go-testing-interface：[V1.0.0](https://github.com/mitchellh/go-testing-interface/tree/v1.0.0)
- github.com/mitchellh/gox：[V0.4.0](https://github.com/mitchellh/gox/tree/v0.4.0)
- github.com/mitchellh/iochan：[V1.0.0](https://github.com/mitchellh/iochan/tree/v1.0.0)
- github.com/pascaldekloe/goe：[57f6aae](https://github.com/pascaldekloe/goe/tree/57f6aae)
- github.com/posener/complete：[V1.1.1](https://github.com/posener/complete/tree/v1.1.1)
- github.com/ryanuber/columnize：[9b3edd6](https://github.com/ryanuber/columnize/tree/9b3edd6)
- github.com/sean-/seed：[e2103e2](https://github.com/sean-/seed/tree/e2103e2)
- github.com/subosito/gotenv：[V1.2.0](https://github.com/subosito/gotenv/tree/v1.2.0)
- github.com/willf/bitset：[d5bec33](https://github.com/willf/bitset/tree/d5bec33)
- gopkg.in/ini.v1：v1.51.0
- gopkg.in/yaml.v3：9f266ea
- rsc.io/quote/v3：v3.1.0
- rsc.io/sampler：v1.3.0

### 已变更

- cloud.google.com/go/bigquery：v1.0.1→v1.4.0
- cloud.google.com/go/datastore：v1.0.0→v1.1.0
- cloud.google.com/go/pubsub：v1.0.1→v1.2.0
- cloud.google.com/go/storage：v1.0.0→v1.6.0
- cloud.google.com/go：v0.51.0→v0.54.0
- github.com/Azure/go-autorest/autorest/adal：[v0.8.2→v0.9.5](https://github.com/Azure/go-autorest/autorest/adal/compare/v0.8.2...v0.9.5)
- github.com/Azure/go-autorest/autorest/date：[v0.2.0→v0.3.0](https://github.com/Azure/go-autorest/autorest/date/compare/v0.2.0...v0.3.0)
- github.com/Azure/go-autorest/autorest/mocks：[v0.3.0→v0.4.1](https://github.com/Azure/go-autorest/autorest/mocks/compare/v0.3.0...v0.4.1)
- github.com/Azure/go-autorest/autorest：[v0.9.6→v0.11.1](https://github.com/Azure/go-autorest/autorest/compare/v0.9.6...v0.11.1)
- github.com/Azure/go-autorest/logger：[v0.1.0→v0.2.0](https://github.com/Azure/go-autorest/logger/compare/v0.1.0...v0.2.0)
- github.com/Azure/go-autorest/tracing：[v0.5.0→v0.6.0](https://github.com/Azure/go-autorest/tracing/compare/v0.5.0...v0.6.0)
- github.com/Microsoft/go-winio：[fc70bd9→v0.4.15](https://github.com/Microsoft/go-winio/compare/fc70bd9...v0.4.15)
- github.com/aws/aws-sdk-go：[v1.28.2→v1.35.24](https://github.com/aws/aws-sdk-go/compare/v1.28.2...v1.35.24)
- github.com/blang/semver：v3.5.0 [+不兼容→v3.5.1 +不兼容](https://github.com/blang/semver/compare/v3.5.0...v3.5.1)
- github.com/checkpoint-restore/go-criu/v4：[V4.0.2→V4.1.0](https://github.com/checkpoint-restore/go-criu/v4/compare/v4.0.2...v4.1.0)
- github.com/containerd/containerd：[V1.3.3→V1.4.1](https://github.com/containerd/containerd/compare/v1.3.3...v1.4.1)
- github.com/containerd/ttrpc：[V1.0.0→V1.0.2](https://github.com/containerd/ttrpc/compare/v1.0.0...v1.0.2)
- github.com/containerd/typeurl：[V1.0.0→V1.0.1](https://github.com/containerd/typeurl/compare/v1.0.0...v1.0.1)
- github.com/coreos/etcd：v3.3.10 [+不兼容→v3.3.13 +不兼容](https://github.com/coreos/etcd/compare/v3.3.10...v3.3.13)
- github.com/docker/docker：[aa6a989→bd33bbf](https://github.com/docker/docker/compare/aa6a989...bd33bbf)
- github.com/go-gl/glfw/v3.3/glfw：[12ad95a→6f7a984](https://github.com/go-gl/glfw/v3.3/glfw/compare/12ad95a...6f7a984)
- github.com/golang/groupcache：[215e871→8c9f03a](https://github.com/golang/groupcache/compare/215e871...8c9f03a)
- github.com/golang/mock：[V1.3.1→V1.4.1](https://github.com/golang/mock/compare/v1.3.1...v1.4.1)
- github.com/golang/protobuf：[5.0上→1.4.3](https://github.com/golang/protobuf/compare/v1.4.2...v1.4.3)
- github.com/google/cadvisor：[v0.37.0→v0.38.5](https://github.com/google/cadvisor/compare/v0.37.0...v0.38.5)
- github.com/google/go-cmp：[V0.4.0→v0.5.2](https://github.com/google/go-cmp/compare/v0.4.0...v0.5.2)
- github.com/google/pprof：[d4f498a→1ebb73c](https://github.com/google/pprof/compare/d4f498a...1ebb73c)
- github.com/google/uuid：[V1.1.1→V1.1.2](https://github.com/google/uuid/compare/v1.1.1...v1.1.2)
- github.com/gorilla/mux：[v1.7.3→v1.8.0](https://github.com/gorilla/mux/compare/v1.7.3...v1.8.0)
- github.com/gorilla/websocket：[V1.4.0→5.0上](https://github.com/gorilla/websocket/compare/v1.4.0...v1.4.2)
- github.com/jmespath/go-jmespath：[c2b33e8→V0.4.0](https://github.com/jmespath/go-jmespath/compare/c2b33e8...v0.4.0)
- github.com/karrick/godirwalk：[v1.7.5→v1.16.1](https://github.com/karrick/godirwalk/compare/v1.7.5...v1.16.1)
- github.com/opencontainers/go-digest：[V1.0.0-RC1→V1.0.0](https://github.com/opencontainers/go-digest/compare/v1.0.0-rc1...v1.0.0)
- github.com/opencontainers/runc：[819fcc6→V1.0.0-rc92](https://github.com/opencontainers/runc/compare/819fcc6...v1.0.0-rc92)
- github.com/opencontainers/runtime-spec：[237cc4f→4d89ac9](https://github.com/opencontainers/runtime-spec/compare/237cc4f...4d89ac9)
- github.com/opencontainers/selinux：[V1.5.2→V1.6.0](https://github.com/opencontainers/selinux/compare/v1.5.2...v1.6.0)
- github.com/prometheus/procfs：[v0.1.3→v0.2.0](https://github.com/prometheus/procfs/compare/v0.1.3...v0.2.0)
- github.com/quobyte/api：[v0.1.2→v0.1.8](https://github.com/quobyte/api/compare/v0.1.2...v0.1.8)
- github.com/spf13/cobra：[V1.0.0→V1.1.1](https://github.com/spf13/cobra/compare/v1.0.0...v1.1.1)
- github.com/spf13/viper：[V1.4.0→V1.7.0](https://github.com/spf13/viper/compare/v1.4.0...v1.7.0)
- github.com/storageos/go-api：[343b3ef→V2.2.0 +不兼容](https://github.com/storageos/go-api/compare/343b3ef...v2.2.0)
- github.com/stretchr/testify：[V1.4.0→V1.6.1](https://github.com/stretchr/testify/compare/v1.4.0...v1.6.1)
- github.com/vishvananda/netns：[52d707b→db3c7e5](https://github.com/vishvananda/netns/compare/52d707b...db3c7e5)
- go.etcd.io/etcd：17cef6e→dd1b699
- go.opencensus.io：v0.22.2→v0.22.3
- golang.org/x/crypto：75b2880→7f63de1
- golang.org/x/exp：da58074→6cc2880
- golang.org/x/lint：fdd1cda→738671d
- golang.org/x/net：ab34263→69a7880
- golang.org/x/oauth2：858c2ad→bf48bf1
- golang.org/x/sys：ed371f2→5cba982
- golang.org/x/text：v0.3.3→v0.3.4
- golang.org/x/time：555d28b→3af7569
- golang.org/x/xerrors：9bdfabe→5ec99f8
- google.golang.org/api：v0.15.1→v0.20.0
- google.golang.org/genproto：cb27e3a→8816d57
- google.golang.org/grpc：v1.27.0→v1.27.1
- google.golang.org/protobuf：v1.24.0→v1.25.0
- honnef.co/go/tools：v0.0.1-2019.2.3→v0.0.1-2020.1.3
- k8s.io/gengo：8167cfd→83324d8
- k8s.io/klog/v2：v2.2.0→v2.4.0
- k8s.io/kube-openapi：6aeccd4→d219536
- k8s.io/system-validators：v1.1.2→v1.2.0
- k8s.io/utils：d5654de→67b214c
- sigs.k8s.io/apiserver-network-proxy/konnectivity-client：v0.0.9→v0.0.14
- sigs.k8s.io/structured-merge-diff/v4：v4.0.1→v4.0.2

### 已移除

- github.com/armon/consul-api：[eb2c6b5](https://github.com/armon/consul-api/tree/eb2c6b5)
- github.com/go-ini/ini：[v1.9.0](https://github.com/go-ini/ini/tree/v1.9.0)
- github.com/ugorji/go：[V1.1.4](https://github.com/ugorji/go/tree/v1.1.4)
- github.com/xlab/handysort：[fb3537e](https://github.com/xlab/handysort/tree/fb3537e)
- github.com/xordataexchange/crypt：[b2862e3](https://github.com/xordataexchange/crypt/tree/b2862e3)
- vbom.ml/util：db5cfe1

# v1.20.0-rc.0

## v1.20.0-rc.0的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes.tar.gz) | acfee8658831f9503fccda0904798405434f17be7064a361a9f34c6ed04f1c0f685e79ca40cef5fcf34e3193bacbf467665e8dc277e0562ebdc929170034b5ae |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-src.tar.gz) | 9d962f8845e1fa221649cf0c0e178f0f03808486c49ea15ab5ec67861ec5aa948cf18bc0ee9b2067643c8332227973dd592e6a4457456a9d9d80e8ef28d5f7c3 |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-darwin-amd64.tar.gz) | 062b57f1a450fe01d6184f104d81d376bdf5720010412821e315fd9b1b622a400ac91f996540daa66cee172006f3efade4eccc19265494f1a1d7cc9450f0b50a |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-linux-386.tar.gz) | 86e96d2c2046c5e62e02bef30a6643f25e01f1b3eba256cab7dd61252908540c26cb058490e9cecc5a9bad97d2b577f5968884e9f1a90237e302419f39e068bc |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-linux-amd64.tar.gz) | 619d3afb9ce902368390e71633396010e88e87c5fd848e3adc71571d1d4a25be002588415e5f83afee82460f8a7c9e0bd968335277cb8f8cb51e58d4bb43e64e |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-linux-arm.tar.gz) | 60965150a60ab3d05a248339786e0c7da4b89a04539c3719737b13d71302bac1dd9bcaa427d8a1f84a7b42d0c67801dce2de0005e9e47d21122868b32ac3d40f |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-linux-arm64.tar.gz) | 688e064f4ef6a17189dbb5af468c279b9de35e215c40500fb97b1d46692d222747023f9e07a7f7ba006400f9532a8912e69d7c5143f956b1dadca144c67ee711 |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-linux-ppc64le.tar.gz) | 47b8abc02b42b3b1de67da184921b5801d7e3cb09befac840c85913193fc5ac4e5e3ecfcb57da6b686ff21af9a3bd42ae6949d4744dbe6ad976794340e328b83 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-linux-s390x.tar.gz) | 971b41d3169f30e6c412e0254c180636abb7ccc8dcee6641b0e9877b69752fc61aa30b76c19c108969df654fe385da3cb3a44dd59d3c28dc45561392d7e08874 |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-windows-386.tar.gz) | 2d34e8387e31531d9aca5655f2f0d18e75b01825dc1c39b7beb73a7b7b610e2ba429e5ca97d5c41a71b67e75e7096c86ab63fda9baab4c0878c1ccb3a1aefac8 |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-client-windows-amd64.tar.gz) | f909640f4140693bb871936f10a40e79b43502105d0adb318b35bb7a64a770ad9d05a3a732368ccd3d15d496d75454789165bd1f5c2571da9a00569b3e6c007c |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-server-linux-amd64.tar.gz) | 0ea4458ae34108c633b4d48f1f128c6274dbc82b613492e78b3e0a2f656ac0df0bb9a75124e15d67c8e81850adcecf19f4ab0234c17247ee7ddf84f2df3e5eaa |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-server-linux-arm.tar.gz) | aef6a4d457faa29936603370f29a8523bb274211c3cb5101bd31aaf469c91ba6bd149ea99a4ccdd83352cf37e4d6508c5ee475ec10292bccd2f77ceea31e1c28 |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-server-linux-arm64.tar.gz) | 4829f473e9d60f9929ad17c70fdc2b6b6509ed75418be0b23a75b28580949736cb5b0bd6382070f93aa0a2a8863f0b1596daf965186ca749996c29d03ef7d8b8 |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-server-linux-ppc64le.tar.gz) | 9ab0790d382a3e28df1c013762c09da0085449cfd09d176d80be932806c24a715ea829be0075c3e221a2ad9cf06e726b4c39ab41987c1fb0fee2563e48206763 |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-server-linux-s390x.tar.gz) | 98670b587e299856dd9821b7517a35f9a65835b915b153de08b66c54d82160438b66f774bf5306c07bc956d70ff709860bc23162225da5e89f995d3fdc1f0122 |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-node-linux-amd64.tar.gz) | 699e9c8d1837198312eade8eb6fec390f6a2fea9e08207d2f58e8bb6e3e799028aca69e4670aac0a4ba7cf0af683aee2c158bf78cc520c80edc876c8d94d521a |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-node-linux-arm.tar.gz) | f3b5eab0669490e3cd7e802693daf3555d08323dfff6e73a881fce00fed4690e8bdaf1610278d9de74036ca3763101607575e5695a02158b7d3e7582b20ef7fa35 |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-node-linux-arm64.tar.gz) | e5012f77363561a609aaf791baaa17d09009819c4085a57132e5feb5366275a54640094e6ed1cba527f42b586c6d62999c2a5435edf5665ff0e114db4423c2ae |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-node-linux-ppc64le.tar.gz) | 2a6d6501620b1a9838dff05c66a40260cc22154a28027813346eb16e18c386bc3865298a46a0f08da71cd55149c5e7d07c4c4c431b4fd231486dd9d716548adb |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-node-linux-s390x.tar.gz) | 5eca02777519e31428a1e5842fe540b813fb8c929c341bbc71dcfd60d98deb89060f8f37352e8977020e21e053379eead6478eb2d54ced66fb9d38d5f3142bf0 |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-rc.0/kubernetes-node-windows-amd64.tar.gz) | 8ace02e7623dff894e863a2e0fa7dfb916368431d1723170713fe82e334c0ae0481b370855b71e2561de0fb64fed124281be604761ec08607230b66fb9ed1c03 |

## 自v1.20.0-beta.2起的变更日志

## 种类变化

### 特征

- Kubernetes现在使用go1.15.5构建
  - 版本：更新至k/repo-infra@v0.1.2（支持go1.15.5）（[＃95776](https://github.com/kubernetes/kubernetes/pull/95776)，[@justaugustus](https://github.com/justaugustus)）[SIG云提供程序，规范，发布和测试]

### 测试失败

- 解决了在群集上运行Ingress一致性测试的问题，该群集使用Ingress对象的终结器来管理释放的负载均衡器资源（[＃96742](https://github.com/kubernetes/kubernetes/pull/96742)，[@ spencerhance](https://github.com/spencerhance)）[SIG网络和测试]
- 一致性测试“验证具有相同hostPort但不同hostIP和协议的Pod之间没有冲突”现在除了功能之外，还验证了与每个hostPort的连接性。（[＃96627](https://github.com/kubernetes/kubernetes/pull/96627)，[@aojea](https://github.com/aojea)）[SIG计划和测试]

### 错误或回归

- 将节点问题检测器版本升级到v0.8.5，以使用Linux内核5.1+（[＃96716](https://github.com/kubernetes/kubernetes/pull/96716)，[@ tosi3k](https://github.com/tosi3k)）修复OOM检测[SIG云提供程序，可伸缩性和测试]
- 已恢复对1.20.0-beta.2中超时参数处理的更改，以避免破坏与现有客户端的向后兼容性。（[＃96727](https://github.com/kubernetes/kubernetes/pull/96727)，[@liggitt](https://github.com/liggitt)）[SIG API机械和测试]
- 现在，API服务器会删除创建/更新/补丁请求中重复的所有者引用条目。现在，发送请求的客户端会在API响应中收到警告标头。客户应停止发送具有重复所有者引用的请求。API服务器可能最早于1.24拒绝此类请求。（[＃96185](https://github.com/kubernetes/kubernetes/pull/96185)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械和测试]
- 修复：处于连接状态时调整Azure磁盘大小的问题（[＃96705](https://github.com/kubernetes/kubernetes/pull/96705)，[@andyzhangx](https://github.com/andyzhangx)）[SIG Cloud Provider]
- 修复了报告已删除apiservices的aggregator_unavailable_apiservice指标的错误。（[＃96421](https://github.com/kubernetes/kubernetes/pull/96421)，[@dgrisonnet](https://github.com/dgrisonnet)）[SIG API机械和仪器]
- 修复了非命名空间创建子资源假客户端测试的代码生成。（[＃96586](https://github.com/kubernetes/kubernetes/pull/96586)，[@Doude](https://github.com/Doude)）[SIG API机械]
- 默认情况下，所有Kubernetes客户端都启用HTTP / 2连接运行状况检查。该功能应立即可用。如果需要，用户可以通过HTTP2_READ_IDLE_TIMEOUT_SECONDS和HTTP2_PING_TIMEOUT_SECONDS环境变量来调整功能。如果HTTP2_READ_IDLE_TIMEOUT_SECONDS设置为0，则该功能被禁用。（[＃95981](https://github.com/kubernetes/kubernetes/pull/95981)，[@caesarxuchao](https://github.com/caesarxuchao)）[SIG API机制，CLI，云提供程序，群集生命周期，检测和节点]
- Kubeadm：在kubeadm升级过程中有新的默认配置（[＃96907](https://github.com/kubernetes/kubernetes/pull/96907)，[@pacoxu](https://github.com/pacoxu)）时，应该触发修复coredns迁移[SIG集群生命周期]
- 减少vSphere卷的卷名长度（[＃96533](https://github.com/kubernetes/kubernetes/pull/96533)，[@gnufied](https://github.com/gnufied)）[SIG存储]
- 解决了1.19+版本中的回归问题，目标为已弃用的beta os / arch标签的工作负载在节点启动时陷入了NodeAffinity状态。（[＃96810](https://github.com/kubernetes/kubernetes/pull/96810)，[@liggitt](https://github.com/liggitt)）[SIG节点]

## 依存关系

### 添加

*什么也没有变。*

### 已变更

- github.com/google/cadvisor：[v0.38.4→v0.38.5](https://github.com/google/cadvisor/compare/v0.38.4...v0.38.5)

### 已移除

*什么也没有变。*

# v1.20.0-beta.2

## v1.20.0-beta.2的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes.tar.gz) | fe769280aa623802a949b6a35fbddadbba1d6f9933a54132a35625683719595ecf58096a9aa0f7456f8d4931774df21bfa98e148bc3d85913f1da915134f77bd |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-src.tar.gz) | ce1c8d97c52e5189af335d673bd7e99c564816f6adebf249838f7e3f0e920f323b4e398a5d163ea767091497012ec38843c59ff14e6fdd07683b682135eed645 |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-darwin-amd64.tar.gz) | d6c14bd0f6702f4bbdf14a6abdfa4e5936de5b4efee38aa86c2bd7272967ec6d7868b88fc00ad4a7c3a20717a35e6be2b84e56dec04154fd702315f641409f7c |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-linux-386.tar.gz) | b923c44cb0acb91a8f6fd442c2168aa6166c848f5d037ce50a7cb11502be3698db65836b373c916f75b648d6ac8d9158807a050eecc4e1c77cffa25b386c8cdb |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-linux-amd64.tar.gz) | 8cae14146a9034dcd4e9d69d5d700f195a77aac35f629a148960ae028ed8b4fe12213993fe3e6e464b4b3e111adebe6f3dd7ca0accc70c738ed5cfd8993edd7c |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-linux-arm.tar.gz) | 1f54e5262a0432945ead57fcb924e6bfedd9ea76db1dd9ebd946787a2923c247cf16e10505307b47e365905a1b398678dac5af0f433c439c158a33e08362d97b |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-linux-arm64.tar.gz) | 31cf79c01e4878a231b4881fe3ed5ef790bd5fb5419388438d3f8c6a2129e655aba9e00b8e1d77e0bc5d05ecc75cf4ae02cf8266788822d0306c49c85ee584ed |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-linux-ppc64le.tar.gz) | 2527948c40be2e16724d93916ad5363f15aa22ebf42d59359d8b6f757d30cfef6447434cc93bc5caa5a23a6a00a2da8d8191b6441e06bba469d9d4375989a97 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-linux-s390x.tar.gz) | b777ad764b3a46651ecb0846e5b7f860bb2c1c4bd4d0fcc468c6ccffb7d3b8dcb6dcdd73b13c16ded7219f91bba9f1e92f9258527fd3bb162b54d7901ac303ff |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-windows-386.tar.gz) | 8a2f58aaab01be9fe298e4d01456536047cbdd39a37d3e325c1f69ceab3a0504998be41a9f41a894735dfc4ed22bed02591eea5f3c75ce12d9e95ba134e72ec5 |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-client-windows-amd64.tar.gz) | 2f69cda177a178df149f5de66b7dba7f5ce14c1ffeb7c8d7dc4130c701b47d89bb2fbe74e7a262f573e4d21dee2c92414d050d7829e7c6fc3637a9d6b0b9c5c1 |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-server-linux-amd64.tar.gz) | 3ecaac0213d369eab691ac55376821a80df5013cb12e1263f18d1c236a9e49d42b3cea422175556d8f929cdf3109b22c0b6212ac0f2e80cc7a5f4afa3aba5f24 |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-server-linux-arm.tar.gz) | 580030b57ff207e177208fec0801a43389cae10cc2c9306327d354e7be6a055390184531d54b6742e0983550b7a76693cc4a705c2d2f4ac30495cf63cef26b9b |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-server-linux-arm64.tar.gz) | 3e3286bd54671549fbef0dfdaaf1da99bc5c3efb32cc8d1e1985d9926520cea0c43bcf7cbcbbc8b1c1a95eab961255693008af3bb1ba743362998b5f0017d6d7 |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-server-linux-ppc64le.tar.gz) | 9fa051e7e97648e97e26b09ab6d26be247b41b1a5938d2189204c9e6688e455afe76612bbcdd994ed5692935d0d960bd96dc222bce4b83f61d62557752b9d75b |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-server-linux-s390x.tar.gz) | fa85d432eff586f30975c95664ac130b9f5ae02dc52b97613ed7a41324496631ea11d1a267daba564cf2485a9e49707814d86bbd3175486c7efc8b58a9314af5 |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-node-linux-amd64.tar.gz) | 86e631f95fe670b467ead2b88d34e0364eaa275935af433d27cc378d82dcaa22041ccce40f5fa9561b9656dadaa578dc018ad458a59b1690d35f86dca4776b5c |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-node-linux-arm.tar.gz) | a8754ff58a0e902397056b8615ab49af07aca347ba7cc4a812c238e3812234862270f25106b6a94753b157bb153b8eae8b39a01ed67384774d798598c243583b |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-node-linux-arm64.tar.gz) | 28d727d7d08e2c856c9b4a574ef2dbf9e37236a0555f7ec5258b4284fa0582fb94b06783aaf50bf661f7503d101fbd70808aba6de02a2f0af94db7d065d25947 |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-node-linux-ppc64le.tar.gz) | a1283449f1a0b155c11449275e9371add544d0bdd4609d6dc737ed5f7dd228e84e24ff249613a2a153691627368dd894ad64f4e6c0010eecc6efd2c13d4fb133 |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-node-linux-s390x.tar.gz) | 5806028ba15a6a9c54a34f90117bc3181428dbb0e7ced30874c9f4a953ea5a0e9b2c73e6b1e2545e1b4e5253e9c7691588538b44cdfa666ce6865964b92d2fa8 |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.2/kubernetes-node-windows-amd64.tar.gz) | d5327e3b7916c78777b9b69ba0f3758c3a8645c67af80114a0ae52babd7af27bb504febbaf51b1bfe5bd2d74c8c5c573471e1cb449f2429453f4b1be9d5e682a |

## 自v1.20.0-beta.1起的变更日志

## 紧急升级说明

### （不，实际上，您必须在升级之前阅读此内容）

- 在kubelet中修复了一个错误，该错误中不遵守exec探测超时的问题。确保依赖此行为的Pod已更新，以正确处理探测超时。

对于某些群集，此行为更改可能是意外的，并且可以通过关闭ExecProbeTimeout功能门来禁用。此门将在以后的版本中锁定和删除，因此始终遵守exec探测超时。（[＃94115](https://github.com/kubernetes/kubernetes/pull/94115)，[@andrewsykim](https://github.com/andrewsykim)）[SIG节点和测试]

- 对于CSI驱动程序，kubelet不再根据CSI规范为NodePublishVolume创建target_path。Kubelet也不再检查登台路径和目标路径是否已装入或已损坏。CSI驱动程序需要是幂等的，并执行任何必要的安装验证。（[＃88759](https://github.com/kubernetes/kubernetes/pull/88759)，[@andyzhangx](https://github.com/andyzhangx)）[SIG存储]
- 库贝丹：
- 现在已弃用了应用于控制平面节点的标签“ node-role.kubernetes.io/master”，并将在GA弃用期过后的将来版本中将其删除。
- 引入一个新标签“ node-role.kubernetes.io/control-plane”，该标签将与“ node-role.kubernetes.io/master”并行应用，直到删除“ node-role.kubernetes.io/master”为止“ 标签。
- 使“ kubeadm升级适用”在升级过程中仅具有“ node-role.kubernetes.io/master”标签的现有节点上添加“ node-role.kubernetes.io/control-plane”标签。
- 请调整您在kubeadm之上构建的工具，以使用“ node-role.kubernetes.io/control-plane”标签。
- 现在已弃用了应用于控制平面节点“ node-role.kubernetes.io/master:NoSchedule”的污点，并将在GA弃用期过后的将来版本中将其删除。
- 对kubeadm CoreDNS / kube-dns托管清单的新的，将来的污点“ node-role.kubernetes.io/control-plane:NoSchedule”应用公差。请注意，此污点尚未应用于kubeadm控制平面节点。
- 请调整您的工作负载以抢先忍受相同的未来污点。

有关更多详细信息，请参见：[http](http://git.k8s.io/enhancements/keps/sig-cluster-lifecycle/kubeadm/2067-rename-master-label-taint/README.md) : [//git.k8s.io/enhancements/keps/sig-cluster-lifecycle/kubeadm/2067-rename-master-label-taint/README.md](https://github.com/neolit123)（[＃95382](https://github.com/kubernetes/kubernetes/pull/95382)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]

## 种类变化

### 弃用

- kubelet中的Docker支持现已弃用，并将在以后的版本中删除。Kubelet使用名为“ dockershim”的模块，该模块实现了对Docker的CRI支持，并且在Kubernetes社区中看到了维护问题。我们鼓励您评估向容器运行时的迁移，该运行时是CRI（符合v1alpha1或v1）的完整实现。（[＃94624](https://github.com/kubernetes/kubernetes/pull/94624)，[@dims](https://github.com/dims)）[SIG节点]
- Kubectl：弃用--delete-local-data（[＃95076](https://github.com/kubernetes/kubernetes/pull/95076)，[@dougsland](https://github.com/dougsland)）[SIG CLI，云提供程序和可伸缩性]

### API变更

- 启用APF的Beta优先于beta 1.19服务器的API优先级和公平性不应在具有1.20+服务器的多服务器群集中运行。（[＃96527](https://github.com/kubernetes/kubernetes/pull/96527)，[@adtac](https://github.com/adtac)）[SIG API机械和测试]

- 添加LoadBalancerIPMode功能门（[＃92312](https://github.com/kubernetes/kubernetes/pull/92312)，[@ Sh4d1](https://github.com/Sh4d1)）[SIG应用，CLI，云提供商和网络]

- 将WindowsContainerResources和注释添加到CRI-API UpdateContainerResourcesRequest（[＃95741](https://github.com/kubernetes/kubernetes/pull/95741)，[@katiewasnothere](https://github.com/katiewasnothere)）[SIG节点]

- `terminating`向EndpointSlice API添加“服务”和条件。

  `serving`跟踪端点的就绪状态，无论其终止状态如何。这与之不同，`ready`因为`ready`只有当Pod没有终止时才如此。 `terminating`当端点终止时为true。对于Pod，这是带有删除时间戳记的任何端点。（[＃92968](https://github.com/kubernetes/kubernetes/pull/92968)，[@andrewsykim](https://github.com/andrewsykim)）[SIG应用和网络]

- 向向下的API（[＃86102](https://github.com/kubernetes/kubernetes/pull/86102)，[@derekwaynecarr](https://github.com/derekwaynecarr)）添加对大页面的支持[SIG API机械，应用程序，CLI，网络，节点，计划和测试]

- 添加了kubelet alpha功能，`GracefulNodeShutdown`该功能使kubelet知道节点系统已关闭，并导致在系统关闭期间正常终止Pod。（[＃96129](https://github.com/kubernetes/kubernetes/pull/96129)，[@bobbypage](https://github.com/bobbypage)）[SIG节点]

- AppProtocol现在是用于端点和服务的GA。ServiceAppProtocol功能闸将在1.21中弃用。（[＃96327](https://github.com/kubernetes/kubernetes/pull/96327)，[@robscott](https://github.com/robscott)）[SIG应用和网络]

- 现在，可以通过设置（新）参数Service.spec.allocateLoadBalancerNodePorts = false来禁用为LoadBalancer类型的服务自动分配NodePorts。默认情况是为类型为LoadBalancer的服务分配NodePorts，这是现有行为。（[＃92744](https://github.com/kubernetes/kubernetes/pull/92744)，[@uablrek](https://github.com/uablrek)）[SIG应用和网络]

- 记录需要使用ServiceTopology功能`service.spec.topologyKeys`。（[＃96528](https://github.com/kubernetes/kubernetes/pull/96528)，[@andrewsykim](https://github.com/andrewsykim)）[SIG应用]

- EndpointSlice具有一个新的NodeName字段，该字段由EndpointSliceNodeName功能门保护。

  - 在即将发布的版本中，将不建议使用EndpointSlice拓扑字段。
  - 在Kubernetes 1.17中弃用EndpointSlice“ IP”地址类型后，该地址类型被正式删除。
  - Discovery.k8s.io/v1alpha1 API已过时，将在Kubernetes 1.21中删除。（[＃96440](https://github.com/kubernetes/kubernetes/pull/96440)，[@robscott](https://github.com/robscott)）[SIG API机械，应用程序和网络]

- 列举了较少的候选人来抢占来提高大型集群中的性能（[＃94814](https://github.com/kubernetes/kubernetes/pull/94814)，[@adtac](https://github.com/adtac)）[SIG计划]

- 如果启用了BoundServiceAccountTokenVolume，则群集管理员可以使用指标`serviceaccount_stale_tokens_total`来监视依赖于扩展令牌的工作负载。如果没有此类工作负载，请通过`kube-apiserver`以标志`--service-account-extend-token-expiration=false`（[＃96273](https://github.com/kubernetes/kubernetes/pull/96273)，[@zshihang](https://github.com/zshihang)）开头关闭扩展令牌。[SIG API机械与认证]

- 在kubelet中引入对基于exec的容器注册表凭据提供程序插件的alpha支持。（[＃94196](https://github.com/kubernetes/kubernetes/pull/94196)，[@andrewsykim](https://github.com/andrewsykim)）[SIG节点和发行版]

- Kube-apiserver现在删除过期的kube-apiserver租赁对象：

  - 该功能位于功能门下`APIServerIdentity`。
  - 将标记添加到kube-apiserver：`identity-lease-garbage-collection-check-period-seconds`（[＃95895](https://github.com/kubernetes/kubernetes/pull/95895)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械，应用程序，[身份](https://github.com/roycaihw)验证和测试]

- 将Pod的可配置fsgroup更改策略移至Beta（[＃96376](https://github.com/kubernetes/kubernetes/pull/96376)，[@ gnufied](https://github.com/gnufied)）[SIG应用和存储]

- 引入了新标记，即--topology-manager-scope = container | pod。默认值为“容器”范围。（[＃92967](https://github.com/kubernetes/kubernetes/pull/92967)，[@cezaryzukowski](https://github.com/cezaryzukowski)）[SIG仪器，节点和测试]

- 可以使用AddedAffinity配置NodeAffinity插件。（[＃96202](https://github.com/kubernetes/kubernetes/pull/96202)，[@alculquicondor](https://github.com/alculquicondor)）[SIG节点，计划和测试]

- 将RuntimeClass功能升级为GA。将node.k8s.io API组从v1beta1升级到v1。（[＃95718](https://github.com/kubernetes/kubernetes/pull/95718)，[@SergeyKanzhelev](https://github.com/SergeyKanzhelev)）[SIG应用，[身份](https://github.com/SergeyKanzhelev)验证，节点，计划和测试]

- 提醒：不赞成使用标签“ failure-domain.beta.kubernetes.io/zone”和“ failure-domain.beta.kubernetes.io/region”，而应使用“ topology.kubernetes.io/zone”和“ topology.kubernetes” .io / region”。“ failure-domain.beta ...”标签的所有用户都应切换到“ topology ...”等效项。（[＃96033](https://github.com/kubernetes/kubernetes/pull/96033)，[@thockin](https://github.com/thockin)）[SIG API机械，应用程序，CLI，云提供程序，网络，节点，计划，存储和测试]

- 如果启用了新功能门MixedProtocolLBSVC，则可以在同一LoadBalancer服务中使用混合协议值。“需要执行的操作”功能门默认情况下处于禁用状态。用户必须为API服务器启用它。（[＃94028](https://github.com/kubernetes/kubernetes/pull/94028)，[@janosi](https://github.com/janosi)）[SIG API机械和应用程序]

- 此PR将引入一个功能门CSIServiceAccountToken以及中的两个附加字段`CSIDriverSpec`。（[＃93130](https://github.com/kubernetes/kubernetes/pull/93130)，[@zshihang](https://github.com/zshihang)）[SIG API机械，应用程序，[身份](https://github.com/zshihang)验证，CLI，网络，节点，存储和测试]

- 用户可以使用功能门尝试cronjob控制器v2。这将是将来版本中的默认控制器。（[＃93370](https://github.com/kubernetes/kubernetes/pull/93370)，[@ alaypatel07](https://github.com/alaypatel07)）[SIG API机械，应用程序，[身份](https://github.com/alaypatel07)验证和测试]

- VolumeSnapshotDataSource在1.20版（[＃95282](https://github.com/kubernetes/kubernetes/pull/95282)，[@ xing-yang](https://github.com/xing-yang)）中移至GA [SIG Apps]

### 特征

- TokenRequest和TokenRequestProjection现在是GA功能。API服务器需要以下标志：
  - `--service-account-issuer`，应设置为一个URL，以标识在群集生存期内将保持稳定的API服务器。
  - `--service-account-key-file`，设置为一个或多个文件，其中包含一个或多个用于验证令牌的公共密钥。
  - `--service-account-signing-key-file`，设置为包含用于签署服务帐户令牌的私钥的文件。可以给同一个文件`kube-controller-manager`用`--service-account-private-key-file`。（[＃95896](https://github.com/kubernetes/kubernetes/pull/95896)，[@zshihang](https://github.com/zshihang)）[SIG API机械和集群生命周期]
- Kubernetes调度程序在`/metrics/resources`端点下报告了一组新的Alpha指标，使管理员可以轻松查看资源消耗（Pod上所有资源的请求和限制），并将其与Pod的实际使用量或节点容量进行比较。（[＃94866](https://github.com/kubernetes/kubernetes/pull/94866)，[@smarterclayton](https://github.com/smarterclayton)）[SIG API机械，工具，节点和调度]
- 添加--experimental-logging-sanitization标志，启用运行时保护，以免泄露日志中的敏感数据（[＃96370](https://github.com/kubernetes/kubernetes/pull/96370)，[@serathius](https://github.com/serathius)）[SIG API机械，集群生命周期和检测]
- 添加一个StorageVersionAPI功能闸，使API服务器在处理某些写入请求之前更新storageversions。此功能使存储迁移器可以管理内置资源的存储迁移。要启用此功能，需要启用internal.apiserver.k8s.io/v1alpha1 API和APIServerIdentity功能门。（[＃93873](https://github.com/kubernetes/kubernetes/pull/93873)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械，认证和测试]
- 添加新`vSphere`指标：`cloudprovider_vsphere_vcenter_versions`。它的内容显示`vCenter`主机名以及相关的服务器版本。（[＃94526](https://github.com/kubernetes/kubernetes/pull/94526)，[@ Danil-Grigorev](https://github.com/Danil-Grigorev)）[SIG云提供程序和工具]
- 将功能添加到大小支持内存的卷（[＃94444](https://github.com/kubernetes/kubernetes/pull/94444)，[@ derekwaynecarr](https://github.com/derekwaynecarr)）中[SIG存储和测试]
- 添加node_authorizer_actions_duration_seconds指标，该指标可用于估计节点授权者的负载。（[＃92466](https://github.com/kubernetes/kubernetes/pull/92466)，[@mborsz](https://github.com/mborsz)）[SIG API机械，认证和检测]
- 将基于pod_的CPU和内存指标添加到Kubelet的/ metrics / resource端点（[＃95839](https://github.com/kubernetes/kubernetes/pull/95839)，[@egernst](https://github.com/egernst)）[SIG仪器，节点和测试]
- 在node-local-cache插件上添加无头服务。（[＃88412](https://github.com/kubernetes/kubernetes/pull/88412)，[@stafot](https://github.com/stafot)）[SIG云提供商和网络]
- CRD：对于结构模式，现在将删除不可为空的null映射字段，并且如果有默认值，则默认为默认值。列表中的空项目将继续保留，如果不能为空，则验证失败。（[＃95423](https://github.com/kubernetes/kubernetes/pull/95423)，[@apelisse](https://github.com/apelisse)）[SIG API机械]
- PodFsGroupChangePolicy的E2e测试（[＃96247](https://github.com/kubernetes/kubernetes/pull/96247)，[@ saikat-royc](https://github.com/saikat-royc)）[SIG存储和测试]
- 将Pod Resources API升级到GA引入了pod_resources_endpoint_requests_total指标，该指标跟踪对pod资源API的请求总数（[＃92165](https://github.com/kubernetes/kubernetes/pull/92165)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）[SIG仪器，节点和测试]
- 介绍api-extensions类别，该类别将返回：例如，当在kubectl get中使用时，对入场配置进行突变，验证入场配置，CRD和APIService。（[＃95603](https://github.com/kubernetes/kubernetes/pull/95603)，[@soltysh](https://github.com/soltysh)）[SIG API机械]
- Kube-apiserver现在维护一个Lease对象来标识自己：
  - 该功能位于功能门下`APIServerIdentity`。
  - 向kube-apiserver添加了两个标志：`identity-lease-duration-seconds`，`identity-lease-renew-interval-seconds`（[＃95533](https://github.com/kubernetes/kubernetes/pull/95533)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械]
- Kube-apiserver：现在可以使用来配置对etcd进行运行状况检查时使用的超时`--etcd-healthcheck-timeout`。默认超时为2秒，与以前的行为匹配。（[＃93244](https://github.com/kubernetes/kubernetes/pull/93244)，[@ Sh4d1](https://github.com/Sh4d1)）[SIG API机械]
- Kubectl：以前，用户无法通过KUBECTL_EXTERNAL_DIFF env向外部差异工具提供参数。现在，此版本允许用户为KUBECTL_EXTERNAL_DIFF env指定args。（[＃95292](https://github.com/kubernetes/kubernetes/pull/95292)，[@dougsland](https://github.com/dougsland)）[SIG CLI]
- 如果新旧Pod的resourceVersion相同，则Scheduler现在将忽略Pod更新事件。（[＃96071](https://github.com/kubernetes/kubernetes/pull/96071)，[@ Huang-Wei](https://github.com/Huang-Wei)）[SIG调度]
- 支持针对云提供商托管资源的自定义标签（[＃96450](https://github.com/kubernetes/kubernetes/pull/96450)，[@ nilo19](https://github.com/nilo19)）[SIG云提供商]
- 支持自定义负载平衡器运行状况探测协议和请求路径（[＃96338](https://github.com/kubernetes/kubernetes/pull/96338)，[@ nilo19](https://github.com/nilo19)）[SIG云提供程序]
- 在一个群集中支持多个标准负载均衡器（[＃96111](https://github.com/kubernetes/kubernetes/pull/96111)，[@ nilo19](https://github.com/nilo19)）[SIG Cloud Provider]
- Beta`RootCAConfigMap`功能门默认情况下处于启用状态，并导致kube-controller-manager向每个名称空间发布“ kube-root-ca.crt” ConfigMap。此ConfigMap包含一个CA捆绑包，用于验证与kube-apiserver的连接。（[＃](https://github.com/kubernetes/kubernetes/pull/96197)[96197](https://github.com/zshihang)，[@zshihang](https://github.com/zshihang)）[SIG API机械，应用程序，[身份](https://github.com/zshihang)验证和测试]
- kubelet_runtime_operations_duration_seconds指标另外获得了60、300、600、900和1200秒的存储桶（[＃96054](https://github.com/kubernetes/kubernetes/pull/96054)，[@ alvaroaleman](https://github.com/alvaroaleman)）[SIG仪表和节点]
- 有一个新的pv_collector_total_pv_count度量标准，该度量标准通过卷插件名称和卷模式对持久卷进行计数。（[＃95719](https://github.com/kubernetes/kubernetes/pull/95719)，[@tsmetana](https://github.com/tsmetana)）[SIG应用，仪器，存储和测试]
- 卷快照e2e测试，用于验证PVC和VolumeSnapshotContent终结器（[＃95863](https://github.com/kubernetes/kubernetes/pull/95863)，[@ RaunakShah](https://github.com/RaunakShah)）[SIG云提供程序，存储和测试]
- 在执行kubectl apply / diff到当前正在删除的资源时警告用户。（[＃95544](https://github.com/kubernetes/kubernetes/pull/95544)，[@SaiHarshaK](https://github.com/SaiHarshaK)）[SIG CLI]
- `kubectl alpha debug`已毕业到beta版了`kubectl debug`。（[＃96138](https://github.com/kubernetes/kubernetes/pull/96138)，[@verb](https://github.com/verb)）[SIG CLI和测试]
- `kubectl debug`在复制用于调试的Pod时获得更改容器映像的支持，类似于`kubectl set image`工作原理。请参阅`kubectl help debug`以获取更多信息。（[＃96058](https://github.com/kubernetes/kubernetes/pull/96058)，[@verb](https://github.com/verb)）[SIG CLI]

### 文献资料

- 更新有关外部云提供商的云提供商InstancesV2和Zones接口的文档和指南：
  - 删除InstancesV2的实验性警告
  - 文档说明InstancesV2的实现将禁用对区域的调用
  - 赞成使用InstancesV2（[＃96397](https://github.com/kubernetes/kubernetes/pull/96397)，[@andrewsykim](https://github.com/andrewsykim)）弃用区域[SIG云提供程序]

### 错误或回归

- 在csi和flexvolume的fsgroupapplymetrics中更改插件名称，以区分不同的驱动程序（[＃95892](https://github.com/kubernetes/kubernetes/pull/95892)，[@JornShen](https://github.com/JornShen)）[SIG仪表，存储和测试]

- 使用nodeport（[＃71573](https://github.com/kubernetes/kubernetes/pull/71573)，[@JacobTanenbaum](https://github.com/JacobTanenbaum)）时，清除端点更改上的UDP conntrack条目[SIG网络]

- 公开并为TokenReview客户端设置DelegatingAuthenticationOptions（[＃96217](https://github.com/kubernetes/kubernetes/pull/96217)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）的默认超时[SIG API机械和云提供商]

- 修复了CVE-2020-8555的Quobyte客户端连接。（[＃95206](https://github.com/kubernetes/kubernetes/pull/95206)，[@misterikkit](https://github.com/misterikkit)）[SIG存储]

- 修复UDP和TCP数据包的IP碎片不支持LoadBalancer规则（[＃96464](https://github.com/kubernetes/kubernetes/pull/96464)，[@ nilo19](https://github.com/nilo19)）上的问题[SIG Cloud Provider]

- 修复了使用（旧式）调度程序策略时DefaultPreemption插件被禁用的错误。（[＃96439](https://github.com/kubernetes/kubernetes/pull/96439)，[@ Huang-Wei](https://github.com/Huang-Wei)）[SIG计划和测试]

- 修复JSON路径解析器中的错误，该错误在范围为空时发生错误（[＃95933](https://github.com/kubernetes/kubernetes/pull/95933)，[@brianpursley](https://github.com/brianpursley)）[SIG API机械]

- 修复客户端通用方法，以正确显示在某些环境中访问的API路径。（[＃74363](https://github.com/kubernetes/kubernetes/pull/74363)，[@aanm](https://github.com/aanm)）[SIG API机械]

- 修复基础时间来回切换时kube-apiserver中的内存泄漏。（[＃96266](https://github.com/kubernetes/kubernetes/pull/96266)，[@ chenyw1990](https://github.com/chenyw1990)）[SIG API机械]

- 修复了Azure API使用非空的nextLink（[＃96211](https://github.com/kubernetes/kubernetes/pull/96211)，[@feiskyer](https://github.com/feiskyer)）返回空值时的分页问题[SIG Cloud Provider]

- 使用Azure管理身份（[＃96355](https://github.com/kubernetes/kubernetes/pull/96355)，[@andyzhangx](https://github.com/andyzhangx)）修复来自多个[ACR的](https://github.com/kubernetes/kubernetes/pull/96355)拉取图像错误[SIG Cloud Provider]

- 修复可能错误地附加到错误节点的vSphere卷（[＃96224](https://github.com/kubernetes/kubernetes/pull/96224)，[@ gnufied](https://github.com/gnufied)）[SIG云提供程序和存储]

- 修复了阻止kubectl使用对象字段的x-kubernetes-preserve-unknown-fields验证带有模式的CRD的错误。（[＃96369](https://github.com/kubernetes/kubernetes/pull/96369)，[@gautierdelorme](https://github.com/gautierdelorme)）[SIG API机械和测试]

- 对于vSphere Cloud Provider，如果删除了工作节点的VM，则节点控制器（[＃92608](https://github.com/kubernetes/kubernetes/pull/92608)，[@lubronzhan](https://github.com/lubronzhan)）也将删除该节点[SIG Cloud Provider]

- 默认情况下，所有Kubernetes客户端都启用HTTP / 2连接运行状况检查。该功能应立即可用。如果需要，用户可以通过HTTP2_READ_IDLE_TIMEOUT_SECONDS和HTTP2_PING_TIMEOUT_SECONDS环境变量来调整功能。如果HTTP2_READ_IDLE_TIMEOUT_SECONDS设置为0，则该功能被禁用。（[＃95981](https://github.com/kubernetes/kubernetes/pull/95981)，[@caesarxuchao](https://github.com/caesarxuchao)）[SIG API机制，CLI，云提供程序，群集生命周期，检测和节点]

- 如果用户在请求URL中指定了无效的超时，则该请求将使用HTTP 400终止。

  - 如果用户在请求URL中指定的超时时间超过了apiserver允许的最大请求期限，则该请求将使用HTTP 400终止。（[＃96061](https://github.com/kubernetes/kubernetes/pull/96061)，[@tkashem](https://github.com/tkashem)）[SIG API机械，网络和测试]

- 改进与nodePort端点更改conntrack条目清除相关的错误消息。（[＃96251](https://github.com/kubernetes/kubernetes/pull/96251)，[@ravens](https://github.com/ravens)）[SIG网络]

- 在-v = 4而不是-v = 2（[＃94663](https://github.com/kubernetes/kubernetes/pull/94663)，[@soltysh](https://github.com/soltysh)）上打印go堆栈跟踪信息[SIG CLI]

- 在emptyDir卷TearDown期间，删除就绪文件及其目录（在卷设置期间创建）。（[＃95770](https://github.com/kubernetes/kubernetes/pull/95770)，[@ jingxu97](https://github.com/jingxu97)）[SIG存储]

- 当遇到拥有不正确数据的ownerReferences时，解决垃圾收集控制器的不确定行为。

  ```
  OwnerRefInvalidNamespace
  ```

  当检测到子对象和所有者对象之间的名称空间不匹配时，将记录原因为的事件。

  - 现在，将具有ownerReference引用命名空间类型的uid（该命名空间不存在于同一命名空间中）的命名空间对象统一视为该所有者不存在，并且删除子对象。
  - 现在可以一致地对待具有ownerReference引用命名空间类型的uid的群集范围内的对象，就像该所有者是不可解析的一样，并且垃圾回收器将忽略子对象。（[＃92743](https://github.com/kubernetes/kubernetes/pull/92743)，[@liggitt](https://github.com/liggitt)）[SIG API机械，应用和测试]

- 跳过[k8s.io/kubernetes@v1.19.0/test/e2e/storage/testsuites/base.go:162]：驱动程序azure磁盘不支持快照类型DynamicSnapshot-跳过跳过[k8s.io/kubernetes@v1 .19.0 / test / e2e / storage / testsuites / base.go：185]：驱动程序azure-disk不支持[ntfs-](https://github.com/kubernetes/kubernetes/pull/96144)跳过（[＃96144](https://github.com/kubernetes/kubernetes/pull/96144)，[@qinpingli](https://github.com/qinpingli)）[SIG存储和测试]

- 现在可以在服务创建期间指定AWS网络负载平衡器属性（[＃95247](https://github.com/kubernetes/kubernetes/pull/95247)，[@kishorj](https://github.com/kishorj)）[SIG Cloud Provider]

- kube-apiserver将不再提供应在GA非alpha级中删除的API。Alpha级别将继续服务于已删除的API，以便CI不会立即中断。（[＃96525](https://github.com/kubernetes/kubernetes/pull/96525)，[@ deads2k](https://github.com/deads2k)）[SIG API机械]

- 更新max azure数据磁盘计数图（[＃96308](https://github.com/kubernetes/kubernetes/pull/96308)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序和存储]

- 在路由协调循环（[＃96545](https://github.com/kubernetes/kubernetes/pull/96545)，[@ nilo19](https://github.com/nilo19)）中更新路由表标记[SIG Cloud Provider]

- 卷绑定：未找到绑定的PV时，报告UnschedulableAndUnresolvable状态而不是错误（[＃95541](https://github.com/kubernetes/kubernetes/pull/95541)，[@cofyc](https://github.com/cofyc)）[SIG Apps，计划和存储]

- [kubectl]当本地源文件不存在时失败（[＃90333](https://github.com/kubernetes/kubernetes/pull/90333)，[@bamarni](https://github.com/bamarni)）[SIG CLI]

### 其他（清理或片状）

- 处理cronjob控制器v2中的慢速cronjob lister并改善内存占用。（[＃96443](https://github.com/kubernetes/kubernetes/pull/96443)，[@ alaypatel07](https://github.com/alaypatel07)）[SIG应用]
- --redirect-container-streaming不再起作用。该标志将在v1.22中删除（[＃95935](https://github.com/kubernetes/kubernetes/pull/95935)，[@tallclair](https://github.com/tallclair)）[SIG节点]
- 一个新的指标`requestAbortsTotal`已引入中止计数为每个请求`group`，`version`，`verb`，`resource`，`subresource`和`scope`。（[＃95002](https://github.com/kubernetes/kubernetes/pull/95002)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）[SIG API机械，云提供程序，检测和调度]
- API优先级和公平性指标在标签名称中使用snake_case（[＃96236](https://github.com/kubernetes/kubernetes/pull/96236)，[@adtac](https://github.com/adtac)）[SIG API机械，集群生命周期，检测和测试]
- 将翻译应用于所有命令描述（[＃95439](https://github.com/kubernetes/kubernetes/pull/95439)，[@HerrNaN](https://github.com/HerrNaN)）[SIG CLI]
- 更改：从HTTP探针中删除了默认的“ Accept-Encoding”标头。见https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#http-probes（[＃96127](https://github.com/kubernetes/kubernetes/pull/96127)，[@ fonsecas72](https://github.com/fonsecas72)）[SIG网络和节点]
- 服务的生成器已从kubectl（[＃95256](https://github.com/kubernetes/kubernetes/pull/95256)，[@ Git-Jiro](https://github.com/Git-Jiro)）中删除[SIG CLI]
- 介绍kubectl-convert插件。（[＃96190](https://github.com/kubernetes/kubernetes/pull/96190)，[@soltysh](https://github.com/soltysh)）[SIG CLI和测试]
- 现在，Kube-scheduler在启动时记录已处理的组件配置（[＃96426](https://github.com/kubernetes/kubernetes/pull/96426)，[@damemi](https://github.com/damemi)）[SIG计划]
- 无（[＃96179](https://github.com/kubernetes/kubernetes/pull/96179)，[@ bbyrne5](https://github.com/bbyrne5)）[SIG网络]
- 用户现在将能够配置AWS NLB运行状况检查间隔的所有受支持的值以及新资源的阈值。（[＃96312](https://github.com/kubernetes/kubernetes/pull/96312)，[@kishorj](https://github.com/kishorj)）[SIG云提供商]

## 依存关系

### 添加

- cloud.google.com/go/firestore：v1.1.0
- github.com/armon/go-metrics：[f0300d1](https://github.com/armon/go-metrics/tree/f0300d1)
- github.com/armon/go-radix：[7fddfc3](https://github.com/armon/go-radix/tree/7fddfc3)
- github.com/bketelsen/crypt：[5cbc8cc](https://github.com/bketelsen/crypt/tree/5cbc8cc)
- github.com/hashicorp/consul/api：[V1.1.0](https://github.com/hashicorp/consul/api/tree/v1.1.0)
- github.com/hashicorp/consul/sdk：[v0.1.1](https://github.com/hashicorp/consul/sdk/tree/v0.1.1)
- github.com/hashicorp/errwrap：[V1.0.0](https://github.com/hashicorp/errwrap/tree/v1.0.0)
- github.com/hashicorp/go-cleanhttp：[v0.5.1](https://github.com/hashicorp/go-cleanhttp/tree/v0.5.1)
- github.com/hashicorp/go-immutable-radix：[V1.0.0](https://github.com/hashicorp/go-immutable-radix/tree/v1.0.0)
- github.com/hashicorp/go-msgpack：[v0.5.3](https://github.com/hashicorp/go-msgpack/tree/v0.5.3)
- github.com/hashicorp/go-multierror：[V1.0.0](https://github.com/hashicorp/go-multierror/tree/v1.0.0)
- github.com/hashicorp/go-rootcerts：[V1.0.0](https://github.com/hashicorp/go-rootcerts/tree/v1.0.0)
- github.com/hashicorp/go-sockaddr：[V1.0.0](https://github.com/hashicorp/go-sockaddr/tree/v1.0.0)
- github.com/hashicorp/go-uuid：[V1.0.1](https://github.com/hashicorp/go-uuid/tree/v1.0.1)
- github.com/hashicorp/go.net：[v0.0.1](https://github.com/hashicorp/go.net/tree/v0.0.1)
- github.com/hashicorp/logutils：[V1.0.0](https://github.com/hashicorp/logutils/tree/v1.0.0)
- github.com/hashicorp/mdns：[V1.0.0](https://github.com/hashicorp/mdns/tree/v1.0.0)
- github.com/hashicorp/memberlist：[v0.1.3](https://github.com/hashicorp/memberlist/tree/v0.1.3)
- github.com/hashicorp/serf：[v0.8.2](https://github.com/hashicorp/serf/tree/v0.8.2)
- github.com/mitchellh/cli：[V1.0.0](https://github.com/mitchellh/cli/tree/v1.0.0)
- github.com/mitchellh/go-testing-interface：[V1.0.0](https://github.com/mitchellh/go-testing-interface/tree/v1.0.0)
- github.com/mitchellh/gox：[V0.4.0](https://github.com/mitchellh/gox/tree/v0.4.0)
- github.com/mitchellh/iochan：[V1.0.0](https://github.com/mitchellh/iochan/tree/v1.0.0)
- github.com/pascaldekloe/goe：[57f6aae](https://github.com/pascaldekloe/goe/tree/57f6aae)
- github.com/posener/complete：[V1.1.1](https://github.com/posener/complete/tree/v1.1.1)
- github.com/ryanuber/columnize：[9b3edd6](https://github.com/ryanuber/columnize/tree/9b3edd6)
- github.com/sean-/seed：[e2103e2](https://github.com/sean-/seed/tree/e2103e2)
- github.com/subosito/gotenv：[V1.2.0](https://github.com/subosito/gotenv/tree/v1.2.0)
- github.com/willf/bitset：[d5bec33](https://github.com/willf/bitset/tree/d5bec33)
- gopkg.in/ini.v1：v1.51.0
- gopkg.in/yaml.v3：9f266ea
- rsc.io/quote/v3：v3.1.0
- rsc.io/sampler：v1.3.0

### 已变更

- cloud.google.com/go/bigquery：v1.0.1→v1.4.0
- cloud.google.com/go/datastore：v1.0.0→v1.1.0
- cloud.google.com/go/pubsub：v1.0.1→v1.2.0
- cloud.google.com/go/storage：v1.0.0→v1.6.0
- cloud.google.com/go：v0.51.0→v0.54.0
- github.com/Microsoft/go-winio：[fc70bd9→v0.4.15](https://github.com/Microsoft/go-winio/compare/fc70bd9...v0.4.15)
- github.com/aws/aws-sdk-go：[v1.35.5→v1.35.24](https://github.com/aws/aws-sdk-go/compare/v1.35.5...v1.35.24)
- github.com/blang/semver：v3.5.0 [+不兼容→v3.5.1 +不兼容](https://github.com/blang/semver/compare/v3.5.0...v3.5.1)
- github.com/checkpoint-restore/go-criu/v4：[V4.0.2→V4.1.0](https://github.com/checkpoint-restore/go-criu/v4/compare/v4.0.2...v4.1.0)
- github.com/containerd/containerd：[V1.3.3→V1.4.1](https://github.com/containerd/containerd/compare/v1.3.3...v1.4.1)
- github.com/containerd/ttrpc：[V1.0.0→V1.0.2](https://github.com/containerd/ttrpc/compare/v1.0.0...v1.0.2)
- github.com/containerd/typeurl：[V1.0.0→V1.0.1](https://github.com/containerd/typeurl/compare/v1.0.0...v1.0.1)
- github.com/coreos/etcd：v3.3.10 [+不兼容→v3.3.13 +不兼容](https://github.com/coreos/etcd/compare/v3.3.10...v3.3.13)
- github.com/docker/docker：[aa6a989→bd33bbf](https://github.com/docker/docker/compare/aa6a989...bd33bbf)
- github.com/go-gl/glfw/v3.3/glfw：[12ad95a→6f7a984](https://github.com/go-gl/glfw/v3.3/glfw/compare/12ad95a...6f7a984)
- github.com/golang/groupcache：[215e871→8c9f03a](https://github.com/golang/groupcache/compare/215e871...8c9f03a)
- github.com/golang/mock：[V1.3.1→V1.4.1](https://github.com/golang/mock/compare/v1.3.1...v1.4.1)
- github.com/golang/protobuf：[5.0上→1.4.3](https://github.com/golang/protobuf/compare/v1.4.2...v1.4.3)
- github.com/google/cadvisor：[v0.37.0→v0.38.4](https://github.com/google/cadvisor/compare/v0.37.0...v0.38.4)
- github.com/google/go-cmp：[V0.4.0→v0.5.2](https://github.com/google/go-cmp/compare/v0.4.0...v0.5.2)
- github.com/google/pprof：[d4f498a→1ebb73c](https://github.com/google/pprof/compare/d4f498a...1ebb73c)
- github.com/google/uuid：[V1.1.1→V1.1.2](https://github.com/google/uuid/compare/v1.1.1...v1.1.2)
- github.com/gorilla/mux：[v1.7.3→v1.8.0](https://github.com/gorilla/mux/compare/v1.7.3...v1.8.0)
- github.com/gorilla/websocket：[V1.4.0→5.0上](https://github.com/gorilla/websocket/compare/v1.4.0...v1.4.2)
- github.com/karrick/godirwalk：[v1.7.5→v1.16.1](https://github.com/karrick/godirwalk/compare/v1.7.5...v1.16.1)
- github.com/opencontainers/runc：[819fcc6→V1.0.0-rc92](https://github.com/opencontainers/runc/compare/819fcc6...v1.0.0-rc92)
- github.com/opencontainers/runtime-spec：[237cc4f→4d89ac9](https://github.com/opencontainers/runtime-spec/compare/237cc4f...4d89ac9)
- github.com/opencontainers/selinux：[V1.5.2→V1.6.0](https://github.com/opencontainers/selinux/compare/v1.5.2...v1.6.0)
- github.com/prometheus/procfs：[v0.1.3→v0.2.0](https://github.com/prometheus/procfs/compare/v0.1.3...v0.2.0)
- github.com/quobyte/api：[v0.1.2→v0.1.8](https://github.com/quobyte/api/compare/v0.1.2...v0.1.8)
- github.com/spf13/cobra：[V1.0.0→V1.1.1](https://github.com/spf13/cobra/compare/v1.0.0...v1.1.1)
- github.com/spf13/viper：[V1.4.0→V1.7.0](https://github.com/spf13/viper/compare/v1.4.0...v1.7.0)
- github.com/stretchr/testify：[V1.4.0→V1.6.1](https://github.com/stretchr/testify/compare/v1.4.0...v1.6.1)
- github.com/vishvananda/netns：[52d707b→db3c7e5](https://github.com/vishvananda/netns/compare/52d707b...db3c7e5)
- go.opencensus.io：v0.22.2→v0.22.3
- golang.org/x/exp：da58074→6cc2880
- golang.org/x/lint：fdd1cda→738671d
- golang.org/x/net：ab34263→69a7880
- golang.org/x/oauth2：858c2ad→bf48bf1
- golang.org/x/sys：ed371f2→5cba982
- golang.org/x/text：v0.3.3→v0.3.4
- golang.org/x/time：555d28b→3af7569
- golang.org/x/xerrors：9bdfabe→5ec99f8
- google.golang.org/api：v0.15.1→v0.20.0
- google.golang.org/genproto：cb27e3a→8816d57
- google.golang.org/grpc：v1.27.0→v1.27.1
- google.golang.org/protobuf：v1.24.0→v1.25.0
- honnef.co/go/tools：v0.0.1-2019.2.3→v0.0.1-2020.1.3
- k8s.io/gengo：8167cfd→83324d8
- k8s.io/klog/v2：v2.2.0→v2.4.0
- k8s.io/kube-openapi：8b50664→d219536
- k8s.io/utils：d5654de→67b214c
- sigs.k8s.io/apiserver-network-proxy/konnectivity-client：v0.0.12→v0.0.14
- sigs.k8s.io/structured-merge-diff/v4：b3cf1e8→v4.0.2

### 已移除

- github.com/armon/consul-api：[eb2c6b5](https://github.com/armon/consul-api/tree/eb2c6b5)
- github.com/go-ini/ini：[v1.9.0](https://github.com/go-ini/ini/tree/v1.9.0)
- github.com/ugorji/go：[V1.1.4](https://github.com/ugorji/go/tree/v1.1.4)
- github.com/xordataexchange/crypt：[b2862e3](https://github.com/xordataexchange/crypt/tree/b2862e3)

# v1.20.0-beta.1

## v1.20.0-beta.1的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes.tar.gz) | 4eddf4850c2d57751696f352d0667309339090aeb30ff93e8db8a22c6cdebf74cb2d5dc78d4ae384c4e25491efc39413e2e420a804b76b421a9ad934e56b0667 |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-src.tar.gz) | 59de5221162e9b6d88f5abbdb99765cb2b2e501498ea853fb65f2abe390211e28d9f21e0d87be3ade550a5ea6395d04552cf093d2ce2f99fd45ad46545dd13cb |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-darwin-amd64.tar.gz) | d69ffed19b034a4221fc084e43ac293cf392e98febf5bf580f8d92307a8421d8b3aab18f9ca70608937e836b42c7a34e829f88eba6e040218a4486986e2fca21 |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-linux-386.tar.gz) | 1b542e165860c4adcd4550adc19b86c3db8cd75d2a1b8db17becc752da78b730ee48f1b0aaf8068d7bfbb1d8e023741ec293543bc3dd0f4037172a6917db8169 |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-linux-amd64.tar.gz) | 90ad52785eecb43a6f9035b92b6ba39fc84e67f8bc91cf098e70f8cfdd405c4b9d5c02dccb21022f21bb5b6ce92fdef304def1da0a7255c308e2c5fb3a9cdaab |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-linux-arm.tar.gz) | d0cb3322b056e1821679afa70728ffc0d3375e8f3326dabbe8185be2e60f665ab8985b13a1a432e10281b84a929e0f036960253ac0dd6e0b44677d539e98e61b |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-linux-arm64.tar.gz) | 3aecc8197e0aa368408624add28a2dd5e73f0d8a48e5e33c19edf91d5323071d16a27353a6f3e22df4f66ed7bfbae8e56e0a9050f7bbdf927ce6aeb29bba6374 |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-linux-ppc64le.tar.gz) | 6ff145058f62d478b98f1e418e272555bfb5c7861834fbbf10a8fb334cc7ff09b32f2666a54b230932ba71d2fc7d3b1c1f5e99e6fe6d6ec83926a9b931cd2474 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-linux-s390x.tar.gz) | ff7b8bb894076e05a3524f6327a4a6353b990466f3292e84c92826cb64b5c82b3855f48b8e297ccadc8bcc15552bc056419ff6ff8725fc4e640828af9cc1331b |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-windows-386.tar.gz) | 6c6dcac9c725605763a130b5a975f2b560aa976a5c809d4e0887900701b707baccb9ca1aebc10a03cfa7338a6f42922bbf838ccf6800fc2a3e231686a72568b6 |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-client-windows-amd64.tar.gz) | d12e3a29c960f0ddd1b9aabf5426ac1259863ac6c8f2be1736ebeb57ddca6b1c747ee2c363be19e059e38cf71488c5ea3509ad4d0e67fd5087282a5ad0ae9a48 |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-server-linux-amd64.tar.gz) | 904e8c049179e071c6caa65f525f465260bb4d4318a6dd9cc05be2172f39f7cfc69d1672736e01d926045764fe8872e806444e3af77ffef823ede769537b7d20 |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-server-linux-arm.tar.gz) | 5934959374868aed8d4294de84411972660bca7b2e952201a9403f37e40c60a5c53eaea8001344d0bf4a00c8cd27de6324d88161388de27f263a5761357cb82b |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-server-linux-arm64.tar.gz) | 4c884585970f80dc5462d9a734d7d5be9558b36c6e326a8a3139423efbd7284fa9f53fb077983647e17e19f03f5cb9bf26201450c78daecf10afa5a1ab5f9efc |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-server-linux-ppc64le.tar.gz) | 235b78b08440350dcb9f13b63f7722bd090c672d8e724ca5d409256e5a5d4f46d431652a1aa908c3affc5b1e162318471de443d38b93286113e79e7f90501a9b |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-server-linux-s390x.tar.gz) | 220fc9351702b3ecdcf79089892ceb26753a8a1deaf46922ffb3d3b62b999c93fef89440e779ca6043372b963081891b3a966d1a5df0cf261bdd44395fd28dce |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-node-linux-amd64.tar.gz) | fe59d3a1f21c47bab126f689687657f77fbcb46a2caeef48eecd073b2b22879f997a466911b5c5c829e9cf27e68a36ecdf18686d42714839d4b97d6c7281578d |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-node-linux-arm.tar.gz) | 93e545aa963cfd11e0b2c6d47669b5ef70c5a86ef80c3353c1a074396bff1e8e7371dda25c39d78c7a9e761f2607b8b5ab843fa0c10b8ff9663098fae8d25725 |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-node-linux-arm64.tar.gz) | 5e0f177f9bec406a668d4b37e69b191208551fdf289c82b5ec898959da4f8a00a2b0695cbf1d2de5acb809321c6e5604f5483d33556543d92b96dcf80e814dd3 |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-node-linux-ppc64le.tar.gz) | 574412059e4d257eb904cd4892a075b6a2cde27adfa4976ee64c46d6768facece338475f1b652ad94c8df7cfcbb70ebdf0113be109c7099ab76ffdb6f023eefd |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-node-linux-s390x.tar.gz) | b1ffaa6d7f77d89885c642663cb14a86f3e2ec2afd223e3bb2000962758cf0f15320969ffc4be93b5826ff22d54fdbae0dbea09f9d8228eda6da50b6fdc88758 |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.1/kubernetes-node-windows-amd64.tar.gz) | 388983765213cf3bdc1f8b27103ed79e39028767e5f1571e35ed1f91ed100e49f3027f7b7ff19b53fab7fbb6d723c0439f21fc6ed62be64532c25f5bfa7ee265 |

## 从v1.20.0-beta.0开始的变更日志

## 种类变化

### 弃用

- 需要采取的措施：从v1.10开始不推荐使用的在不安全端口上服务的kube-apiserver功能已被删除。不安全的位置标志`--address`，并`--insecure-bind-address`在KUBE-API服务器没有影响，在V1.24被删除。不安全的端口标志`--port`，`--insecure-port`只能设置为0，并将在v1.24中删除。（[＃95856](https://github.com/kubernetes/kubernetes/pull/95856)，[@ knight42](https://github.com/knight42)）[SIG API机械，节点和测试]

### API变更

- - `TokenRequest`并且`TokenRequestProjection`功能已升级到通用航空。此功能允许生成在“秘密”对象中不可见并且与Pod对象的生存期相关的服务帐户令牌。有关配置和使用此功能的详细信息，请参见https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection。该`TokenRequest`和`TokenRequestProjection`功能大门将在V1.21被删除。
  - kubeadm的kube-apiserver Pod清单现在默认包含以下标志：“-service-account-key-file”，“-service-account-signing-key-file”，“-service-account-issuer”。（[＃93258](https://github.com/kubernetes/kubernetes/pull/93258)，[@zshihang](https://github.com/zshihang)）[SIG API机械，[身份](https://github.com/zshihang)验证，群集生命周期，存储和测试]
- 将服务更改为`type`不需要这些字段的模式时，将自动清除Service对象上的某些字段。例如，从type = LoadBalancer更改为type = ClusterIP将清除NodePort分配，而不是强制用户清除它们。（[＃95196](https://github.com/kubernetes/kubernetes/pull/95196)，[@thockin](https://github.com/thockin)）[SIG API机械，应用程序，网络和测试]
- 服务现在将具有一个`clusterIPs`领域`clusterIP`。 `clusterIPs[0]`是的同义词`clusterIP`，将在创建和更新操作时同步化。（[＃95894](https://github.com/kubernetes/kubernetes/pull/95894)，[@thockin](https://github.com/thockin)）[SIG网络]

### 特征

- `apiserver_request_filter_duration_seconds`引入了新的度量标准，以秒为单位度量请求过滤器的延迟。（[＃95207](https://github.com/kubernetes/kubernetes/pull/95207)，[@tkashem](https://github.com/tkashem)）[SIG API机械和仪器]
- 添加一个新标志来设置Windows节点上kubelet的优先级，以使工作负载不会通过破坏kubelet进程淹没那里的节点。（[＃96051](https://github.com/kubernetes/kubernetes/pull/96051)，[@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)）[SIG节点和Windows]
- 更改：将默认的“ Accept：*/* ”标头添加到HTTP探针。见https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#http-probes（https://github.com/kubernetes/website/pull/24756） （[＃95641](https://github.com/kubernetes/kubernetes/pull/95641)，[@ fonsecas72](https://github.com/fonsecas72)）[SIG网络和节点]
- 现在，可以通过KUBERNETES_EXEC_INFO环境变量在当前群集信息中传递客户端证书凭据插件。（[＃95489](https://github.com/kubernetes/kubernetes/pull/95489)，[@ankeesler](https://github.com/ankeesler)）[SIG API机械和认证]
- Kube-apiserver：添加了对使用`--audit-log-compress`（[＃94066](https://github.com/kubernetes/kubernetes/pull/94066)，[@lojies](https://github.com/lojies)）压缩旋转审核日志文件的支持[SIG API的机制和认证]

### 文献资料

- 伪造的动态客户端：List不会在UnstructuredList中保留TypeMeta的文档（[＃95117](https://github.com/kubernetes/kubernetes/pull/95117)，[@andrewsykim](https://github.com/andrewsykim)）[SIG API机制]

### 错误或回归

- 通过Windows上的直接服务器返回（DSR）负载平衡器，为kube-proxy添加了对externalTrafficPolicy = Local设置的支持。（[＃93166](https://github.com/kubernetes/kubernetes/pull/93166)，[@ elweb9858](https://github.com/elweb9858)）[SIG网络]
- 禁用事件的监视缓存（[＃96052](https://github.com/kubernetes/kubernetes/pull/96052)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/96052)[-t](https://github.com/wojtek-t)）[SIG API机械]
- `LocalStorageCapacityIsolation`在计划期间将禁用禁用功能门。（[＃96092](https://github.com/kubernetes/kubernetes/pull/96092)，[@ Huang-Wei](https://github.com/Huang-Wei)）[SIG调度]
- 修复JSON路径解析器中的错误，该错误在范围为空时发生错误（[＃95933](https://github.com/kubernetes/kubernetes/pull/95933)，[@brianpursley](https://github.com/brianpursley)）[SIG API机械]
- 修复k8s.io/apimachinery/pkg/api/meta.SetStatusCondition以更新ObservedGeneration（[＃95961](https://github.com/kubernetes/kubernetes/pull/95961)，[@KnicKnic](https://github.com/KnicKnic)）[SIG API机械]
- 修复了以下回归问题：`docker/default`如果存在允许`runtime/default`seccomp配置文件的PodSecurityPolicy ，则会阻止在1.19中创建带有seccomp批注的容器。（[＃95985](https://github.com/kubernetes/kubernetes/pull/95985)，[@saschagrunert](https://github.com/saschagrunert)）[SIG[身份](https://github.com/saschagrunert)验证]
- Kubectl：如果用户将标志放在插件名称之前（[＃92343](https://github.com/kubernetes/kubernetes/pull/92343)，[@ knight42](https://github.com/knight42)），[则会](https://github.com/knight42)出现打印错误[SIG CLI]
- 当创建具有已设置volume.beta.kubernetes.io/storage-provisioner注释的PVC时，PV控制器可能会错误地删除新配置的PV，而不是将其绑定到PVC，具体取决于时间和系统负载。（[＃95909](https://github.com/kubernetes/kubernetes/pull/95909)，[@pohly](https://github.com/pohly)）[SIG应用和存储]

### 其他（清理或片状）

- Kubectl：已弃用该`generator`标志，`kubectl autoscale`并且该标志无效，它将在功能版本中删除（[＃92998](https://github.com/kubernetes/kubernetes/pull/92998)，[@SataQiu](https://github.com/SataQiu)）[SIG CLI]
- V1helpers.MatchNodeSelectorTerms现在仅接受节点和条款列表（[＃95871](https://github.com/kubernetes/kubernetes/pull/95871)，[@damemi](https://github.com/damemi)）[SIG应用，计划和存储]
- `MatchNodeSelectorTerms`函数移至`k8s.io/component-helpers`（[＃95531](https://github.com/kubernetes/kubernetes/pull/95531)，[@damemi](https://github.com/damemi)）[SIG应用，计划和存储]

## 依存关系

### 添加

*什么也没有变。*

### 已变更

*什么也没有变。*

### 已移除

*什么也没有变。*

# v1.20.0-beta.0

## v1.20.0-beta.0的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes.tar.gz) | 385e49e32bbd6996f07bcadbf42285755b8a8ef9826ee1ba42bd82c65827cf13f63e5634b834451b263a93b708299cbb4b4b0b8ddbc688433deaf6bec240aa67 |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-src.tar.gz) | 842e80f6dcad461426fb699de8a55fde8621d76a94e54288fe9939cc1a3bbd0f4799abadac2c59bcf3f91d743726dbd17e1755312ae7fec482ef560f336dbcbb |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-darwin-amd64.tar.gz) | bde5e7d9ee3e79d1e69465a3ddb4bb36819a4f281b5c01a7976816d7c784410812dde133cdf941c47e5434e9520701b9c5e8b94d61dca77c172f87488dfaeb26 |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-linux-386.tar.gz) | 721bb8444c9e0d7a9f8461e3f5428882d76fcb3def6eb11b8e8e08fae7f7383630699248660d69d4f6a774124d6437888666e1fa81298d5b5518bc4a6a6b6c2c92 |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-linux-amd64.tar.gz) | 71e4edc41afbd65f813e7ecbc22b27c95f248446f005e288d758138dc4cc708735be7218af51bcf15e8b9893a3598c45d6a685f605b46f50af3762b02c32ed76 |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-linux-arm.tar.gz) | bbefc749156f63898973f2f7c7a6f1467481329fb430d641fe659b497e64d679886482d557ebdddb95932b93de8d1e3e365c91d4bf9f110b68bd94b0ba702ded |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-linux-arm64.tar.gz) | 9803190685058b4b64d002c2fbfb313308bcea4734ed53a8c340cfdae4894d8cb13b3e819ae64051bafe0fbf8b6ecab53a6c1dcf661c57640c75b0eb60041113 |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-linux-ppc64le.tar.gz) | bcdceea64cba1ae38ea2bab50d8fd77c53f6d673de12566050b0e3c204334610e6c19e4ace763e68b5e48ab9e811521208b852b1741627be30a2b17324fc1daf |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-linux-s390x.tar.gz) | 41e36d00867e90012d5d5adfabfaae8d9f5a9fd32f290811e3c368e11822916b973afaaf43961081197f2cbab234090d97d89774e674aeadc1da61f7a64708a9 |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-windows-386.tar.gz) | c50fec5aec2d0e742f851f25c236cb73e76f8fc73b0908049a10ae736c0205b8fff83eb3d29b1748412edd942da00dd738195d9003f25b577d6af8359d84fb2f |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-client-windows-amd64.tar.gz) | 0fd6777c349908b6d627e849ea2d34c048b8de41f7df8a19898623f597e6debd35b7bcbf8e1d43a1be3a9abb45e4810bc498a0963cf780b109e93211659e9c7e |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-server-linux-amd64.tar.gz) | 30d982424ca64bf0923503ae8195b2e2a59497096b2d9e58dfd491cd6639633027acfa9750bc7bccf34e1dc116d29d2f87cbd7ae713db4210ce9ac16182f0576 |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-server-linux-arm.tar.gz) | f08b62be9bc6f0745f820b0083c7a31eedb2ce370a037c768459a59192107b944c8f4345d0bb88fc975f2e7a803ac692c9ac3e16d4a659249d4600e84ff75d9e |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-server-linux-arm64.tar.gz) | e3472b5b3dfae0a56e5363d52062b1e4a9fc227a05e0cf5ece38233b2c442f427970aab94a52377fb87e583663c120760d154bc1c4ac22dca1f4d0d1ebb96088 |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-server-linux-ppc64le.tar.gz) | 06c254e0a62f755d31bc40093d86c44974f0a60308716cc3214a6b3c249a4d74534d909b82f8a3dd3a3c9720e61465b45d2bb3a327ef85d3caba865750020dfb |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-server-linux-s390x.tar.gz) | 2edeb4411c26a0de057a66787091ab1044f71774a464aed898ffee26634a40127181c2edddb38e786b6757cca878fd0c3a885880eec6c3448b93c645770abb12 |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-node-linux-amd64.tar.gz) | cc1d5b94b86070b5e7746d7aaeaeac3b3a5e5ebbff1ec33885f7eeab270a6177d593cb1975b2e56f4430b7859ad42da76f266629f9313e0ff688571691ac448ed |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-node-linux-arm.tar.gz) | 75e82c7c9122add3b24695b94dcb0723c52420c3956abf47511e37785aa48a1fa8257db090c6601010c4475a325ccfff13eb3352b65e3aa1774f104b09b766b0 |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-node-linux-arm64.tar.gz) | 16ef27c40bf4d678a55fcd3d3f7d09f1597eec2cc58f9950946f0901e52b82287be397ad7f65e8d162d8a9cdb4a34a610b6db8b5d0462be8e27c4b6eb5d6e5e7 |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-node-linux-ppc64le.tar.gz) | 939865f2c4cb6a8934f22a06223e416dec5f768ffc1010314586149470420a1d62aef97527c34d8a636621c9669d6489908ce1caf96f109e8d073cee1c030b50 |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-node-linux-s390x.tar.gz) | bbfdd844075fb816079af7b73d99bc1a78f41717cdbadb043f6f5872b4dc47bc619f7f95e2680d4b516146db492c630c17424e36879edb45e40c91bc2ae4493c |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-beta.0/kubernetes-node-windows-amd64.tar.gz) | a2b3ea40086fd71aed71a4858fd3fc79fd1907bc9ea8048ff3c82ec56477b0a791b724e5a52d79b3b36338c7fbd93dfd3d03b00ccea9042bda0d270fc891e4ec |

## 自v1.20.0-alpha.3起的变更日志

## 紧急升级说明

### （不，实际上，您必须在升级之前阅读此内容）

- Kubeadm：改进serviceSubnet和podSubnet的验证。由于实现细节，必须限制ServiceSubnet的大小，并且掩码不能分配超过20位。PodSubnet针对kube-controller-manager的相应群集“ --node-cidr-mask-size”进行验证，如果值不兼容，它将失败。kubeadm不再在IPv6部署上自动设置节点掩码，您必须检查您的IPv6服务子网掩码是否与默认节点掩码/ 64兼容或正确设置。以前，对于IPv6，如果podSubnet的掩码小于/ 112，则kubeadm计算出的节点掩码为8的倍数，并拆分可用位以最大化用于节点的数量。（[＃95723](https://github.com/kubernetes/kubernetes/pull/95723)，[@aojea](https://github.com/aojea)）[SIG集群生命周期]
- Windows hyper-v容器功能门在1.20中已弃用，在1.21中将被删除（[＃95505](https://github.com/kubernetes/kubernetes/pull/95505)，[@ wawa0210](https://github.com/wawa0210)）[SIG节点和Windows]

## 种类变化

### 弃用

- 在EgressSelectorConfiguration API中支持将“ controlplane”作为有效的EgressSelection类型。“ Master”已弃用，并将在v1.22中删除。（[＃](https://github.com/kubernetes/kubernetes/pull/95235)[95235](https://github.com/andrewsykim)，[@andrewsykim](https://github.com/andrewsykim)）[SIG API机械]

### API变更

- 添加双栈服务（alpha）。这是对alpha API的重大更改。它将双栈API wrt服务从单个ipFamily字段更改为3个字段：ipFamilyPolicy（SingleStack，PreferDualStack，RequireDualStack），ipFamily（分配的族列表）和clusterIP（包括clusterIP）。大多数用户根本不需要设置任何东西，默认情况下会为他们处理。服务是单栈的，除非用户要求双栈。所有这些都由“ IPv6DualStack”功能门控制。（[＃](https://github.com/kubernetes/kubernetes/pull/91824)[91824](https://github.com/khenidak)，[@khenidak](https://github.com/khenidak)）[SIG API机械，应用程序，CLI，网络，节点，计划和测试]
- 引入了HPA的度量标准源，该度量标准源允许根据容器资源的使用量进行扩展。（[＃](https://github.com/kubernetes/kubernetes/pull/90691)[90691](https://github.com/arjunrn)，[@arjunrn](https://github.com/arjunrn)）[SIG API机械，应用程序，自动[缩放](https://github.com/arjunrn)和CLI]

### 特征

- 添加用于执行递归权限更改所花费时间的度量标准（[＃95866](https://github.com/kubernetes/kubernetes/pull/95866)，[@JornShen](https://github.com/JornShen)）[SIG仪表和存储]
- 允许在不同平台上交叉编译kubernetes。（[＃94403](https://github.com/kubernetes/kubernetes/pull/94403)，[@bnrjee](https://github.com/bnrjee)）[SIG版本]
- 命令来启动网络代理更改自'KUBE_ENABLE_EGRESS_VIA_KONNECTIVITY_SERVICE ./cluster/kube-up.sh'到'KUBE_ENABLE_KONNECTIVITY_SERVICE =真./hack/kube-up.sh'（[＃92669](https://github.com/kubernetes/kubernetes/pull/92669)，[@Jefftree](https://github.com/Jefftree)）[SIG云供应商]
- DefaultPodTopologySpread升级到Beta。默认情况下，功能门处于启用状态。（[＃95631](https://github.com/kubernetes/kubernetes/pull/95631)，[@alculquicondor](https://github.com/alculquicondor)）[SIG计划和测试]
- Kubernetes E2E测试映像清单清单现在包含Windows映像。（[＃77398](https://github.com/kubernetes/kubernetes/pull/77398)，[@claudiubelu](https://github.com/claudiubelu)）[SIG测试和Windows]
- 增加了对Windows容器映像（操作系统版本：1809、1903、1909、2004）的支持：pause：3.4映像。（[＃](https://github.com/kubernetes/kubernetes/pull/91452)[91452](https://github.com/claudiubelu)，[@claudiubelu](https://github.com/claudiubelu)）[SIG节点，版本和Windows]

### 文献资料

- 伪造的动态客户端：List不会在UnstructuredList中保留TypeMeta的文档（[＃95117](https://github.com/kubernetes/kubernetes/pull/95117)，[@andrewsykim](https://github.com/andrewsykim)）[SIG API机制]

### 错误或回归

- 公开并设置DelegatingAuthorizationOptions的SubjectAccessReview客户端的默认超时。（[＃95725](https://github.com/kubernetes/kubernetes/pull/95725)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）[SIG API机械和云提供商]
- 使用pvc（[＃95635](https://github.com/kubernetes/kubernetes/pull/95635)，[@RaunakShah](https://github.com/RaunakShah)）更改措辞来描述[广告](https://github.com/kubernetes/kubernetes/pull/95635)[连播](https://github.com/RaunakShah)[SIG CLI]
- 如果我们在scaleUp行为或scaleDown行为上设置SelectPolicy MinPolicySelect，则Horizontal Pod Autoscaler不会自动正确缩放Pod的数量（[＃95647](https://github.com/kubernetes/kubernetes/pull/95647)，[@JoshuaAndrew](https://github.com/JoshuaAndrew)）[SIG Apps and Autoscaling]
- 忽略非Linux操作系统（[＃93220](https://github.com/kubernetes/kubernetes/pull/93220)，[@ wawa0210](https://github.com/wawa0210)）的apparmor [SIG节点和Windows]
- ipvs：确保已加载选定的调度程序内核模块（[＃93040](https://github.com/kubernetes/kubernetes/pull/93040)，[@cmluciano](https://github.com/cmluciano)）[SIG网络]
- Kubeadm：将丢失的“ --experimental-patches”标志添加到“ kubeadm init相位控制平面”（[＃95786](https://github.com/kubernetes/kubernetes/pull/95786)，[@ Sh4d1](https://github.com/Sh4d1)）[SIG集群生命周期]
- 重组了iptables规则以解决性能问题（[＃95252](https://github.com/kubernetes/kubernetes/pull/95252)，[@tssurya](https://github.com/tssurya)）[SIG网络]
- 如果有足够的健康豆荚，则可以成功驱逐PDB覆盖的不健康豆荚。（[＃94381](https://github.com/kubernetes/kubernetes/pull/94381)，[@michaelgugino](https://github.com/michaelgugino)）[SIG应用]
- 在LB更新期间不处于成功置备状态的PIP时进行更新。（[＃95748](https://github.com/kubernetes/kubernetes/pull/95748)，[@ nilo19](https://github.com/nilo19)）[SIG云提供商]
- `pipName`更改服务的批注（[＃95813](https://github.com/kubernetes/kubernetes/pull/95813)，[@ nilo19](https://github.com/nilo19)）时更新前端IP配置[SIG Cloud Provider]

### 其他（清理或片状）

- 否（[＃95690](https://github.com/kubernetes/kubernetes/pull/95690)，[@nikhita](https://github.com/nikhita)）[SIG发行]

## 依存关系

### 添加

- github.com/form3tech-oss/jwt-go：[V3.2.2 +不兼容](https://github.com/form3tech-oss/jwt-go/tree/v3.2.2)

### 已变更

- github.com/Azure/go-autorest/autorest/adal：[v0.9.0→v0.9.5](https://github.com/Azure/go-autorest/autorest/adal/compare/v0.9.0...v0.9.5)
- github.com/Azure/go-autorest/autorest/mocks：[V0.4.0→v0.4.1](https://github.com/Azure/go-autorest/autorest/mocks/compare/v0.4.0...v0.4.1)
- golang.org/x/crypto：75b2880→7f63de1

### 已移除

*什么也没有变。*

# v1.20.0-alpha.3

## v1.20.0-alpha.3的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes.tar.gz) | 542cc9e0cd97732020491456402b6e2b4f54f2714007ee1374a7d363663a1b41e82b50886176a5313aaccfbfd4df2bc611d6b32d19961cdc98b5821b75d6b17c |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-src.tar.gz) | 5e5d725294e552fd1d14fd6716d013222827ac2d4e2d11a7a1fdefb77b3459bbeb69931f38e1597de205dd32a1c9763ab524c2af1551faef4f502ef0890f7fbf |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-darwin-amd64.tar.gz) | 60004939727c75d0f06adc4449e16b43303941937c0e9ea9aca7d947e93a5aed5d11e53d1fc94caeb988be66d39acab118d406dc2d6cead61181e1ced6d2be1a |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-linux-386.tar.gz) | 7edba9c4f1bf38fdf1fa5bff2856c05c0e127333ce19b17edf3119dc9b80462c027404a1f58a5eabf1de73a8f2f20aced043dda1fafd893619db1a188cda550c |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-linux-amd64.tar.gz) | db1818aa82d072cb3e32a2a988e66d76ecf7cebc6b8a29845fa2d6ec27f14a36e4b9839b1b7ed8c43d2da9cde00215eb672a7e8ee235d2e3107bc93c22e58d38 |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-linux-arm.tar.gz) | d2922e70d22364b1f5a1e94a0c115f849fe2575b231b1ba268f73a9d86fc0a9fbb78dc713446839a2593acf1341cb5a115992f350870f13c1a472bb107b75af7 |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-linux-arm64.tar.gz) | 2e3ae20e554c7d4fc3a8afdfcafe6bbc81d4c5e9aea036357baac7a3fdc2e8098aa8a8a8c8dded3951667d57f667ce3fbf37ec5ae5ceb2009a569dc9002d3a92f9 |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-linux-ppc64le.tar.gz) | b54a34e572e6a86221577de376e6f7f9fcd82327f7fe94f2fc8d21f35d302db8a0f3d51e60dc89693999f5df37c96d0c3649a29f07f095efcdd59923ae285c95 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-linux-s390x.tar.gz) | 5be1b70dc437d3ba88cb0b89cd1bc555f79896c3f5b5f4fa0fb046a0d09d758b994d622ebe5cef8e65bba938c5ae945b81dc297f9dfa0d98f82ea75f344a3a0d |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-windows-386.tar.gz) | 88cf3f66168ef3bf9a5d3d2275b7f33799406e8205f2c202997ebec23d449aa4bb48b010356ab1cf52ff7b527b8df7c8b9947a43a82ebe060df83c3d21b7223a |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-client-windows-amd64.tar.gz) | 87d2d4ea1829da8cfa1a705a03ea26c759a03bd1c4d8b96f2c93264c4d172bb63a91d9ddda65cdc5478b627c30ae8993db5baf8be262c157d83bffcebe85474e |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-server-linux-amd64.tar.gz) | 7af691fc0b13a937797912374e3b3eeb88d5262e4eb7d4ebe92a3b64b3c226cb049aedfd7e39f639f6990444f7bcf2fe58699cf0c29039daebe100d7eebf60de |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-server-linux-arm.tar.gz) | 557c47870ecf5c2090b2694c8f0c8e3b4ca23df5455a37945bd037bc6fb5b8f417bf737bb66e6336b285112cb52de0345240fdb2f3ce1c4fb335ca7ef1197f99 |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-server-linux-arm64.tar.gz) | 981de6cf7679d743cdeef1e894314357b68090133814801870504ef30564e32b5675e270db20961e9a731e35241ad9b037bdaf749da87b87c6c4ce8889eeb1c5855 |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-server-linux-ppc64le.tar.gz) | 506578a21601ccff609ae757a55e68634c15cbfecbf13de972c96b32a155ded29bd71aee069c77f5f721416672c7a7ac0b8274de22bfd28e1ecae306313d96c5 |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-server-linux-s390x.tar.gz) | af0cdcd4a77a7cc8060a076641615730a802f1f02dab084e41926023489efec6102d37681c70ab0dbe7440cd3e72ea0443719a365467985360152b9aae657375 |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-node-linux-amd64.tar.gz) | 2d92c61596296279de1efae23b2b707415565d9d50cd61a7231b8d10325732b059bcb90f3afb36bef2575d203938c265572721e38df408e8792d3949523bd5d9 |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-node-linux-arm.tar.gz) | c298de9b5ac1b8778729a2d8e2793ff86743033254fbc27014333880b03c519de81691caf03aa418c729297ee8942ce9ec89d11b0e34a80576b9936015dc1519 |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-node-linux-arm64.tar.gz) | daa3c65afda6d7aff206c1494390bbcc205c2c6f8db04c10ca967a690578a01c49d49c6902b85e7158f79fd4d2a87c5d397d56524a75991c9d7db85ac53059a7 |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-node-linux-ppc64le.tar.gz) | 05661908bb73bfcaf9c2eae96e9a6a793db5a7a100bce6df9e057985dd53a7a5248d72e81b6d13496bd38b9326c17cdb2edaf0e982b6437507245fb846e1efc6 |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-node-linux-s390x.tar.gz) | 845e518e2c4ef0cef2c3b58f0b9ea5b5fe9b8a249717f789607752484c424c26ae854b263b7c0a004a8426feb9aa3683c177a9ed2567e6c3521f4835ea08c24a |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.3/kubernetes-node-windows-amd64.tar.gz) | 530e536574ed2c3e5973d3c0f0fdd2b4d48ef681a7a7c02db13e605001669eeb4f4b8a856fc08fc21436658c27b377f5d04dbcb3aae438098abc953b6eaf5712 |

## 自v1.20.0-alpha.2起的变更日志

## 种类变化

### API变更

- 新的参数`defaultingType`为`PodTopologySpread`插件允许使用限定的或用户提供的默认约束K8S（[＃95048](https://github.com/kubernetes/kubernetes/pull/95048)，[@alculquicondor](https://github.com/alculquicondor)）[SIG调度]

### 特征

- 添加了新的k8s.io/component-helpers存储库，为（核心）组件提供了共享的帮助程序代码。（[＃92507](https://github.com/kubernetes/kubernetes/pull/92507)，[@ingvagabund](https://github.com/ingvagabund)）[SIG应用，节点，发行和计划]
- 将`create ingress`命令添加到`kubectl`（[＃78153](https://github.com/kubernetes/kubernetes/pull/78153)，[@amimof](https://github.com/amimof)）[SIG CLI和网络]
- Kubectl create现在支持创建入口对象。（[＃94327](https://github.com/kubernetes/kubernetes/pull/94327)，[@rikatz](https://github.com/rikatz)）[SIG CLI和网络]
- 当使用污点和节点相似性时，新的默认调度插件顺序减少了调度和抢占延迟（[＃95539](https://github.com/kubernetes/kubernetes/pull/95539)，[@soulxu](https://github.com/soulxu)）[SIG调度]
- API对象（Pod，Service，NetworkPolicy）中的SCTP支持现在为GA。请注意，这对是否在内核级别的节点上启用SCTP没有影响，并且请注意，某些云平台和网络插件不支持SCTP通信。（[＃95566](https://github.com/kubernetes/kubernetes/pull/95566)，[@danwinship](https://github.com/danwinship)）[SIG应用和网络]
- 计划框架：将Run [Pre] ScorePlugins函数公开给PreemptionHandle，可在PostFilter扩展点中使用。（[＃93534](https://github.com/kubernetes/kubernetes/pull/93534)，[@everpeace](https://github.com/everpeace)）[SIG计划和测试]
- 当启用DefaultPodTopologySpread功能（[＃95448](https://github.com/kubernetes/kubernetes/pull/95448)，[@alculquicondor](https://github.com/alculquicondor)）时，SelectorSpreadPriority映射到PodTopologySpread插件[SIG计划]
- SetHostnameAsFQDN已升级为Beta，因此默认情况下已启用。（[＃95267](https://github.com/kubernetes/kubernetes/pull/95267)，[@javidiaz](https://github.com/javidiaz)）[SIG节点]

### 错误或回归

- 现在，解决了`volume.kubernetes.io/storage-resizer`当PVC StorageClass已更新为树外配置程序时，阻止卷扩展控制器注释PVC的问题。（[＃94489](https://github.com/kubernetes/kubernetes/pull/94489)，[@ialidzhikov](https://github.com/ialidzhikov)）[SIG API机械，应用程序和存储]
- 将挂载方式从systemd更改为普通挂载，但ceph和glusterfs intree-volume除外。（[＃94916](https://github.com/kubernetes/kubernetes/pull/94916)，[@smileusd](https://github.com/smileusd)）[SIG应用，云提供商，网络，节点，存储和测试]
- 修复了大于4TB的磁盘的azure磁盘附加故障（[＃95463](https://github.com/kubernetes/kubernetes/pull/95463)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]
- 修复了卸载磁盘（[＃95456](https://github.com/kubernetes/kubernetes/pull/95456)，[@andyzhangx](https://github.com/andyzhangx)）时Windows上的天蓝色磁盘数据丢失问题[SIG云提供程序和存储]
- 修复kube-apiserver指标的动词和范围报告（列表报告而不是GET）（[＃95562](https://github.com/kubernetes/kubernetes/pull/95562)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/95562)[-t](https://github.com/wojtek-t)）[SIG API机械和测试]
- 修复静态PV的vsphere分离失败（[＃95447](https://github.com/kubernetes/kubernetes/pull/95447)，[@ gnufied](https://github.com/gnufied)）[SIG云提供程序和存储]
- 修复：smb有效路径错误（[＃95583](https://github.com/kubernetes/kubernetes/pull/95583)，[@andyzhangx](https://github.com/andyzhangx)）[SIG存储]
- 修复了导致格式错误的错误`kubectl describe ingress`。（[＃94985](https://github.com/kubernetes/kubernetes/pull/94985)，[@howardjohn](https://github.com/howardjohn)）[SIG CLI和网络]
- 修正了在客户端去一臭虫，与新客户定制的`Dial`，`Proxy`，`GetCert`配置可能会过时的HTTP传输。（[＃95427](https://github.com/kubernetes/kubernetes/pull/95427)，[@roycaihw](https://github.com/roycaihw)）[SIG API机械]
- 修复了kubectl消耗（[＃95260](https://github.com/kubernetes/kubernetes/pull/95260)，[@amandahla](https://github.com/amandahla)）中的高CPU使用率[SIG CLI]
- 支持节点标签`node.kubernetes.io/exclude-from-external-load-balancers`（[＃95542](https://github.com/kubernetes/kubernetes/pull/95542)，[@ nilo19](https://github.com/nilo19)）[SIG Cloud Provider]

### 其他（清理或片状）

- 修复功能名称NewCreateCreateDeploymentOptions（[＃91931](https://github.com/kubernetes/kubernetes/pull/91931)，[@ lixiaobing1](https://github.com/lixiaobing1)）[SIG CLI]
- Kubeadm：在Windows上将默认的暂停图像版本更新为1.4.0。通过此更新，该映像支持Windows版本1809（2019LTS），[1903、1909、2004](https://github.com/kubernetes/kubernetes/pull/95419)（[＃95419](https://github.com/kubernetes/kubernetes/pull/95419)，[@jsturtevant](https://github.com/jsturtevant)）[SIG群集生命周期和Windows]
- 将快照控制器升级到3.0.0（[＃95412](https://github.com/kubernetes/kubernetes/pull/95412)，[@ saikat-royc](https://github.com/saikat-royc)）[SIG云提供程序]
- 删除apiserver / cloud-provider / controller-manager上csi-translation-lib模块的依赖项（[＃95543](https://github.com/kubernetes/kubernetes/pull/95543)，[@ wawa0210](https://github.com/wawa0210)）[SIG发行版]
- 调度程序框架接口从pkg / scheduler / framework / v1alpha移至pkg / scheduler / framework（[＃95069](https://github.com/kubernetes/kubernetes/pull/95069)，[@farah](https://github.com/farah)）[SIG调度，存储和测试]
- UDP和SCTP协议可能会留下需要清除的陈旧连接，以避免服务中断，但是它们可能会导致难以调试的问题。使用大于或等于4的日志级别的Kubernetes组件将记录conntrack操作及其输出，以显示已删除的条目。（[＃95694](https://github.com/kubernetes/kubernetes/pull/95694)，[@aojea](https://github.com/aojea)）[SIG网络]

## 依存关系

### 添加

*什么也没有变。*

### 已变更

*什么也没有变。*

### 已移除

*什么也没有变。*

# v1.20.0-alpha.2

## v1.20.0-alpha.2的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes.tar.gz) | 45089a4d26d56a5d613ecbea64e356869ac738eca3cc71d16b74ea8ae1b4527bcc32f1dc35ff7aa8927e138083c7936603faf063121d965a2f0f8ba28fa128d8 |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-src.tar.gz) | 646edd890d6df5858b90aaf68cc6e1b4589b8db09396ae921b5c400f2188234999e6c9633906692add08c6e8b4b09f12b2099132b0a7533443fb2a01cfc2bf81 |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-darwin-amd64.tar.gz) | c136273883e24a2a50b5093b9654f01cdfe57b97461d34885af4a68c2c4d108c07583c02b1cdf7f57f82e91306e542ce8f3bddb12fcce72b744458bc4796f8eb |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-linux-386.tar.gz) | 6ec59f1ed30569fa64ddb2d0de32b1ae04cda4ffe13f339050a7c9d7c63d425ee6f6d963dcf82c17281c4474da3eaf32c08117669052872a8c81bdce2c8a5415 |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-linux-amd64.tar.gz) | 7b40a4c087e2ea7f8d055f297fcd39a3f1cb6c866e7a3981a9408c3c3eb5363c648613491aad11bc7d44d5530b20832f8f96f6ceff43deede911fb74aafad35f |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-linux-arm.tar.gz) | cda9955feebea5acb8f2b5b87895d24894bbbbde47041453b1f926ebdf47a258ce0496aa27d06bcbf365b5615ce68a20d659b64410c54227216726e2ee432fca |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-linux-arm64.tar.gz) | f65bd9241c7eb88a4886a285330f732448570aea4ededaebeabcf70d17ea185f51bf8a7218f146ee09fb1adceca7ee71fb3c3683834f2c415163add820fba96e |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-linux-ppc64le.tar.gz) | 1e377599af100a81d027d9199365fb8208d443a8e0a97affff1a79dc18796e14b78cb53d6e245c1c1e8defd0e050e37bf5f2a23c8a3ff45a6d18d03619709bf5 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-linux-s390x.tar.gz) | 1cdee81478246aa7e7b80ae4efc7f070a5b058083ae278f59fad088b75a8052761b0e15ab261a6e667ddafd6a69fb424fc307072ed47941cad89a85af7aee93d |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-windows-386.tar.gz) | d8774167c87b6844c348aa15e92d5033c528d6ab9e95d08a7cb22da68bafd8e46d442cf57a5f6affad62f674c10ae6947d524b94108b5e450ca78f92656d63c0 |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-client-windows-amd64.tar.gz) | f664b47d8daa6036f8154c1dc1f881bfe683bf57c39d9b491de3848c03d051c50c6644d681baf7f9685eae45f9ce62e4c6dfea2853763cfe8256a61bdd59d894 |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-server-linux-amd64.tar.gz) | d6fcb4600be0beb9de222a8da64c35fe22798a0da82d41401d34d0f0fc7e2817512169524c281423d8f4a007cd77452d966317d5a1b67d2717a05ff346e8aa7d |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-server-linux-arm.tar.gz) | 022a76cf10801f8afbabb509572479b68fdb4e683526fa0799cdbd9bab4d3f6ecb76d1d63d0eafee93e3edf6c12892d84b9c771ef2325663b95347728fa3d6c0 |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-server-linux-arm64.tar.gz) | 0679aadd60bbf6f607e5befad74b5267eb2d4c1b55985cc25a97e0f4c5efb7acbb3ede91bfa6a5a5713dae4d7a302f6faaf678fd6b359284c33d9a6aca2a08bb |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-server-linux-ppc64le.tar.gz) | 9f2cfeed543b515eafb60d9765a3afff4f3d323c0a5c8a0d75e3de25985b2627817bfcbe59a9a61d969e026e2b861adb974a09eae75b58372ed736ceaaed2a82 |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-server-linux-s390x.tar.gz) | 937258704d7b9dcd91f35f2d34ee9dd38c18d9d4e867408c05281bfbbb919ad012c95880bee84d2674761aa44cc617fb2fae1124cf63b689289286d6eac1c407 |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-node-linux-amd64.tar.gz) | 076165d745d47879de68f4404eaf432920884be48277eb409e84bf2c61759633bf3575f46b0995f1fc693023d76c0921ed22a01432e756d7f8d9e246a243b126 |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-node-linux-arm.tar.gz) | 1ff2e2e3e43af41118cdfb70c778e15035bbb1aca833ffd2db83c4bcd44f55693e956deb9e65017ebf3c553f2820ad5cd05f5baa33f3d63f3e00ed980ea4dfed |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-node-linux-arm64.tar.gz) | b232c7359b8c635126899beee76998078eec7a1ef6758d92bcdebe8013b0b1e4d7b33ecbf35e3f82824fe29493400845257e70ed63c1635bfa36c8b3b4969f6f |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-node-linux-ppc64le.tar.gz) | 51d415a068f554840f4c78d11a4fedebd7cb03c686b0ec864509b24f7a8667ebf54bb0a25debcf2b70f38be1e345e743f520695b11806539a55a3620ce21946f |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-node-linux-s390x.tar.gz) | b51c082d8af358233a088b632cf2f6c8cfe5421471c27f5dc9ba4839ae6ea75df25d84298f2042770097554c01742bb7686694b331ad9bafc93c86317b867728 |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.2/kubernetes-node-windows-amd64.tar.gz) | 91b9d26620a2dde67a0edead0039814efccbdfd54594dda3597aaced6d89140dc92612ed0727bc21d63468efeef77c845e640153b09e39d8b736062e6eee0c76 |

## 自v1.20.0-alpha.1起的变更日志

## 种类变化

### 弃用

- 需要采取的措施：kubeadm：将“ kubeadm alpha certs”命令升级为父命令“ kubeadm certs”。命令“ kubeadm alpha certs”已被弃用，在以后的版本中将被删除。请迁移。（[＃94938](https://github.com/kubernetes/kubernetes/pull/94938)，[@yagonobre](https://github.com/yagonobre)）[SIG群集生命周期]
- 需要执行的操作：kubeadm：从kubeadm命令中删除不推荐使用的功能--experimental-kustomize。该功能在1.19中被替换为--experimental-patches。要进行迁移，请参见--experimental-patches标志的--help说明。（[＃94871](https://github.com/kubernetes/kubernetes/pull/94871)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]
- Kubeadm：不赞成使用自托管支持。实验命令“ kubeadm alpha自托管”现已弃用，并将在以后的版本中删除。（[＃95125](https://github.com/kubernetes/kubernetes/pull/95125)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]
- 删除不推荐使用的调度程序指标DeprecatedSchedulingDuration，DeprecatedSchedulingAlgorithmPredicateEvaluationSecondsDuration，DeprecatedSchedulingAlgorithmPriorityEvaluationSecondsDuration（[＃94884](https://github.com/kubernetes/kubernetes/pull/94884)，[@ arghya88](https://github.com/arghya88)）[SIG仪器和调度]
- 不建议使用调度程序Alpha指标binding_duration_seconds和schedule_algorithm_preemption_evaluation_seconds，这两个指标现在都作为framework_extension_point_duration_seconds的一部分涵盖，前者作为PostFilter，后者作为PostFilter，而Bind插件。该计划是在1.21（[＃95001](https://github.com/kubernetes/kubernetes/pull/95001)，[@ arghya88](https://github.com/arghya88)）中同时删除两者[SIG仪表和计划]

### API变更

- 默认情况下，现在默认禁用kubelet提供的GPU指标（[＃95184](https://github.com/kubernetes/kubernetes/pull/95184)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）[SIG节点]
- 新的参数`defaultingType`为`PodTopologySpread`插件允许使用限定的或用户提供的默认约束K8S（[＃95048](https://github.com/kubernetes/kubernetes/pull/95048)，[@alculquicondor](https://github.com/alculquicondor)）[SIG调度]
- 现在，服务器端应用将LabelSelector字段视为原子字段（意味着整个选择器由单个编写者管理并一起更新），因为它们包含相互关联且不可分割的字段，这些字段无法以直观的方式合并。（[＃93901](https://github.com/kubernetes/kubernetes/pull/93901)，[@jpbetz](https://github.com/jpbetz)）[SIG API机制，Auth，CLI，云提供程序，群集生命周期，检测，网络，节点，存储和测试]
- 不含“ preserveUnknownFields：false”的v1beta1 CRD的状态将显示冲突“ spec.preserveUnknownFields：无效值：true：必须为false”（[＃93078](https://github.com/kubernetes/kubernetes/pull/93078)，[@vareti](https://github.com/vareti)）[SIG API机制]

### 特征

- 已将`get-users`和添加`delete-user`到`kubectl config`子命令（[＃89840](https://github.com/kubernetes/kubernetes/pull/89840)，[@eddiezane](https://github.com/eddiezane)）[SIG CLI]

- 添加了计数器指标“ apiserver_request_self”以对带有动词，资源和子资源标签的API服务器自我请求进行计数。（[＃94288](https://github.com/kubernetes/kubernetes/pull/94288)，[@LogicalShark](https://github.com/LogicalShark)）[SIG API机械，[身份](https://github.com/LogicalShark)验证，检测和调度]

- 添加了新的k8s.io/component-helpers存储库，为（核心）组件提供了共享的帮助程序代码。（[＃92507](https://github.com/kubernetes/kubernetes/pull/92507)，[@ingvagabund](https://github.com/ingvagabund)）[SIG应用，节点，发行和计划]

- 将`create ingress`命令添加到`kubectl`（[＃78153](https://github.com/kubernetes/kubernetes/pull/78153)，[@amimof](https://github.com/amimof)）[SIG CLI和网络]

- 允许通过服务注释（[＃94546](https://github.com/kubernetes/kubernetes/pull/94546)，[@kishorj](https://github.com/kishorj)）配置AWS LoadBalancer健康状况检查协议[SIG Cloud Provider]

- Azure：支持共享一个IP地址的多个服务（[＃94991](https://github.com/kubernetes/kubernetes/pull/94991)，[@ nilo19](https://github.com/nilo19)）[SIG云提供程序]

- 临时容器现在应用与[initContainers](https://github.com/kubernetes/kubernetes/pull/94896)和容器相同的API默认值（[＃94896](https://github.com/kubernetes/kubernetes/pull/94896)，[@ wawa0210](https://github.com/wawa0210)）[SIG Apps和CLI]

- 现在，在双栈裸机集群中，您可以将双栈IP传递给`kubelet --node-ip`。例如：`kubelet --node-ip 10.1.0.5,fd01::0005`。非裸金属群集尚不支持此功能。

  在节点具有双栈地址的双栈群集中，hostNetwork Pod现在将获得双栈PodIP。（[＃95239](https://github.com/kubernetes/kubernetes/pull/95239)，[@danwinship](https://github.com/danwinship)）[SIG网络和节点]

- 引入了一个新的GCE特定集群创建变量KUBE_PROXY_DISABLE。设置为true时，这将跳过kube-proxy（守护程序集或静态pod）的创建。这可以用来独立于节点的生命周期来控制kube-proxy的生命周期。（[＃91977](https://github.com/kubernetes/kubernetes/pull/91977)，[@varunmar](https://github.com/varunmar)）[SIG云提供商]

- Kubeadm：如果当前系统时间在已加载证书的NotBefore和NotAfter范围之外，请不要抛出错误。改为打印警告。（[＃94504](https://github.com/kubernetes/kubernetes/pull/94504)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]

- Kubeadm：使命令“ kubeadm alpha kubeconfig用户”接受“ --config”标志，并删除以下标志：

  - apiserver-advertise-address / apiserver-bind-port：使用InitConfiguration中的localAPIEndpoint或ClusterConfiguration中的controlPlaneEndpoint。
  - cluster-name：使用ClusterConfiguration中的clusterName
  - cert-dir：使用ClusterConfiguration中的certificateDir（[＃94879](https://github.com/kubernetes/kubernetes/pull/94879)，[@ knight42](https://github.com/knight42)）[SIG群集生命周期]

- Kubectl推出历史记录sts / sts-name --revision = some-revision将开始显示该指定修订版（[＃86506](https://github.com/kubernetes/kubernetes/pull/86506)，[@dineshba](https://github.com/dineshba)）上sts的详细视图[SIG CLI]

- 计划框架：将Run [Pre] ScorePlugins函数公开给PreemptionHandle，可在PostFilter扩展点中使用。（[＃93534](https://github.com/kubernetes/kubernetes/pull/93534)，[@everpeace](https://github.com/everpeace)）[SIG计划和测试]

- 将gce节点启动脚本日志发送到控制台和日志（[＃95311](https://github.com/kubernetes/kubernetes/pull/95311)，[@karan](https://github.com/karan)）[SIG云提供程序和节点]

- 支持kubectl删除孤立/前景/背景选项（[＃93384](https://github.com/kubernetes/kubernetes/pull/93384)，[@ zhouya0](https://github.com/zhouya0)）[SIG CLI和测试]

### 错误或回归

- 将挂载方式从systemd更改为普通挂载，但ceph和glusterfs intree-volume除外。（[＃94916](https://github.com/kubernetes/kubernetes/pull/94916)，[@smileusd](https://github.com/smileusd)）[SIG应用，云提供商，网络，节点，存储和测试]
- 云节点控制器：处理来自getProviderID（[＃95342](https://github.com/kubernetes/kubernetes/pull/95342)，[@nicolehanjing](https://github.com/nicolehanjing)）的空providerID [SIG Cloud Provider]
- 修复了端点切片控制器未将父服务标签镜像到其相应的端点切片（[＃94443](https://github.com/kubernetes/kubernetes/pull/94443)，[@aojea](https://github.com/aojea)）的错误[SIG Apps and Network]
- 修复了大于4TB的磁盘的azure磁盘附加故障（[＃95463](https://github.com/kubernetes/kubernetes/pull/95463)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]
- 修复了卸载磁盘（[＃95456](https://github.com/kubernetes/kubernetes/pull/95456)，[@andyzhangx](https://github.com/andyzhangx)）时Windows上的天蓝色磁盘数据丢失问题[SIG云提供程序和存储]
- 修复了[虚拟机](https://github.com/kubernetes/kubernetes/pull/95177)不存在时分离天蓝色磁盘的问题（[＃95177](https://github.com/kubernetes/kubernetes/pull/95177)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]
- 修复了针对Endpoints / EndpointSlice删除的network_programming_latency指标报告，在该报告中我们没有正确的时间戳（[＃95363](https://github.com/kubernetes/kubernetes/pull/95363)，[@ wojtek-t](https://github.com/wojtek-t)）[SIG网络和可伸缩性]
- 当节点在其[Pod](https://github.com/kubernetes/kubernetes/pull/95130)（[＃95130](https://github.com/kubernetes/kubernetes/pull/95130)，[@alculquicondor](https://github.com/alculquicondor)）之前被删除时，修复调度程序缓存快照[SIG调度]
- 修复静态PV的vsphere分离失败（[＃95447](https://github.com/kubernetes/kubernetes/pull/95447)，[@ gnufied](https://github.com/gnufied)）[SIG云提供程序和存储]
- 修复了一个错误，该错误阻止在存在经过验证的准入网络挂钩的情况下使用临时容器。（[＃94685](https://github.com/kubernetes/kubernetes/pull/94685)，[@verb](https://github.com/verb)）[SIG节点和测试]
- 当其父级比例集丢失（[＃95289](https://github.com/kubernetes/kubernetes/pull/95289)，[@bpineau](https://github.com/bpineau)）时，优雅地删除节点[SIG Cloud Provider]
- 在双堆栈群集中，kubelet现在将同时设置IPv4和IPv6 iptables规则，这可能会解决某些问题，例如HostPorts。（[＃94474](https://github.com/kubernetes/kubernetes/pull/94474)，[@danwinship](https://github.com/danwinship)）[SIG网络和节点]
- Kubeadm：对于Docker作为容器运行时，请在删除容器之前使“ kubeadm reset”命令停止容器（[＃94586](https://github.com/kubernetes/kubernetes/pull/94586)，[@BedivereZero](https://github.com/BedivereZero)）[SIG集群生命周期]
- Kubeadm：如果用户提供了所有证书，密钥和kubeconfig文件，则在“ kubeadm join --control-plane”期间警告但不要丢失根CA，前代理CA和etcd CA的“ ca.key”文件需要使用给定的CA密钥进行签名。（[＃94988](https://github.com/kubernetes/kubernetes/pull/94988)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]
- 端口映射允许将其映射`containerPort`为多个，`hostPort`而无需显式命名该映射。（[＃94494](https://github.com/kubernetes/kubernetes/pull/94494)，[@SergeyKanzhelev](https://github.com/SergeyKanzhelev)）[SIG网络和节点]
- 通过kubectl（[＃92492](https://github.com/kubernetes/kubernetes/pull/92492)，[@eddiezane](https://github.com/eddiezane)）使用自定义动词创建Roles和ClusterRoles时发出警告而不是失败[SIG CLI]

### 其他（清理或片状）

- 在舱内一致性测试中添加了细粒度的调试功能，以帮助轻松解决运行一致性测试或声波浮标测试时可能不健康的节点的网络问题。（[＃93837](https://github.com/kubernetes/kubernetes/pull/93837)，[@ jayunit100](https://github.com/jayunit100)）[SIG网络和测试]
- 现在，为创建命名空间API对象而发送的AdmissionReview对象`namespace`始终填充属性（以前`namespace`通过POST请求创建命名空间时该属性为空，而通过服务器端应用PATCH请求创建的命名空间中该属性为空）（[＃95012](https://github.com/kubernetes/kubernetes/pull/95012)，[@nodo](https://github.com/nodo)）[ SIG API机械和测试]
- 现在，Client-go标头日志记录（详细级别> = 9）掩盖了`Authorization`标头内容（[＃95316](https://github.com/kubernetes/kubernetes/pull/95316)，[@sfowl](https://github.com/sfowl)）[SIG API Machinery]
- 增强verifyRunAsNonRoot的日志信息，添加容器，容器信息（[＃94911](https://github.com/kubernetes/kubernetes/pull/94911)，[@ wawa0210](https://github.com/wawa0210)）[SIG节点]
- 来自staticcheck的错误：
  vendor / k8s.io / client-go / discovery / cached / memory / memcache_test.go：94：2：从未使用过此g值（SA4006）（[＃95098](https://github.com/kubernetes/kubernetes/pull/95098)，[@phunziker](https://github.com/phunziker)）[SIG API机械]
- Kubeadm：在Windows上将默认的暂停图像版本更新为1.4.0。通过此更新，该映像支持Windows版本1809（2019LTS），[1903、1909、2004](https://github.com/kubernetes/kubernetes/pull/95419)（[＃95419](https://github.com/kubernetes/kubernetes/pull/95419)，[@jsturtevant](https://github.com/jsturtevant)）[SIG群集生命周期和Windows]
- 当logLevel> = 4（[＃95245](https://github.com/kubernetes/kubernetes/pull/95245)，[@sfowl](https://github.com/sfowl)）[SIG存储]时，[掩盖ceph](https://github.com/sfowl) RBD admin在日志中[秘密](https://github.com/sfowl)
- 将快照控制器升级到3.0.0（[＃95412](https://github.com/kubernetes/kubernetes/pull/95412)，[@ saikat-royc](https://github.com/saikat-royc)）[SIG云提供程序]
- 从kubectl cluster-info命令（[＃95202](https://github.com/kubernetes/kubernetes/pull/95202)，[@rikatz](https://github.com/rikatz)）中删除令人反感的单词[SIG体系结构，CLI和测试]
- 可以使用以下新指标。
  - network_plugin_operations_total
  - network_plugin_operations_errors_total（[＃93066](https://github.com/kubernetes/kubernetes/pull/93066)，[@AnishShah](https://github.com/AnishShah)）[SIG仪器，网络和节点]
- vSphere：改善节点缓存刷新事件（[＃95236](https://github.com/kubernetes/kubernetes/pull/95236)，[@andrewsykim](https://github.com/andrewsykim)）上的日志记录消息[SIG Cloud Provider]
- `kubectl api-resources`现在可以打印API版本（作为“ API组/版本”，与的输出相同`kubectl api-versions`）。APIGROUP列现在为APIVERSION（[＃95253](https://github.com/kubernetes/kubernetes/pull/95253)，[@sallyom](https://github.com/sallyom)）[SIG CLI]

## 依存关系

### 添加

- github.com/jmespath/go-jmespath/internal/testify：[V1.5.1](https://github.com/jmespath/go-jmespath/internal/testify/tree/v1.5.1)

### 已变更

- github.com/aws/aws-sdk-go：[v1.28.2→v1.35.5](https://github.com/aws/aws-sdk-go/compare/v1.28.2...v1.35.5)
- github.com/jmespath/go-jmespath：[c2b33e8→V0.4.0](https://github.com/jmespath/go-jmespath/compare/c2b33e8...v0.4.0)
- k8s.io/kube-openapi：6aeccd4→8b50664
- sigs.k8s.io/apiserver-network-proxy/konnectivity-client：v0.0.9→v0.0.12
- sigs.k8s.io/structured-merge-diff/v4：v4.0.1→b3cf1e8

### 已移除

*什么也没有变。*

# v1.20.0-alpha.1

## v1.20.0-alpha.1的下载

### 源代码

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes.tar.gz) | e7daed6502ea07816274f2371f96fe1a446d0d7917df4454b722d9eb3b5ff6163bfbbd5b92dfe7a0c1d07328b8c09c4ae966e482310d6b36de8813aaf87380b5 |
| [kubernetes-src.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-src.tar.gz) | e91213a0919647a1215d4691a63b12d89a3e74055463a8ebd71dc1a4cabf4006b3660881067af0189960c8dab74f4a7faf86f594df69021901901eeee5b56550ea |

### 客户二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-client-darwin-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-darwin-amd64.tar.gz) | 1f3add5f826fa989820d715ca38e8864b66f30b59c1abeacbb4bfb96b4e9c694eac6b3f4c1c81e0ee3451082d44828cb7515315d91ad68116959a5efbdaef1e1 |
| [kubernetes-client-linux-386.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-linux-386.tar.gz) | c62acdc8993b0a950d4b0ce0b45473bf96373d501ce61c88adf4007afb15c1d53da8d53b778a7eccac6c1624f7fdda322be9f3a8bc2d80aaad7b4237c39f5eaf |
| [kubernetes-client-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-linux-amd64.tar.gz) | 1203ababfe00f9bc5be5c059324c17160a96530c1379a152db33564bbe644ccdb94b30eea15a0655bd652efb17895a46c31bbba19d4f5f473c2a0ff62f6e551f |
| [kubernetes-client-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-linux-arm.tar.gz) | 31860088596e12d739c7aed94556c2d1e217971699b950c8417a3cea1bed4e78c9ff1717b9f3943354b75b4641d4b906cd910890dbf4278287c0d224837d9a7d |
| [kubernetes-client-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-linux-arm64.tar.gz) | 8d469f37fe20d6e15b5debc13cce4c22e8b7a4f6a4ac787006b96507a85ce761f63b28140d692c54b5f7deb08697f8d5ddb9bbfa8f5ac0d9241fc7de3a3fe3cd |
| [kubernetes-client-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-linux-ppc64le.tar.gz) | 0d62ee1729cd5884946b6c73701ad3a570fa4d642190ca0fe5c1db0fb0cba9da3ac86a948788d915b9432d28ab8cc499e28aadc64530b7d549ee752a6ed93ec1 |
| [kubernetes-client-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-linux-s390x.tar.gz) | 0fc0420e134ec0b8e0ab2654e1e102cebec47b48179703f1e1b79d51ee0d6da55a4e7304d8773d3cf830341ac2fe3cede1e6b0460fd88f7595534e0730422d5a |
| [kubernetes-client-windows-386.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-windows-386.tar.gz) | 3fb53b5260f4888c77c0e4ff602bbcf6bf38c364d2769850afe2b8d8e8b95f7024807c15e2b0d5603e787c46af8ac53492be9e88c530f578b8a389e3bd50c099 |
| [kubernetes-client-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-client-windows-amd64.tar.gz) | 2f44c93463d6b5244ce0c82f147e7f32ec2233d0e29c64c3c5759e23533aebd12671bf63e986c0861e9736f9b5259bb8d138574a7c8c8efc822e35cd637416c0 |

### 服务器二进制文件

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-服务器-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-server-linux-amd64.tar.gz) | ae82d14b1214e4100f0cc2c988308b3e1edd040a65267d0eddb9082409f79644e55387889e3c0904a12c710f91206e9383edf510990bee8c9ea2e297b6472551 |
| [kubernetes-服务器-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-server-linux-arm.tar.gz) | 9a2a5828b7d1ddb16cc19d573e99a4af642f84129408e6203eeeb0558e7b8db77f3269593b5770b6a976fe9df4a64240ed27ad05a4bd43719e55fce1db0abf58 |
| [kubernetes-服务器-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-server-linux-arm64.tar.gz) | ed700dd226c999354ce05b73927388d36d08474c15333ae689427de15de27c84feb6b23c463afd9dd81993315f31eb8265938cfc7ecf6f750247aa42b9b33fa9 |
| [kubernetes-服务器-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-server-linux-ppc64le.tar.gz) | abb7a9d726538be3ccf5057a0c63ff9732b616e213c6ebb81363f0c49f1e168ce8068b870061ad7cba7ba1d49252f94cf00a5f68cec0f38dc8fce4e24edc5ca6 |
| [kubernetes-server-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-server-linux-s390x.tar.gz) | 3a51888af1bfdd2d5b0101d173ee589c1f39240e4428165f5f85c610344db219625faa42f00a49a83ce943fb079be873b1a114a62003fae2f328f9bf9d1227a4 |

### 节点二进制

| 文档名称                                                     | sha512哈希                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [kubernetes-node-linux-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-node-linux-amd64.tar.gz) | d0f28e3c38ca59a7ff1bfecb48a1ce97116520355d9286afdca1200d346c10018f5bbdf890f130a388654635a2e83e908b263ed45f8a88defca52a7c1d0a7984 |
| [kubernetes-node-linux-arm.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-node-linux-arm.tar.gz) | ed9d3f13028beb3be39bce980c966f82c4b39dc73beaae38cc075fea5be30b0309e555cb2af8196014f2cc9f0df823354213c314b4d6545ff6e30dd2d00ec90e |
| [kubernetes-node-linux-arm64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-node-linux-arm64.tar.gz) | ad5b3268db365dcdded9a9a4bffc90c7df0f844000349accdf2b8fb5f1081e553de9b9e9fb25d5e8a4ef7252d51fa94ef94d36d2ab31d157854e164136f662c2 |
| [kubernetes-node-linux-ppc64le.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-node-linux-ppc64le.tar.gz) | c4de2524e513996def5eeba7b83f7b406f17eaf89d4d557833a93bd035348c81fa9375dcd5c27cfcc55d73995449fc8ee504be1b3bd7b9f108b0b2f153cb05ae |
| [kubernetes-node-linux-s390x.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-node-linux-s390x.tar.gz) | 9157b44e3e7bd5478af9f72014e54d1afa5cd19b984b4cd8b348b312c385016bb77f29db47f44aea08b58abf47d8a396b92a2d0e03f2fe8acdd30f4f9466cbdb |
| [kubernetes-node-windows-amd64.tar.gz](https://dl.k8s.io/v1.20.0-alpha.1/kubernetes-node-windows-amd64.tar.gz) | 8b40a43c5e6447379ad2ee8aac06e8028555e1b370a995f6001018a62411abe5fbbca6060b3d1682c5cadc07a27d49edd3204e797af46368800d55f4ca8aa1de |

## 自v1.20.0-alpha.0起的变更日志

## 紧急升级说明

### （不，实际上，您必须在升级之前阅读此内容）

- 不建议使用Azure Blob磁盘功能（`kind`：`Shared`，`Dedicated`），应在存储类中使用`kind`：。（[＃](https://github.com/kubernetes/kubernetes/pull/92905)[92905](https://github.com/andyzhangx)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序和存储]`Managed``kubernetes.io/azure-disk`
- CVE-2020-8559（中）：从受感染节点到群集的特权升级。有关更多详细信息，请参见https://github.com/kubernetes/kubernetes/issues/92914。API服务器将不再代理非101响应的升级请求。这可能会破坏用非101响应代码响应升级请求的代理后端（例如扩展API服务器）。（[＃92941](https://github.com/kubernetes/kubernetes/pull/92941)，[@tallclair](https://github.com/tallclair)）[SIG API机械]

## 种类变化

### 弃用

- Kube-apiserver：不建议使用componentstatus API。该API提供了etcd，kube-scheduler和kube-controller-manager组件的状态，但是仅当这些组件在API服务器本地且kube-scheduler和kube-controller-manager暴露了不安全的运行状况端点时才起作用。代替此API，etcd健康包含在kube-apiserver健康检查中，并且可以直接针对那些组件的健康端点进行kube-scheduler / kube-controller-manager健康检查。（[＃93570](https://github.com/kubernetes/kubernetes/pull/93570)，[@liggitt](https://github.com/liggitt)）[SIG API机械，应用程序和集群生命周期]
- Kubeadm：弃用“ kubeadm alpha kubelet config enable-dynamic”命令。要继续使用该功能，请参考k8s.io上的“动态Kubelet配置”指南。（[＃92881](https://github.com/kubernetes/kubernetes/pull/92881)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]
- Kubeadm：删除不推荐使用的“ kubeadm alpha kubelet config enable-dynamic”命令。要继续使用该功能，请参考k8s.io上的“动态Kubelet配置”指南。此更改还删除了父命令“ kubeadm alpha kubelet”，因为暂时没有下面的子命令。（[＃94668](https://github.com/kubernetes/kubernetes/pull/94668)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]
- Kubeadm：删除命令“ kubeadm升级节点”（[＃94869](https://github.com/kubernetes/kubernetes/pull/94869)，[@ neolit123](https://github.com/neolit123)）弃用的--kubelet-config标志[SIG集群生命周期]
- Kubelet不推荐使用的端点`metrics/resource/v1alpha1`已被删除，请采用`metrics/resource`。（[＃](https://github.com/kubernetes/kubernetes/pull/94272)[94272](https://github.com/RainbowMango)，[@RainbowMango](https://github.com/RainbowMango)）[SIG仪器和节点]
- v1alpha1 PodPreset API和准入插件已被删除，没有内置替代。准入网络挂钩可用于在创建时修改pod。（[＃94090](https://github.com/kubernetes/kubernetes/pull/94090)，[@ deads2k](https://github.com/deads2k)）[SIG API机械，应用程序，CLI，云提供程序，可伸缩性和测试]

### API变更

- `nofuzz`现在，新的go build标签将禁用gofuzz支持。发布二进制文件可启用此功能。（[＃92491](https://github.com/kubernetes/kubernetes/pull/92491)，[@BenTheElder](https://github.com/BenTheElder)）[SIG API机械]
- `SupportsFsGroup`为CSIDrivers引入了一个新的alpha级别字段，以允许它们指定是否支持卷所有权和权限修改。该`CSIVolumeSupportFSGroup`功能门必须能够允许使用此字段。（[＃92001](https://github.com/kubernetes/kubernetes/pull/92001)，[@huffmanca](https://github.com/huffmanca)）[SIG API机械，CLI和存储]
- 为seccomp配置文件添加了pod版本倾斜策略，以将不赞成使用的注释与新的API服务器字段同步。请参阅[KEP中](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/20190717-seccomp-ga.md#version-skew-strategy)的相应部分[以](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/20190717-seccomp-ga.md#version-skew-strategy)获取更多详细说明。（[＃91408](https://github.com/kubernetes/kubernetes/pull/91408)，[@saschagrunert](https://github.com/saschagrunert)）[SIG应用，[身份](https://github.com/saschagrunert)验证，CLI和节点]
- 添加了禁用由Kubelet（[＃91930](https://github.com/kubernetes/kubernetes/pull/91930)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）[SIG节点]收集的加速器/ GPU指标的功能。
- 现在，新的EndpointSliceMirroring控制器将自定义端点镜像到EndpointSlices。（[＃91637](https://github.com/kubernetes/kubernetes/pull/91637)，[@robscott](https://github.com/robscott)）[SIG API机械，应用程序，[身份](https://github.com/robscott)验证，云提供程序，规范，网络和测试]
- 面向外部的API podresources现在可以在k8s.io/kubelet/pkg/apis/下获得（[＃92632](https://github.com/kubernetes/kubernetes/pull/92632)，[@RenaudWasTaken](https://github.com/RenaudWasTaken)）[SIG节点和测试]
- 修复自定义指标的转化。（[＃94481](https://github.com/kubernetes/kubernetes/pull/94481)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94481)[-t](https://github.com/wojtek-t)）[SIG API机械和仪器]
- 通用临时卷是`GenericEphemeralVolume`功能闸门下方的一个新的alpha功能，它提供了更灵活的`EmptyDir`卷替代方案：与一样`EmptyDir`，Kubernetes会为每个吊舱自动创建和删除卷。但是，由于使用了正常的供应过程（`PersistentVolumeClaim`），因此可以由第三方存储供应商提供存储，并且所有常规的卷功能都可以使用。卷不需要清空。例如，支持从快照还原。（[＃92784](https://github.com/kubernetes/kubernetes/pull/92784)，[@pohly](https://github.com/pohly)）[SIG API机械，应用程序，[身份](https://github.com/pohly)验证，CLI，规范，节点，计划，存储和测试]
- Kube-controller-manager：可以限制批量插件通过设置来联系本地和环回地址`--volume-host-allow-local-loopback=false`，或者通过设置来限制联系特定的CIDR范围`--volume-host-cidr-denylist`（例如，`--volume-host-cidr-denylist=127.0.0.1/28,feed::/16`）（[＃91785](https://github.com/kubernetes/kubernetes/pull/91785)，[@mattcary](https://github.com/mattcary)）[SIG API机械，应用程序，[身份](https://github.com/mattcary)验证，CLI ，网络，节点，存储和测试]
- Kubernetes现在使用golang 1.15.0-rc.1。构建。
  - 默认情况下，当不存在“使用者备用名称”时，将X.509服务证书上的CommonName字段视为主机名的不推荐使用的旧行为现在被禁用。可以通过将值x509ignoreCN = 0添加到GODEBUG环境变量来临时重新启用它。（[＃93264](https://github.com/kubernetes/kubernetes/pull/93264)，[@justaugustus](https://github.com/justaugustus)）[SIG API机制，Auth，CLI，云提供程序，群集生命周期，检测，网络，节点，版本，可伸缩性，存储和测试]
- 迁移调度程序，控制器-管理器和云控制器-管理器以使用LeaseLock（[＃94603](https://github.com/kubernetes/kubernetes/pull/94603)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94603)[-t](https://github.com/wojtek-t)）[SIG API机械，应用程序，云提供程序和调度]
- 修改DNS-1123错误消息以指示未完全遵循RFC 1123（[＃94182](https://github.com/kubernetes/kubernetes/pull/94182)，[@mattfenwick](https://github.com/mattfenwick)）[SIG API机械，应用程序，[身份](https://github.com/mattfenwick)验证，网络和节点]
- ServiceAccountIssuerDiscovery功能闸现在为Beta，默认情况下已启用。（[＃91921](https://github.com/kubernetes/kubernetes/pull/91921)，[@mtaufen](https://github.com/mtaufen)）[SIG[身份](https://github.com/mtaufen)验证]
- 现在，由kube-controller-manager管理的签名者可以具有不同的签名证书和密钥。请参阅有关的帮助`--cluster-signing-[signer-name]-{cert,key}-file`。 `--cluster-signing-{cert,key}-file`仍然是默认值。（[＃90822](https://github.com/kubernetes/kubernetes/pull/90822)，[@ deads2k](https://github.com/deads2k)）[SIG API机械，应用程序和[身份](https://github.com/deads2k)验证]
- 创建networking.k8s.io/v1 Ingress API对象时，`spec.tls[*].secretName`需要使用值来传递针对Secret API对象名称的验证规则。（[＃93929](https://github.com/kubernetes/kubernetes/pull/93929)，[@liggitt](https://github.com/liggitt)）[SIG网络]
- WinOverlay功能已升级到Beta版（[＃94807](https://github.com/kubernetes/kubernetes/pull/94807)，[@ksubrmnn](https://github.com/ksubrmnn)）[SIG Windows]

### 特征

- 需要采取的措施：在CoreDNS v1.7.0中，[指标名称已更改](https://github.com/coredns/coredns/blob/master/notes/coredns-1.7.0.md#metric-changes)，将与使用旧指标名称的现有报告公式向后不兼容。升级之前，将您的公式调整为新名称。

  Kubeadm现在包括CoreDNS版本1.7.0。一些主要更改包括：

  - 修复了可能导致CoreDNS停止更新服务记录的错误。
  - 修复了前向插件中的一个错误，该错误中无论设置了哪个策略，始终仅选择第一个上游服务器。
  - 删除已过时的选项`resyncperiod`，并`upstream`在Kubernetes插件。
  - 包括Prometheus度量标准名称更改（以使其与标准Prometheus度量标准命名约定保持一致）。它们将与使用旧指标名称的现有报告公式向后不兼容。
  - 联合插件（允许v1 Kubernetes联合）已被删除。更多细节，请https://coredns.io/2020/06/15/coredns-1.7.0-release/（[＃92651](https://github.com/kubernetes/kubernetes/pull/92651)，[@rajansandeep](https://github.com/rajansandeep)）[SIG API机械，CLI，云提供商，集群生命周期及仪表]

- 添加Azure服务操作（路由和负载平衡器）的指标。（[＃94124](https://github.com/kubernetes/kubernetes/pull/94124)，[@ nilo19](https://github.com/nilo19)）[SIG Cloud Provider and Instrumentation]

- 在Azure帐户创建中添加网络规则支持（[＃94239](https://github.com/kubernetes/kubernetes/pull/94239)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 添加对Azure文件驱动程序（[＃92825](https://github.com/kubernetes/kubernetes/pull/92825)，[@ZeroMagic](https://github.com/ZeroMagic)）的标签支持[SIG Cloud Provider and Storage]

- 添加了kube-apiserver指标：apiserver_current_inflight_request_measures，并且在启用“ API优先级和公平性”时，增加了windowed_request_stats。（[＃91177](https://github.com/kubernetes/kubernetes/pull/91177)，[@MikeSpreitzer](https://github.com/MikeSpreitzer)）[SIG API机械，仪器和测试]

- 现在，针对过时的API版本的API请求的审核事件包括`"k8s.io/deprecated": "true"`审核注释。如果标识了目标删除版本，则审核事件也将包括`"k8s.io/removal-release": "<majorVersion>.<minorVersion>"`审核注释。（[＃92842](https://github.com/kubernetes/kubernetes/pull/92842)，[@liggitt](https://github.com/liggitt)）[SIG API机械和仪器]

- 云节点控制器使用InstancesV2（[＃91319](https://github.com/kubernetes/kubernetes/pull/91319)，[@gongguan](https://github.com/gongguan)）[SIG应用，云提供商，可伸缩性和存储]

- Kubeadm：添加飞行前检查，以确保控制平面节点至少具有1700MB RAM（[＃93275](https://github.com/kubernetes/kubernetes/pull/93275)，[@ xlgao-zju](https://github.com/xlgao-zju)）[SIG集群生命周期]

- Kubeadm：将“ --cluster-name”标志添加到“ kubeadm alpha kubeconfig用户”，以允许在生成的kubeconfig文件中配置集群名称（[＃93992](https://github.com/kubernetes/kubernetes/pull/93992)，[@ prabhu43](https://github.com/prabhu43)）[SIG集群生命周期]

- Kubeadm：将“ --kubeconfig”标志添加到“ kubeadm init phase upload-certs”命令，以允许用户传递kubeconfig文件的自定义位置。（[＃94765](https://github.com/kubernetes/kubernetes/pull/94765)，[@ zhanw15](https://github.com/zhanw15)）[SIG集群生命周期]

- Kubeadm：弃用“ kubeadm init phase certs”子命令的“ --csr-only”和“ --csr-dir”标志。请改用“ kubeadm alpha certs generate-csr”。通过此新命令，您可以为所有控制平面组件生成新的私钥和证书签名请求，以便可以由外部CA签名证书。（[＃92183](https://github.com/kubernetes/kubernetes/pull/92183)，[@wallrj](https://github.com/wallrj)）[SIG群集生命周期]

- Kubeadm：默认情况下，使etcd pod请求100m CPU，100Mi内存和100Mi ephemeral_storage（[＃94479](https://github.com/kubernetes/kubernetes/pull/94479)，[@ knight42](https://github.com/knight42)）[SIG集群生命周期]

- Kubemark现在在单个群集中同时支持实节点和空心节点。（[＃93201](https://github.com/kubernetes/kubernetes/pull/93201)，[@ellistarn](https://github.com/ellistarn)）[SIG可伸缩性]

- Kubernetes现在使用go1.15.2构建

  - 版本：更新至k/repo-infra@v0.1.1（支持go1.15.2）

  - 构建：使用go-runner：buster-v2.0.1（使用go1.15.1构建）

  - bazel：用Starlark构建设置标志替换--features

  - hack / lib / util.sh：一些bash清理

    - 切换了一个位置以使用kube :: logging
    - make kube :: util :: find-binary在找不到任何内容时会返回错误，从而使hack脚本快速失败，而不是出现“二进制未找到”错误。
    - 这需要删除一些genfeddoc内容。自从我们删除了federation /之后，该二进制文件就不再存在于k / k存储库中，而且我也没有在[https://github.com/kubernetes-sigs/kubefed/中](https://github.com/kubernetes-sigs/kubefed/)看到它。我假设它已经一去不复返了。

  - bazel：直接从go_binary_conditional_pure输出go_binary规则

    来自：[@mikedanese](https://github.com/mikedanese)：而不是别名。别名以多种方式令人烦恼。现在，这特别困扰我，因为它们使操作图更难以以编程方式进行分析。通过在此处使用别名，我们将需要处理可能别名的go_binary目标并取消对有效目标的引用。

    该注释引用了一个问题，`pure = select(...)`考虑到现在的版本，该问题似乎已解决。

  - 使kube :: util :: find-binary不依赖于bazel-out /结构

    实现一个方面，输出用于go二进制文件的go_build_mode元数据，并在二进制选择期间使用它。（[＃94449](https://github.com/kubernetes/kubernetes/pull/94449)，[@justaugustus](https://github.com/justaugustus)）[SIG体系结构，CLI，群集生命周期，节点，发布和测试]

- 仅在附加/分离时更新Azure数据磁盘（[＃94265](https://github.com/kubernetes/kubernetes/pull/94265)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 向GA推广SupportNodePidsLimit，以提供节点到容器pid的隔离。向GA推广SupportPodPidsLimit，以提供限制每个容器的pid的能力（[＃94140](https://github.com/kubernetes/kubernetes/pull/94140)，[@ derekwaynecarr](https://github.com/derekwaynecarr)）[SIG节点和测试]

- 将pod_preemption_metrics重命名为preemption_metrics。（[＃93256](https://github.com/kubernetes/kubernetes/pull/93256)，[@ ahg-g](https://github.com/ahg-g)）[SIG检测和调度]

- 在从已应用的配置中删除字段的情况下，服务器端应用行为已得到规范。没有其他所有者的已删除字段将从活动对象中删除，如果有，则重置为其默认值。安全所有权转移，例如`replicas`从用户到HPA的字段转移而不重置为默认值，在[转移所有权](https://kubernetes.io/docs/reference/using-api/api-concepts/#transferring-ownership)（[＃92661](https://github.com/kubernetes/kubernetes/pull/92661)，[@jpbetz](https://github.com/jpbetz)）[SIG API机械，CLI，云提供程序，集群生命周期，工具和测试]

- 将CSIMigrationvSphere功能门设置为beta。用户应启用CSIMigration + CSIMigrationvSphere功能并安装vSphere CSI驱动程序（https://github.com/kubernetes-sigs/vsphere-csi-driver），以将工作负载从树内vSphere插件“ kubernetes.io/vsphere-volume”中移出。到vSphere CSI驱动程序。

  要求：vSphere vCenter / ESXi版本：7.0u1，硬件版本：VM版本15（[＃92816](https://github.com/kubernetes/kubernetes/pull/92816)，[@divyenpatel](https://github.com/divyenpatel)）[SIG云提供程序和存储]

- 支持[service.beta.kubernetes.io/azure-pip-ip-tags]批注，以允许客户指定ip标签以影响Azure中的公共IP创建[Tag1 = Value1，Tag2 = Value2等]（[＃94114](https://github.com/kubernetes/kubernetes/pull/94114)，[@MarcPow](https://github.com/MarcPow)）[SIG云提供商]

- 支持从客户端应用到服务器端应用的平滑升级而没有冲突，并支持相应的降级。（[＃90187](https://github.com/kubernetes/kubernetes/pull/90187)，[@julianvmodesto](https://github.com/julianvmodesto)）[SIG API机械和测试]

- apiserver日志中的跟踪输出更加有条理和全面。跟踪是嵌套的，对于所有非长时间运行的请求端点，将对整个过滤器链进行检测（例如，包括身份验证检查）。（[＃88936](https://github.com/kubernetes/kubernetes/pull/88936)，[@jpbetz](https://github.com/jpbetz)）[SIG API机械，CLI，云提供程序，集群生命周期，检测和调度]

- `kubectl alpha debug`现在，通过创建在节点的主机名称空间中运行的调试容器来支持调试节点。（[＃92310](https://github.com/kubernetes/kubernetes/pull/92310)，[@verb](https://github.com/verb)）[SIG CLI]

### 文献资料

- Kubelet：删除CNI标志的alpha警告。（[＃94508](https://github.com/kubernetes/kubernetes/pull/94508)，[@andrewsykim](https://github.com/andrewsykim)）[SIG网络和节点]

### 测试失败

- Kube-proxy iptables min-sync-period默认为1秒。以前是0。（[＃92836](https://github.com/kubernetes/kubernetes/pull/92836)，[@aojea](https://github.com/aojea)）[SIG网络]

### 错误或回归

- `informer-sync`现在，修复了由运行状况检查程序在apiserver中引起的紧急情况。（[＃93600](https://github.com/kubernetes/kubernetes/pull/93600)，[@ialidzhikov](https://github.com/ialidzhikov)）[SIG API机械]

- 添加kubectl wait --ignore-not-found标志（[＃90969](https://github.com/kubernetes/kubernetes/pull/90969)，[@ zhouya0](https://github.com/zhouya0)）[SIG CLI]

- 将修订添加到statefulset控制器以在创建pod之前等待pvc删除。（[＃93457](https://github.com/kubernetes/kubernetes/pull/93457)，[@ ymmt2005](https://github.com/ymmt2005)）[SIG应用]

- Azure ARM客户端：不要对空响应和http错误（[＃94078](https://github.com/kubernetes/kubernetes/pull/94078)，[@bpineau](https://github.com/bpineau)）进行[隔离](https://github.com/bpineau)（SIG Cloud Provider）

- Azure：修复了一个错误，如果配置了错误的Azure VMSS名称，kube-controller-manager将会恐慌（[＃94306](https://github.com/kubernetes/kubernetes/pull/94306)，[@ knight42](https://github.com/knight42)）[SIG云提供程序]

- Azure：每个VMSS VMSS VM进行缓存，以防止在具有许多附加VMSS（[＃93107](https://github.com/kubernetes/kubernetes/pull/93107)，[@bpineau](https://github.com/bpineau)）的群集上节流[SIG Cloud Provider]

- 审核事件的apiserver_request_duration_seconds指标和RequestReceivedTimestamp字段均考虑了请求在apiserver请求过滤器中花费的时间。（[＃94903](https://github.com/kubernetes/kubernetes/pull/94903)，[@tkashem](https://github.com/tkashem)）[SIG API机械，认证和检测]

- 构建/库/发行版：在构建服务器映像时明确使用“ --platform”

  当我们切换到go-runner来构建apiserver，controller-manager和Scheduler服务器组件时，我们不再在映像名称中引用各个体系结构，尤其是在服务器映像Dockerfile的'FROM'指令中。

  结果，非amd64映像的服务器映像将以go-runner amd64二进制文件而不是与该体系结构匹配的go-runner复制。

  该提交显式设置了“ --platform = linux / $ {arch}”，以确保我们从清单列表中提取正确的go-runner拱。

  之前： `FROM ${base_image}`

  之后： `FROM --platform=linux/${arch} ${base_image}`（[＃94552](https://github.com/kubernetes/kubernetes/pull/94552)，[@justaugustus](https://github.com/justaugustus)）[SIG发行]

- 可以在卷附件期间部署CSIDriver对象。（[＃93710](https://github.com/kubernetes/kubernetes/pull/93710)，[@ Jiawei0227](https://github.com/Jiawei0227)）[SIG应用，节点，存储和测试]

- CVE-2020-8557（中）：通过容器/ etc / hosts文件的节点本地拒绝服务。有关更多详细信息，请参见https://github.com/kubernetes/kubernetes/issues/93032。（[＃92916](https://github.com/kubernetes/kubernetes/pull/92916)，[@joelsmith](https://github.com/joelsmith)）[SIG节点]

- 不要将标记为kubernetes.azure.com/managed=false的节点添加到负载均衡器的后端池。（[＃93034](https://github.com/kubernetes/kubernetes/pull/93034)，[@ matthias50](https://github.com/matthias50)）[SIG云提供商]

- 不要对空元素进行排序。（[＃94666](https://github.com/kubernetes/kubernetes/pull/94666)，[@soltysh](https://github.com/soltysh)）[SIG CLI]

- 如果CSI驱动程序返回FailedPrecondition错误（[＃92986](https://github.com/kubernetes/kubernetes/pull/92986)，[@gnufied](https://github.com/gnufied)）[SIG节点和存储] ，[请](https://github.com/gnufied)不要重试卷扩展

- Dockershim安全：荚沙箱现在总是运行`no-new-privileges`和`runtime/default`的Seccomp轮廓dockershim的Seccomp：当设置为荚层自定义配置文件现在可以有小型材的Seccomp（[＃90948](https://github.com/kubernetes/kubernetes/pull/90948)，[@pjbgf](https://github.com/pjbgf)）[SIG节点]

- 双堆栈：默认情况下启用双堆栈功能门（[＃90439](https://github.com/kubernetes/kubernetes/pull/90439)，[@SataQiu](https://github.com/SataQiu)）时，使nodeipam与现有的单堆栈群集兼容[SIG API Machinery]

- 端点删除事件发生后，端点控制器重新排队服务，以确认不需要删除的端点，以减轻端点端点缓存不同步的影响。（[＃93030](https://github.com/kubernetes/kubernetes/pull/93030)，[@swetharepakula](https://github.com/swetharepakula)）[SIG应用和网络]

- 现在，如果遇到创建，更新或删除资源的错误，EndpointSlice控制器将立即返回。（[＃93908](https://github.com/kubernetes/kubernetes/pull/93908)，[@robscott](https://github.com/robscott)）[SIG应用和网络]

- EndpointSliceMirroring控制器现在将标签从端点复制到EndpointSlices。（[＃93442](https://github.com/kubernetes/kubernetes/pull/93442)，[@robscott](https://github.com/robscott)）[SIG应用和网络]

- EndpointSliceMirroring控制器现在可以镜像没有与其关联的服务的端点。（[＃94171](https://github.com/kubernetes/kubernetes/pull/94171)，[@robscott](https://github.com/robscott)）[SIG应用，网络和测试]

- 确保将Azure armclient的退避步骤设置为1。（[＃94180](https://github.com/kubernetes/kubernetes/pull/94180)，[@feiskyer](https://github.com/feiskyer)）[SIG云提供者]

- 确保当Azure VMSS的网络接口为null（[＃94355](https://github.com/kubernetes/kubernetes/pull/94355)，[@feiskyer](https://github.com/feiskyer)）[SIG云提供程序]时，getPrimaryInterfaceID不会发生混乱。

- 对具有非零DeletionTimestamp的Pod的驱逐请求将始终成功（[＃91342](https://github.com/kubernetes/kubernetes/pull/91342)，[@michaelgugino](https://github.com/michaelgugino)）[SIG Apps]

- 在Winkernel kube-proxy中扩展了DSR负载平衡器功能，使其达到HNS版本9.3-9.max，10.2 +（[＃93080](https://github.com/kubernetes/kubernetes/pull/93080)，[@ elweb9858](https://github.com/elweb9858)）[SIG网络]

- 修复HandleCrash顺序（[＃93108](https://github.com/kubernetes/kubernetes/pull/93108)，[@ lixiaobing1](https://github.com/lixiaobing1)）[SIG API机械]

- 修复kubelet中的并发映射写入错误（[＃93773](https://github.com/kubernetes/kubernetes/pull/93773)，[@ knight42](https://github.com/knight42)）[SIG节点]

- 修复了向“ kubeadm升级计划”命令（[＃94421](https://github.com/kubernetes/kubernetes/pull/94421)，[@rosti](https://github.com/rosti)）提供可选版本命令行参数时kubeadm因致命错误而失败的回归问题（SIG集群生命周期）

- 修复azure文件迁移恐慌（[＃94853](https://github.com/kubernetes/kubernetes/pull/94853)，[@andyzhangx](https://github.com/andyzhangx)）[SIG Cloud Provider]

- 修复由于缺少资源组＃75198（[＃93962](https://github.com/kubernetes/kubernetes/pull/93962)，[@ phiphi282](https://github.com/phiphi282)）而导致负载均衡器删除卡住的错误[SIG Cloud Provider]

- 修复在先前连接的EBS卷（[＃93567](https://github.com/kubernetes/kubernetes/pull/93567)，[@gnufied](https://github.com/gnufied)）上调用AttachDisk的问题[SIG云提供程序，存储和测试]

- 修复了映像文件系统的检测，devicemapper的磁盘指标，5.0 + linux内核上的OOM Kills的检测。（[＃92919](https://github.com/kubernetes/kubernetes/pull/92919)，[@dashpole](https://github.com/dashpole)）[SIG API机械，CLI，云提供程序，集群生命周期，检测和节点]

- 修复kube-apiserver（[＃94773](https://github.com/kubernetes/kubernetes/pull/94773)，[@tkashem](https://github.com/tkashem)）报告的etcd_object_counts指标[SIG API机械]

- 修复针对CRD对象的kube-apiserver指标错误报告的动词（[＃93523](https://github.com/kubernetes/kubernetes/pull/93523)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/93523)[-t](https://github.com/wojtek-t)）[SIG API机械和工具]

- 修复了在短时间内重新创建Azure节点（[＃93316](https://github.com/kubernetes/kubernetes/pull/93316)，[@feiskyer](https://github.com/feiskyer)）时找不到实例的问题[SIG云提供程序]

- 修复kube-apiserver / readyz包含“ informer-sync”检查，确保内部通知者已同步。（[＃93670](https://github.com/kubernetes/kubernetes/pull/93670)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/93670)[-t](https://github.com/wojtek-t)）[SIG API机械和测试]

- 在数组类型上使用x-kubernetes-preserve-unknown-fields修复具有模式的CRD上的kubectl SchemaError。（[＃94888](https://github.com/kubernetes/kubernetes/pull/94888)，[@sttts](https://github.com/sttts)）[SIG API机械]

- 修复EndpointSliceMirrorer for EndpointSliceMirroring控制器中的内存泄漏。（[＃93441](https://github.com/kubernetes/kubernetes/pull/93441)，[@robscott](https://github.com/robscott)）[SIG应用和网络]

- 修复并行csinode更新期间节点上缺少的csi注释。（[＃94389](https://github.com/kubernetes/kubernetes/pull/94389)，[@pacoxu](https://github.com/pacoxu)）[SIG存储]

- 修复`cloudprovider_azure_api_request_duration_seconds`指标存储桶以正确捕获延迟指标。以前，大多数调用将属于“ + Inf”存储桶。（[＃94873](https://github.com/kubernetes/kubernetes/pull/94873)，[@marwanad](https://github.com/marwanad)）[SIG云提供程序和工具]

- 修复：如果源不存在，请[执行“](https://github.com/andyzhangx)天蓝色磁盘调整大小”错误（[＃93011](https://github.com/kubernetes/kubernetes/pull/93011)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序]

- 修复：分离在Azure Stack（[＃94885](https://github.com/kubernetes/kubernetes/pull/94885)，[@andyzhangx](https://github.com/andyzhangx)）上损坏的azure磁盘[SIG Cloud Provider]

- 修复：根据IP系列（[＃93043](https://github.com/kubernetes/kubernetes/pull/93043)，[@aramase](https://github.com/aramase)）确定正确的IP配置[SIG云提供程序]

- 修复：安装天蓝色磁盘和文件（[＃93052](https://github.com/kubernetes/kubernetes/pull/93052)，[@andyzhangx](https://github.com/andyzhangx)）的初始延迟[SIG云提供程序和存储]

- 修复：在Windows挂载上使用sensitiveOptions（[＃94126](https://github.com/kubernetes/kubernetes/pull/94126)，[@andyzhangx](https://github.com/andyzhangx)）[SIG云提供程序和存储]

- 修复了不存在ceph.conf（[＃92027](https://github.com/kubernetes/kubernetes/pull/92027)，[@juliantaylor](https://github.com/juliantaylor)）时Ceph RBD卷扩展的问题[SIG存储]

- 修复了以下错误：端点的不正确存储和比较导致端点控制器（[＃94112](https://github.com/kubernetes/kubernetes/pull/94112)，[@damemi](https://github.com/damemi)）的API[流](https://github.com/kubernetes/kubernetes/pull/94112)[量过大](https://github.com/damemi)[SIG应用，网络和测试]

- 修复了一个错误，该错误导致在启用TopologyManager（[＃93189](https://github.com/kubernetes/kubernetes/pull/93189)，[@klueska](https://github.com/klueska)）时不[遵循](https://github.com/kubernetes/kubernetes/pull/93189)可重用CPU和设备的分配[SIG节点]

- 修复了当pod具有多个init容器或临时容器（[＃94580](https://github.com/kubernetes/kubernetes/pull/94580)，[@ kiyoshim55](https://github.com/kiyoshim55)）时，在kubectl调试中出现恐慌的问题[SIG CLI]

- 修复了`kubectl portforward`在同一端口（[＃94728](https://github.com/kubernetes/kubernetes/pull/94728)，[@amorenoz](https://github.com/amorenoz)）上配置TCP和UDP服务时有时无法正常运行的回归问题[SIG CLI]

- 修复了反射器中无法从API服务器1.17.0-1.18.5（[＃94316](https://github.com/kubernetes/kubernetes/pull/94316)，[@janeczku](https://github.com/janeczku)）的“资源太大版本”错误中恢复的错误[SIG API机械]

- 修复了当--sort-by和--containers标志一起使用时（[＃93692](https://github.com/kubernetes/kubernetes/pull/93692)，[@brianpursley](https://github.com/brianpursley)）不对kubectl顶部容器输出进行排序的错误（SIG CLI）

- 修复了kubelet在所有容器成功之后（[＃92614](https://github.com/kubernetes/kubernetes/pull/92614)，[@tnqn](https://github.com/tnqn)）为带有RestartPolicyOnFailure的pod创建额外的沙箱的问题[SIG节点和测试]

- 修复了[pointerSliceTracker](https://github.com/kubernetes/kubernetes/pull/92838)（[＃92838](https://github.com/kubernetes/kubernetes/pull/92838)，[@tnqn](https://github.com/tnqn)）中的内存泄漏[SIG Apps and Network]

- 对于跨区域的节点数不平衡的群集，在kube-scheduler中丢失了固定的节点数据（[＃93355](https://github.com/kubernetes/kubernetes/pull/93355)，[@maelk](https://github.com/maelk)）[SIG调度]

- 修复了EndpointSliceController可以为仅IPv6的Pod正确创建端点。

  修复了EndpointController，如果启用了IPv6DualStack功能门，则允许通过`ipFamily: IPv6`在服务上进行指定来允许IPv6无头服务。（这已经与EndpointSliceController一起使用。）（[＃91399](https://github.com/kubernetes/kubernetes/pull/91399)，[@danwinship](https://github.com/danwinship)）[SIG应用和网络]

- 修复了在容忍度有限的污点后驱逐Pod的错误从节点（[＃93722](https://github.com/kubernetes/kubernetes/pull/93722)，[@liggitt](https://github.com/liggitt)）删除了[第二个](https://github.com/kubernetes/kubernetes/pull/93722)[容忍度](https://github.com/liggitt)[SIG Apps and Node]

- 修复了快速重新创建服务后无法重新创建EndpointSlices的错误。（[＃94730](https://github.com/kubernetes/kubernetes/pull/94730)，[@robscott](https://github.com/robscott)）[SIG应用，网络和测试]

- 修复了kubelet pod处理中的竞争条件（[＃94751](https://github.com/kubernetes/kubernetes/pull/94751)，[@auxten](https://github.com/auxten)）[SIG节点]

- 解决了在不指定端口（[＃94834](https://github.com/kubernetes/kubernetes/pull/94834)，[@liggitt](https://github.com/liggitt)）的情况下代理ipv6 pod的问题[SIG API机械和网络]

- 修复了以下问题：如果删除定义了自定义资源的CRD并同时删除了名称空间，则删除命名空间的自定义资源可能导致孤立的命名空间自定义资源被隔离。（[＃93790](https://github.com/kubernetes/kubernetes/pull/93790)，[@liggitt](https://github.com/liggitt)）[SIG API机械和应用程序]

- Windows pod启动时忽略root用户检查（[＃92355](https://github.com/kubernetes/kubernetes/pull/92355)，[@ wawa0210](https://github.com/wawa0210)）[SIG节点和Windows]

- 将AWS EBS io1卷的最大IOPS增加到64,000（当前AWS最高）。（[＃](https://github.com/kubernetes/kubernetes/pull/90014)[90014](https://github.com/jacobmarble)，[@jacobmarble](https://github.com/jacobmarble)）[SIG云提供程序和存储]

- K8s.io/apimachinery：runtime.DefaultUnstructuredConverter.FromUnstructured现在可处理将整数字段转换为类型化的浮点值（[＃93250](https://github.com/kubernetes/kubernetes/pull/93250)，[@liggitt](https://github.com/liggitt)）[SIG API机械]

- Kube-aggregator证书在更改时从磁盘上动态加载（[＃92791](https://github.com/kubernetes/kubernetes/pull/92791)，[@ p0lyn0mial](https://github.com/p0lyn0mial)）[SIG API机械]

- Kube-apiserver：修复了从列表请求返回不一致结果的错误，该请求设置了字段或标签选择器并设置了分页限制（[＃94002](https://github.com/kubernetes/kubernetes/pull/94002)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94002)[-t](https://github.com/wojtek-t)）[SIG API机械]

- Kube-apiserver：不再对自定义资源打印机列（[＃93408](https://github.com/kubernetes/kubernetes/pull/93408)，[@joelsmith](https://github.com/joelsmith)）评估具有连续递归下降运算符的jsonpath表达式[SIG API Machinery]

- 现在，Kube-proxy会修剪在loadBalancerSourceRanges中找到的多余空间以匹配服务验证。（[＃94107](https://github.com/kubernetes/kubernetes/pull/94107)，[@robscott](https://github.com/robscott)）[SIG网络]

- 现在，Kube-up包括CoreDNS版本1.7.0。一些主要更改包括：

  - 修复了可能导致CoreDNS停止更新服务记录的错误。
  - 修复了前向插件中的一个错误，该错误中无论设置了哪个策略，始终仅选择第一个上游服务器。
  - 删除已过时的选项`resyncperiod`，并`upstream`在Kubernetes插件。
  - 包括Prometheus度量标准名称更改（以使其与标准Prometheus度量标准命名约定保持一致）。它们将与使用旧指标名称的现有报告公式向后不兼容。
  - 联合插件（允许v1 Kubernetes联合）已被删除。更多细节，请https://coredns.io/2020/06/15/coredns-1.7.0-release/（[＃92718](https://github.com/kubernetes/kubernetes/pull/92718)，[@rajansandeep](https://github.com/rajansandeep)）[SIG云供应商]

- Kubeadm现在确保即使没有更改etcd的版本，也可以在升级时重新生成etcd清单（[＃94395](https://github.com/kubernetes/kubernetes/pull/94395)，[@ rosti](https://github.com/rosti)）[SIG集群生命周期]

- Kubeadm：确定升级期间是否支持运行版本的CoreDNS时避免恐慌（[＃94299](https://github.com/kubernetes/kubernetes/pull/94299)，[@zouyee](https://github.com/zouyee)）[SIG集群生命周期]

- Kubeadm：如果用户安装了根目录“ / var / lib / kubelet”，则确保“ kubeadm reset”不会卸载根目录“ / var / lib / kubelet”（[＃93702](https://github.com/kubernetes/kubernetes/pull/93702)，[@thtanaka](https://github.com/thtanaka)）[SIG集群生命周期]

- Kubeadm：确保在控制平面初始化和加入过程中以0700权限创建etcd数据目录（[＃94102](https://github.com/kubernetes/kubernetes/pull/94102)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]

- Kubeadm：修复了即使CRI套接字用于另一个CR（[＃94555](https://github.com/kubernetes/kubernetes/pull/94555)，[@SataQiu](https://github.com/SataQiu)），kubeadm仍尝试调用“ docker info”的错误[SIG集群生命周期]

- Kubeadm：使kube-controller-manager和kube-scheduler的kubeconfig文件使用LocalAPIEndpoint而不是ControlPlaneEndpoint。这使kubeadm群集在不可变升级期间更能解决版本倾斜问题：[https](https://kubernetes.io/docs/setup/release/version-skew-policy/#kube-controller-manager-kube-scheduler-and-cloud-controller-manager) ://kubernetes.io/docs/setup/release/version-skew-policy/#kube-controller-manager-kube-scheduler-and-cloud-controller [-manager](https://kubernetes.io/docs/setup/release/version-skew-policy/#kube-controller-manager-kube-scheduler-and-cloud-controller-manager)（[＃94398](https://github.com/kubernetes/kubernetes/pull/94398)，[@ neolit123](https://github.com/neolit123)）[SIG群集生命周期]

- Kubeadm：放松对kubeconfig服务器URL的验证。允许用户定义自定义kubeconfig服务器URL，而无需在验证现有kubeconfig文件的过程中出错（例如，使用外部CA模式时）。（[＃94816](https://github.com/kubernetes/kubernetes/pull/94816)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]

- Kubeadm：从生成的证书中删除重复的DNS名称和IP地址（[＃92753](https://github.com/kubernetes/kubernetes/pull/92753)，[@QianChenglong](https://github.com/QianChenglong)）[SIG群集生命周期]

- Kubelet：假定`/proc/swaps`不存在时禁用交换功能（[＃93931](https://github.com/kubernetes/kubernetes/pull/93931)，[@SataQiu](https://github.com/SataQiu)）[SIG节点]

- Kubelet：修复pluginWatcher（[＃93622](https://github.com/kubernetes/kubernetes/pull/93622)，[@ knight42](https://github.com/knight42)）中的竞争条件[SIG节点]

- Kuberuntime安全性：pod沙箱现在始终与`runtime/default`seccomp配置文件一起运行kuberuntime seccomp：在pod级别（[＃90949](https://github.com/kubernetes/kubernetes/pull/90949)，[@pjbgf](https://github.com/pjbgf)）设置时，自定义配置文件现在可以具有较小的seccomp配置文件。[SIG节点]

- 无（[＃71269](https://github.com/kubernetes/kubernetes/pull/71269)，[@DeliangFan](https://github.com/DeliangFan)）[SIG节点]

- 现在，新的Azure实例类型确实具有正确的最大数据磁盘计数信息。（[＃94340](https://github.com/kubernetes/kubernetes/pull/94340)，[@ialidzhikov](https://github.com/ialidzhikov)）[SIG云提供程序和存储]

- 当启用了这些插件（[＃93660](https://github.com/kubernetes/kubernetes/pull/93660)，[@damemi](https://github.com/damemi)）时，具有无效的Affinity / AntiAffinity LabelSelector的Pod现在将无法调度（[＃93660](https://github.com/kubernetes/kubernetes/pull/93660)，[@ damemi](https://github.com/damemi)）[SIG调度]

- 如果在kubelet配置中设置了非默认的cpuCFSQuotaPeriod，则需要功能部件标志CustomCPUCFSQuotaPeriod。（[＃94687](https://github.com/kubernetes/kubernetes/pull/94687)，[@karan](https://github.com/karan)）[SIG节点]

- 在1.19rc1中添加了针对Windows节点的还原的devicemanager。（[＃93263](https://github.com/kubernetes/kubernetes/pull/93263)，[@liggitt](https://github.com/liggitt)）[SIG节点和Windows]

- Scheduler错误修正：快速重新创建节点时，Scheduler不会丢失pod信息。重新启动节点或重新使用节点名重新创建节点时，可能会发生这种情况。（[＃93938](https://github.com/kubernetes/kubernetes/pull/93938)，[@alculquicondor](https://github.com/alculquicondor)）[SIG可伸缩性，计划和测试]

- 现在，EndpointSlice控制器在开始之前等待EndpointSlice和Node缓存同步。（[＃94086](https://github.com/kubernetes/kubernetes/pull/94086)，[@robscott](https://github.com/robscott)）[SIG应用和网络]

- `/debug/api_priority_and_fairness/dump_requests`apiserver上的路径将不再为每个免税优先级级别返回幻像行。（[＃93406](https://github.com/kubernetes/kubernetes/pull/93406)，[@MikeSpreitzer](https://github.com/MikeSpreitzer)）[SIG API机械]

- kubelet识别--containerd-namespace标志以配置cadvisor使用的命名空间。（[＃87054](https://github.com/kubernetes/kubernetes/pull/87054)，[@changyaowei](https://github.com/changyaowei)）[SIG节点]

- 镜像容器应遵循容器规范中的终止GracePeriodSeconds。（[＃92442](https://github.com/kubernetes/kubernetes/pull/92442)，[@tedyu](https://github.com/tedyu)）[SIG节点和测试]

- 将Calico更新到v3.15.2（[＃94241](https://github.com/kubernetes/kubernetes/pull/94241)，[@lmm](https://github.com/lmm)）[SIG Cloud Provider]

- 将默认的etcd服务器版本更新为3.4.13（[＃94287](https://github.com/kubernetes/kubernetes/pull/94287)，[@jingyih](https://github.com/jingyih)）[SIG API机械，云提供程序，集群生命周期和测试]

- 将群集自动缩放器更新为1.19.0；（[＃93577](https://github.com/kubernetes/kubernetes/pull/93577)，[@vivekbagade](https://github.com/vivekbagade)）[SIG自动[缩放](https://github.com/vivekbagade)和云提供商]

- 在运行状况检查SG规则（[＃93515](https://github.com/kubernetes/kubernetes/pull/93515)，[@ t0rr3sp3dr0](https://github.com/t0rr3sp3dr0)）中使用NLB子网CIDR代替VPC CIDR [SIG云提供程序]

- 用户将看到删除Pod的时间增加，并保证从api服务器中删除Pod将意味着从容器运行时删除所有资源。（[＃92817](https://github.com/kubernetes/kubernetes/pull/92817)，[@kmala](https://github.com/kmala)）[SIG节点]

- 现在可以`kubectl patch`使用该`--patch-file`标志指定很大的补丁，而不是直接在命令行中包含它们。在`--patch`和`--patch-file`标志是互斥的。（[＃93548](https://github.com/kubernetes/kubernetes/pull/93548)，[@smarterclayton](https://github.com/smarterclayton)）[SIG CLI]

- 现在，在创建networking.k8s.io/v1 Ingress API对象时，`spec.rules[*].http`如果该`host`字段包含通配符，则将一致地验证值。（[＃93954](https://github.com/kubernetes/kubernetes/pull/93954)，[@Miciah](https://github.com/Miciah)）[SIG CLI，云提供程序，群集生命周期，工具，网络，存储和测试]

### 其他（清理或片状）

- --cache-dir设置http和发现的缓存目录，默认为$ HOME / .kube / cache（[＃92910](https://github.com/kubernetes/kubernetes/pull/92910)，[@soltysh](https://github.com/soltysh)）[SIG API机械和CLI]
- 为/ metrics，/ livez / *，/ readyz /*和/ healthz /-端点添加自举ClusterRole，ClusterRoleBinding和组。（[＃93311](https://github.com/kubernetes/kubernetes/pull/93311)，[@logicalhan](https://github.com/logicalhan)）[SIG API机械，[身份](https://github.com/logicalhan)验证，云提供程序和工具]
- 基本映像：更新为debian-iptables：buster-v1.3.0
  - 使用iptables 1.8.5
  - base-images：更新至debian-base：buster-v1.2.0
  - cluster / images / etcd：构建etcd：3.4.13-1映像
    - 使用debian-base：buster-v1.2.0（[＃94733](https://github.com/kubernetes/kubernetes/pull/94733)，[@justaugustus](https://github.com/justaugustus)）[SIG API机制，发布和测试]
- 构建：更新到debian-base@v2.1.2和debian-iptables@v12.1.1（[＃93667](https://github.com/kubernetes/kubernetes/pull/93667)，[@justaugustus](https://github.com/justaugustus)）[SIG API机制，发布和测试]
- 构建：更新到debian-base@v2.1.3和debian-iptables@v12.1.2（[＃93916](https://github.com/kubernetes/kubernetes/pull/93916)，[@justaugustus](https://github.com/justaugustus)）[SIG API机制，发布和测试]
- 建立：更新至go-runner：buster- [v2.0.0](https://github.com/kubernetes/kubernetes/pull/94167)（[＃94167](https://github.com/kubernetes/kubernetes/pull/94167)，[@justaugustus](https://github.com/justaugustus)）[SIG版本]
- 修复kubelet以在启动容器时正确记录日志。以前，有时日志会说一个容器已死，并且在第一次启动时已重新启动。仅当将Pod与initContainers和常规容器一起使用时，才会发生这种情况。（[＃91469](https://github.com/kubernetes/kubernetes/pull/91469)，[@rata](https://github.com/rata)）[SIG节点]
- 修复：Blob磁盘功能（[＃92824](https://github.com/kubernetes/kubernetes/pull/92824)，[@andyzhangx](https://github.com/andyzhangx)）中的许可证问题[SIG Cloud Provider]
- 修复了有关为configmap / secret卷设置卷所有权的泛滥警告消息（[＃92878](https://github.com/kubernetes/kubernetes/pull/92878)，[@jvanz](https://github.com/jvanz)）[SIG仪表，节点和存储]
- 修复了有关调度程序中的指标无身份验证的消息。（[＃94035](https://github.com/kubernetes/kubernetes/pull/94035)，[@ zhouya0](https://github.com/zhouya0)）[SIG调度]
- Kube-up：默认情况下，将关键Pod限制在kube-system命名空间中，以匹配1.17（[＃93121](https://github.com/kubernetes/kubernetes/pull/93121)，[@liggitt](https://github.com/liggitt)）之前的行为[SIG Cloud Provider and Scheduling]
- Kubeadm：日志消息中单独的参数键/值（[＃94016](https://github.com/kubernetes/kubernetes/pull/94016)，[@mrueg](https://github.com/mrueg)）[SIG集群生命周期]
- Kubeadm：删除对“ ci / k8s-master”版本标签的支持。该标签已在Kubernetes CI发布过程中删除，将不再在kubeadm中起作用。您可以改用“ ci / latest”版本标签。参见[kubernetes / test-infra＃18517](https://github.com/kubernetes/test-infra/pull/18517)。（[＃93626](https://github.com/kubernetes/kubernetes/pull/93626)，[@vikkyomkar](https://github.com/vikkyomkar)）[SIG集群生命周期]
- Kubeadm：应用插件时删除CoreDNS检查以获取已知图像摘要（[＃94506](https://github.com/kubernetes/kubernetes/pull/94506)，[@ neolit123](https://github.com/neolit123)）[SIG集群生命周期]
- Kubernetes现在使用go1.15.0（[＃93939](https://github.com/kubernetes/kubernetes/pull/93939)，[@justaugustus](https://github.com/justaugustus)）[构建](https://github.com/justaugustus)[SIG发布和测试]
- Kubernetes现在使用go1.15.0-rc.2（[＃93827](https://github.com/kubernetes/kubernetes/pull/93827)，[@justaugustus](https://github.com/justaugustus)）[构建](https://github.com/justaugustus)[SIG API机械，CLI，云提供程序，集群生命周期，工具，节点，发行和测试]
- 将ExternalPolicyForExternalIP锁定为默认值，此功能门将在1.22中删除。（[＃94581](https://github.com/kubernetes/kubernetes/pull/94581)，[@knabben](https://github.com/knabben)）[SIG网络]
- Service.beta.kubernetes.io/azure-load-balancer-disable-tcp-reset已删除。所有标准负载平衡器将始终启用tcp重置。（[＃94297](https://github.com/kubernetes/kubernetes/pull/94297)，[@MarcPow](https://github.com/MarcPow)）[SIG云提供商]
- 在kube-apiserver（[＃94397](https://github.com/kubernetes/kubernetes/pull/94397)，[@ ](https://github.com/wojtek-t)[wojtek ](https://github.com/kubernetes/kubernetes/pull/94397)[-t](https://github.com/wojtek-t)）中停止传播SelfLink（在1.16版中已弃用）[SIG API机械与测试]
- 在Windows上剥离不必要的安全上下文（[＃93475](https://github.com/kubernetes/kubernetes/pull/93475)，[@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)）[SIG节点，测试和Windows]
- 为了确保代码坚固，请为GetAddressAndDialer添加单元测试（[＃93180](https://github.com/kubernetes/kubernetes/pull/93180)，[@ FreeZhang61](https://github.com/FreeZhang61)）[SIG节点]
- 将CNI插件更新到v0.8.7（[＃94367](https://github.com/kubernetes/kubernetes/pull/94367)，[@justaugustus](https://github.com/justaugustus)）[SIG云提供程序，网络，节点，版本和测试]
- 将Golang更新到v1.14.5
  - 将repo-infra更新为0.0.7（以支持go1.14.5和go1.13.13）
    - 包括：
      - bazelbuild/bazel-toolchains@3.3.2
      - bazelbuild/rules_go@v0.22.7（[＃93088](https://github.com/kubernetes/kubernetes/pull/93088)，[@justaugustus](https://github.com/justaugustus)）[SIG发行和测试]
- 将Golang更新到v1.14.6
  - 将repo-infra更新为0.0.8（以支持go1.14.6和go1.13.14）
    - 包括：
      - bazelbuild/bazel-toolchains@3.4.0
      - bazelbuild/rules_go@v0.22.8（[＃93198](https://github.com/kubernetes/kubernetes/pull/93198)，[@justaugustus](https://github.com/justaugustus)）[SIG发行和测试]
- 将cri-tools更新到[v1.19.0](https://github.com/kubernetes-sigs/cri-tools/releases/tag/v1.19.0)（[＃94307](https://github.com/kubernetes/kubernetes/pull/94307)，[@xmudrii](https://github.com/xmudrii)）[SIG Cloud Provider]
- 将默认的etcd服务器版本更新为3.4.9（[＃92349](https://github.com/kubernetes/kubernetes/pull/92349)，[@jingyih](https://github.com/jingyih)）[SIG API机械，云提供程序，集群生命周期和测试]
- 将etcd客户端更新为v3.4.13（[＃94259](https://github.com/kubernetes/kubernetes/pull/94259)，[@jingyih](https://github.com/jingyih)）[SIG API机械和云提供商]
- `kubectl get ingress`现在更喜欢`networking.k8s.io/v1`过`extensions/v1beta1`（因为V1.14不建议使用）。要明确请求不推荐使用的版本，请使用`kubectl get ingress.v1beta1.extensions`。（[＃94309](https://github.com/kubernetes/kubernetes/pull/94309)，[@liggitt](https://github.com/liggitt)）[SIG API机械和CLI]

## 依存关系

### 添加

- github.com/Azure/go-autorest：[v14.2.0 +兼容](https://github.com/Azure/go-autorest/tree/v14.2.0)
- github.com/fvbommel/sortorder：[V1.0.1](https://github.com/fvbommel/sortorder/tree/v1.0.1)
- github.com/yuin/goldmark：[v1.1.27](https://github.com/yuin/goldmark/tree/v1.1.27)
- sigs.k8s.io/structured-merge-diff/v4：v4.0.1

### 已变更

- github.com/Azure/go-autorest/autorest/adal：[v0.8.2→v0.9.0](https://github.com/Azure/go-autorest/autorest/adal/compare/v0.8.2...v0.9.0)
- github.com/Azure/go-autorest/autorest/date：[v0.2.0→v0.3.0](https://github.com/Azure/go-autorest/autorest/date/compare/v0.2.0...v0.3.0)
- github.com/Azure/go-autorest/autorest/mocks：[v0.3.0→V0.4.0](https://github.com/Azure/go-autorest/autorest/mocks/compare/v0.3.0...v0.4.0)
- github.com/Azure/go-autorest/autorest：[v0.9.6→v0.11.1](https://github.com/Azure/go-autorest/autorest/compare/v0.9.6...v0.11.1)
- github.com/Azure/go-autorest/logger：[v0.1.0→v0.2.0](https://github.com/Azure/go-autorest/logger/compare/v0.1.0...v0.2.0)
- github.com/Azure/go-autorest/tracing：[v0.5.0→v0.6.0](https://github.com/Azure/go-autorest/tracing/compare/v0.5.0...v0.6.0)
- github.com/Microsoft/hcsshim：[v0.8.9→5eafd15](https://github.com/Microsoft/hcsshim/compare/v0.8.9...5eafd15)
- github.com/cilium/ebpf：[9f1617e→1c8d4c9](https://github.com/cilium/ebpf/compare/9f1617e...1c8d4c9)
- github.com/containerd/cgroups：[bf292b2→0dbf7f0](https://github.com/containerd/cgroups/compare/bf292b2...0dbf7f0)
- github.com/coredns/corefile-migration：[v1.0.8→v1.0.10](https://github.com/coredns/corefile-migration/compare/v1.0.8...v1.0.10)
- github.com/evanphx/json-patch：[e83c0a1→v4.9.0 +不兼容](https://github.com/evanphx/json-patch/compare/e83c0a1...v4.9.0)
- github.com/google/cadvisor：[8450c56→v0.37.0](https://github.com/google/cadvisor/compare/8450c56...v0.37.0)
- github.com/json-iterator/go：[V1.1.9→v1.1.10](https://github.com/json-iterator/go/compare/v1.1.9...v1.1.10)
- github.com/opencontainers/go-digest：[V1.0.0-RC1→V1.0.0](https://github.com/opencontainers/go-digest/compare/v1.0.0-rc1...v1.0.0)
- github.com/opencontainers/runc：[1b94395→819fcc6](https://github.com/opencontainers/runc/compare/1b94395...819fcc6)
- github.com/prometheus/client_golang：[V1.6.0→V1.7.1](https://github.com/prometheus/client_golang/compare/v1.6.0...v1.7.1)
- github.com/prometheus/common：[v0.9.1→v0.10.0](https://github.com/prometheus/common/compare/v0.9.1...v0.10.0)
- github.com/prometheus/procfs：[v0.0.11→v0.1.3](https://github.com/prometheus/procfs/compare/v0.0.11...v0.1.3)
- github.com/rubiojr/go-vhd：[0bfd3b3→02e2102](https://github.com/rubiojr/go-vhd/compare/0bfd3b3...02e2102)
- github.com/storageos/go-api：[343b3ef→V2.2.0 +不兼容](https://github.com/storageos/go-api/compare/343b3ef...v2.2.0)
- github.com/urfave/cli：[v1.22.1→v1.22.2](https://github.com/urfave/cli/compare/v1.22.1...v1.22.2)
- go.etcd.io/etcd：54ba958→dd1b699
- golang.org/x/crypto：bac4c82→75b2880
- golang.org/x/mod：v0.1.0→v0.3.0
- golang.org/x/net：d3edc99→ab34263
- golang.org/x/tools：c00d67e→c1934b7
- k8s.io/kube-openapi：656914f→6aeccd4
- k8s.io/system-validators：v1.1.2→v1.2.0
- k8s.io/utils：6e3d28b→d5654de

### 已移除

- github.com/godbus/dbus：[ade71ed](https://github.com/godbus/dbus/tree/ade71ed)
- github.com/xlab/handysort：[fb3537e](https://github.com/xlab/handysort/tree/fb3537e)
- sigs.k8s.io/structured-merge-diff/v3：v3.0.0
- vbom.ml/util：db5cfe1