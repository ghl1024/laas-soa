influxdb一般情况下比较稳定，但是随着数据量越来越大，也会出现一些性能问题，需要进行一些调优。我目前遇到的关于influxdb的性能问题大体上可以分为两类

1. CPU持续居高不下
2. 内存持续居高不下，并伴随着较高的iowait

下面分别来讨论我当时的处理方法。

# CPU持续居高不下

当时遇到的现象是，influxdb进程的CPU利用率持续居高不下，查询数据的速度很慢。经过分析，最终定位到influxdb.conf配置文件中的一个参数

```
  # The maximum time a query will is allowed to execute before being killed by the system.  This limit
  # can help prevent run away queries.  Setting the value to 0 disables the limit.
  # query-timeout = "0"
123
```

我认为这简直是influxdb的一个bug，默认情况下查询数据居然没有超时时间。一般情况下大家都是在grafana上展示influxdb的数据，如果一次查询了非常多的数据，那么这个查询就会执行很长时间，如果这种大的查询比较多的话，influxdb就会耗费几乎所有的CPU来做这些数据查询，并且其它小的查询也会受到影响。

我的做法是设置了一个60秒的超时时间

```
query-timeout = "60s"
1
```

这样的话，大查询如果60秒内结束不了，会超时并结束，不影响后续的查询。

# 内存持续居高不下，并伴随着较高的iowait

针对这种情况，我认为比较常见的原因是series过多。

关于series，influxdb官网的解释是

> InfluxDB, a series is a collection of points that share a measurement, tag set, and field key.

简单来讲，series就是一个监控对象的一组相同的tag，它决定了被监控对象的粒度。

我的理解是，series是influxdb的索引，会被存储在内存里，series过多的话，就会导致内存持续居高不下。

对于这种问题，首先需要识别出哪各数据库的series比较多，然后再降低series的数量。

### 发现哪个数据库的series过多

influxdb本身提供了一些针对调试的支持，通过下面的接口返回的数据，可以分析出所有数据库的series数量

http://localhost:8086/debug/vars

在返回的数据中，每个数据库都会出现下面的数据，`numSeries`就是series的数量

```
"database:_internal": {
    "name": "database",
    "tags": {
        "database": "_internal"
    },
    "values": {
        "numMeasurements": 12,
        "numSeries": 2050
    }
}
12345678910
```

上面的数据显示的是`_internal`数据库的数据。

一般情况下，如果series的数量在10万以内，对性能不会造成太大影响。

### 如何发现哪个measurement的series过多

当发现某个数据库的series数量很多，并不一定能够直接识别出问题，还需要进一步分析是哪个measurement的series数量比较大。查看一个measurement的series的个数比较简单，运行下面的命令

```
show series from measurements
1
```

然后数一下有多少行就行了。但是，这个过程比较耗时，尤其是当一个数据库的measurement的数量比较多的时候。可以使用下面的脚本，来批量地计算每个measurement的series个数

```
#!/bin/bash
INFLUX_HOST=$1
DATABASE=$2
influx -host "$INFLUX_HOST" -execute 'show measurements' -database "$DATABASE" > /tmp/measurements.txt
tail -n +4 /tmp/measurements.txt | while read line
do
    echo "series count of measurements $line is "
    influx -host "$INFLUX_HOST" -execute "show series from \"$line\" " -database "$DATABASE" | wc -l
done
123456789
```

运行脚本的时候需要指定influxdb的host和数据库名称，例如：

```
influxdb-series-inspect.sh 192.268.1.2 mydb
1
```

### 如何降低series的数量

series的多少，主要是由tag的个数和tag的值决定的，所以如果要降低series的数量，可以从两个方面来考虑。

第一，通过合理地规划，来减少不必要的tag。如果某个tag的值分布非常的多，可以考虑下它是否有必要作为tag，是不是作为field更合适。

第二，通过设置保留策略，保留更少的数据。influxdb是时序数据库，主要被用来存储监控数据，可以根据具体场景来保留更短的数据，这样的话会有一些旧数据由于过期而被清理掉，从而减少series的数量。

关于如何设置series的保留策略，可以参考

[influxdb的retention policy](https://blog.csdn.net/daguanjia11/article/details/90666888)

# 磁盘占用过多

这个问题一般比较好理解，有些数据库可能会保存大量数据，从而占用过多的磁盘空间，进而对服务器造成一定的影响。

**一个influxdb数据库的数据量大小和series的数量没有什么绝对的关系。**

识别这个问题也比较简单，influxdb的数据默认存储在 /var/lib/influxdb/data 目录下，只要 cd 到这个目录下，然后通过 du 来查下哪个目录最大即可。

```
# cd /var/lib/influxdb/data
# du -d 1 -h .
12
```

找出比较大的数据库，然后再想办法减少数据量。