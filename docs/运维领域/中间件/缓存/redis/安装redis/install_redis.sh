echo "拉取redis镜像"
docker pull redis

echo "运行测试redis"
docker run --name myredis -p 6379:6379 -d redis

echo "查看日志"
docker logs -f 100 myredis