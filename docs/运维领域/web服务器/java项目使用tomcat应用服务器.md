java项目如果使用tomcat应用服务器

在监控方面有很大的优势, 指标中直接包含session信息, 该session信息直接对应到java应用服务器的连接数, 对session进行告警有很大帮助

改动如下:

注释掉其他应用服务器

不排除tomcat

```
        <!-- 添加 Undertow内置容器依赖 -->
<!--        <dependency>-->
<!--            <groupId>org.springframework.boot</groupId>-->
<!--            <artifactId>spring-boot-starter-undertow</artifactId>-->
<!--        </dependency>-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <!-- 排除Tomcat依赖 -->
<!--            <exclusions>-->
<!--                <exclusion>-->
<!--                    <groupId>org.springframework.boot</groupId>-->
<!--                    <artifactId>spring-boot-starter-tomcat</artifactId>-->
<!--                </exclusion>-->
<!--            </exclusions>-->
        </dependency>
```

