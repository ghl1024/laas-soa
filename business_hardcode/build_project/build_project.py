"""
构建项目

需要依赖一些数据
    构建服务器
    源码仓库信息
    项目配置信息
"""
import json
import os
import traceback

from rest.operate.executor import context

local_executor_root_path = os.path.join(os.getcwd(), "business_hardcode/build_project")
remote_executor_root_path = "/data/tristan/1"  # 远程执行器根目录
# 准备本地目录
local_executor_data_data_path = os.path.join(local_executor_root_path, "data_data")
context.prepare_local_dirs([local_executor_data_data_path])
# 本地数据版本记录文件
local_update_datetime_record_path = local_executor_root_path + "/" + "local_update_datetime_record"


def build_project(executor_data_id, data_data_data):
    """
    构建项目
    :param executor_data_id:
    :param data_data_data:
    :return:
    """
    # 记录全局数据
    context.global_data.executor_data_id = executor_data_id
    try:
        """
        {'id': 11, 'git_server': '1', 'project_name': '仓库系统', 'branches': 'master', 'tags': '', 
        'program_language': 'java', 'docker_registry_id': '1', 'update_datetime': {'$date': 1605035741000}, 
        'create_datetime': {'$date': 1605035741000}, 'repo_path': 'http://git.wjh.com/wms/wms_service'}
        """
        # 查询执行器
        host_build = context.select_data_by_data_id__data_data_id(15, 1)[0]  # 查询服务器连接信息
        context.log('host_build: ' + str(host_build))
        # 获取最新版本的数据, 保存数据到本地, 同步最新版本的数据到执行器目录
        latest_update_datetime_record = ""
        """
        data_data:
            git_server.json
            docker_registry.json
        """
        # 查询 git服务器
        data_data_git_server = context.select_data_by_data_id__data_data_id('5', data_data_data['git_server'])[0]
        latest_update_datetime_record += str(data_data_git_server["update_datetime"]) + ";"
        # 查询 docker镜像仓库
        data_data_docker_registry = \
            context.select_data_by_data_id__data_data_id('4', data_data_data['docker_registry_id'])[0]
        latest_update_datetime_record += str(data_data_docker_registry["update_datetime"]) + ";"
        # 查询 仓库地址

        local_update_datetime_record = None
        if os.path.exists(local_update_datetime_record_path):
            with open(local_update_datetime_record_path) as f:
                local_update_datetime_record = f.read()
        if not local_update_datetime_record or local_update_datetime_record != latest_update_datetime_record:
            # ############### 同步数据到文件到远程服务器
            # 准备远程目录
            context.log(context.declare_remote_dirs(host_build, [remote_executor_root_path]))
            context.write_data_data_2_file(data_data_git_server, local_executor_data_data_path + '/git_server.json')
            context.write_data_data_2_file(data_data_docker_registry,
                                           local_executor_data_data_path + '/docker_registry.json')
            # 获取最新版本的业务, 保存业务到本地, 同步最新版本的业务到执行器
            """
            business_hyper_fusion:
                java:
                    do_build_project.sh
                    build_project.sh
                    clean_build_project.sh
                    startup.sh
                    Dockerfile
                    do_build_docker.sh
                    clean_build_docker.sh
            """
            # 同步数据、业务脚本目录到服务器
            context.sync_dirs_2_remote(host_build, local_executor_root_path, remote_executor_root_path,
                                       ["data_data", "business_hyper_fusion"])
            # 同步启动文件到服务器
            context.sync_files_2_remote(host_build, local_executor_root_path, remote_executor_root_path, ["startup.py"])
            with open(local_update_datetime_record_path, 'w')as f:
                f.write(latest_update_datetime_record)
        # ######每次执行器都需要创建执行目录, 并将启动数据写入执行目录的data_data.json文件中
        remote_executor_run_n_path = remote_executor_root_path + "/run/" + str(executor_data_id)
        # 创建这次执行器的运行目录
        context.declare_remote_dirs(host_build, [remote_executor_run_n_path])
        # 写入启动参数
        context.execute_remote_command(host_build, """
sudo cat >> %s<<EOF
%s
EOF
        """ % (remote_executor_run_n_path + "/data_data.json", json.dumps(data_data_data, ensure_ascii=False)))
        # 是否应该考虑将共享文件拷贝到自己的区域???
        # 好处是什么? 目录都都可以在自己的目录, 坏处是什么, 需要拷贝文件
        command = "cd %s && python startup.py -ei %s" % (remote_executor_root_path, executor_data_id)
        # execute_result = context.execute_remote_command(host_build, command)
        # context.log(execute_result)
        # shin, shout, sherr = context.ShellHandler(host_build["ip"], host_build["port"], host_build["username"],
        #                                           host_build["password"]).execute(command)
        # if len(sherr) > 0:
        #     context.log("".join(sherr))
        # else:
        #     context.log("".join(shout))
        result = context.RemoteShell(host_build["ip"], host_build["port"], host_build["username"],
                                     host_build["password"]).exec(command)
        print("=" * 200)

    except Exception as e:
        traceback.print_exc()
        context.log(str(e))
