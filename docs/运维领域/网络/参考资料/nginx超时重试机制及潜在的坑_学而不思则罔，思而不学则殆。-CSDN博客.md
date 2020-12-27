**问题描述：**

有一个发送短信的http服务，客户端调用之后，只有一次请求，但是发了三次短信。

**分析：**

   1、客户端仅发起了一次请求，

   2、服务端收到了三次请求

   3、三次请求分别落在了三台后端机器上。每台后端机器仅收到一次请求

**基本的架构如下：**

![img](nginx超时重试机制及潜在的坑_学而不思则罔，思而不学则殆。-CSDN博客.assets/20180913120751398)

**分析及解决:**

   分析代码，代码中没有重试机制，并且通过请求分布来看，并不是一台机器处理了三次，而是每台机器处理了一次。所以分析，可能是由于nginx转发导致。 

   查看接口的响应时间，发现每个接口的响应时间为18s左右（PS：由于是调用外部接口，此调用时间属于正常的时间。。。）。

   猜测是由于后端服务器未能及时返回数据，导致了nginx的超时重试机器，将请求分发到了另外一台机器上。

   查看nginx的配置文件，发现如下配置：

   

proxy_next_upstream http_502 http_504 error timeout invalid_header;

   上面的配置表示，如果后端服务器如下情况，将会把请求转发到下一台后端服务器上。

- error - 在连接到一个服务器，发送一个请求，或者读取应答时发生错误。
- timeout - 在连接到服务器，转发请求或者读取应答时发生超时。
- invalid_header - 服务器返回空的或者错误的应答。
- http_502 - 服务器返回502代码。
- http_504 - 服务器返回504代码。

 继续查看超时时间  

proxy_read_timeout 15;

超时时间为15s，所以后端服务器响应慢，nginx没有在15s内收到返回的数据，所以将请求切换到下一台后端机器了，所以，同样的情况下， 请求第二台后端机器时，也没有在规定的时间内得到响应，所以又切换到第三台机器了，最终导致短信发送了三次。 

 

几个参数说明：

 

proxy_send_timeout   后端服务器数据回传时间(代理发送超时时间)

proxy_read_timeout    连接成功后，后端服务器响应时间(代理接收超时时间)

proxy_connect_timeout   nginx连接后端的超时时间，一般不超过75s

如何解决呢？

   1、第一种办法：因为后端机器无法再进行优化减少响应时间，所以可以更改nginx的超时时间，将原本的15s更改为40s，这样可以保证结果正常返回。

   2、第二种办法 ：关闭自动切换到下台机器的功能，即将proxy_next_upstream配置为off。但是这样虽然能解决问题，但是会导致nginx的容错能力下降。

   3、第三种办法：从业务角度出发，本质上我们是需要只发一次短信的。 所以可以采用分布式锁的方式解决。

以上现象还可能出现在以下的场景：

1、上传excel，然后服务端处理excel内容，插入到db里面的时候，可能存在多次转发导致数据重复。

2、post请求处理时间过长，可能出现重复提交的问题。

 

几篇文章：（介绍nginx的proxy的机制等）

http://saiyaren.iteye.com/blog/1914865

https://my.oschina.net/greki/blog/109643

http://blog.csdn.net/mj158518/article/details/49847119

https://my.oschina.net/xsh1208/blog/199674

http://nginx.org/en/docs/http/ngx_http_proxy_module.html

http://blog.csdn.net/liujiyong7/article/details/18228915

http keepalive的解释

http://www.nowamagic.net/academy/detail/23350305