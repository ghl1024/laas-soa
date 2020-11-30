# 10条Linux命令锦囊，防你牢底坐穿

[xjjdog.cn](http://xjjdog.cn/) 对200+原创文章进行了细致的分类，阅读更流畅，欢迎收藏。

> 原创：小姐姐味道（微信公众号ID：xjjdog），欢迎分享，转载请保留出处。任何不保留此声明的转载都是抄袭。

每一年，都会有删库跑路的新闻。现实中，删库容易，跑路难，从业者充满了泪水。

这些动作里面，并不总是存在主观的恶意，而是这些命令太危险了。线上操作时，一定要保持清醒的头脑，切记马虎大意。

你说你误操作的，谁信呢？

切记：

- 严禁酒后登录线上服务器操作
- 严禁吵架后情绪激动登录线上服务器操作
- 严禁长时间加班后操作线上环境
- 禁止在线上试验不熟悉的命令
- 重要系统先做备份

## 1. 准备工作

在执行危险命令时，请深呼吸。首先执行`ifconfig`，或者`ip addr`命令，确认是在正确的服务器上。

```python
$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:16:3e:34:e9:a9 brd ff:ff:ff:ff:ff:ff
    inet 172.19.26.39/20 brd 172.19.31.255 scope global dynamic noprefixroute eth0
       valid_lft 313267185sec preferred_lft 313267185sec
    inet6 fe80::216:3eff:fe34:e9a9/64 scope link
       valid_lft forever preferred_lft forever
复制代码
```

这时候，再次深呼吸，然后执行`pwd`命令，确保自己是在正确的目录下面。

```bash
$ pwd
/etc/nginx
复制代码
```

接下来，就可以看一下执行的命令，是不是危险指令。

## 2. rm -rf命令

`-rf`参数将递归删除文件，误删文件导致数据丢失，产生严重后果。如果多一个空格，或者 `/`没有补齐，或者文件有特殊符号，导致误删文件的误操作居多。

```bash
rm -rf ./* => rm -rf /
rm -rf abc/ => rm -rf abc /
复制代码
```

执行rm命令，手速一定要慢。按<tab>补全，一定要等屏幕回显后操作。

另外，在脚本中，rm的坑也不小，比如：

```bash
rm -rf ${p}/*
复制代码
```

如果p变量没有设置，就会是灾难性的后果，命令等同于`rm -rf /`。所以rm还有另外一条谨言：在脚本中执行rm的时候，请先判断相关的变量是否为空。

## 3. chmod命令

chmod是更改目录和文件权限用的，如果处理不当，会产生和rm一样的后果。

这里介绍一种非常霸道的恢复方法。在执行这个命令之前，先把所有文件的权限备份一下。这里用到`getfacl`这个命令。

```bash
getfacl -R / > chmod.txt 
复制代码
```

恢复的时候，执行

```bash
setfacl --restore=chmod.txt
复制代码
```

它将回放这个文件的权限，有时候是救命的。

## 4. cat命令

cat命令也能出错？是的，而且还很严重，因为你掌握了高级技能：重定向符。

如果你想要向文件中`追加` 内容，会使用 `cat >> file`的方式，如果你不小心少输入了一个`>`，那么不好意思，你的文件内容就丢失了。

类似的命令还有`echo`等，可以看到，问题不在cat，在重定向符，太容易写错。

在此，请你操作之前，确保每次深呼吸，数好箭头的个数再操作。

## 5. dd命令

`dd`命令很酷，和`xjjdog`的`jj`遥相呼应。命令如下：

```bash
dd if=/dev/zero of=/dev/sda bs=512 count=1
复制代码
```

以上命令，用于格式化硬盘，如果你的剪贴板里面有这样的命令，而且不小心粘到了命令行里，你的数据将会蒸发。

## 6. cp命令

cp命令会产生覆盖，如果你后悔了，想找到原文件，将非常困难。

建议增加`alias cp ='cp -i'`，i参数表示会在拷贝时生成一个备份。大多数时候没用，有时候很有用。

和我们买保险一个道理。

mv命令类似，也可以加上-i。

## 7. tar命令

不要觉得tar很安全，我就曾经因为tar命令丢失过数据。

第一，tar -xf 解压的时候， 如果解压的文件已经在当前目录，覆盖原有的文件夹及文件。`覆盖`这两个字，很多时候意味着不安全。

## 8. vim命令

vim容易在打开大文件的时候，造成系统内存占用过高。如果触发了操作系统的`oom-killer`，将会造成其他正常进程的死亡。

如果你手速过快，执行了`:wq`，将会造成文件的不一致甚至损坏。

可是使用`less`或者`more`这样的命令，来查看信息。更高效，也更安全。

如果你实在不得不用vim，请保持使用`view`命令，它是vim的只读模式。

## 9. mkfs.*

类似于mkfs.ext4这种指令，将会格式化硬盘，一般用于线上环境初始化，否则不要执行。

## 10. MySQL

（1）使用mysql -U

```
--safe-updates, --i-am-a-dummy, -U
复制代码
```

使用`mysql -U` 防止`delete`、`update `执行没带where条件的操作。当发出没有WHERE或LIMIT关键字的UPDATE或DELETE时，mysql程序拒绝执行。

alias同样是我们的好帮手，可以这么设置：

```bash
alias mysql='mysql -U'
复制代码
```

（2）重要操作时，使用事务

```sql
start transaction
执行
确认
commit
复制代码
```

（3）DML误操作回滚，可以使用`binlog2sql`

（4）小心DDL操作

DDL往往意味着巨大的坑，锁表、误删、数据转变，往往是灾难性的。DDL 对整个表进行操作，或者是整个表所有的行、列，产生exclusive锁，产生疯狂io、严重影响生产。

这里面的任何一条，都是要命的。

仔细检查DDL，尽量在业务低峰执行，而且尽量采用`inplace`方式操作。

# End

线上值万金，执行需谨慎。小心驶得万年船，在危险的线上环境，做事追求的不是快，而是稳。

毕竟，成熟的公司，光审批阶段就耗了好几天，你又为啥这么在乎这几秒钟呢？