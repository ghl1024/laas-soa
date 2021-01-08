# Loki日志系统详解4——语法

![img](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[linkt1234](https://blog.csdn.net/Linkthaha) 2019-09-06 16:48:22 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes.png) 5910 ![img](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect.png) 收藏 7

分类专栏： [loki](https://blog.csdn.net/linkthaha/category_9331298.html) [容器云](https://blog.csdn.net/linkthaha/category_9331124.html) 文章标签： [k8s](https://so.csdn.net/so/search/s.do?q=k8s&t=blog&o=vip&s=&l=&f=&viparticle=) [grafana](https://www.csdn.net/tags/MtTaEg0sMzE3ODYtYmxvZwO0O0OO0O0O.html) [loki](https://www.csdn.net/tags/MtzaMg0sODczMzYtYmxvZwO0O0OO0O0O.html)

版权

# Loki日志系统详解3——部署

Loki提供了HTTP接口，我们这里就不详解了，大家可以看：

https://github.com/grafana/loki/blob/master/docs/api.md

我们这里说下查询的接口如何使用：

第一步，获取当前Loki的元数据类型：

```
curl http://192.168.25.30:30972/api/prom/label
{
	"values": ["alertmanager", "app", "component", "container_name", "controller_revision_hash", "deployment", "deploymentconfig", "docker_registry", "draft", "filename", "instance", "job", "logging_infra", "metrics_infra", "name", "namespace", "openshift_io_component", "pod_template_generation", "pod_template_hash", "project", "projectname", "prometheus", "provider", "release", "router", "servicename", "statefulset_kubernetes_io_pod_name", "stream", "tekton_dev_pipeline", "tekton_dev_pipelineRun", "tekton_dev_pipelineTask", "tekton_dev_task", "tekton_dev_taskRun", "type", "webconsole"]
}
1234
```

第二步，获取某个元数据类型的值：

```
curl http://192.168.25.30:30972/api/prom/label/namespace/values
{"values":["cicd","default","gitlab","grafanaserver","jenkins","jx-staging","kube-system","loki","mysql-exporter","new2","openshift-console","openshift-infra","openshift-logging","openshift-monitoring","openshift-node","openshift-sdn","openshift-web-console","tekton-pipelines","test111"]}
12
```

第三步，根据label进行查询，例如：

```
http://192.168.25.30:30972/api/prom/query?direction=BACKWARD&limit=1000&regexp=&query={namespace="cicd"}&start=1567644457221000000&end=1567730857221000000&refId=A
1
```

参数解析：

- query: 一种查询语法详细见下面章节，{name=~“mysql.+”} or {namespace=“cicd”} |= "error"表示查询，namespace为cicd的日志中，有error字样的信息。
- limit: 返回日志的数量
- `start：开始时间，Unix时间表示方法 默认为，一小时前时间
- end: 结束时间，默认为当前时间
- direction: forward 或者 backward, .指定limit时候有用，默认为 backward.
- regexp:对结果进行regex过滤

## logQL语法

### 选择器

对于查询表达式的标签部分，将放在{}中，多个标签表达式用逗号分隔：

```
{app="mysql",name="mysql-backup"}
1
```

支持的符号有：

- = 完全相同。
- != 不平等。
- =~ 正则表达式匹配。
- !~ 不要正则表达式匹配。

### 过滤表达式

编写日志流选择器后，您可以通过编写搜索表达式进一步过滤结果。搜索表达式可以文本或正则表达式。

如：

- {job=“mysql”} |= “error”
- {name=“kafka”} |~ “tsdb-ops.*io:2003”
- {instance=~“kafka-[23]”,name=“kafka”} != kafka.server:type=ReplicaManager

支持多个过滤

- {job=“mysql”} |= “error” != “timeout”

目前支持的操作符：

- |= line包含字符串。
- != line不包含字符串。
- |~ line匹配正则表达式。
- !~ line与正则表达式不匹配。

表达式遵循https://github.com/google/re2/wiki/Syntax语法