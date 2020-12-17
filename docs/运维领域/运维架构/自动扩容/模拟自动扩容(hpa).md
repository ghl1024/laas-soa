index.php

```
<?php
  $x = 0.0001;
  for ($i = 0; $i <= 1000000; $i++) {
    $x += sqrt($x);
  }
  echo "OK!";
?>
```

Dockerfile

```
FROM php:5-apache
ADD index.php /var/www/html/index.php
RUN chmod a+rx index.php
```

准备镜像

```
registry.cn-shenzhen.aliyuncs.com/google_containers_hw/hpa-example
```

创建并运行应用

application/php-apache.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-apache
spec:
  selector:
    matchLabels:
      run: php-apache
  replicas: 1
  template:
    metadata:
      labels:
        run: php-apache
    spec:
      containers:
      - name: php-apache
        image: k8s.gcr.io/hpa-example
        ports:
        - containerPort: 80
        resources:
          limits:
            cpu: 500m
          requests:
            cpu: 200m

---

apiVersion: v1
kind: Service
metadata:
  name: php-apache
  labels:
    run: php-apache
spec:
  ports:
  - port: 80
  selector:
    run: php-apache


```

```shell
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml
```



```
kubectl delete deployment php-apache
kubectl run php-apache --image=registry.cn-shenzhen.aliyuncs.com/google_containers_hw/hpa-example --requests=cpu=200m --expose --port=80 --replicas=3
kubectl get deployment|grep php-apache
kubectl describe deployment/php-apache

kubectl get pod |grep php-apache
```

设置HPA

```
kubectl delete hpa php-apache
kubectl get hpa
kubectl autoscale deployment php-apache --cpu-percent=50 --min=2 --max=10
```

一方面查看hpa情况

```
sudo cat >> test_hpa_tracing.sh<<EOF
while : ;do
reset
kubectl get hpa
sleep 2
done
EOF

chmod +x test_hpa_tracing.sh && ./test_hpa_tracing.sh
```

一方面模拟高并发请求

```
kubectl delete deployments/load-generator
kubectl run -i --tty load-generator --image=busybox /bin/sh

Hit enter for command prompt

while true; do wget -q -O- http://php-apache.default.svc.cluster.local; done
```

确实看到效果, 当高并发时造成资源剧增时会自动的增加副本数量

当资源降低之后 副本数量也会自动降低下来