# java

为每一个项目内嵌一个agent

```text
FROM apache/skywalking-base:8.3.0-es7 as skywalking
FROM ...
COPY --from=skywalking /skywalking/agent /agent
ENV SW_AGENT_NAMESPACE='tristan' SW_AGENT_NAME='$namespace-${service_name}' SW_AGENT_COLLECTOR_BACKEND_SERVICES='test.oap.skywalking.com:11800'
```

配置客户端采样数量顶点值: SW_AGENT_SAMPLE

配置服务端采样率: SW_TRACE_SAMPLE_RATE