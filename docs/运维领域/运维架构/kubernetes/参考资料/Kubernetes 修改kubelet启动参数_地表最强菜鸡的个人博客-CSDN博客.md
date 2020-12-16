# Kubernetes 修改kubelet启动参数

![img](Kubernetes 修改kubelet启动参数_地表最强菜鸡的个人博客-CSDN博客.assets/reprint.png)

[张志翔](https://vegetable-chicken.blog.csdn.net/) 2019-07-17 12:53:26 ![img](Kubernetes 修改kubelet启动参数_地表最强菜鸡的个人博客-CSDN博客.assets/articleReadEyes.png) 1905 ![img](Kubernetes 修改kubelet启动参数_地表最强菜鸡的个人博客-CSDN博客.assets/tobarCollect.png) 收藏

分类专栏： [Kubernetes](https://blog.csdn.net/qq_19734597/category_9094708.html) 文章标签： [修改 K8s kubelet启动参数](https://so.csdn.net/so/search/s.do?q=修改 K8s kubelet启动参数&t=blog&o=vip&s=&l=&f=&viparticle=)

版权

## 背景

最近，我在虚拟机上通过rpm包安装了k8s集群。我想创建静态Pod，那么就需要更改kubelet的启动参数。相关环境信息如下：

| role   | OS        | IP         | module                                                |
| :----- | :-------- | :--------- | :---------------------------------------------------- |
| Master | Centos7.2 | 10.1.2.182 | kube-apiserver kube-controller-manager kube-scheduler |
| Node1  | Centos7.2 | 10.1.2.183 | kubelet kube-proxy                                    |
| Node2  | Centos7.2 | 10.1.2.184 | kubelet kube-proxy                                    |

### 一、查看kubelet启动参数

k8s组件是通过systemctl来管理的，因此可以在 /etc/systemd/system 或 /usr/lib/systemd/system下查找相关配置文件

```bash
找到kubelet对应服务的配置文件目录
# cd /etc/systemd/system/kubelet.service.d/   
查看原文件内容
# cat 10-kubeadm.conf
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--kubeconfig=/etc/kubernetes/kubelet.conf --require-kubeconfig=true"
Environment="KUBELET_SYSTEM_PODS_ARGS=--pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true"
Environment="KUBELET_NETWORK_ARGS=--network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin"
Environment="KUBELET_DNS_ARGS=--cluster-dns=10.12.0.10 --cluster-domain=cluster.local"
Environment="KUBELET_EXTRA_ARGS=--v=4"
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_SYSTEM_PODS_ARGS $KUBELET_NETWORK_ARGS $KUBELET_DNS_ARGS $KUBELET_EXTR
A_ARGS
查看kubelet的相关启动参数
# ps -ef | grep kubelet
/usr/bin/kubelet --require-kubeconfig=true --pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true --network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin --cluster-dns=10.12.0.10 --cluster-domain=cluster.local --v=4
```

### 二、修改kubelet启动参数

添加一个新的参数 –config

```
# vim 10-kubeadm.conf
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--config=/etc/kubelet.d/ --kubeconfig=/etc/kubernetes/kubelet.conf --require-kubeconfig=true"
Environment="KUBELET_SYSTEM_PODS_ARGS=--pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true"
Environment="KUBELET_NETWORK_ARGS=--network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin"
Environment="KUBELET_DNS_ARGS=--cluster-dns=10.12.0.10 --cluster-domain=cluster.local"
Environment="KUBELET_EXTRA_ARGS=--v=4"
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_SYSTEM_PODS_ARGS $KUBELET_NETWORK_ARGS $KUBELET_DNS_ARGS $KUBELET_EXTR
A_ARGS
执行如下命令使新增参数生效
# systemctl stop kubelet
# systemctl daemon-reload
# systemctl start kubelet
systemctl status kubelet
检查新增参数是否已经生效
# ps -ef | grep kubelet
/usr/bin/kubelet --config=/etc/kubelet.d/ --kubeconfig=/etc/kubernetes/kubelet.conf --require-kubeconfig=true --pod-manifest-path=/etc/kubernetes/manifests --allow-privileged=true --network-plugin=cni --cni-conf-dir=/etc/cni/net.d --cni-bin-dir=/opt/cni/bin --cluster-dns=10.12.0.10 --cluster-domain=cluster.local --v=4
```

同理，此方法也可添加kubelet其他启动参数。