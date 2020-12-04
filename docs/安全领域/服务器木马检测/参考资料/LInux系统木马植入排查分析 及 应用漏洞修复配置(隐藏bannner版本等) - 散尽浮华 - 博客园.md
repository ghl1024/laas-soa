在日常繁琐的运维工作中，对linux服务器进行安全检查是一个非常重要的环节。今天，分享一下如何检查linux系统是否遭受了入侵？

一、是否入侵检查

1）检查系统日志

```
检查系统错误登陆日志，统计IP重试次数（last命令是查看系统登陆日志，比如系统被reboot或登陆情况）
[root@bastion-IDC ~]# last
```

2）检查系统用户

```
查看是否有异常的系统用户
[root@bastion-IDC ~]# cat /etc/passwd

查看是否产生了新用户，UID和GID为0的用户
[root@bastion-IDC ~]# grep "0" /etc/passwd

查看passwd的修改时间，判断是否在不知的情况下添加用户
[root@bastion-IDC ~]# ls -l /etc/passwd

查看是否存在特权用户
[root@bastion-IDC ~]# awk -F: '$3==0 {print $1}' /etc/passwd

查看是否存在空口令帐户
[root@bastion-IDC ~]# awk -F: 'length($2)==0 {print $1}' /etc/shadow
```

3）检查异常进程

```
注意UID为0的进程
使用ps -ef命令查看进程

察看该进程所打开的端口和文件
[root@bastion-IDC ~]# lsof -p pid命令查看

检查隐藏进程
[root@bastion-IDC ~]# ps -ef | awk '{print }' | sort -n | uniq >1

[root@bastion-IDC ~]# ls /porc |sort -n|uniq >2

[root@bastion-IDC ~]# diff 1 2
```

4）检查异常系统文件

```
[root@bastion-IDC ~]# find / -uid 0 –perm -4000 –print
[root@bastion-IDC ~]# find / -size +10000k –print
[root@bastion-IDC ~]# find / -name "…" –print
[root@bastion-IDC ~]# find / -name ".." –print
[root@bastion-IDC ~]# find / -name "." –print
[root@bastion-IDC ~]# find / -name " " –print
```

5）检查系统文件完整性

```
[root@bastion-IDC ~]# rpm –qf /bin/ls
[root@bastion-IDC ~]# rpm -qf /bin/login
[root@bastion-IDC ~]# md5sum –b 文件名
[root@bastion-IDC ~]# md5sum –t 文件名
```

6）检查RPM的完整性

```
[root@bastion-IDC ~]# rpm -Va #注意相关的/sbin,/bin,/usr/sbin,/usr/bin
输出格式说明：S – File size differs
M – Mode differs (permissions)
5 – MD5 sum differs
D – Device number mismatch
L – readLink path mismatch
U – user ownership differs
G – group ownership differs
T – modification time differs
```

7）检查网络

```
[root@bastion-IDC ~]# ip link | grep PROMISC（正常网卡不该在promisc模式，可能存在sniffer）
[root@bastion-IDC ~]# lsof –i 
[root@bastion-IDC ~]# netstat –nap（察看不正常打开的TCP/UDP端口)
[root@bastion-IDC ~]# arp –a
```

8）检查系统计划任务

```
[root@bastion-IDC ~]# crontab –u root –l
[root@bastion-IDC ~]# cat /etc/crontab
[root@bastion-IDC ~]# ls /etc/cron.*
```

9）检查系统后门

```
[root@bastion-IDC ~]# cat /etc/crontab
[root@bastion-IDC ~]# ls /var/spool/cron/
[root@bastion-IDC ~]# cat /etc/rc.d/rc.local
[root@bastion-IDC ~]# ls /etc/rc.d
[root@bastion-IDC ~]# ls /etc/rc3.d
```

10）检查系统服务

```
[root@bastion-IDC ~]# chkconfig —list
[root@bastion-IDC ~]# rpcinfo -p（查看RPC服务）
```

11）检查rootkit

```
[root@bastion-IDC ~]# rkhunter -c
[root@bastion-IDC ~]# chkrootkit -q
```

二、linux系统被入侵/中毒的表象

```
比较常见的中毒表现在以下三个方面：
1）服务器出去的带宽会跑高这个是中毒的一个特征。
因为服务器中毒之后被别人拿去利用，常见的就是拿去当肉鸡攻击别人；再者就是拿你的数据之类的。
所以服务器带宽方面需要特别注意下，如果服务器出去的带宽跑很高，那肯定有些异常，需要及时检查一下！
2）系统里会产生多余的不明的用户
中毒或者被入侵之后会导致系统里产生一些不明用户或者登陆日志，所以这方面的检查也是可以看出一些异常的。
3）开机是否启动一些不明服务和crond任务里是否有一些来历不明的任务？
因为中毒会随系统的启动而启动的，所以一般会开机启动，检查一下启动的服务或者文件是否有异常，一般会在/etc/rc.local 和crondtab -l 显示出来。
```

三、顺便说下一次Linux系统被入侵/中毒的解决过程

```
在工作中碰到系统经常卡，而且有时候远程连接不上，从本地以及远程检查一下这个系统，发现有不明的系统进程。
初步判断就是可能中毒了！！！
解决过程：
1）在监控里检查一下这台服务器的带宽，发现服务器出去的带宽跑很高，所以才会导致远程连接卡甚至连接不上，这是一个原因。
为什么服务器出去的带宽这么高且超出了开通的带宽值？这个原因只能进入服务器系统里检查了。
2）远程进入系统里检查了下， ps -aux查到不明进程 ，立刻关闭它。
3）检查一下开机启动项：#chkconfig --list | grep 3:on 服务器启动级别是3的，我检查一下了开机启动项，没有特别明显的服务。然后检查了一下开机启动的一个文件#more /etc/rc.local看到这个文件里被添加了很多未知项，注释了它。
4）然后在远程连接这台服务器的时候，还是有些卡。检查了一下系统的计划任务crond，使用crondtab -l 命令进行查看，看到很多注释行。这些注释行与/etc/rc.local的内容差不多。最后备份下/var/spool/cron/root文件（也就是root下的crontab计划任务内容），就删除了crontab内容，然后停止crond任务，并chkconfig crond off 禁用它开机启动。
5）为了彻底清除危害，我检查了一下系统的登陆日志（last命令查看），看到除了root用户之外还有其它的用户登陆过。检查了一下/etc/passwd，看到有不明的用户，立刻用usermod -L XXX 禁用这些用户。然后更新了下系统的复杂密码。
```

==============================================================

```
禁用/锁定用户登录系统的方法
1. usermod -L username 锁定用户 usermod -U username 解锁
2. passwd -l username 锁定用户 passwd -u username 解锁
3.修改用户的shell类型为/sbin/nologin（/etc/passwd文件里修改）
4.在/etc/下创建空文件nologin，这样就锁定了除root之外的全部用户
```

四、怎样确保linux系统安全

```
1）从以往碰到的实例来分析，密码太简单是一个错 用户名默认，密码太简单是最容易被入侵的对象，所以切忌不要使用太过于简单的密码，先前碰到的那位客户就是使用了太简单的且规则的密码 1q2w3e4r5t， 这种密码在扫描的软件里是通用的，所以很容易被别人扫描出来的。
2）不要使用默认的远程端口，避免被扫描到扫描的人都是根据端口扫描，然后再进行密码扫描，默认的端口往往就是扫描器的对象，他们扫描一个大的IP 段，哪些开放22端口且认为是ssh服务的linux系统，所以才会猜这机器的密码。更改远程端口也是安全的一个措施！
3）使用一些安全策略进行保护系统开放的端口使用iptables或者配置/etc/hosts.deny 和/etc/hosts.allow进行白名单设置可以对/etc/passwd、/etc/group、/etc/sudoers、/etc/shadow等用户信息文件进行锁定（chattr +ai）
4）禁ping设置# echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
```

====================================================
发现一次服务器被getshell渗透的解决办法：

```
1）使用top命令发现一个python程序占用了95%的cpu
2）使用ps -ef|grep python发现下面程序：python -c import pty;pty.spamn("/bin/sh")这个程序命令表示通过webshell反弹shell回来之后获取真正的ttyshell进行渗透到服务器里。kill掉这个进程！
3）发现在/var/spool/cron下面设置了一个nobody的定时执行上面获取getshell的渗透命令！果断删除这个任务！
4）ss -a发现一个可疑ip以及它的进程，果断在iptables里禁止这个ip的所有请求：  -I INPUT -s 180.125.131.192 -j DROP
```

比如: 在一台服务器上，已经启动了80端口的nginx进程，但是执行“lsof －i:80”或者"ps -ef"命令后，没有任何信息输出！这是为什么？
怀疑机器上的ps命令被人黑了！执行：

```
[root@locahost ~]# which ps/bin/ps
[root@locahost ~]# ls -l /bin/ps-rwxr-xr-x. 1 root root 85304 5月 11 2016 /bin/ps
[root@locahost ~]# stat /bin/ps File: "/bin/ps" Size: 85304    Blocks: 168    IO Block: 4096  普通文件Device: fc02h/64514d  Inode: 13549    Links: 1Access: (0755/-rwxr-xr-x) Uid: (  0/  root)  Gid: (  0/  root)Access: 2017-05-07 17:14:37.862999884 +0800Modify: 2016-05-11 07:23:09.000000000 +0800Change: 2017-05-07 17:14:37.146999967 +0800 发现ps命令的二进制文件果然在近期被改动过。解决办法：可以拷贝别的机器上的/bin/ps二进制文件覆盖本机的这个文件。
```

**=======================记一次Linux操作系统被入侵的排查过程=======================**

```
某天突然发现IDC机房一台测试服务器的流量异常，几乎占满了机房的总带宽，导致其他服务器程序运行业务受阻！意识到了这台测试机被人种了木马，于是开始了紧张的排查过程： 
1）运行ps和top命令发现了两个陌生名称的程序（比如mei34hu）占用了大部分CPU资源，显然这是别人植入的程序！果断尝试kill掉这两个进程，kill后，测试机流量明显降下去。然而不幸的是，不一会儿又恢复了之前的状态。 
2）将IDC这台测试机的外网关闭。远程通过跳板机内网登陆这台机器。 
3）查看这些陌生程序所在路径查找程序路径：ls /proc/进程号/exe，然后再次kill掉进程，又会生成一个新的进程名，发现路径也是随机在PATH变量的路径中变换，有时在/bin目录，有时在/sbin，有时在/usr/bin目录中。看来还有后台主控程序在作怪，继续查找。 
4）尝试查找跟踪程序查看/bin，/sbin，/usr/bin等目录下是否存在以.开头的文件名，发现不少，而且部分程序移除后会自动生成。
[root@localhost ~]# ls /usr/bin/.  //按Tab键补全./ ../ .ssh.hmac 这说明还没找到主控程序。 
5）接着用strace命令跟踪这些陌生程序：
[root@localhost ~]# strace /bin/mei34hu 结果发现在跟踪了这个程序后，它居然自杀了（把自己进程文件干掉了)！然后想用netstat看下网络连接情况，结果居然查不到任何对外的网络连接，于是开始怀疑命令被修改过了。使用stat 查看系统命令ps、ls 、netstat、pstree等等：
[root@localhost ~]# which ps/usr/bin/ps
[root@localhost ~]# which lsalias ls='ls --color=auto'  /usr/bin/ls
[root@localhost ~]# which netstat/usr/bin/netstat
[root@localhost ~]# stat /usr/bin/netstat
[root@localhost ~]# stat /usr/bin/ps
[root@localhost ~]# stat /usr/bin/ls...... 发现修改时间都是在最近的3天内，这让我猛然想起传说中的rootkit用户态级病毒！！有可能是这台测试机刚安装好系统后，设置了root密码为123456，之后又把它放到过公网上被人入侵了。 接着查一下它在相关路径中还放了哪些程序：
[root@localhost ~]# find /bin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /usr/bin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /use/sbin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /sbin -mtime -3 -type f | xargs rm -f 将上面查找出的3天前的程序统统都删掉，并强制断电，重启服务器！然而可恨的是这些程序在机器重启后又好端端的运行以来！很明显，这些程序都被设置了开机自启动 
6）查看系统启动项[root@localhost ~]# find /etc/rc.d/ -mtime -3 ! -type d 果然这些程序都被设置了开机自启动。于是，就再来一次删除，然后暴力重启服务器。
[root@localhost ~]# find /bin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /usr/bin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /use/sbin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /sbin -mtime -3 -type f | xargs rm -f
[root@localhost ~]# find /etc/rc.d/ -mtime -3 ! -type d | xargs rm -f 重启完服务器后，用top命令查看，系统CPU使用率也不高了。居然这样就被干掉了。 7）顾虑到系统常用命令中（如ls，ps等）可能会隐藏启动进程，这样一旦执行又会拉起木马程序。于是再查看下系统中是否创建了除root以外的管理员账号：[root@localhost ~]# awk -F":" '{if($3 == 0) print $1}' /etc/passwdroot 结果发现只输入了root这一个用户，说明系统用户是正常的。其实，当系统被感染rootkit后，系统已经变得不可靠了，唯一的办法就是重装系统了。 
8）对于一些常用命令程序的修复思路：找出常用命令所在的rpm包，然后强制删除，最后在通过yum安装（由于外网已拿掉，可以通过squid代理上网的yum下载）[root@localhost ~]# rpm -qf /bin/ps
[root@localhost ~]# rpm -qf /bin/ls
[root@localhost ~]# rpm -qf /bin/netstat
[root@localhost ~]# rpm -qf /usr/bin/pstree 然后将上面命令查找出来的rpm包强制卸载
[root@localhost ~]# rpm -e --nodeps ......[root@localhost ~]# rpm -e --nodeps ......[root@localhost ~]# rpm -e --nodeps ......[root@localhost ~]# rpm -e --nodeps ...... 接着再重新安装
[root@localhost ~]# yum install -y procps coreutils net-tools psmisc 最后重启下系统即可。
除了上面这次排查之外，还可以：
1）结合服务器的系统日志/var/log/messages、/var/log/secure进行仔细检查。
2）将可疑文件设为不可执行，用chattr +ai将几个重要目录改为不可添加和修改，再将进程杀了，再重启
3）chkrootkit之类的工具查一下 对于以上这些梳理的木马排查的思路要清楚，排查手段要熟练。遇到问题不要慌，静下心，细查系统日志，根据上面的排查思路来一步步处理，这样Hacker就基本"投降"了~~~
```

=====================针对一些linux应用漏洞, 做出的必要修改 (应用版本信息隐藏等)===================
1) 关闭Apache服务器的TRACE请求, 或是禁止远端WWW服务支持TRACE请求

```
TRACE_Method是HTTP（超文本传输）协议定义的一种协议调试方法，该方法会使服务器原样返回任意客户端请求的任何内容。TRACE和TRACK是用来调试web服务器连接的HTTP方式。支持该方式的服务器存在跨站脚本漏洞，通常在描述各种浏览器缺陷的时候，把"Cross-Site-Tracing"简称为XST。攻击者可以利用此漏洞欺骗合法用户并得到他们的私人信息。 1) 虚拟主机用户可以在.htaccess文件中添加如下代码过滤TRACE请求:RewriteEngine onRewriteCond %{REQUEST_METHOD} ^(TRACE|TRACK)RewriteRule .* - [F] 2) 服务器用户在httpd.conf尾部添加如下指令后重启apache即可:TraceEnable off
```

2) 隐藏apache的版本(banner信息). 一些应用的banner信息，容易让黑客更快的匹配到漏洞信息，所以隐藏起来可以提升一定的安全性。

```
在apache的http.conf中添加或修改成如下二条代码即可：ServerSignature OffServerTokens Prod 经过以上修改，可以隐藏一些 banner. 但是用wget -S和curl -I还是可以看到apache字样! 彻底伪装的话需要修改源文件:
[root@localhost include]# pwd/usr/local/src/httpd-2.4.37/include
[root@localhost include]# ll ap_release.h-rw-r--r-- 1 root dip 3144 Oct 18 22:33 ap_release.h 编辑ap_release.h文 件，修改#define AP_SERVER_BASEPRODUCT "Apache"为#define AP_SERVER_BASEPRODUCT "Microsoft-IIS/5.0" 
[root@localhost httpd-2.4.37]# pwd/usr/local/src/httpd-2.4.37
[root@localhost httpd-2.4.37]# ll ./os/unix/os.h-rw-r--r-- 1 root dip 1668 Sep 24 2011 ./os/unix/os.h 编辑os/unix/os.h文 件修改#define PLATFORM "Unix"为#define PLATFORM "Win64" 最后再重新编译apache
```

3) 隐藏php的版本

```
在php的php.ini中添加或修改成如下一条代码即可：expose_php = Off
```

4) 隐藏openssh版本

```
[root@localhost ~]# telnet 172.16.60.207 22Trying 172.16.60.207...Connected to 172.16.60.207.Escape character is '^]'.SSH-2.0-OpenSSH_7.6 如上, 可以看到openssh版本泄露了. 下面介绍下隐藏openssh版本的方法: 找到openssh的解压目录
[root@localhost ~]# cd /usr/local/src/openssh-7.6p1[root@localhost openssh-7.6p1]# cat version.h/* $OpenBSD: version.h,v 1.80 2017/09/30 22:26:33 djm Exp $ */ #define SSH_VERSION   "OpenSSH_7.6" #define SSH_PORTABLE  "p1"#define SSH_RELEASE   SSH_VERSION SSH_PORTABLE 修改 #define SSH_VERSION   "OpenSSH_7.6" 这一行, 比如修改为"#define SSH_VERSION   "OpenSSH""接着进行编译安装即可
```

5) 隐藏ssh版本

```
修改SSH登录时的Banner信息 首先创建一个文件, 用于ssh登录后的banner信息提示, 提示内容可以自行定义
[root@localhost ~]# touch /etc/ssh_banner_change
[root@localhost ~]# echo "welcome to login this server:172.16.60.207" > /etc/ssh_banner_change
[root@localhost ~]# cat /etc/ssh_banner_changewelcome to login this server:172.16.60.207 接着修改SSH配置文件中的banner文件路径[root@localhost ~]# vim /etc/ssh/sshd_config#Banner noneBanner /etc/ssh_banner_change 然后重启ssh服务
[root@localhost ~]# /etc/init.d/sshd restartStopping sshd:                       [ OK ]Starting sshd:                       [ OK ] 这样, 在远程登录这台机器, 就会看到定义的banner信息了
```

6) 隐藏Proftpd版本信息

```
修改proftpd的配置文件：
1) 伪装登入欢迎信息修改ServerIdent on "Serv-U FTP Server v5.0 for WinSock ready...\"或ServerIdent off 如上配置后, telnet proftpd端口后会显示：220 ::ffff:192.168.2.3 FTP server ready 2) 伪装banner信息DisplayLogin [msgfile] DisplayConnect [msgfile]
```

7) 隐藏vsftpd版本信息

```
配置文件：vsftpd.conf 修改 ftpd_banner=welcome to this FTP server
```

8) 隐藏Nginx版本信息

```
在nginx.conf 的 http区域里头加入 server_tokens 的参数server_tokens off; 如果想要彻底屏敝, 则需要修改源码
[root@uatclient-node01 core]# pwd/data/software/nginx-1.12.2/src/core
[root@uatclient-node01 core]# ll nginx.h-rw-r--r-- 1 ambari-qa 1001 476 Oct 17 2017 nginx.h 找到#define nginx_version      1012002#define NGINX_VERSION   "1.12.2"#define NGINX_VER       "nginx/" NGINX_VERSION 把上面三行内容 伪装成其他信息, 如下#define nginx_version      1111111#define NGINX_VERSION   "0.0000"#define NGINX_VER       "nginx/" NGINX_VERSION 然后再次编辑即可
```

9) TTL

```
用以下命令修改Linux的TTL基数为128（默认为64）
[root@uatclient-node01 core]# cat /proc/sys/net/ipv4/ip_default_ttl64
[root@uatclient-node01 core]# echo "128" > /proc/sys/net/ipv4/ip_default_ttl
[root@uatclient-node01 core]# cat /proc/sys/net/ipv4/ip_default_ttl    128 还可以在内核参数里修改
[root@uatclient-node01 core]# vim /etc/sysctl.confnet.ipv4.ip_default_ttl = 128[root@uatclient-node01 core]# sysctl -p
```



1）检查系统日志

```
检查系统错误登陆日志，统计IP重试次数（last命令是查看系统登陆日志，比如系统被reboot或登陆情况）
[root@bastion-IDC ~]# last
```