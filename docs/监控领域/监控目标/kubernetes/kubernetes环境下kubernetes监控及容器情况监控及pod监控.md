# 思路

重建prometheus operator: 删除原来的 prometheus operator(可省略), 创建新的prometheus operator, 创建维护专用ingress

外部访问prometheus

在统一的prometheus中配置一个子联邦prometheus同步端点

创建dashboard

# 添加联邦prometheus节点

```
scrape_configs:
  - job_name: 'federate'
    scrape_interval: 15s
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]':
        - '{job="prometheus"}'
        - '{job="nginx-upstreams"}'
        - '{job="kubernetes-services"}'
        - '{job="kubernetes-service-endpoints"}'
        - '{job="kubernetes-pods"}'
        - '{job="kubernetes-nodes-kubelet"}'
        - '{job="kubernetes-nodes-cadvisor"}'
        - '{job="kubernetes-apiservers"}'
    static_configs:
      - targets:
        - '192.168.2.20:32396'
```



