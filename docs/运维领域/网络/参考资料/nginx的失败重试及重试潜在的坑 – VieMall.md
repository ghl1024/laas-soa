 [Leave a Comment](http://www.dczou.com/viemall/603.html#comments)

 Updated on 十一月 19, 2017

# nginx的失败重试及重试潜在的坑

by [Tony](http://www.dczou.com/viemall/author/admin)



 本章章节:

  1.怎么配置nginx的失败重试;

  \2. Nginx 失败重试潜在的坑;

现在对外服务的网站，很少只使用一个服务节点，而是部署多台服务器，上层通过一定机制保证容错和负载均衡。

 nginx就是常用的一种HTTP和反向代理服务器，支持容错和负载均衡。

 nginx的重试机制就是容错的一种。



 主要有两部分配置: upstream server 和proxy_pass

```
 ``upstream backend {``   ``server ``127.0``.``0.1``:``8081` `max_fails=``2` `fail_timeout=10s weight=``1``;``   ``server ``127.0``.``0.1``:``8082` `max_fails=``2` `fail_timeout=10s weight=``1``;`` ``}
```

  通过配置上有服务器的max_fails 和fail_timeout，来指定每个上有服务器，当fail_timeout时间内失败了max_fails次请求，则认为该上游服务器不可用/不存活，然后会摘掉该上有服务器，fail_timeout时间后会再次将该服务器加入到存活上有服务器列表进行重试.

在nginx的配置文件中，proxy_next_upstream项定义了什么情况下进行重试，官网文档中给出的说明如下：



```
1``.Syntax: proxy_next_upstream error | timeout | invalid_header ``  ``| http_500 | http_502 | http_503 | http_504 | http_403 | http_404 | off ...; ``2``.Default:  proxy_next_upstream error timeout; ``3``.Context:  http, server, location
```

  默认情况下，当请求服务器发生错误或超时时，会尝试到下一台服务器。

  还有一个参数影响了重试的次数：proxy_next_upstream_tries，官方文档中给出的说明如下：



```
1``.Syntax: proxy_next_upstream_tries number; ``2``.Default:  proxy_next_upstream_tries ``0``; ``3``.Context:  http, server, location ``4``.This directive appeared in version ``1.7``.``5``.
```

具体配置:



```
upstream backend_server {``  ``server ``192.168``.``61.1``:``9080` `max_fails=``2` `fail_timeout=10s weight=``1``;``  ``server ``192.168``.``61.1``:``9090` `max_fails=``2` `fail_timeout=10s weight=``1``;``}
```



```
server {``  ``……``  ``location /test {``    ``proxy_connect_timeout 5s;``    ``proxy_read_timeout 5s;``    ``proxy_send_timeout 5s;``    ``proxy_next_upstream error timeout;``    ``proxy_next_upstream_timeout ``0``;``    ``proxy_next_upstream_tries ``0``;``    ``proxy_pass http:``//backend_server;``    ``add_header upstream_addr $upstream_addr;``  ``}``}
```



  backend_server定义了两个上游服务器192.168.61.1:9080（返回hello）和192.168.61.1:9090（返回hello2）。

  如上指令主要有三组配置：网络连接/读/写超时设置、失败重试机制设置、upstream存活超时设置。

  网络连接/读/写超时设置。

  • proxy_connect_timeout time：与后端/上游服务器建立连接的超时时间，默认为60s，此时间不超过5s。

  • proxy_read_timeout time：设置从后端/上游服务器读取响应的超时时间，默认为60s，此超时时间指的是两次成功读操作间隔时间，而不是读取整个响应体的超时时间，如果在此超时时间内上游服务器没有发送任何响应，则Nginx关闭此连接。

  • proxy_send_timeout time：设置往后端/上游服务器发送请求的超时时间，默认为60s，此超时时间指的是两次成功写操作间隔时间，而不是发送     整个请求的超时时间，如果在此超时时间内上游服务器没有接收任何响应，则Nginx关闭此连接。

  对于内网高并发服务，请根据需要调整这几个参数，比如内网服务TP999为1s，可以将连接超时设置为100~500毫秒，而读超时可以为1.5~3秒左右。

  失败重试机制设置。

   proxy_next_upstream error | timeout | invalid_header | http_500 | http_502 | http_503 | http_504 |http_403 | http_404 |   non_idempotent | off …：配置什么情况下需要请求下一台上游服务器进行重试。默认为“errortimeout”。error表示与上游服务器建立连接、写请求或者读响应头出错。

   timeout表示与上游服务器建立连接、写请求或者读响应头超时。invalid_header表示上游服务器返回空的或错误的响应头。      

   http_XXX表示上游服务器返回特定的状态码。

​    non_idempotent表示RFC-2616定义的非幂等HTTP方法（POST、LOCK、PATCH），也可以在失败后重试下一台上游服务器（即默认幂等方法GET、HEAD、PUT、DELETE、OPTIONS、TRACE才可以重试）。

​    off表示禁用重试。

重试不能无限制进行，因此，需要如下两个指令控制重试次数和重试超时时间。

​     • proxy_next_upstream_tries number：设置重试次数，默认0表示不限制，注意此重试次数指的是所有请求次数（包括第一次和之后的重试次数之和）。

​    • proxy_next_upstream_timeout time：设置重试最大超时时间，默认0表示不限制。

   即在proxy_next_upstream_timeout时间内允许proxy_next_upstream_tries次重试。如果超过了其中一个设置，则Nginx也会结束重试并返回客户端响应（可能是错误码）。

   如下配置表示当error/timeout时重试upstream中的下一台上游服务器，如果重试的总时间超出了6s或者重试了1次，则表示重试失败（因为之前已经请求一次了，所以还能重试一次），Nginx结束重试并返回客户端响应。

​    proxy_next_upstream error timeout;

​    proxy_next_upstream_timeout 6s;

​    proxy_next_upstream_tries 2;

  不了解这个机制，在日常开发web服务的时候，就可能会踩坑。

​    比如有这么一个场景：  一个用于导入数据的web页面，上传一个excel，通过读取、处理excel，向数据库中插入数据，处理时间较长（如1分钟），且为同步操作（即处理完成后才返回结果）。暂且不论这种方式的好坏，若nginx配置的响应等待时间（proxy_read_timeout）为30秒，就会触发超时重试，将请求又打到另一台。如果处理中没有考虑到重复数据的场景，就会发生数据多次重复插入！ 或者发送短信的业务功能,发送的业务时间超时，也会引起发送了多条的短信信息；

   [ << nginx超时重试机制及潜在的坑>>](https://www.dutycode.com/nginx_chongshi_chongfuqingqiu.html)

   [<>](http://blog.csdn.net/jackpk/article/details/54632468)