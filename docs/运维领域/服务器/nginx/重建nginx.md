

```
重建nginx
killall nginx
# yum install -y psmisc

ps aux|grep nginx

/usr/local/openresty/nginx/sbin/nginx -c /usr/local/openresty/nginx/conf/nginx.conf

/usr/local/openresty/nginx/sbin/nginx -s reload


systemctl stop nginx
systemctl start   nginx
systemctl restart nginx
systemctl status nginx
```

