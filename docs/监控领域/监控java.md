# 数据源

## springboot项目集成监控依赖(推荐使用)

### 调整项目依赖

如果有顶级父pom或者公共pom, 建议在上层pom中加上以下依赖

```
        <!-- java项目监控 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>io.micrometer</groupId>
            <artifactId>micrometer-registry-prometheus</artifactId>
        </dependency>
```

### 调整配置

```
management:
  endpoints:
    web:
      exposure:
        include: prometheus,info
  metrics:
    tags:
      application: ${spring.application.name}
```

# 数据抓取点

k8s中直接使用prometheus operator

为每一个服务添加ServiceMonitor

统一监控体系使用联邦机制同步K8S中的prometheus

假设svc的定义如下:

```
apiVersion: v1
kind: Service
metadata:
  annotations:
    traffic.sidecar.istio.io/excludeOutboundIPRanges: 0.0.0.0/0
  labels:
    app: <service_name>
  name: <service_name>
  namespace: <namespace_name>
spec:
  ports:
  - name: http
    port: 80
    targetPort: 80
  selector:
    app: <service_name>
```

那么:

```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: <service_name>
  name: app: <service_name>
  namespace: <namespace_name>
spec:
  endpoints:
  - interval: 15s
    port: 80
    path: "/prometheus"
  selector:
    matchLabels:
      app: <service_name>
```

# 展示效果

监控线程数量, 可用, 已用, 是否有阻塞, 等待队列大小, 忙碌线程情况

当有阻塞线程时进行报警

grafana id: 4701

效果如下

![image-20201210141343552](监控java.assets/image-20201210141343552.png)