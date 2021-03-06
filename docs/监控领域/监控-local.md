基于主机: 172.30.1.153

# alertmanager

## 安装dingding webhook

```
rm -rf /data/tristan/prometheus_webhook_dingtalk
mkdir -p /data/tristan/prometheus_webhook_dingtalk/template && chmod 777 /data/tristan/prometheus_webhook_dingtalk/template

sudo tee /data/tristan/prometheus_webhook_dingtalk/template/alert.tmpl <<-'EOF'
{{ define "__subject" }}[{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}] {{ .GroupLabels.SortedPairs.Values | join " " }} {{ if gt (len .CommonLabels) (len .GroupLabels) }}({{ with .CommonLabels.Remove .GroupLabels.Names }}{{ .Values | join " " }}{{ end }}){{ end }}{{ end }}
{{ define "__alertmanagerURL" }}{{ .ExternalURL }}/#/alerts?receiver={{ .Receiver }}{{ end }}
{{ define "__text_alert_list" }}{{ range . }}
**报警详情**
{{ range .Annotations.SortedPairs }}> - {{ .Name }}: {{ .Value | markdown | html }}
{{ end }}

{{ end }}{{ end }}

{{ define "ding.link.title" }}{{ template "__subject" . }}{{ end }}
{{ define "ding.link.content" }}#### \[{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}\] **[{{ index .GroupLabels "alertname" }}]({{ template "__alertmanagerURL" . }})**
{{ template "__text_alert_list" .Alerts.Firing }}
{{ end }}
EOF

docker stop prometheus_webhook_dingtalk && docker rm prometheus_webhook_dingtalk
docker run -d \
  --name=prometheus_webhook_dingtalk \
  -p 8060:8060 --restart always \
  -v /data/tristan/prometheus_webhook_dingtalk/template:/opt/dingding_api/ \
  timonwong/prometheus-webhook-dingtalk:v1.4.0 --ding.profile="webhook1=https://oapi.dingtalk.com/robot/send?access_token=<access_token>" --template.file="/opt/dingding_api/alert.tmpl"

docker logs -f --tail 100 prometheus_webhook_dingtalk
docker restart prometheus_webhook_dingtalk
```

## 安装alertmanager

```
rm -rf /data/tristan/alertmanager
mkdir -p /data/tristan/alertmanager/configs && chmod 777 /data/tristan/alertmanager/configs
mkdir -p /data/tristan/alertmanager/template && chmod 777 /data/tristan/alertmanager/template

sudo tee /data/tristan/alertmanager/template/wechat.tmpl <<-'EOF'
{{ define "wechat.html" }}
{{ range .Alerts }}
======== 阿里云报警 ==========
***请注意告警状态: {{   .Status }}
告警级别: {{ .Labels.severity }}
告警类型: {{ .Labels.alertname }}
故障主机: {{ .Labels.instance }}
告警主题: {{ .Annotations.summary }}
告警详情: {{ .Annotations.description }}
触发时间: {{ .StartsAt.Format "2006-01-02 15:04:05" }}
========end==========
{{ end }}
{{ end }}
EOF

sudo tee /data/tristan/alertmanager/configs/config.yml <<-'EOF'
global:
  resolve_timeout: 5m
templates:
  - "/etc/alertmanager/template/wechat.tmpl"
route:
  receiver: webhook
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 5m
  group_by: [alertname]
  routes:
  - receiver: webhook
    group_wait: 10s
receivers:
- name: webhook
  webhook_configs:
  - url: http://192.168.2.21:8060/dingtalk/webhook1/send  
    send_resolved: true
EOF

docker stop alertmanager && docker rm alertmanager
docker run -d \
  --name=alertmanager \
  --restart=always \
  -p 9093:9093 \
  -v /data/tristan/alertmanager/configs/config.yml:/etc/alertmanager/config.yml \
  -v /data/tristan/alertmanager/template:/etc/alertmanager/template \
  prom/alertmanager:v0.14.0

docker logs -f --tail 100 alertmanager
```



# prometheus

安装

```
rm -rf /home/data/tristan/prometheus
mkdir -p  /home/data/tristan/prometheus && chmod 777 /home/data/tristan/prometheus
mkdir -p  /home/data/tristan/prometheus/data && chmod 777 /home/data/tristan/prometheus/data
mkdir -p  /home/data/tristan/prometheus/rules && chmod 777 /home/data/tristan/prometheus/rules
sudo tee /home/data/tristan/prometheus/prometheus.yml <<-'EOF'
global:
  scrape_interval:     15s
  evaluation_interval: 15s
alerting:
  alertmanagers:
  - static_configs:
    - targets: ["172.30.1.153:9093"]
rule_files:
  - "/usr/local/prometheus/rules/*.rules"
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
    - targets: ['localhost:9090']
EOF

docker stop prometheus && docker rm prometheus
docker run -d \
  --name=prometheus \
  --restart=always \
  -p 9090:9090 \
  -v /home/data/tristan/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  -v /home/data/tristan/prometheus/data:/prometheus \
  -v /home/data/tristan/prometheus/rules:/usr/local/prometheus/rules \
  prom/prometheus:v2.23.0
  
docker logs -f --tail=100 prometheus
```

当需要加载配置文件时访问: curl -X POST http://192.168.2.21:9090/-/reload

# grafana

安装

```
rm -rf /home/data/tristan/grafana
mkdir -p /home/data/tristan/grafana/configs /home/data/tristan/grafana/data
chmod 777 /home/data/tristan/grafana/configs /home/data/tristan/grafana/data

docker stop grafana && docker rm grafana
docker run -d \
  --name=grafana \
  --restart=always \
  -p 80:3000 \
  -v /home/data/tristan/grafana/data:/var/lib/grafana \
  grafana/grafana:7.3.4

docker logs -f --tail=100 grafana
```

添加数据源



# exporter

node_exporter

redis

zookeeper

