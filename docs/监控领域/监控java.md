集成springboot监控依赖

如果有顶级父pom或者公共pom, 建议在上层pom中加上以下依赖

```
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <!-- Micrometer Prometheus registry  -->
        <dependency>
            <groupId>io.micrometer</groupId>
            <artifactId>micrometer-registry-prometheus</artifactId>
        </dependency>
```

调整配置

```
management:
  endpoints:
    web:
      exposure:
        include: prometheus,info
```

手动配置服务svc到prometheus scrape抓取点

undertow线程数量, 可用, 已用, 是否有阻塞, 等待队列大小, 忙碌线程情况