## 一个800万的教训：运维怎样避免面向监狱编程？

dbaplus社群 2020-04-21 10:06:58

本文内容由dbaplus社群发起，参与专家有：京东数科数据库团队负责人-高新刚、交通行业运维经理-Jan、广州维他奶技术总监-叶熙昌、安徽天元技术总监-徐传贵、DBA-秦世黎、DBA-蔡鹏。

 

这两天，“郑大一附院系统瘫痪2小时，违规操作的运维被判5年半”的事件刷了屏。据目前公开资料显示，北京中科某某科技有限公司的夏某某在未经授权或许可的情况下，私自编写了“数据库性能观测程序”和锁表语句，并利用私自记录的账号密码将该程序私自连接郑大一附院“HIS数据库”，导致该锁表语句在“HIS数据库”运行并锁定，造成郑大一附院三个院区所有门诊、临床计算机业务受恶意语句攻击，多个门诊业务系统无法正常操作，所有门诊相关业务停滞近2个小时，严重影响医院的正常医疗工作。（详情可见：[一个违规操作、损失800万、被判五年半：运维夏某某致「郑大一附院」智慧医院系统瘫痪2个小时，判破坏计算机信息系统罪](http://mp.weixin.qq.com/s?__biz=MzI4OTc4MzI5OA==&mid=2247521985&idx=1&sn=2720283074d8ecd92028225245e3b270&chksm=ec2b3dacdb5cb4ba0a8ebc52733038eb215232175106fd8adb1f93895ec76b92ec61da432bd8&scene=21#wechat_redirect)）

 

![img](一个800万的教训：运维怎样避免面向监狱编程？ - 运维 - dbaplus社群.assets/20200421100816411.png)

 

事件引发了持续的热议，其中也不乏争议，针对关注度较高的问题，包括防止运维人员的骚操作、如何兼顾运维效率与安全、事件中的甲乙两方存有哪些不足、企业等保工作如何开展和有效落地等，dbaplus社群整理并归总观点如下，希望能给大家今后相关工作的展开和处理提供参考：

 

**1、如何防止运维人员在生产环境搞测试、自己编写程序连生产库等骚操作？**

 

- 权限控制+日常审计。对核心生产环境进行白名单机制，明确每一个终端每一个账号的连接以及进程，对异常情况进行阻断或监控。

   

- 除了grant权限以外，给予开发运维人员slave或dev环境。

 

- 通过运维系统和堡垒机隔离运维人员和服务器。程序要纳入代码管控，严禁文件上传下载。

 

**2、运维人员应不应该为了工作之便在客户系统上使用自己编写的工具？**

 

- 要有授权，要经过测试，要经过许可。据我了解电力行业的一些规范，要推行软件、工具，甚至要去电科院进行测试，获得证书才可部署试行。所以如果甲方要求不太严格，可以把自己的工具拿出来一起评审，没问题的话搞就行，切忌私自运行。

   

- 运维人员不应该有权限在客户的系统上运行自己编写的程序，所有程序必须是公对公的行为。包括各种脚本，都是需要进行代码review的，实验过没问题才可以上。

 

**3、流程一旦复杂，势必会影响运维的效率，应该怎么设置运维人员的工作流程、权限划分才能兼顾到效率与安全？**

 

- 甲方自身没有对系统的管控能力，还应用于核心系统，等于把命脉交在别人手里。所以甲方应该把日常工作流程化，有明确的操作流程，并对乙方的权限划分遵循最小化赋权，最好由堡垒机录屏，定期审计外包操作内容。

 

- 这个还是得看业务的重要性和核心生产环境的操作，一定要有确认、复审的流程，然后才能执行，这一块一定要严格。实际上有些方法是可以在技术方面杜绝一些高危操作的，比如细化权限分配和明示高危操作，不同的账号做不同的事情，精细化分工；阻断drop，rm-rf等高危操作。在核心问题方面，质量可以大于效率。

   

- 关于流程跟标注化或者规范化的实施及操作，长期以来我只奉行一个观点：凡是不能通过代码来表达的流程、规范/标准化都是在扯淡。公司项目多了，人也多了之后不可能每一个人都会严格遵循流程来的，一旦有一个人失误就会造成事故，因此现在很多公司都在推行DevOps不是没有道理的。

   

- 流程复杂尽量使用脚本操作，或者类似Python Ansible的工作。

 

**4、事件中可以看出乙方存有哪些不足？**

 

- 其实这个事故本来可以快速定位并解决的，结果耗时这么久！从解决该问题的运维人员的操作复盘来看，第一时间居然是通过plsql看问题，这显然是存在问题的。我想象的处理场景应该是外包公司有一套可靠的监控系统（通过员工复盘过程可以看出监控系统应该还是有的，但为何监控没有第一时间预警，这里也存在问题），当发现异常后运维/DBA应该能通过平台去定位问题甚至解决问题，显然该乙方在平台化方面做的有所欠缺。

 

**5、甲方对外包人员应该做到怎样的权限管理？**

 

- 一是区分外包人员管理范围，明确外包人员工作职责；二是甲方应该管理核心权限。对外包人员要有适度权限管控；三是用系统或者运维平台替代外包人员手动操作。减少人、机直接接触。四是根据等保要求定期进行安全巡检和变更密码；五是对外包人员进行能力考核，防止能力不过硬的运维人员接触核心系统。

 

- 主要从三方面来考虑和管控，一是要明确规章制度和管理规范，明确外包人员的职责范围；二是在技术方面要做好隔离，杜绝某一项目的外包人员拥有其他项目的权限，这一块主要是从技术上实现；三是做好审计，定时审计和控制。

 

- 我们这边的做法是，供应商不准有VPN，所有操作必须通过堡垒机，后台录像。然后后面有一套安全的大数据平台，会分析他们的行为，如果有不正常的话，直接报警。

   

- 一是不要给外包root administator之类过高的权限；二是尽量不要给外包人员登录生产环境；三是给予slave和测试环境给开发人员使用。

   

- 核心功能权限不可以给外包人员，得做好分权分域，并做好安全培训，签订安全协议。

 

**6、甲方自身应该做好怎样的应急预案？**

 

- 一是加强系统化建设，通过运维管控系统实现自动化管理；二是加强制度管理，提高运维人员安全意识和操作规范度；三是成立技术评委会，对产品、性能和安全进行定期评估。制定应急方案。

 

- 从这个事件上来讲，其实技术性不是很强，系统卡顿，数据库排查，查到锁表，监控到锁表的账户和语句，进行kill，应该快速恢复。如果要就该事件讨论应急预案的话，建议以时间调查和溯源为切入点，即出现可以操作到时系统中断，应该从网络、硬件、存储、客户端、数据库、应用等方面进行排查，从问题的排查方法策略、日志、操作审计溯源等方面，进行应急预案，同时强化备份以及备份验证的频次。实际上结合我的经验，数据库有哪些账号，那些客户端在链接应该有台账并建立白名单信息的。

   

- 安全架构落实到位，堡垒机、监控、代码审计、账号权限、密码修改策略等等；服务器方面HA的方案很多很多。白天可以做限制锁表等危险性操作，写好监控程序比如触发器，禁止该系列危险操作并发出警告，除非收到最高权限授权。

   

- 备份和高可用方案要做好。

 

**7、企业的等保工作如何开展并落实到位？**

 

- 从某种程度上来讲，等保工作其实是表面大于实际效果，这也是由于企业甲方不够重视引起的。做等保不难，难的是根据等保的要求和规范来开展和执行安全工作。等保的测评机构领企业进安全的门，给指导规范和标准，剩下大部分的时间都应该是企业自己进行消化、吸收开展和执行。实际上等保2.0非常具有现实指导意义，很值得企业结合自身情况进行研究。

 

- 一是从规范管理、到标准化，再到流程管理、事件管理、故障复盘、iso20000认证考核；二是定期请相关专业审计机构进行风险评估，查漏补缺。

 

- 企业等保要求一定的密码字符复杂度和定期进行密码修改，以及SSL链接加密。

 

 

**8、运维人员应该严守哪些工作准则、具备哪些安全意识？**

 

- 作为运维人员一定要小心谨慎，每个命令发下去前一定要想好可能带来的后果，不做没有把握的事情。每次代码更新一定要经过严格的测试CodeReview（尤其是大批量操作时哪怕是只执行一个select也要反复确认）。操作前最好有人跟你double check，要学会通过流程办事，这是对自己的保护，切不可迷之自信！

   

- 运维人员做任何变更之前都要想好rollback方案，以及回滚时间，而且必须事先和用户说清楚。

 

**9、运维真如多数人吐槽的那样，是份“高危”职业吗？这个职业的上岗标准和保障条例是否应该进一步优化？**

 

- 规范操作，规范流程制度，增加审核审计，加强应急演练。之后运维就是安全的。

 

- 实际上没那么夸张，每个职业，只要超越了法律底线，都是高危。

   

- 以后就没有运维，做SRE就可以了，做什么运维？以后新世界就不需要传统运维了。

   

- 我个人其实很同情这位运维人员，确实很可惜，处罚也过重了（想想携程事件吧）。建议有一定能力的技术人员尽量到互联网公司，不管从个人技术成长还是未来发展空间都要靠谱一些。

   

- 运维确实是高危行业，经常晚上干活，俗话说赚的卖白菜的钱，担着卖白粉的风险。

 

 

引用大多数网友总结的一句话作为结尾——不该看的不看，不该记的不记，不该说的不说。至于由以上观点延伸出的更多具体的问题，欢迎大家在评论区或投稿给我们继续探讨：

 

1. 如何制定生产运行管理规范，明确权责，提高生产环境安全、责任意识？
2. 生产操作怎么做到有授权、有记录、有跟踪、有监控？
3. 未经充分测试的程序、未经充分确认的操作命令、未经充分讨论确认的方案，如何严格规定不得在生产执行？
4. 账号权限如何管理？
5. 工作职责如何管理？