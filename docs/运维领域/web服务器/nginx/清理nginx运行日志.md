

```
nginx专用服务器文件爆满, 那么肯定就是nginx 产生的日志过多导致的
清理nginx日志
cd /usr/local/openresty/nginx/logs
ll -h
rm -rf `ls |grep -v nginx.pid`

重新生成日志文件
/usr/local/openresty/nginx/sbin/nginx -s reopen
systemctl status nginx
```



