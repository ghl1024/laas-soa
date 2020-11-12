FROM registry.wjh.com/registry/openjdk:8-alpine
ADD target/*.jar app.jar
ADD startup.sh startup.sh
RUN chmod 777 startup.sh
RUN echo 'Asia/Shanghai' > /etc/timezone
RUN  mkdir -p /data/servicesLog/logs
ENTRYPOINT ["./startup.sh"]