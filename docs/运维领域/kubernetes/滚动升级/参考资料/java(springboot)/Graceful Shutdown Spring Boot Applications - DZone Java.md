# Graceful Shutdown Spring Boot Applications

### Want to find out how to gracefully shutdown your Spring Boot apps? Click here to learn more about shutting down Spring Boot apps and installing newer versions.

[![Marcos Barbero user avatar](Graceful Shutdown Spring Boot Applications - DZone Java.assets/thumbnail) ](https://dzone.com/users/3221114/marcosbarbero.html)by 

[Marcos Barbero](https://dzone.com/users/3221114/marcosbarbero.html)

 

 CORE ·

 Jul. 10, 18 · [Java Zone ](https://dzone.com/java-jdk-development-tutorials-tools-news)· Tutorial

 Like [(33)](https://dzone.com/articles/graceful-shutdown-spring-boot-applications#)

 

 Comment (7)

 

 Save

 

[ Tweet ](https://dzone.com/articles/graceful-shutdown-spring-boot-applications)

 72.46K Views

Join the DZone community and get the full member experience.

 [JOIN FOR FREE](https://dzone.com/static/registration.html)

<iframe frameborder="0" src="https://2a93387e799fa8e1d335bf0be53cca8e.safeframe.googlesyndication.com/safeframe/1-0-37/html/container.html" id="google_ads_iframe_/2916070/dz2_bumper_text_ad_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="0" height="100" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" data-google-container-id="4" data-load-complete="true" style="box-sizing: border-box; border: 0px; vertical-align: bottom; min-width: 100%;"></iframe>

This guide walks through the process gracefully shutting down a [Spring Boot](https://spring.io/projects/spring-boot) application.

> The implementation of this blog post is originally created by [Andy Wilkinson](https://twitter.com/ankinson) and adapted by me to Spring Boot 2. The code is based on this   [GitHub comment](https://github.com/spring-projects/spring-boot/issues/4657#issuecomment-161354811).

## Introduction

A lot of developers and architects discuss the application design, traffic load, frameworks, and patterns to apply to code, but very few of them are discussing the shutdown phase.

Let’s consider this scenario — there’s an application that has a long blocking process. Along with that, this app needs to be shut down and replaced with a newer version. Wouldn't it be nice if, instead of killing all the connections, it just gracefully waited to finish before the shutdown?

That’s what we are going to cover in this guide!

## Pre-requisites

- [JDK 1.8](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
- A text editor or your favorite IDE
- [Maven 3.0+](https://maven.apache.org/download.cgi)

## Spring Boot, Tomcat

To make this feature work, the first step is to implement the `TomcatConnectorCustomizer`.

1

```
import org.apache.catalina.connector.Connector;
```

2

```
import org.slf4j.Logger;
```

3

```
import org.slf4j.LoggerFactory;
```

4

```
import org.springframework.boot.web.embedded.tomcat.TomcatConnectorCustomizer;
```

5

```
import org.springframework.context.ApplicationListener;
```

6

```
import org.springframework.context.event.ContextClosedEvent;
```

7

```

```

8

```
import java.util.concurrent.Executor;
```

9

```
import java.util.concurrent.ThreadPoolExecutor;
```

10

```
import java.util.concurrent.TimeUnit;
```

11

```

```

12

```
public class GracefulShutdown implements TomcatConnectorCustomizer, ApplicationListener&lt;ContextClosedEvent&gt; {
```

13

```

```

14

```
    private static final Logger log = LoggerFactory.getLogger(GracefulShutdown.class);
```

15

```

```

16

```
    private volatile Connector connector;
```

17

```

```

18

```
    @Override
```

19

```
    public void customize(Connector connector) {
```

20

```
        this.connector = connector;
```

21

```
    }
```

22

```

```

23

```
    @Override
```

24

```
    public void onApplicationEvent(ContextClosedEvent event) {
```

25

```
        this.connector.pause();
```

26

```
        Executor executor = this.connector.getProtocolHandler().getExecutor();
```

27

```
        if (executor instanceof ThreadPoolExecutor) {
```

28

```
            try {
```

29

```
                ThreadPoolExecutor threadPoolExecutor = (ThreadPoolExecutor) executor;
```

30

```
                threadPoolExecutor.shutdown();
```

31

```
                if (!threadPoolExecutor.awaitTermination(30, TimeUnit.SECONDS)) {
```

32

```
                    log.warn("Tomcat thread pool did not shut down gracefully within "
```

33

```
                            + "30 seconds. Proceeding with forceful shutdown");
```

34

```
                }
```

35

```
            } catch (InterruptedException ex) {
```

36

```
                Thread.currentThread().interrupt();
```

37

```
            }
```

38

```
        }
```

39

```
    }
```

40

```
}
```



In the implementation shown above, the `ThreadPoolExecutor` will be waiting `30` seconds prior to proceeding with the shutdown. Pretty simple, right? With that in place, it’s now time to register this bean to the `application context` and inject it to `Tomcat`.

To do that, just create the following Spring `@Bean`s.

1

```
@Bean
```

2

```
public GracefulShutdown gracefulShutdown() {
```

3

```
    return new GracefulShutdown();
```

4

```
}
```

5

```

```

6

```
@Bean
```

7

```
public ConfigurableServletWebServerFactory webServerFactory(final GracefulShutdown gracefulShutdown) {
```

8

```
    TomcatServletWebServerFactory factory = new TomcatServletWebServerFactory();
```

9

```
    factory.addConnectorCustomizers(gracefulShutdown);
```

10

```
    return factory;
```

11

```
}
```



## How to Test?

To test this implementation, I just created a `LongProcessController` that which has a `Thread.sleep` of `10` seconds.

1

```
import org.springframework.web.bind.annotation.RequestMapping;
```

2

```
import org.springframework.web.bind.annotation.RestController;
```

3

```

```

4

```
@RestController
```

5

```
public class LongProcessController {
```

6

```

```

7

```
    @RequestMapping("/long-process")
```

8

```
    public String pause() throws InterruptedException {
```

9

```
        Thread.sleep(10000);
```

10

```
        return "Process finished";
```

11

```
    }
```

12

```
}
```



Now, it’s just a matter of running your Spring Boot application, making a request to the `/long-process` endpoint, and, in the meantime, kill it with a `SIGTERM`.

### Locate the Process ID

When you start the application, you can locate the process ID in the logs. In my case, it’s `6578`.

1

```
2018-06-28 20:37:28.292  INFO 6578 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
```

2

```
2018-06-28 20:37:28.296  INFO 6578 --- [           main] c.m.wd.gracefulshutdown.Application      : Started Application in 2.158 seconds (JVM running for 2.591)
```



### Request and Shutdown

Perform a request with the `/long-process` endpoint. I’m using `curl`for that:

1

```
$ curl -i localhost:8080/long-process
```



Send a `SIGTERM` to the process:

1

```
$ kill 6578
```



The `curl` request still needs to respond as below:

1

```
HTTP/1.1 200
```

2

```
Content-Type: text/plain;charset=UTF-8
```

3

```
Content-Length: 14
```

4

```
Date: Thu, 28 Jun 2018 18:39:56 GMT
```

5

```

```

6

```
Process finished
```



### Summary

Congratulations! You just learned how to gracefully shutdown Spring Boot apps.