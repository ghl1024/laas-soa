因为历史遗留问题, 客户端配置不能动, 需要改动服务端

当然也可以修改客户端配置, 重新构建客户端



192.168.2.20

搭建

```
rm -rf /data/tristan/nginx
mkdir -p /data/tristan/nginx && chmod 777 /data/tristan/nginx
sudo tee /data/tristan/nginx/default.conf <<-'EOF'

EOF




docker stop mynginx
docker rm   mynginx

docker run -d --restart=always --name mynginx -p 11801:11801 -v /data/tristan/laashub/nginx/default.conf:/etc/nginx/conf.d/default.conf -v /data/tristan/laashub/nginx/ca:/etc/nginx/ca nginx

docker logs -f --tail 100 mynginx
```

