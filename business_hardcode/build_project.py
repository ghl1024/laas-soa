"""
构建项目

需要依赖一些数据
    构建服务器
    源码仓库信息
    项目配置信息
"""
import paramiko

from rest.operate.executor import context


def build_project(executor_data_id, data_id, data_data_id):
    context.log(executor_data_id,
                "executor_data_id: %s data_id: %s data_data_id: %s" % (executor_data_id, data_id, data_data_id))
    # 得到执行数据
    business_data = context.select_by_data_id__data_data_id(data_id, data_data_id)
    context.log(executor_data_id, "startup_parameters: " + str(business_data))
    # [{'id': 3, 'git_server': '1', 'project_name': '仓库', 'gitlab_id': '43', 'branches': 'master', 'tags': None}]
    # 连接到目标服务器
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 查询连接信息
        host_build = context.select_by_data_id__data_data_id(15, 1)[0]
        ssh.connect(host_build['ip'], int(host_build['port']), host_build['username'],
                    host_build['password'])
        stdin, stdout, stderr = ssh.exec_command('ls -alh /')
        context.log(executor_data_id, stdout.read().decode('utf-8'))
    except Exception as e:
        context.log(executor_data_id, str(e))
    finally:
        ssh.close()
