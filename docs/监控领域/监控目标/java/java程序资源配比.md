计算公式

```
heap + noheap

heap   = eden space + survivor space + old gen   
noheap = metaspace + code cache  + compressed class space + 线程*Xss(XX:ThreadStackSize 默认1024kb)
```

观察jvm情况

拿值时需要向上取整: 取1024 或者 取双

--- heap

max(eden space) = 600

max(survivor space) = 62

max(old gen) = 970

--- non heap

max(code cache) = 130

max(meta space) = 200



max(jvm stack) = 681+215 = 896



600 + 62 + 970 = 1632

1632/0.5 = 3264

(130 + 200 + 896)/0.7 = 1752

3264 + 1752= 5016



设置最小堆内存为1632

设置最大堆内存为3264

设置容器最大内存为5016