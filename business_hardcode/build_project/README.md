[toc]



# 业务场景

构建代码

基于docker进行资源隔离和构建器管理

服务端执行器启动执行, 通过SSH传递构建脚本到服务器, 后台启动startup.py(python2)

暂时为本地硬编码方式实现业务功能, 基于python2语法, 不使用特殊包, 仅仅使用数据处理部分, 结合shell文件, python2加载数据json文件到执行业务过程中, 将数据初始化、目录初始化放到python2中

记录查询数据的更新时间, 当同步数据文件成功之后将更新时间列表记录到local_update_time_record文件中, 同步之前先对比更新时间与local_update_time_record, 当不一致时再次同步文件

在脚本中记录日志到日志文件、记录状态到状态文件

统计时间消耗、资源消耗



在run目录下创建当前执行目录, 目录名为"执行器id", 将启动参数写入data_data.json文件中

远程启动startup.py文件并设置启动参数:  "执行器id"

根据项目目录创建并切换到运行目录

运行时的目录结构如下:

```
build_project_path = "/data/tristan/1/run/1"  # /data/tristan 代表执行器的目录 /1代表业务id /run代表运行时目录 /1代表执行器id

dependency_lib通过放置缓存的依赖库文件、远程依赖库配置
假设:
	执行器根目录 = /data/tristan
	业务id	 = 1
	执行器id	= 1
	<分支名>	= master
	<标签名>	= 1

<执行器根目录>
	<业务id>
		startup.py
		business_hyper_fusion:
            java:
                do_build_project.sh
                build_project.sh
                clean_build_project.sh
                startup.sh
                Dockerfile
                do_build_docker.sh
                build_docker.sh
                clean_build_docker.sh
        data_data:
        	git_server.json
			docker_registry.json
			docker_registry_password
		cache
			dependency
				java
				nodejs
			code
				<源码仓库地址转目录>
                    <项目访问后部分目录>
                        branches
                            <分支名>
                        tags
                            <标签名>
		run
			<执行器id>
				data_data.json



借助docker进行构建时, 需要挂载:
	/<执行器根目录>/<业务id>/cache
	/<执行器根目录>/<业务id>/run/<执行器id>/<源码仓库地址转目录>/<项目访问后部分目录>
```

cache中保存该仓库的构建缓存数据, 直接在分支下存源码, 使用version文件记录构建脚本文件的版本, 当版本一致时则不拉取最新构建脚本, 反之则拉取最新构建脚本

拉取源码

​	tag中的代码不会缓存, branch中会缓存最近一次代码, 首次使用完整clone, 第二次使用fetch

创建容器进行构建

​	找寻`build_依赖镜像`镜像是否存在, 如果不存在则根据依赖镜镜像构建`build_依赖镜像`镜像, 如果存在则启动镜像、传递参数、挂载target目录

​		拷贝编译脚本进去, 执行编译脚本

​	

服务端需要配置:

​	构建机器信息:

​		服务器连接信息: ip、port、username、password

​	镜像仓库信息:

​		描述信息: 名称、描述

​		连接信息: ip、port、username、password

​	构建信息:

​			编译镜像名称

​			镜像仓库地址

​			compile_to_execute.sh

​			package_to_docker.sh

​			Dockerfile

​	git服务器信息:

​			连接信息: ip、port、username、password, 该连接账号的权限只需要只读即可

​			是否默认

​	

​	配置项目信息:

​		git服务器: 默认使用默认的git服务器

​		地址: 可从git服务器选择, 也可以直接输入

​		项目描述: 如果是gitlab服务器则自动带出项目描述, 也可以直接输入

​		项目类型: java/php/nodejs/python

​		构建信息: 选择一个构建信息, 可进行预览

​	镜像构建:

​		镜像仓库地址

​		编译镜像名称

​		compile_to_execute.sh

​		package_to_docker.sh

​		Dockerfile



和服务端的维持关系:

使用websocket方式 或者 http

当网络连接状态良好时使用websocket, 当网络连接状态不好时使用http

# 之前类似的做法

之前基于gitlab-runner做ci的案例:

父镜像Dockerfile:

```
FROM apache/skywalking-base:6.5.0 as skywalking
FROM anapsix/alpine-java
COPY --from=skywalking /skywalking/agent /agent
ENV SW_AGENT_NAMESPACE='tristan' SW_AGENT_NAME=${IMAGE_PROJECT_TAG} SW_AGENT_COLLECTOR_BACKEND_SERVICES='skywalking-skywalking-oap.skywalking:11800'
RUN echo 'Asia/Shanghai' > /etc/timezone
```

被依赖项目的.gitlab-ci.yml:

```
build:code:
  image: maven:3-alpine
  variables:
    MAVEN_CLI_OPTS: "-s .m2/settings.xml --batch-mode"
    GIT_STRATEGY: clone
  script:
    - echo "Asia/Shanghai" > /etc/timezone
    - mvn deploy
```

部署型项目的.gitlab-ci.yml:

```
build:code:
  stage: build
  image: maven:3-alpine
  variables:
    MAVEN_CLI_OPTS: "-s .m2/settings.xml --batch-mode"
    GIT_STRATEGY: clone
  cache:
    paths:
      - target/
  script:
    - mvn clean package -DskipTests
test:image:
  stage: test
  image: docker
  cache:
    paths:
      - target/
  dependencies:
    - :build:code
  script:
    - chmod 777 build-docker.sh && dos2unix build-docker.sh && source build-docker.sh
```

build-docker.sh:

```
#!/bin/bash
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>开始构建服务:'${JOB_NAME}
dos2unix /root/.m2/dockerregistry && source /root/.m2/dockerregistry
CUR_DATETIME_STR=$(date "+%Y%m%d%H%M")
IMAGE_PROJECT_TAG=${CI_PROJECT_NAME}"-"${CI_COMMIT_REF_NAME}
IMAGE_ID=${DOCKER_REGISTRY_URL}"/"${IMAGE_PROJECT_TAG}":"${CI_BUILD_ID}"_"${CUR_DATETIME_STR}
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>正在登录镜像仓库'
cat /root/.m2/dockerregistry-auth |  docker login ${DOCKER_REGISTRY_URL} --username ${DOCKER_REGISTRY_USERNAME} --password-stdin
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<登录镜像仓库成功'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<正在构建镜像'
docker build --build-arg IMAGE_PROJECT_TAG=${IMAGE_PROJECT_TAG} -t ${IMAGE_ID}  .
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<构建镜像成功'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>正在推送镜像到镜像仓库'
docker push ${IMAGE_ID}
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<推送镜像到镜像仓库成功'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>正在清理本地镜像'
docker rmi ${IMAGE_ID}
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<清理本地镜像成功'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<完成构建服务:'${JOB_NAME}
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo '请拷贝镜像id到下一环节,镜像id为:'
echo ${IMAGE_ID}
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
echo '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
```

Dockerfile:

```
FROM registry-vpc.cn-shenzhen.aliyuncs.com/xxx/base_image-master:2790_201911271640
ADD target/*.jar app.jar
ADD startup.sh startup.sh
RUN bash -c 'touch app.jar'
RUN chmod 777 startup.sh
ARG IMAGE_PROJECT_TAG
ENV SW_AGENT_NAME ${IMAGE_PROJECT_TAG}
ENTRYPOINT ["./startup.sh"]
```

# 开发

通过各个语言

暂时将该数据保存到代码内部的字符串中, 在字符串内部使用{key}引用外部变量, 在使用时使用字符串的format函数传递key:value到字符串中

```
在startup.py中准备目录, 依次加载shell文件内进行执行


do_build_project.sh:
docker run -it --name exe1cute_business_1_1 -v /data/tristan/1/cache/java:/root/.m2 -v /data/tristan/1/cache/<目录>:/source_code -v /.../build:/source_code/target maven:3-alpine git配置名称/仓库目录/compile_to_execute.sh



build_project.sh:
mvn clean package -DskipTests


clean_build_project.sh:
docker stop execute_business_1_1
docker rm execute_business_1_1


startup.sh：
java /app.jar


Dockerfile:
FROM registry-vpc.cn-shenzhen.aliyuncs.com/xxx/base_image-master:2790_201911271640
ADD target/*.jar app.jar
ADD startup.sh startup.sh
RUN bash -c 'touch app.jar'
RUN chmod 777 startup.sh
ARG IMAGE_PROJECT_TAG
ENV SW_AGENT_NAME ${IMAGE_PROJECT_TAG}
ENTRYPOINT ["./startup.sh"]


do_build_docker.sh:
docker run -it --name execute_business_1_1 -v /data:实际目录 docker  git配置名称/仓库目录/package_to_docker.sh


build_docker.sh:
cat /root/.m2/dockerregistry-auth |  docker login ${DOCKER_REGISTRY_URL} --username ${DOCKER_REGISTRY_USERNAME} --password-stdin
docker build --build-arg IMAGE_PROJECT_TAG=${IMAGE_PROJECT_TAG} -t ${IMAGE_ID}  .
docker push ${IMAGE_ID}


clean_build_docker.sh
docker rm execute_business_1_1
docker rm <镜像id>
```

状态、日志会增量收集同步到服务器上(filebeat)

# 功能

配置git服务器信息、docker注册仓库信息、项目信息

根据选择的项目构建信息构建项目并推送到指定的镜像仓库中(目前只时硬编码实现了java项目的构建)

# 未来功能

针对一个仓库中冗杂多个模块的项目进行单独配置, 分离被依赖型项目和部署型项目, 主动构建只需要关注部署型项目模块即可

开发环境自动构建部署回滚开发环境

根据传入的分支名创建tag, tag构建时会基于分支中已有的缓存进行构建

# 一些问题

远程执行shell与本地执行shell有区别

直接执行shell时日志的问题, 状态的问题

执行器平均分配动作

是否需要支持这种多环境? 按照环境去打包?

这样的话, 可以更加持续性的, 否则改动就比较大了

我就算是接入原来的方式, 因为目前构建和部署耦合性大, 暂时也用不了, 目前应该去写项目配置

目前 日志/状态 也没有记录