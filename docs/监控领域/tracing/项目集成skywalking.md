# java

为每一个项目内嵌一个agent

```text
FROM apache/skywalking-base:8.3.0-es7 as skywalking
FROM ...
COPY --from=skywalking /skywalking/agent /agent
ENV SW_AGENT_NAMESPACE='tristan' SW_AGENT_NAME='$namespace-${service_name}' SW_AGENT_COLLECTOR_BACKEND_SERVICES='test.oap.skywalking.com:11800'
```

