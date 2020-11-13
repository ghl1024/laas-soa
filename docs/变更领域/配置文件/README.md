# 数据模型设计

## 数据: 配置项目数据

名称

url

## 数据: 配置项目部署环境数据

​	有哪些项目

​		项目名称	项目路径	项目环境(默认: dev,stage,pre,prod)

```
project_id
environments: dev,stage,pre,prod
```

## 数据: 配置项目配置文件数据

​	项目

​	环境

​	配置文件路径

​		对比其他环境

​		配置文件历史信息

​		合并到其他环境

​	配置文件内容

```
id
environment
path
content
```

## 开放数据

服务连接数据

# 数据模型



## 项目-环境

| 字段         | 类型        | 含义     | 关联模型 |
| ------------ | ----------- | -------- | -------- |
| project      | string      | 项目     |          |
| environments | list_string | 环境列表 |          |

## 配置文件

| 字段        | 类型        | 含义 | 关联模型                |
| ----------- | ----------- | ---- | ----------------------- |
| project     | string      | 项目 | 项目-环境(project)      |
| environment | string      | 环境 | 项目-环境(environments) |
| path        | path_string | 路径 |                         |
| content     | file_string | 内容 |                         |

# 案例数据

## 项目-环境

| 项目      | 环境               |
| --------- | ------------------ |
| project_1 | dev,stage,pre,prod |



## 配置文件

| 项目      | 环境 | 路径          | 内容 |
| --------- | ---- | ------------- | ---- |
| project_1 | dev  | test/test.txt | test |

