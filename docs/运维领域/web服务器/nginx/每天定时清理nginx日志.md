每天定时清理nginx运行日志

创建脚本文件

```
rm -rf /data/tristan/nginx_clean
mkdir -p /data/tristan/nginx_clean && chmod 777 /data/tristan/nginx_clean

sudo tee /data/tristan/nginx_clean/clean_log.sh <<-'EOF'
#!/bin/bash
rm -rf /usr/local/openresty/nginx/logs/*.log
rm -rf /usr/local/openresty/nginx/logs/*.json
/usr/local/openresty/nginx/sbin/nginx -s reopen
EOF

chmod +x /data/tristan/nginx_clean/clean_log.sh
```

添加计划任务

```
crontab -e

* 0 * * * /data/tristan/nginx_clean/clean_log.sh

/sbin/service crond restart
crontab -l
```





