target_server_list = []
with open('target_server') as f:
    original_target_server_list = f.readlines()
    for item in original_target_server_list:
        if not item or "" == item:
            continue
        item = item.strip().replace("\n", "").replace("\t", "")
        target_server_list.append(item)

result = ""
for item in target_server_list:
    result += """  - job_name: 'node_exporter_%s'
    metrics_path: '/metrics'
    static_configs:
    - targets: ['%s:9100']\n""" % (item, item)
with open('prometheus.yml', 'w') as f:
    f.write(result)
print(result)
