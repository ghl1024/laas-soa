target_server_list = []
with open("target_server", encoding="utf-8")as f:
    file_lines = f.readlines()
    for file_line in file_lines:
        file_line = file_line.strip().replace("\n", "").replace("\t", "")
        if file_line == "":
            continue
        target_server_list.append(file_line)

result = ""
for item in target_server_list:
    index = item.index("|")
    host = item[:index].strip().replace("\n", "").replace("\t", "")
    name = item[index + 1:].replace("\n", "").replace("\t", "")
    host_suffix = host
    host_suffix = host_suffix[host_suffix.find(".") + 1:]
    host_suffix = host_suffix[host_suffix.find(".") + 1:]
    # print("host: %s \t name: %s" % (host, name))
    result += """
  - job_name: 'h_%s'
    static_configs:
      - targets: ['%s:9100']
        labels:
          nodename: '%s'""" % (host_suffix, host, name)

"""
        labels:
          hostname: '%s'
"""
with open('prometheus.yml', 'w', encoding="utf-8") as f:
    f.write(result.strip())
print(result)

if __name__ == '__main__':
    pass
