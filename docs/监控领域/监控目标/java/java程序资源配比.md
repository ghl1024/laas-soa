计算公式

```
heap + noheap

heap      = eden space + survivor space + old gen   
noheap    = metaspace + code cache  + compressed class space
jvm stack = 线程数*Xss(XX:ThreadStackSize 默认1024kb)
gc本身     = 400m
```

只要gc情况正常, 内存是不会溢出的

观察gc time情况, 是否一直处于长时间gc, 是否有下降趋势







观察jvm情况



--- heap

max(eden space) = 966

max(survivor space) = 100

max(old gen) = 970

--- non heap

max(code cache) = 130

max(meta space) = 200

max(compressed class space) = 20

--- jvm stack

max(jvm stack) = 681+215 = 896



600 + 62 + 970 = 1632

1632/0.5 = 3264

(130 + 200 + 896)/0.7 = 1752

3264 + 1752= 5016



设置最小堆内存为1632

设置最大堆内存为3264

设置容器最大内存为5016