## 不基于备份和表，生产系统数据误删就能完全恢复？！

刘宝珍 2020-05-08 11:55:08

**作****者介绍**

**刘宝珍，**架构师，目前就职于大型资产管理公司的科技子公司，拥有多年的大型私有云的规划和设计工作经验，熟悉软件的开发流程，目前醉心于研究基于DDD和敏捷的软件的开发模式，对分布式架构有深入的理解，同时也希望同各位朋友交流软件架构和云计算架构的经验。

 

注：本文转载自订阅号MySQL解决方案工程师，由徐轶韬编辑修订。

 

本文通过记录真实案例的形式，对故障排除的过程进行总结和反思。文中不但描述了刘老师解决问题的思路，还清晰的记载了解决问题的方法。仔细阅读此文，你会发现刘老师对故障的排除和修复有着清晰的思路和严谨的执行方法。

 

另外，通过此文，还可以发现刘老师的一大爱好，去GitHub查找资源，并加以利用。这一举动不但体现了开源软件的优势，也体现了开源爱好者的理念。接下来，让我们阅读刘老师的原文。

 

**一、背景和思路**

 

2020年2月25日，微信的朋友圈大量转载微盟遭遇了系统重大故障，36小时内尚未恢复核心生产数据，从而想到本人在两周前处理的一个案例，开发人员误删除了生产数据，本人恢复的一个过程，同时给这个故障的处理过程做一个总结，也对学过的知识做一个梳理，希望对运维的同学们有一个警示作用。

 

2月13日23:00接到微信通知，能否帮忙恢复数据。

 

系统环境信息如下：

 

- 操作系统：RHEL7.5
- 工作流平台：开源activity
- 业务应用：调用activity，生成该应用的流程数据
- 工作流使用的数据库：MYSQL 5.7社区版，一主两备
- 23:05，开始介入数据丢失的故障

 

确认一个大概解决问题的思路：

 

1、找到是什么人在什么时间点做了什么操作？

 

2、这个操作对系统的影响有多大，是否对其他系统有影响？确认这个操作是不是正常业务体现？

 

3、确认数据库里受到影响的日志的时间段。

 

4、在仿真环境复盘整个故障。

 

5、制定技术恢复方案，在仿真环境验证数据恢复方案。

 

6、在仿真环境验证数据恢复后应用是否正常。

 

7、备份生产环境数据，应用数据恢复方案到生产环境。

 

8、生产环境绿灯测试，无误后，恢复完成。

 

由于恢复生产数据是重大的数据调整，需要报请领导批准，需要有完备的数据回退方案。

 

**二、数据恢复过程及技术分析**

 

用了5分钟理清了处理这个问题思路，接下来就是考虑具体的数据恢复了。在处理这个问题过程中，有两个难点需要解决。

 

1、确认要恢复的binlog的开始和结束。

 

2、根据binlog的开始和结束，确认数据恢复方案，以及是否需要需要排除在这个时间段发生的其他干扰数据。

 

首先解决第一个问题：

 

1、询问开发人员，开发人员给出晚间大概20:20左右操作rest接口，调用了activity（以下简称工作流）平台删除流程模板的操作，导致该流程模板下所有的流程实例全部被删除，在该流程模板下有5个在途的流程尚未处理完成。

 

2、根据开发人员的描述，登录到工作流平台的数据库，查看数据库在20:20左右的binlog 文件，并对11号binlog文件进行备份。

 

3、将binlog拷贝到一个开发的服务器，通过mysqlbinlog进行解析。解析命令为：mysqlbinlog -v --base64-output=decode-rows --skip-gtids=true --start-datetime='2020-02-13 20:10:00' --stop-datetime='2020-02-13 21:30:00' -d {$DBNAME} mysql-bin.000011 >>aa.log dbname做了脱敏处理。

 

4、观察解析后的sql，在20:20分并未发现大量的删除操作，确认开发人员的话不可信，做故障诊断的第一原则：**任何人的话都不能全信，也不可能不信，带着疑问来找到论据证明他的说法。**

 

5、继续翻看解析的binlog，20:30开始出现大量的delete和update等操作，开始怀疑这一点是不是有问题的时间段。

 

6、将这一段的sql进行归纳总结，归纳需要操作几个表，对这个几个表的操作类型，以及操作的数据的类别（业务ID）。同工作流平台的同事进行确认，删除一个工作流的模板，是不是涉及到这些表的变更，工作流平台的同事确认是这个过程，数据恢复的希望诞生了！

 

7、根据以前的经验积累，github上有个开源项目binlog2sql，可以将binlog的event翻译成sql语句，也可以翻译成反向sql，顿时觉得这个问题应该很“容易”解决了。

 

8、根据以上思考，开始在仿真环境里安装binlog2sql工具，该工具就是一个python的程序，需要安装好python环境以及需要的三方库即可，具体的使用方式请参考：https://github.com/danfengcao/binlog2sql，同时也再次感谢工具的作者曹老师。

 

9、在仿真环境里，恢复生产环境有问题的实例，同时在工作流平台将应用的jdbc的url指向新的恢复好的实例。

 

以上几个过程，已经解决了第一个问题，接下来我们要解决第二个问题。

 

1、在以上的步骤里，已经在仿真环境复盘了生产环境的故障，同时在也仿真环境里里安装了binlog转成sql的工具。

 

2、使用binlog2sql的工具，解析出来错误执行的sql，让工作流的平台的同时进行确认，同时让工作流的同事，确认在这个时间段内没有其他的应用也在操作这个数据库。

 

3、工作流的同事确认sql全部为误操作产生的sql。具体的确认方式如下：

 

- 在仿真环境模拟创建一个工作流模板。

- 在这个模板上创建几个测试实例

- 通过接口去删除这个工作流模板，观察应用产生的sql，以此来确认本人提供的sql是否正确。

   

 

 

同时，工作流平台确认在问题时间段内无其他应用操作，感觉胜利在望了，该问题可以轻松解决了。

 

4、通过binlog2sql生产反向sql，把sql应用于仿真环境，问题就能解决了，仔细观察反向sql文件，发现里面有一些乱码，查看乱码字段所在的表，发现表的定义是这样的：

 

![img](https://dbaplus.cn/uploadfile/2020/0508/20200508115618376.png)

 

表中有个字段为longblob字段，产生的insert的sql无法执行，这个问题该怎么处理？

 

5、这个问题到这里陷入了僵局，眼看马上就能解决的问题，发现有一个表数据无法通过sql进行插入，询问工作流平台同事，这个表是否很重要，得到答复，没有这个表的数据，系统无法运转。

 

6、换个思路考虑一下，既然sql是通过二进制的binlog生成的，可以考虑生成反向的二进制binlog，然后把这一段反向的binlog应用到数据库，这个问题就解决了。

 

7、带着这个思路，去github里翻看了项目。果然还真有一个：https://github.com/Meituan-Dianping/MyFlash 再次非常感谢美团点评开源的myflash项目。

 

8、利用myflash生成了反向二进制文件，把文件应用到数据库，工作流平台在仿真环境测试，数据完美再现。

 

**三、问题的反思**

 

通过以上分析，基本上就可以轻松解决这个问题。对自己提出几个问题：

 

1、为什么不用备份恢复的方式进行数据库恢复？

 

在这个系统上，数据已经备份了，每天都有全备，不能使用这个恢复的原因，工作流平台里有很多应用的流程引擎，一旦做了基于时间点恢复，别的应用的系统数据一块被恢复了，将会导致别的系统会丢失一部分数据。

 

2、为什么不基于表的数据恢复？

 

因为工作流平台是一个开源的平台，数据模型之间的关联性特别强，如果基于表的恢复，容易导致数据的约束出现问题。

 

反思：

 

1、 为什么在生产环境出现丢失数据的情况？

 

开发人员在生产上线过程越过了仿真环境，直接上生产，对生产上线过程并不严谨，虽然有管理流程，但是对流程的过程执行不力。

 

2、研发人员的技术能力，研发人员对activity并不熟悉，对于修改流程模板的流程也不熟悉，提高研发人员的技术能力必须要提上日程。

 

**四、后续问题**

 

结合以上分析过程，需要指定一些辅助策略来完善发布流程。

 

1、发布流程自动化，应用代码发布自动化发布，尽量避免人为参与。

 

2、应用发布流程标准化，所有的脚本和上线的新的应用的步骤必须经过验证才能上线。

 

作者丨刘宝珍  编辑修订丨徐轶韬

来源丨MySQL解决方案工程师（ID：mysqlse）

dbaplus社群欢迎广大技术人员投稿，投稿邮箱：editor@dbaplus.cn