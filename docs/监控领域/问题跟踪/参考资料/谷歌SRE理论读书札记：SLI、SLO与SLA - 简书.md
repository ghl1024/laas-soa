# 谷歌SRE理论读书札记：SLI、SLO与SLA

[![img](谷歌SRE理论读书札记：SLI、SLO与SLA - 简书.assets/2-9636b13945b9ccf345bc98d0d81074eb.jpg)](https://www.jianshu.com/u/a417f95b0f53)

[wangrui927](https://www.jianshu.com/u/a417f95b0f53)关注

2019.10.16 21:03:43字数 1,521阅读 1,755

趁着这被人扫地出门，无地可去的日子，多学习学习别人的理论知识。
书籍名 《Site Reliability Engineering》网络运维工程，编者Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy

## 第二部分 规则（Principles）

#### 第四章 Service Level Objects

如果你不知道哪些行为对服务有关键影响（无论积极还是消极），那么你就不可能正确地去管理好这个应用。那么为了衡量行为的程度，我们的服务需要一些指标，如果有人调用我们的服务，那他们也应该熟悉这些指标。
**这里我的理解是，比如别人调用我的接口去操作一台网络设备，执行了某个命令。这就是一个行为，但是我们对于这个行为，应该有一些具体的数字进行描述**

谷歌SRE在这里定义了三个名词，分别是：
SLIs、SLOs、SLAs，这里SL是 srvice level,服务级别，而I O A分别是 indicator、object与agreement
这些名词和指标建模、选择、分析息息相关。（这里的指标，就是metric，就是我们现在监控系统所采集的对象），SRE中有个原则是“简单”，所以在监控系统中选择要关注哪些指标是非常重要的，我们既需要这些指标能比较全面、客观地反馈服务的状况，又必须尽可能压缩监控指标的数目（特别接触了对几千台物理设备的监控系统后，我深有体会，每多一个指标，在生产环境是需要multiply几千的）
SLI就是服务状况体现最直观的数字，比如：
request latency 请求延迟（提一嘴，latency这个常见指标，很多时候是从服务端测获取到的，其实不见得能反应服务的真实延迟状况）
error rate 错误率（SRE说，别只统计成功的request数）
system throughput（这个有点意思，按照字面意思，是系统生产力。如果目前系统在服务1000个人，能说系统的生产力很高吗？或许但不一定，因为很可能虽然在服务1000个人，创建了2000个连接，但却没做什么事情。而如果从反馈数据的带宽，是否比前面的连接数更能说明系统的“生产力”呢？）
当然还有一种SLI对于SRE很重要，那就是 n个9 的服务可用性

SLO
SLO是一组值的范围，这个值就是由SLI定义的服务级别数值。自然的SLO定义就是，某SLI在正常情况下需要小于某值或者处于某个大小值之间。
选择一个合适的SLO并不是一件容易的事情，当然你并不需要一开始就设定好这个范围，比如说QPS，这个指标取决于你的用户，而你是无法预先做出判断的。（比如运维平台上线了某个服务，你可能预测这服务最后每天的使用量能达到100次，但实际并没人用，因为可能用户都不知道有这么一项功能）
确定一个SLO，和服务怎样运行也有关系（how service to perform）

SLA
服务级别的协议，可能是明确的协议，也可能是不明确的（implicit，比如约定俗成的、没有纸面协定）
这种协定可能是，如果服务失效、或者达不到预期的效果，该怎样做。一般是赔偿、退款，当然也有其他形式。一般来说，SRE是不参与SLA的制定，因为SLA更靠近商务层面或者产品设计层面。
比如谷歌搜素这项服务，并没有暴露给用户的SLI，但是却有和全世界都签订协议，也就是SLA。（你注册谷歌账号时，一大堆的文字）

# SLI实践

## 了解你的用户关心什么

你不需要把监控系统中每个metric都视为SLI，选择尽可能少的SLI，但这些SLI却能说明服务是否健康。这些SLI应该：
用户侧系统（user-facing serving systems）：可用性（a）延迟（latency）服务生产力（throughput）。换句话说：服务能响应用户的请求吗？响应要耗时多久？我们能处理多少请求？（个人心得：很多时候，我们喜欢在监控系统的dashboard上把agent获取到的数据全都摆上去，看起来很高大上，但却连服务“能”处理多少请求都无法了解，这里能处理多少请求从另外一个角度讲就是服务的饱和度）
存储系统（storage systems）：延迟，可用性和持久性。换句话说：成功写数据需要多久？是否能正确获取到想要的数据？当我们需要这个数据时它是否还在那儿（这应该指的是缓存）
大数据系统（big data systems）：对于数据处理管道（data processing pipeline），就需要去关注生产力与端对端的延迟（end-to-end latency）换句话说：有多少数据被处理？从获取数据到处理完成耗时多少？
对于所有系统，还需要关注正确度（correctness）：服务返回的是否是正确的数据？正确度是关注服务健康的重要的SLI

## 收集indicators

我们绝大多数情况都是从服务侧收集的，比如使用borgmon或prometheus，但是我们也应该关注用户侧的指标收集。

## 聚合