## README.md

# JumpServer 多云环境下更好用的堡垒机

[![Python3](jumpserverjumpserver JumpServer 是全球首款开源的堡垒机，是符合 4A 的专业运维安全审计系统。.assets/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e362d677265656e2e7376673f7374796c653d706c6173746963)](https://www.python.org/) [![Django](jumpserverjumpserver JumpServer 是全球首款开源的堡垒机，是符合 4A 的专业运维安全审计系统。.assets/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d322e322d627269676874677265656e2e7376673f7374796c653d706c6173746963)](https://www.djangoproject.com/) [![Docker Pulls](jumpserverjumpserver JumpServer 是全球首款开源的堡垒机，是符合 4A 的专业运维安全审计系统。.assets/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f6a756d707365727665722f6a6d735f616c6c2e737667)](https://hub.docker.com/u/jumpserver)

- [ENGLISH](https://github.com/jumpserver/jumpserver/blob/master/README_EN.md)

## 紧急BUG修复通知

JumpServer发现远程执行漏洞，请速度修复

**影响版本:**

```
< v2.6.2
< v2.5.4
< v2.4.5 
= v1.5.9
>= v1.5.3
```

**安全版本:**

```
>= v2.6.2
>= v2.5.4
>= v2.4.5 
= v1.5.9 （版本号没变）
< v1.5.3
```

**修复方案:**

将JumpServer升级至安全版本；

**临时修复方案:**

修改 Nginx 配置文件屏蔽漏洞接口

```
/api/v1/authentication/connection-token/
/api/v1/users/connection-token/
```

Nginx 配置文件位置

```
# 社区老版本
/etc/nginx/conf.d/jumpserver.conf

# 企业老版本
jumpserver-release/nginx/http_server.conf
 
# 新版本在 
jumpserver-release/compose/config_static/http_server.conf
```

修改 Nginx 配置文件实例

```
### 保证在 /api 之前 和 / 之前
location /api/v1/authentication/connection-token/ {
   return 403;
}
 
location /api/v1/users/connection-token/ {
   return 403;
}
### 新增以上这些
 
location /api/ {
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://core:8080;
  }
 
...
```

修改完成后重启 nginx

```
docker方式: 
docker restart jms_nginx

nginx方式:
systemctl restart nginx
```

**修复验证**

```
$ wget https://github.com/jumpserver/jumpserver/releases/download/v2.6.2/jms_bug_check.sh 

# 使用方法 bash jms_bug_check.sh HOST 
$ bash jms_bug_check.sh demo.jumpserver.org
漏洞已修复
```

**入侵检测**

下载脚本到 jumpserver 日志目录，这个目录中存在 gunicorn.log，然后执行

```
$ pwd
/opt/jumpserver/core/logs

$ ls gunicorn.log 
gunicorn.log

$ wget 'https://github.com/jumpserver/jumpserver/releases/download/v2.6.2/jms_check_attack.sh'
$ bash jms_check_attack.sh
系统未被入侵
```

------

JumpServer 正在寻找开发者，一起为改变世界做些贡献吧，哪怕一点点，联系我 [ibuler@fit2cloud.com](mailto:ibuler@fit2cloud.com)

JumpServer 是全球首款开源的堡垒机，使用 GNU GPL v2.0 开源协议，是符合 4A 规范的运维安全审计系统。

JumpServer 使用 Python / Django 为主进行开发，遵循 Web 2.0 规范，配备了业界领先的 Web Terminal 方案，交互界面美观、用户体验好。

JumpServer 采纳分布式架构，支持多机房跨区域部署，支持横向扩展，无资产数量及并发限制。

改变世界，从一点点开始。

> 注: [KubeOperator](https://github.com/KubeOperator/KubeOperator) 是 JumpServer 团队在 Kubernetes 领域的的又一全新力作，欢迎关注和使用。

## 特色优势

- 开源: 零门槛，线上快速获取和安装；
- 分布式: 轻松支持大规模并发访问；
- 无插件: 仅需浏览器，极致的 Web Terminal 使用体验；
- 多云支持: 一套系统，同时管理不同云上面的资产；
- 云端存储: 审计录像云端存储，永不丢失；
- 多租户: 一套系统，多个子公司和部门同时使用；
- 多应用支持: 数据库，Windows远程应用，Kubernetes。

## 版本说明

自 v2.0.0 发布后， JumpServer 版本号命名将变更为：v大版本.功能版本.Bug修复版本。比如：

```
v2.0.1 是 v2.0.0 之后的Bug修复版本；
v2.1.0 是 v2.0.0 之后的功能版本。
```

像其它优秀开源项目一样，JumpServer 每个月会发布一个功能版本，并同时维护 3 个功能版本。比如：

```
在 v2.4 发布前，我们会同时维护 v2.1、v2.2、v2.3；
在 v2.4 发布后，我们会同时维护 v2.2、v2.3、v2.4；v2.1 会停止维护。
```

## 功能列表

| 身份认证 Authentication                                      | 登录认证                                           | 资源统一登录与认证                                       |
| ------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------------------------- |
| LDAP/AD 认证                                                 |                                                    |                                                          |
| RADIUS 认证                                                  |                                                    |                                                          |
| OpenID 认证（实现单点登录）                                  |                                                    |                                                          |
| CAS 认证 （实现单点登录）                                    |                                                    |                                                          |
| MFA认证                                                      | MFA 二次认证（Google Authenticator）               |                                                          |
| RADIUS 二次认证                                              |                                                    |                                                          |
| 登录复核（X-PACK）                                           | 用户登录行为受管理员的监管与控制                   |                                                          |
| 账号管理 Account                                             | 集中账号                                           | 管理用户管理                                             |
| 系统用户管理                                                 |                                                    |                                                          |
| 统一密码                                                     | 资产密码托管                                       |                                                          |
| 自动生成密码                                                 |                                                    |                                                          |
| 自动推送密码                                                 |                                                    |                                                          |
| 密码过期设置                                                 |                                                    |                                                          |
| 批量改密（X-PACK）                                           | 定期批量改密                                       |                                                          |
| 多种密码策略                                                 |                                                    |                                                          |
| 多云纳管（X-PACK）                                           | 对私有云、公有云资产自动统一纳管                   |                                                          |
| 收集用户（X-PACK）                                           | 自定义任务定期收集主机用户                         |                                                          |
| 密码匣子（X-PACK）                                           | 统一对资产主机的用户密码进行查看、更新、测试操作   |                                                          |
| 授权控制 Authorization                                       | 多维授权                                           | 对用户、用户组、资产、资产节点、应用以及系统用户进行授权 |
| 资产授权                                                     | 资产以树状结构进行展示                             |                                                          |
| 资产和节点均可灵活授权                                       |                                                    |                                                          |
| 节点内资产自动继承授权                                       |                                                    |                                                          |
| 子节点自动继承父节点授权                                     |                                                    |                                                          |
| 应用授权                                                     | 实现更细粒度的应用级授权                           |                                                          |
| MySQL 数据库应用、RemoteApp 远程应用（X-PACK）               |                                                    |                                                          |
| 动作授权                                                     | 实现对授权资产的文件上传、下载以及连接动作的控制   |                                                          |
| 时间授权                                                     | 实现对授权资源使用时间段的限制                     |                                                          |
| 特权指令                                                     | 实现对特权指令的使用（支持黑白名单）               |                                                          |
| 命令过滤                                                     | 实现对授权系统用户所执行的命令进行控制             |                                                          |
| 文件传输                                                     | SFTP 文件上传/下载                                 |                                                          |
| 文件管理                                                     | 实现 Web SFTP 文件管理                             |                                                          |
| 工单管理（X-PACK）                                           | 支持对用户登录请求行为进行控制                     |                                                          |
| 组织管理（X-PACK）                                           | 实现多租户管理与权限隔离                           |                                                          |
| 安全审计 Audit                                               | 操作审计                                           | 用户操作行为审计                                         |
| 会话审计                                                     | 在线会话内容审计                                   |                                                          |
| 历史会话内容审计                                             |                                                    |                                                          |
| 录像审计                                                     | 支持对 Linux、Windows 等资产操作的录像进行回放审计 |                                                          |
| 支持对 RemoteApp（X-PACK）、MySQL 等应用操作的录像进行回放审计 |                                                    |                                                          |
| 指令审计                                                     | 支持对资产和应用等操作的命令进行审计               |                                                          |
| 文件传输                                                     | 可对文件的上传、下载记录进行审计                   |                                                          |
| 数据库审计 Database                                          | 连接方式                                           | 命令方式                                                 |
| Web UI方式 (X-PACK)                                          |                                                    |                                                          |
| 支持的数据库                                                 | MySQL                                              |                                                          |
| Oracle (X-PACK)                                              |                                                    |                                                          |
| MariaDB (X-PACK)                                             |                                                    |                                                          |
| PostgreSQL (X-PACK)                                          |                                                    |                                                          |
| 功能亮点                                                     | 语法高亮                                           |                                                          |
| SQL格式化                                                    |                                                    |                                                          |
| 支持快捷键                                                   |                                                    |                                                          |
| 支持选中执行                                                 |                                                    |                                                          |
| SQL历史查询                                                  |                                                    |                                                          |
| 支持页面创建 DB, TABLE                                       |                                                    |                                                          |
| 会话审计                                                     | 命令记录                                           |                                                          |
| 录像回放                                                     |                                                    |                                                          |

## 快速开始

- [极速安装](https://docs.jumpserver.org/zh/master/install/setup_by_fast/)
- [完整文档](https://docs.jumpserver.org/)
- [演示视频](https://www.bilibili.com/video/BV1ZV41127GB)

## 组件项目

- [Lina](https://github.com/jumpserver/lina) JumpServer Web UI 项目
- [Luna](https://github.com/jumpserver/luna) JumpServer Web Terminal 项目
- [Koko](https://github.com/jumpserver/koko) JumpServer 字符协议 Connector 项目，替代原来 Python 版本的 [Coco](https://github.com/jumpserver/coco)
- [Guacamole](https://github.com/jumpserver/docker-guacamole) JumpServer 图形协议 Connector 项目，依赖 [Apache Guacamole](https://guacamole.apache.org/)

## 致谢

- [Apache Guacamole](https://guacamole.apache.org/) Web页面连接 RDP, SSH, VNC协议设备，JumpServer 图形化连接依赖
- [OmniDB](https://omnidb.org/) Web页面连接使用数据库，JumpServer Web数据库依赖

## JumpServer 企业版

- [申请企业版试用](https://jinshuju.net/f/kyOYpi)

> 注：企业版支持离线安装，申请通过后会提供高速下载链接。

## 案例研究

- [JumpServer 堡垒机护航顺丰科技超大规模资产安全运维](https://blog.fit2cloud.com/?p=1147)；
- [JumpServer 堡垒机让“大智慧”的混合 IT 运维更智慧](https://blog.fit2cloud.com/?p=882)；
- [携程 JumpServer 堡垒机部署与运营实战](https://blog.fit2cloud.com/?p=851)；
- [小红书的JumpServer堡垒机大规模资产跨版本迁移之路](https://blog.fit2cloud.com/?p=516)；
- [JumpServer堡垒机助力中手游提升多云环境下安全运维能力](https://blog.fit2cloud.com/?p=732)；
- [中通快递：JumpServer主机安全运维实践](https://blog.fit2cloud.com/?p=708)；
- [东方明珠：JumpServer高效管控异构化、分布式云端资产](https://blog.fit2cloud.com/?p=687)；
- [江苏农信：JumpServer堡垒机助力行业云安全运维](https://blog.fit2cloud.com/?p=666)。

## 安全说明

JumpServer是一款安全产品，请参考 [基本安全建议](https://docs.jumpserver.org/zh/master/install/install_security/) 部署安装.

如果你发现安全问题，可以直接联系我们：

- [ibuler@fit2cloud.com](mailto:ibuler@fit2cloud.com)
- [support@fit2cloud.com](mailto:support@fit2cloud.com)
- 400-052-0755

## License & Copyright

Copyright (c) 2014-2020 飞致云 FIT2CLOUD, All rights reserved.

Licensed under The GNU General Public License version 2 (GPLv2) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-2.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.