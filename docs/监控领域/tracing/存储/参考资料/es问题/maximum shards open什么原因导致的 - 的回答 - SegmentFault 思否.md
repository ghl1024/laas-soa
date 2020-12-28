# [maximum shards open什么原因导致的](https://segmentfault.com/q/1010000019243427)

[elasticsearch](https://segmentfault.com/t/elasticsearch)

elk每天一个index 今天kibana刷不出东西看logstash报错内容是：`Validation Failed: 1: this action would add [2] total shards, but this cluster currently has [1001]/[1000] maximum shards open`

可能是什么原因导致的？

阅读 5.6k

 赞踩

 收藏关注 4

[评论](javascript:;) 发布于 2019-05-21



3 个回答

[得票](https://segmentfault.com/q/1010000019243427#comment-area)[时间](https://segmentfault.com/q/1010000019243427/a-1020000019677191?sort=created#comment-area)

[![avatar](maximum shards open什么原因导致的 - 的回答 - SegmentFault 思否.assets/user-64.png)**showsean**](https://segmentfault.com/u/showsean)

-  **16**
- 

你用的7版本以上的elasticsearch吧，默认只允许1000个分片，问题是因为集群分片数不足引起的。
现在在elasticsearch.yml中定义

```
> cluster.max_shards_per_node: 10000
```

貌似也不生效，默认就允许创建1000个分片，我是在kibana的tools中改变临时设置

```
PUT /_cluster/settings
{
  "transient": {
    "cluster": {
      "max_shards_per_node":10000
    }
  }
}
```

这样就生效了