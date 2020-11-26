# CICD-代码审计

2019/09/04 Chenxin

## ***需求说明***

要实现的预期目标是什么?(安全,高效,规范?)->规范
后期考虑安全.

## ***漏洞原理***

**参考**
https://blog.csdn.net/wangzhida2008/article/details/75253369 常见web漏洞原理分析

如果Java、PHP、ASP等程序语言的编程人员的安全意识不足，对程序参数输入等检查不严格等，会导致Web应用安全问题层出不穷。本文根据当前Web应用的安全情况，列举了Web应用程序常见的攻击原理及危害，并给出如何避免遭受Web攻击的建议。

**Web应用漏洞原理**
Web应用攻击是攻击者通过浏览器或攻击工具，在URL或者其它输入区域（如表单等），向Web服务器发送特殊请求，从中发现Web应用程序存在的漏洞，从而进一步操纵和控制网站，查看、修改未授权的信息。

**Web应用的漏洞分类**
1、信息泄露漏洞.
造成信息泄露主要有以下三种原因：
--Web服务器配置存在问题，导致一些系统文件或者配置文件暴露在互联网中；
--Web服务器本身存在漏洞，在浏览器中输入一些特殊的字符，可以访问未授权的文件或者动态脚本文件源码；
--Web网站的程序编写存在问题，对用户提交请求没有进行适当的过滤，直接使用用户提交上来的数据。

2、目录遍历漏洞
目录遍历漏洞是攻击者向Web服务器发送请求，通过在URL中或在有特殊意义的目录中附加“../”、或者附加“../”的一些变形（如“..\”或“..//”甚至其编码），导致攻击者能够访问未授权的目录，以及在Web服务器的根目录以外执行命令。

3、命令执行漏洞
命令执行漏洞是通过URL发起请求，在Web服务器端执行未授权的命令，获取系统信息，篡改系统配置，控制整个系统，使系统瘫痪等。
命令执行漏洞主要有两种情况：
--通过目录遍历漏洞，访问系统文件夹，执行指定的系统命令；
--攻击者提交特殊的字符或者命令，Web程序没有进行检测或者绕过Web应用程序过滤，把用户提交的请求作为指令进行解析，导致执行任意命令。

4、文件包含漏洞
文件包含漏洞是由攻击者向Web服务器发送请求时，在URL添加非法参数，Web服务器端程序变量过滤不严，把非法的文件名作为参数处理。这些非法的文件名可以是服务器本地的某个文件，也可以是远端的某个恶意文件。由于这种漏洞是由php变量过滤不严导致的，所以只有基于PHP开发的Web应用程序才有可能存在文件包含漏洞。

5、SQL注入漏洞
SQL注入漏洞是由于Web应用程序没有对用户输入数据的合法性进行判断，攻击者通过Web页面的输入区域(如URL、表单等) ，用精心构造的SQL语句插入特殊字符和指令，通过和数据库交互获得私密信息或者篡改数据库信息。SQL注入攻击在Web攻击中非常流行，攻击者可以利用SQL注入漏洞获得管理员权限，在网页上加挂木马和各种恶意程序，盗取企业和用户敏感信息。

6、跨站脚本漏洞
跨站脚本漏洞是因为Web应用程序没有对用户提交的语句和变量进行过滤或限制，攻击者通过Web页面的输入区域向数据库或HTML页面中提交恶意代码，当用户打开有恶意代码的链接或页面时，恶意代码通过浏览器自动执行，从而达到攻击的目的。跨站脚本漏洞危害很大，尤其是目前被广泛使用的网络银行，通过跨站脚本漏洞攻击者可以冒充受害者访问用户重要账户，盗窃企业重要信息。
根据漏洞研究机构的调查显示，SQL注入漏洞和跨站脚本漏洞的普遍程度排名前两位。

**SQL注入攻击原理**
SQL注入攻击是通过构造巧妙的SQL语句，同网页提交的内容结合起来进行注入攻击。比较常用的手段有使用注释符号、恒等式（如1＝1）、使用union语句进行联合查询、使用insert或update语句插入或修改数据等，此外还可以利用一些内置函数辅助攻击。

通过SQL注入漏洞攻击网站的步骤一般如下：

```
1探测网站是否存在SQL注入漏洞。
2探测后台数据库的类型。
3根据后台数据库的类型，探测系统表的信息。
4探测存在的表信息。
5探测表中存在的列信息。
6探测表中的数据信息。
```

**跨站脚本攻击原理**
跨站脚本攻击的目的是盗走客户端敏感信息,冒充受害者访问用户的重要账户。跨站脚本攻击主要有以下三种形式：

1、本地跨站脚本攻击
B给A发送一个恶意构造的Web URL，A点击查看了这个URL，并将该页面保存到本地硬盘（或B构造的网页中存在这样的功能）。A在本地运行该网页，网页中嵌入的恶意脚本可以执行A电脑上A所持有的权限下的所有命令。

2、反射跨站脚本攻击
A经常浏览某个网站，此网站为B所拥有。A使用用户名/密码登录B网站，B网站存储下A的敏感信息（如银行帐户信息等）。C发现B的站点包含反射跨站脚本漏洞，编写一个利用漏洞的URL，域名为B网站，在URL后面嵌入了恶意脚本（如获取A的cookie文件），并通过邮件或社会工程学等方式欺骗A访问存在恶意的URL。当A使用C提供的URL访问B网站时，由于B网站存在反射跨站脚本漏洞，嵌入到URL中的恶意脚本通过Web服务器返回给A，并在A浏览器中执行，A的敏感信息在完全不知情的情况下将发送给了C。

3、持久跨站脚本攻击
B拥有一个Web站点，该站点允许用户发布和浏览已发布的信息。C注意到B的站点具有持久跨站脚本漏洞，C发布一个热点信息，吸引用户阅读。A一旦浏览该信息，其会话cookies或者其它信息将被C盗走。持久性跨站脚本攻击一般出现在论坛、留言簿等网页，攻击者通过留言，将攻击数据写入服务器数据库中，浏览该留言的用户的信息都会被泄漏。

**Web应用漏洞的防御实现**
对于以上常见的Web应用漏洞漏洞，可以从如下几个方面入手进行防御：

1Web应用开发者
大部分Web应用常见漏洞，都是在Web应用开发中，开发者没有对用户输入的参数进行检测或者检测不严格造成的。所以，Web应用开发者应该树立很强的安全意识，开发中编写安全代码；对用户提交的URL、查询关键字、HTTP头、POST数据等进行严格的检测和限制，只接受一定长度范围内、采用适当格式及编码的字符，阻塞、过滤或者忽略其它的任何字符。通过编写安全的Web应用代码，可以消除绝大部分的Web应用安全问题。

2Web网站管理员
作为负责网站日常维护管理工作Web管理员，应该及时跟踪并安装最新的、支撑Web网站运行的各种软件的安全补丁，确保攻击者无法通过软件漏洞对网站进行攻击。
除了软件本身的漏洞外，Web服务器、数据库等不正确的配置也可能导致Web应用安全问题。Web网站管理员应该对网站各种软件配置进行仔细检测，降低安全问题的出现可能。
此外，Web管理员还应该定期审计Web服务器日志，检测是否存在异常访问，及早发现潜在的安全问题。

3使用网络防攻击设备
前两种为事前预防方式，是比较理想化的情况。然而在现实中，Web应用系统的漏洞还是不可避免的存在：部分Web网站已经存在大量的安全漏洞，而Web开发者和网站管理员并没有意识到或发现这些安全漏洞。由于Web应用是采用HTTP协议，普通的防火墙设备无法对Web类攻击进行防御，因此可以使用IPS入侵防御设备来实现安全防护。

**完整防护**
一个完整的Web攻击防御解决方案，通过安全的Web应用程序、Web服务器软件、Web防攻击设备共同配合，确保整个网站的安全。任何一个简单的漏洞、疏忽都会造成整个网站受到攻击，造成巨大损失。此外 ，Web攻击防御是一个长期持续的工作，随着Web技术的发展和更新，Web攻击手段也不断发展，针对这些最新的安全威胁，需要及时调整Web安全防护策略，确保Web攻击防御的主动性，使Web网站在一个安全的环境中为企业和客户服务。

## ***攻防之操作系统介绍***

这里列出的5款linux发行版,它们包具备很好的的渗透测试工具以及其他黑客工具.这里列表中目前最受欢迎的Linux发行版是Kail Linux,是因为它在渗透测试中非常流行.它的开发团队 Offensive security .

- Kali Linux (最常用)
  Kali Linux 在渗透测试和白帽子方面是业界领先的 Linux 发行版。默认情况下，该发行版附带了大量入侵和渗透的工具和软件，并且在全世界都得到了广泛认可。
- BackBox
  它包括了一些经常使用的安全和分析工具，可以用于从 web 应用分析到网络分析，从压力测试到嗅探，以及脆弱性分析、计算机取证分析和破解等等的各种用途。 这个发行版的一大特点是，它的 Launchpad 软件库会持续更新各种工具的最新稳定版，它们都是白帽黑客所熟知常用的。该发行版中的新工具集成和开发遵循了开源社区的标准，特别是 Debian 自由软件指导Debian Free Software Guidelines的标准。
- Parrot Security (界面最炫酷)
  是一个基于 Debian GNU/Linux 的发行版，并混以 Frozenbox OS 和 Kali linux 的部分特性，以提供最好的渗透和安全测试体验。它是由 Frozenbox Dev Team 开发的。
  Parrot 采用 Kali 的软件库来更新大部分工具，不过也有提供其自己的定制软件的软件库。这也是为何它不只是一个简单的 Kali 修改版，而是一个建立在 Kali 工具库之上的新系统，因此，它引入了许多新功能和不同的开发选择。Parrot 使用 MATE 作为桌面环境，这是一个轻量级的、高效的 Gnome 2 家族的衍生品。还有来自 FrozenBox 的高度定制的迷人的图标、特制的主题和墙纸。系统外观是由该社区的成员以及关注该项目进展的 Frozenbox Network 的成员建议并设计的
- deft
  是一个 Ubuntu 定制版，带有一整套由数以千计的个人、团队和公司所创建的计算机取证程序和文档。它们每一个都可能采用了不同的许可证，它的许可证策略决定了哪些软件会被放到 deft 中和默认放到它的安装光盘中。
- Pentoo
  是一个用于渗透测试和安全评估的即用 CD 和 USB。它基于 Gentoo Linux ，提供了 32 位和 64 位的即用 CD 。Pentoo 也可以覆盖安装到现有的 Gentoo 环境中。它提供了特色的带有包注入补丁的 WIFI 驱动，GPGPU 破解软件，以及许多渗透测试和安全评估的软件。Pentoo 内核带有 grsecurity 和 PAX 加固补丁，其提供的二进制是由加固工具链编译而成的，其中一些工具还有最新的每日构建版本。

## ***漏洞扫描***

**漏洞扫描工具**

- AWVS
  国外商业收费软件，据了解一个License一年费用是2万多RMB。可见总体漏洞扫描概况，也可导出报告，报告提供漏洞明细说明、漏洞利用方式、修复建议。缺点是限制了并行扫描的网站数
  网上有破解版.
- OWASP Zed（ZAP）
  来自OWASP项目组织的开源免费工具，提供漏洞扫描、爬虫、Fuzz功能，该工具已集成于Kali Linux系统。
- Nikto
  一款开源软件，不仅可用于扫描发现网页文件漏洞，还支持检查网页服务器和CGI的安全问题。它支持指定特定类型漏洞的扫描、绕过IDC检测等配置。该工具已集成于Kali Linux系统。
- BurpSuite
  “Scanner”功能用于漏洞扫描，可设置扫描特定页面，自动扫描结束，可查看当前页面的漏洞总数和漏洞明细。虽说也有漏扫功能，但其核心功能不在于此，因此漏扫功能还是不如其他专业漏洞扫描工具。
- Nessus
  面向个人免费、面向商业收费的形式，不仅扫描Web网站漏洞，同时还会发现Web服务器、服务器操作系统等漏洞。个人用户只需在官网上注册账号即可获得激活码。它是一款Web网站形式的漏洞扫描工具。
  Nessus (渗透测试工具,支持linux,mac,Windows)
  Nessus漏洞扫描教程之安装Nessus工具
  参考 https://www.cnblogs.com/daxueba-ITdaren/p/4635784.html
  Nessus基础知识
  Nessus号称是世界上最流行的漏洞扫描程序，全世界有超过75000个组织在使用它。该工具提供完整的电脑漏洞扫描服务，并随时更新其漏洞数据库。Nessus不同于传统的漏洞扫描软件，Nessus可同时在本机或远端上遥控，进行系统的漏洞分析扫描。对应渗透测试人员来说，Nessus是必不可少的工具之一。所以，本章将介绍Nessus工具的基础知识。
  官方分为家庭版和专业版.一般选择家庭版就可以了.家庭版需要一个邮件地址来接收激活码(免费的).
  Nessus概述
  Nessus通常包括成千上万的最新的漏洞，各种各样的扫描选项，及易于使用的图形界面和有效的报告。Nessus之所以被人们喜爱，是因为该工具具有几个特点。如下所示：

```
q  提供完整的电脑漏洞扫描服务，并随时更新其漏洞数据库。
q  不同于传统的漏洞扫描软件。Nessus可同时在本机或远程控制，进行系统的漏洞分析扫描。
q  其运作效能随着系统的资源而自行调整。如果将主机配置更多的资源（如加快CPU速度或增加内存大小），其效率表现可因为丰富资源而提高。
q  可自行定义插件。
q  NASL（Nessus Attack Scripting Language）是由Tenable所发出的语言，用来写入Nessus的安全测试选项。
q  完全支持SSL（Secure Socket Layer）。
```

- OpenVAS
  是开放式漏洞评估系统，也可以说它是一个包含着相关工具的网络扫描器。其核心部件是一个服务器，包括一套网络漏洞测试程序，可以检测远程系统和应用程序中的安全问题。
- 其他
  一些其他商业漏洞扫描软件（Safe3 WVS、IBM公司的AppScan）、以及其他特定网站类型的扫描工具（针对jboss的jboss-autopwn、针对joomla的joomscan、针对wordpress的wpscan）

## ***Java代码审计常用工具(部分支持.net,c++等)***

### 静态分析

**PMD (java静态分析)**

- 需要安装到 Eclipse 或 IDEA.
- PMD是一款采用BSD协议发布的Java程序代码检查工具。该工具可以做到检查Java代码中是否含有未使用的变量、是否含有空的抓取块、是否含有不必要的对象等。该软件功能强大，扫描效率高，是Java程序员debug的好帮手。

- 与其他分析工具不同的是，PMD通过静态分析获知代码错误。也就是说在不运行Java程序的情况下，报告错误。
- PMD附带了许多可以直接使用的规则，利用这些规则可以找出Java源程序的许多问题。
  -此外，用户还可以自己定义规则。检查Java代码是否符合某些特定的编码规范。常见的类型如下：
  潜在的bug：空的try/catch/finally/switch语句
  未使用的代码：未使用的局部变量、参数、私有方法等
  可选的代码：String/StringBuffer的滥用
  复杂的表达式：不必须的if语句、可以使用while循环完成的for循环
  重复的代码：拷贝/粘贴代码意味着拷贝/粘贴bugs
  循环体创建新对象：尽量不要再for或while循环体内实例化一个新对象
  资源关闭：Connect，Result，Statement等使用之后确保关闭掉

- coinw当前情况
  老的代码问题太多,跑PMD后,没法看.
  新的代码可以.
- hpx
  当前没有用,之后尝试安装到IDE里.

**FindBugs (java bug静态分析)**
同PMD,需要安装到IDE里.
通过一些必要的检查工具来去发现程序潜在的bug，尽管工具不能解决大部分问题，但是也是能够给我们带来很大帮助。
FindBugs是一款 静态分析工具，检查程序潜在bug，在bug报告中快速定位到问题的代码上。

### 静态安全检测 (价格昂贵)

对于应用安全性的检测目前大多数是通过测试的方式来实现。
测试大体上分为黑盒测试和白盒测试两种。
黑盒测试一般使用的是渗透的方法，这种方法仍然带有明显的黑盒测试本身的不足，需要大量的测试用例来进行覆盖，且测试完成后仍无法保证软件是否仍然存在风险。
现在白盒测试中源代码扫描越来越成为一种流行的技术，使用源代码扫描产品对软件进行代码扫描，一方面可以找出潜在的风险，从内对软件进行检测，提高代码的安全性，另一方面也可以进一步提高代码的质量。
黑盒的渗透测试和白盒的源代码扫描内外结合，可以使得软件的安全性得到很大程度的提高。
源代码分析技术由来已久.而在静态源代码安全分析方面，Fortify 公司和 Ounce Labs 公司的静态代码分析器都是非常不错的产品。
对于源代码安全检测领域目前的供应商有很多，这里我们选择其中的三款具有代表性的进行对比，分别是 Fortify公司的Fortify SCA，Security Innovation公司的Checkmarx Suite和Armorize公司的CodeSecure。

**Checkmarx (静态代码安全检测工具)**
Checkmarx 白盒代码审计解决方案，主要通过采用独特的词汇分析技术和CxQL专利查询技术对应用程序源码进行静态分析检查。

```
无需编译，可以直接上传源码zip包，CheckMarx直接扫描源码；
规则可定制，用户可以根据不同的语言类型自定义选择检查规则，针对性强；
静态分析，代码无需运行；
增量扫描，再次扫描，只分析新增代码及相关文件；
低耦合，易于集成到软件开发的任何阶段。
```

开发者:以色列的一家高科技软件公司CheckMarx开发本软件CxSuite（其实就叫这个名字）。
服务器要求：window服务器部署
价格: 大约70万(软件)

**Fortify SCA**
Fortify SCA(Source Code Analysis).
Fortify Software公司是一家总部位于美国硅谷，致力于提供应用软件安全开发工具和管理方案的厂商。
开发生命周期中花最少的时间和成本去识别和修复软件源代码中的安全隐患。
Fortify SCA是Fortify360产品套装中的一部分，它使用fortify公司特有的X-Tier Dataflow™ analysis技术去检测软件安全问题。
优点：目前全球最大静态源代码检测厂商、支持语言最多
缺点：价格昂贵、使用不方便.大约100万.

**Armorize CodeSecure**
Armorize CodeSecure阿码科技2006年，总部设立于美国加州，研发位于台湾.
阿码科技提供全方位网络安全解决方案，捍卫企业免于受到黑客利用 Web 应用程序的漏洞所发动的攻击。
CodeSecure内建语法剖析功能无需依赖编译环境，任何人员均可利用 Web操作与集成开发环境双接口，找出存在信息安全问题的源代码，并提供修补建议进行调整。
CodeSecure依托于自行开发的主机进行远程源代码检测，在保证速度稳定的同时方便用户进行Web远程操作。
优点：Web结合硬件，速度快、独具特色的深度分析
缺点：支持语言种类较少、价格不菲.大约100万.

### 其他静态源代码检测产品

公司 产品 支持语言
art of defence Hypersource JAVA
Coverity Prevent JAVA .NET C/C++
开源 Flawfinder C/C++
Grammatech CodeSonar C/C++
HP DevInspect JAVA
KlocWork Insight JAVA .NET C/C++，C#
Ounce Labs Ounce 6 JAVA .NET
Parasoft JTEST等 JAVA .NET C/C++
SofCheck Inspector for JAVA JAVA
University of Maryland FindBugs JAVA
Veracode SecurityReview JAVA .NET
FindBug PMD／Lint4 JAVA

### 代码审计工具的部署与使用

请参考本文后半段部分.比如 sonar 等.
代码检测工具其实有很多，IDEA建议直接安装阿里代码检测插件（Alibaba Java Coding Guidelines），简单实用。

## ***代码审计常用工具(其他语言)***

**PHP类**

- No1 Seay源代码审计工具
  Seay源代码审计工具一款php代码审计工具，主要是运用于windows，这款工具可以发现常见的php漏洞，另外还支持一键审计、代码调试、函数定位、插件扩展、数据库执行监控等功能！
- No2 rips源代码审计系统
  Rips源代码审计系统是可以用于linux和windows上的一款源代码审计系统！使用方式很简单，直接将rips源码放在web应用的根目录下就可以了。(PHP)

## ***代码覆盖率工具***

- 代码覆盖率
  代码覆盖（Code coverage）是软件测试中的一种度量，描述程式中源代码被测试的比例和程度，所得比例称为代码覆盖率。
  代码覆盖率是衡量测试质量的一个重要指标。在对一个软件产品进行了单元测试、组装测试、集成测试以及接口测试等繁多的测试之后，我们能不能就此对软件的质量产生一定的信心呢？这就需要我们对测试的质量进行考察。如果测试仅覆盖了代码的一小部分，那么不管我们写了多少测试用例，我们也不能相信软件质量是有保证的。相反，如果测试覆盖到了软件的绝大部分代码，我们就能对软件的质量有一个合理的信心。
- 常用工具对比
  Jacoco,Emma,Cobertura

**Jacoco (覆盖率工具.可以集成到cicd里)**

- 简介Jacoco
  是一个开源的覆盖率工具。
  Jacoco 可以嵌入到 Ant 、Maven 中，并提供了 EclEmma Eclipse 插件.
  很多第三方的工具提供了对 Jacoco 的集成，如：Sonar、Jenkins、IDEA.
  目前Java常用覆盖率工具Jacoco、Emma和Cobertura、Clover(商用)
  建议集成到CICD流程里,统一规划.
- 部署参考
  https://www.jianshu.com/p/e7fc806ea0e0

## 其他参考

向阳:我们目前在测试代码规范的工具。用的clang-format和tscancode。(都是c语言类的.tscancode是腾讯出的)
何庆:sonar+Jenkins.开发自己审计+安全部门审计

## 当前可采取方案

1.研发部门本地IDE安装PMD,findbugs插件,在每次合并到Git主分支(或发布分支)前进行检测排查.
2.Jenkins里配置Sonar.Jacoco可以根据情况决定是否集成进CICD.
3.使用安全检测软件扫描代码,如Nessus(家庭免费版).其他商业版,如Fortify SCA(100万).

## Sonar 部署(属于代码审查审计部分)

参考
https://blog.csdn.net/qq_25268441/article/details/88944166 比较详细的说明了3种方案的步骤
https://www.cnblogs.com/rongfengliang/p/6219346.html sonarQube的主要参考
https://blog.csdn.net/javandroid/article/details/84143584 主要区别sonarQube 和 Scanner

### **简介**

- 官网 www.sonarqube.org
  sonar,即sonarqube,sonar scan. Sonar是一个用于代码质量管理的开源平台.
  通过插件机制，Sonar 可以集成不同的测试工具，代码分析工具，以及持续集成工具，比如pmd-cpd、checkstyle、findbugs、Jenkins。
  通过不同的插件对这些结果进行再加工处理，通过量化的方式度量代码质量的变化，从而可以方便地对不同规模和种类的工程进行代码质量管理。
  同时 Sonar 还对大量的持续集成工具提供了接口支持，可以很方便地在持续集成中使用 Sonar。
  此外，Sonar 的插件还可以对 Java 以外的其他编程语言提供支持(比如支持java,python,c++,go等等)，对国际化以及报告文档化也有良好的支持.
  官方特性说明:
  Static code analysis for 15 languages:Java, JavaScript, C#, TypeScript, Kotlin, Ruby, Go, Scala, Flex, Python, PHP, HTML, CSS, XML and VB.NET
  Detect Bugs & Vulnerabilities
  Review Security Hotspots
  Track Code Smells & fix your Technical Debt
  Code Quality Metrics & History
  CI/CD integration
  Extensible, with 60+ community plugins
- 关于sonarQube Scanner说明
  当配置好sonar的服务端后，接下来就要使用sonar检测我们的代码了，sonar主要是借助客户端检测工具来检测代码，所以要使用sonar就必须先在我们本地配置好客户端检测工具。
  客户端可以通过IDE插件、Sonar-Scanner插件、Ant插件和Maven插件方式进行扫描分析。
  常用的有扫描器有Sonar-Scanner和Sonar-Runner，使用起来都差不多。这里我使用Sonar-Scanner来作为检测客户端.
  那么说,sonar scanner就是个客户端.
- sonar可以从以下七个维度来检测代码质量

> 1、不遵循代码标准: sonar可以通过PMD，CheckStyle，Findbugs等代码规则检测工具规范代码的编写；
> 2、潜在的缺陷: sonar可以通过PMD，CheckStyle，Findbugs等代码规则检测工具检测出潜在的缺陷；
> 3、糟糕的代码复杂度分布: 文件、类、方法等，如果复杂度过高将难以改变，且如果没有自动化的单元测试，对于程序中的任何组件的改变都将可能导致需要全面的回归测试；
> 4、重复: 显然程序中包含大量复制粘贴的代码质量低下的，sonar可以展示源码中重复严重的地方；
> 5、注释不足或者过多: 没有注释将使代码可读性变差，特别是当不可避免地出现人员变动时，程序的可读性将大幅度下降；
> 6、缺乏单元测试: sonar可以很方便地统计并展示单元测试覆盖率；
> 7、糟糕的设计: 通过sonar可以找出循环，展示包与包、类与类之间的相互依赖关系，可以展示自定义的架构规则。通过sonar可以管理第三方的jar包，可以利用LCOM4检测单个任务规则的应用秦高，检测耦合。

### **SonarQube数据(库)说明**

1.自带数据库模式(仅限于测试使用)
因sonar7.9版本以及以后的版本都不再支持mysql,故这里使用sonar自带的数据模式.Apache Derby 是Sonar自带并且默认安装使用的数据库(无需额外操作).

```
[root@localhost data]# pwd
/usr/local/sonarqube/data
[root@localhost data]# cat README.txt 
This directory contains data of embedded database (H2 Database Engine). It's recommended for tests and demos only.
```

内嵌数据库只能用于测试场景
内嵌数据库无法扩展，也无法升级到新版本的SonarQube，并且不能支持将你的数据迁移至其他数据库引擎。

2.采用PG数据库模式
PGsql的安装部署请参考对应文档.在安装完sonar后,再进行sonar的sql配置.

### **SonarQube部署,设置**

- 创建系统sonar用户
  不能使用root用户哦.

```
useradd sonar
passwd sonar  # SonarLegend
```

- 安装jdk12
  oracle官网下载最新的JDK(当前是JDK-12,生产系统大多装的是JDK-8u221不符合sonar要求).
  安装完,设置环境变量.

```
[sonar@localhost ~]$ pwd
/home/sonar
[sonar@localhost ~]$ tail .bash_profile 
export JAVA_HOME=/usr/local/jvm12
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
export SONAR_HOME=/usr/local/sonarqube  # 请先安装sonar
export PATH=/usr/local/sonarqube/bin/linux-x86-64:$PATH
```

- 安装sonar

```
下载安装包
http://www.sonarqube.org/downloads/ 下载sonar zip文件
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-7.9.1.zip 为2019/07版本.
解压,放置到相应文件夹
unzip sonarqube-7.9.1.zip 
mv sonarqube-7.9.1 /usr/local/sonarqube
```

- 配置数据库
  cd 至 /usr/local/sonarqube/conf目录下，编辑sonar.properties 文件
  修改以下几项(配置数据库路径、用户名、密码)

```
sonar.jdbc.url=jdbc:postgresql://localhost/sonar
sonar.jdbc.username=postgres
sonar.jdbc.password=PGsqlLG2019
```

因当前数据库中无sonar库,故需要先登录库手动创建一个 create database sonar(可以使用Navicat).当sonar启动成功后,会自动创建很多表.

碰到过的问题

```
查看/usr/local/sonarqube/logs/web.log文件,提示数据库连接问题.
Caused by: java.sql.SQLException: Cannot create PoolableConnectionFactory (致命错误: 用户 "postgres" Ident 认证失败)
```

原因是PG数据库的连接设置/var/lib/pgsql/11/data/pg_hba.conf 文件配置错误.具体配置请参考PG文档说明.

- 启动方式
  启动前准备工作
  文件赋权(否则无法启动)

```
[sonar@localhost ~]$ ll /usr/local/sonarqube/
drwxr-xr-x 6 sonar sonar   94 7月  10 12:21 bin
drwxr-xr-x 2 sonar sonar   50 9月   9 15:56 conf
...
```

设置打开文件数

```
[root@localhost data]# tail /etc/security/limits.conf 
*    soft    nproc    655360
*    hard    nproc    655360
*    soft    nofile    655360
*    hard    nofile    655360
```

设置vm.max_map_count

```
[root@localhost data]# tail /etc/sysctl.conf 
vm.max_map_count=262144
```

### **启动sonarQube**

1）直接启动(推荐)
不使用root用户的原因是sonar需要JDK12,而root环境的是JDK8.
Sonar默认集成了jetty容器，可以直接启动提供服务，也可以通过脚本构建为war包，部署在tomcat容器中。
这里sonar用户登录系统,执行启动脚本

```
su - sonar # 获取sonar系统用户的环境变量(加载JDK12)
/usr/local/sonarqube/bin/linux-x86-64/sonar.sh console # 启动,通过直接控制台输出确认是否有报错
/usr/local/sonarqube/bin/linux-x86-64/sonar.sh start # 一般启动方式.停止为 stop
在浏览器中访问: http://192.168.3.227:9000/ 打开web控制台.
Sonar默认的端口是”9000”、默认的上下文路径是”/”、默认的网络接口是”0.0.0.0”，默认的管理员帐号和密码为:admin/admin (这个是在DB中的,这里通过sonar控制台手动修改为 So123456Nar )
```

启动端口

```
tcp        0      0 127.0.0.1:32000         0.0.0.0:*               LISTEN      18113/java          
tcp6       0      0 :::9000                 :::*                    LISTEN      18286/java          
tcp6       0      0 127.0.0.1:9001          :::*                    LISTEN      18145/java          
tcp6       0      0 127.0.0.1:40942         :::*                    LISTEN      18536/java          
tcp6       0      0 127.0.0.1:9092          :::*                    LISTEN      18286/java  
```

- 更换语言包
  登录Sonar并选择Administration中，选择MarketPlace，搜索Chinese Pack，安装完成后，按照提示重启即可.
  在 /usr/local/sonarqube/extensions/plugins/ 会多出 sonar-l10n-zh-plugin-1.29.jar 包.

2）作为Tomcat的Web项目启动(略过)

```
部署到Tomcat等应用服务器中进行启动
a. 确保conf/sonar.properties、conf/wrapper.conf未被修改使用过
b. 执行如下命令生成war包，将生成的sonar.war部署到应用服务器中
$ ${SONAR_HOME}/war/build-war.sh
c. 启动Tomcat, 通过 http://localhost:8080/sonar 访问.
```

- 配置为系统服务
  略.
  尝试作为开机自启动,如

```
错误方式
/etc/rc.local 添加
sudo -u sonar source /home/sonar/.bash_profile && /usr/local/sonarqube/bin/linux-x86-64/sonar.sh start # 这里无法执行的.因为sodu默认是无法执行source指令的.sodu的Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin .而source是bash的内置指令.

正确方式
/etc/rc.local 添加
sudo -u sonar /home/sonar/sonar-start.sh
脚本如下(将source /home/sonar/.bash_profile 里的内容,直接放到脚本文件里)
cat /home/sonar/sonar-start.sh 
#!/bin/bash
export JAVA_HOME=/usr/local/jvm12
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
export SONAR_HOME=/usr/local/sonarqube
export PATH=/usr/local/nodejs/bin:/usr/local/sonarqube/bin/linux-x86-64:$PATH

/usr/local/sonarqube/bin/linux-x86-64/sonar.sh  start
```

### **插件说明**

- 插件与更新中心
  以管理员用户登录Sonar，进入配置->系统，选择更新中心
  其中Available Plugins选项卡提供了可以选择安装的插件，System Updates可以在线更新Sonar。
  下载插件需要注意其中有些插件是需要购买才能使用的，其License类型为Commercial。
- 插件介绍
  登录Sonar并选择Administration中，选择MarketPlace，搜索插件并安装,会自动放到
  ${SONAR_HOME}extensions\plugins目录下，然后重新启动sonar即可.

sonar默认集成了Java Ecosystem插件，该插件是一组插件的合集
1)Java [sonar-java-plugin]：java源代码解析，计算指标等
2)Squid [sonar-squid-java-plugin]：检查违反Sonar定义规则的代码
3)Checkstyle [sonar-checkstyle-plugin]：使用CheckStyle检查违反统一代码编写风格的代码
4)FindBugs [sonar-findbugs-plugin]：使用FindBugs检查违反规则的缺陷代码 手动安装
5)PMD [sonar-pmd-plugin]：使用pmd检查违反规则的代码 手动安装
6)Surefire [sonar-surefire-plugin]：使用Surefire执行单元测试
7)Cobertura [sonar-cobertura-plugin]：使用Cobertura获取代码覆盖率
8)JaCoCo [sonar-jacoco-plugin]：使用JaCOCO获取代码覆盖率

下面列出了一些常用的插件：
1)JavaScript代码检查：http://docs.codehaus.org/display/SONAR/JavaScript+Plugin
2)python代码检查：http://docs.codehaus.org/display/SONAR/Python+Plugin
3)Web页面检查（HTML、JSP、JSF、Ruby、PHP等）：http://docs.codehaus.org/display/SONAR/Web+Plugin
4)xml文件检查：http://docs.codehaus.org/display/SONAR/XML+Plugin
5)scm源码库统计分析：http://docs.codehaus.org/display/SONAR/SCM+Stats+Plugin
6)文件度量：http://docs.codehaus.org/display/SONAR/Tab+Metrics+Plugin
7)中文语言包：http://docs.codehaus.org/display/SONAR/Chinese+Pack
8)时间表显示度量结果：http://docs.codehaus.org/display/SONAR/Timeline+Plugin
9)度量结果演进图：http://docs.codehaus.org/display/SONAR/Motion+Chart+Plugin

- 插件配置示例（本段内容来自http://www.ibm.com/developerworks/cn/java/j-lo-sonar/）
  Sonar 的主要特色是对不同工具产生的检查结果进行再加工处理，Sonar 还向用户提供了对数据进行个性化处理的方法。
  略.

### **Sonar代码检测/审计的3种方案**

- SonarQube类似于一个展示控制台.而代码检测,则需要对应的插件或者软件.这里说明3种方式.
  1.通过Sonar机器本地安装官方sonar-scanner方式
  2.通过Maven里配置的org.sonarsource.scanner.maven插件方式
  3.通过Jenkins里安装和配置SonarQube Scanner插件方式
  以下针对3种方式分别说明(重点关注Jenkins方式).

**1.方案1,本地安装sonar-scanner命令(这里不采用此方式)**
1.下载安装包
https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744-linux.zip
2.解压后,放置到 /usr/local/sonar-scanner
修改配置文件sonar-scanner.properties，配置指定的web路径和编码.
这里的web路径就是SonarQube的9000端口路径.
3.配置环境变量
将sonar-scanner配置到环境变量
vi /etc/profile
添加如下内容
export PATH="/usr/local/sonar-scanner/bin:$PATH"
source /etc/profile
配置后即可在任何地方运行sonar-scanner命令: sonar-scanner -v
4.在项目工程目录下,新建sonar-project.properties

```
[root@localhost maven-git-test-201908]# pwd
/var/lib/jenkins/workspace/maven-git-test-201908
[root@localhost maven-git-test-201908]# cat sonar-project.properties 
sonar.projectKey=coinw-web2
sonar.projectName=coinw-web2
sonar.projectVersion=1.0
sonar.sources=src
sonar.java.binaries=target/classes
sonar.language=java
```

5 执行sonar-scanner
在当前目录下执行sonar-scanner,稍等片刻看到如下提示则证明扫描成功

```
INFO: ANALYSIS SUCCESSFUL, you can browse http://localhost:9000/dashboard?id=coinw-web2
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
INFO: More about the report processing at http://localhost:9000/api/ce/task?id=AW09yPpckzrUl9yqZSKG
INFO: Analysis total time: 4:45.567 s
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 4:46.083s
INFO: Final Memory: 22M/90M
INFO: ------------------------------------------------------------------------
```

6.报错处理
报错内容

```
ERROR: Failed to find 'typescript' module. Please check, NODE_PATH contains location of global 'typescript' or install locally in your project
```

原因为找不到typescript(属于nodejs).
这里先安装nodejs,如下
大陆官网 http://nodejs.cn/download/ 下载,解压.放置到 ls /usr/local/nodejs/
将 /usr/local/nodejs/bin 路径加入到 /etc/profile 中. source /etc/profile .
执行 node -v 验证安装是否正确(正确则报版本号:v12.10.0 ).
然后, npm install -g typescript (npm为nodejs的bin下的指令)
修改profile文件,增加(第二次修改)
export NODE_PATH=/usr/local/nodejs/lib/node_modules

7.刷新sonarQube的web端查看项目，即可看到扫描后的漏洞和bug

**2.方案2,通过Maven进行集成(这里不采用此方式)**
修改maven的主配置文件（${MAVEN_HOME}/conf/settings.xml文件或者 ~/.m2/settings.xml文件），在其中增加访问Sonar数据库及Sonar服务地址，添加如下配置：

```
<profile>
<id>sonar</id>
<properties>
    <sonar.jdbc.url>jdbc:mysql://localhost:3306/sonar</sonar.jdbc.url>
    <sonar.jdbc.driver>com.mysql.jdbc.Driver</sonar.jdbc.driver>
    <sonar.jdbc.username>sonar</sonar.jdbc.username>
    <sonar.jdbc.password>sonar</sonar.jdbc.password>
    <sonar.host.url>http://localhost:9000</sonar.host.url> <!-- Sonar服务器访问地址 -->
</properties>
</profile>
<activeProfiles>
    <activeProfile>sonar</activeProfile>
</activeProfiles>
```

此处注意sonar.host.url地址应根据sonar部署情况修改
同样，为了避免内存溢出，推荐增加内存堆栈的大小。设置MAVEN_OPTS环境变量：
set MAVEN_OPTS=”-Xmx512m -XX:MaxPermSize=256m”

使用Sonar
a. 运行Sonar服务器;
b. 通过 mvn sonar:sonar 将代码注入到Sonar中进行分析处理,并将处理结果以XML的形式保存在数据库中;
c. 通过浏览器访问,显示分析结果;
d. 持续运行Maven构建,会迭代显示分析结果;
e. 可以显式指定sonar插件的版本,如下:

```
<project>
   <build>
       <plugins>
           <plugin>
               <groupId>org.codehaus.sonar</groupId>
               <artifactId>sonar-maven-plugin</artifactId>
               <version>3.5.1</version>
           </plugin>
       </plugins>
   </build>
</project>
```

f. 可以显式的将sonar绑定到Maven生命周期中,如下:

```
<plugin>  
   <groupId>org.codehaus.sonar</groupId>
   <artifactId>sonar-maven-plugin</artifactId>
   <version>3.5.1</version>
   <executions>
       <execution>
           <id>sonar</id>
           <phase>site</phase>
           <goals>
           <goal>sonar</goal>
           </goals>
       </execution>
   </executions>
</plugin>
```

此时,指定Maven的site声明周期时,则会自动调用sonar.sonar 命令.
在项目路径下执行mvn sonar:sonar,则会自动生成报告,通过sonarQube控制台查看.

**3.方案3,与Jenkins集成**
1.安装Jenkins.略.

2.在Jenkins里,安装插件 SonarQube Scanner(SonarQube Scanner for Jenkins) .略.

3.配置sonar server
系统管理->系统设置
首先在SonarQube的控制台,去创建令牌名称 chenxin 值 43173747aed34a02cdcbe3b18cbc3ea304acd5dc (coinw)
令牌名称 chenxin 值 1d0d3ac22d4abf8525eda9ca9ea2b227f5cae18a (hpx)
Name: sonar-server
Server URL: [http://192.168.3.227:9000](http://192.168.3.227:9000/)
Server authentication token: (选项Server authentication token需要添加一下,注意类型选 Secret text，Secret、ID 都填Sonar首次登录提供的token值).
保存.

4.配置全局工具
系统管理-> 全局工具设置,设置sonarQube Scanner，输入上步设置的sonar server名称,如sonar-server.

5.配置构建步骤
关于git的配置,略.
程序编译部分请参考Jenkins文档.这里只涉及代码审计部分.
设置post-build step,增加"Execute SonarQube Scanner".对应的参数,类似如下.
选择指定的jdk(这里用默认jdk1.8系统里的)

设置Analysis properties
sonar.projectKey=coinw-web     工程key(好像只是个名字,可以任意)
sonar.projectName=coinw-web   工程名(好像只是个名字,可以任意)
sonar.projectVersion=1.0      版本
sonar.sources=src           java代码路径
sonar.java.binaries=target/classes   class路径
sonar.language=java

6.构建的时候,报错说明
报错1 ERROR: Error when running: 'node -v'. Is Node.js available during analysis? No CSS files will be analyzed.原因是Jenkins找不到nodejs的执行路径.需要在系统里安装nodejs(参考sonar-scaner方案一部分).
报错2 ERROR: Error: Cannot find module 'typescript',原因是因为没有给NODE_PATH变量.
以上两个报错,是因为Jenkins里找不到对应的PATH和NODE_PATH变量.需要手动添加.具体请参考Jenkins对应文档内容(并没有继承/etc/profile文件).

### **sonar与ldap集成**

配置文件 /usr/local/sonarqube/conf/sonar.properties 支持 LDAP.
具体配置略.