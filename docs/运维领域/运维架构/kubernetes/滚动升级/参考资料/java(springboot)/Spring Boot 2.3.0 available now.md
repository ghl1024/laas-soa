[RELEASES](https://spring.io/blog/category/releases) 

 

[STÉPHANE NICOLL](https://spring.io/team/snicoll) 

 

MAY 15, 2020

 

[58 COMMENTS](https://spring.io/blog/2020/05/15/spring-boot-2-3-0-available-now#disqus_thread)

On behalf of the Spring Boot team and everyone that has contributed, I am pleased to announce that Spring Boot 2.3.0 has been released and is available now from [repo.spring.io](https://repo.spring.io/release/) and Maven Central.

This release adds a significant number of new features and improvements. For full [upgrade instructions](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.3-Release-Notes#upgrading-from-spring-boot-22) and [new and noteworthy](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.3-Release-Notes#new-and-noteworthy) features please see the [release notes](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.3-Release-Notes).

# What’s new in 2.3

## Dependency upgrades

Spring Boot 2.3 moves to new versions of several Spring projects:

- Spring Data Neumann
- Spring HATEOAS 1.1
- Spring Integration 5.3
- Spring Kafka 2.5
- Spring Security 5.3
- Spring Session Dragonfruit

We’ve also upgraded to the latest stable releases of other third-party libraries wherever possible. Some of the more notable third-party dependency upgrades in this release include:

- Cassandra Driver 4.6
- Couchbase Client 3.0
- Elasticsearch 7.6
- Kafka 2.5
- Micrometer 1.5
- MongoDB 4.0

## Java 14 support

Spring Boot 2.3 supports Java 14 while also remaining compatible with Java 11 and 8.

## Docker support

Spring Boot 2.3 adds some interesting new features that can help you package up your Spring Boot application into Docker images.
Support for building Docker images using [Cloud Native Buildpacks](https://buildpacks.io/) and has been added to the Maven and Gradle plugins via the `spring-boot:build-image` goal and the `bootBuildImage` task. The [Paketo](https://paketo.io/) Java buildpack is used by default to create images.

Also, support for building jar files with contents separated into layers has been added to the Maven and Gradle plugins.

## Graceful shutdown

Graceful shutdown is supported with all four embedded web servers (Jetty, Reactor Netty, Tomcat, and Undertow) and with both reactive and Servlet-based web applications. When a grace period is configured, upon shutdown, the web server will no longer permit new requests and will wait for up to the grace period for active requests to complete.

## Liveness and Readiness probes

Spring Boot 2.3 has built-in knowledge of the availability of your application, tracking whether it is alive and whether it is ready to handle traffic. Check [this blog post](https://spring.io/blog/2020/03/25/liveness-and-readiness-probes-with-spring-boot) for more details.

## Spring Data Neumann

Spring Boot 2.3 ships with [Spring Data Neumann](https://spring.io/blog/2020/05/12/spring-data-neumann-goes-ga) that contains numerous major version and driver upgrades. This release also adds GA support for R2DBC.

## Other changes

There’s a whole host of other changes and improvements that are documented in the [release notes](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.3-Release-Notes). You can also find a list of deprecated classes and methods that we plan to remove in the next version.

# Thank you

We want to take this opportunity to again thank all our users and contributors. We’ve now had over [680 people](https://github.com/spring-projects/spring-boot/graphs/contributors) submit code, and there have been over [26000 commits](https://github.com/spring-projects/spring-boot/commits/master) to the project.

If you’re interested in helping out, check out the [“ideal for contribution” tag](https://github.com/spring-projects/spring-boot/labels/status%3A ideal-for-contribution) in the issue repository. If you have general questions, please ask at [stackoverflow.com](https://stackoverflow.com/) using the [`spring-boot` tag](https://stackoverflow.com/tags/spring-boot) or chat with the community [on Gitter](https://gitter.im/spring-projects/spring-boot).

[Project Page](https://spring.io/projects/spring-boot/) | [GitHub](https://github.com/spring-projects/spring-boot) | [Issues](https://github.com/spring-projects/spring-boot/issues) | [Documentation](https://docs.spring.io/spring-boot/docs/2.3.0.RELEASE/reference/html) | [Stack Overflow](https://stackoverflow.com/questions/tagged/spring-boot) | [Gitter](https://gitter.im/spring-projects/spring-boot)