计算公式

```
heap + noheap +  metaspace  + code cache  + compressed class space + 线程*Xss(XX:ThreadStackSize 默认1024kb)
	 + 垃圾收集程序的占用内存
	 + JIT优化程序的占用内存
	 + 堆外分配: 外部引用jar包的内存, --agent skywalking  jmx_exporter, 反射类
	 [+ JNI 调用]
```

观察jvm情况

拿值时需要向上取整

拿一个Heap max值, 假设为1024M

拿一个noheap值, 假设为300M

拿一个metaspace值, 假设为200M

拿一个code cache值, 假设为300M

拿一个compressed class space值, 假设为20M

拿一个线程数值, 假设为700*1024 = 700M

```
通过执行以下指令查看
java -XX:+PrintFlagsFinal -version |grep ThreadStackSize
```

1024*2 = 2048

(2048 + 300 + 200 + 300 + 20 + 700) / 0.7 = 5097



设置时需要向上取双数

设置最小堆内存为1024

设置最大堆内存为2048

设置容器最大内存为5098