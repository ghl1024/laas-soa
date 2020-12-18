仍然是kubelet不可用



```
查看docker和kubelet的实时运行日志
journalctl -xefu docker
journalctl -xefu kubelet

发现kubelet连接不上docker
发现docker大量出现文件写不可用, 导致docker异常
停止容器、删除容器
docker stop $(docker ps -qa)
docker rm   $(docker ps -qa)
重启docker
systemctl restart docker
重启kubelet
systemctl restart kubelet

继续查看实时运行日志
发现kubelet的cgroup driver直接跟docker的不一样了
修改kubelet的cgroup driver
重启kubelet

问题解决

```



总结:

docker中的文件千万不要轻易删除

如果需要释放文件需要通过docker stop <容器名> && docker rm <容器名>