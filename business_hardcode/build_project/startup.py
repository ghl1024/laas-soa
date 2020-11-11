#!/usr/local/bin/python
# coding: utf-8
import argparse
import json
import os

parser = argparse.ArgumentParser(description='executor start up command args')
parser.add_argument('-ei', '--executor_id', nargs=1, type=int, help='executor id')
args = parser.parse_args()

executor_id = args.executor_id[0]  # 当前执行器id
root_path = os.getcwd()
cur_executor_path = root_path + "/" + "run" + "/" + str(executor_id)
# 加载数据
startup_data = None
docker_registry_data = None
git_server_data = None
# 加载源码
finally_project_code_path = None
finally_project_build_path = None
# 加载业务脚本, 将部分数据替换到业务脚本中, 执行业务脚本
business_hyper_fusion_path = None
"""
{"id": 1, "url": "http://git.xxx.com", "robot_username": "xxx", "robot_password": "xxx", 
"name": "本地git服务器", "update_datetime": {"$date": 1604953278000}, "create_datetime": {"$date": 1604953278000}}
"""


def execute_shell(command, is_print=True):
    print(command)
    out_log = os.popen(command).read()
    if is_print:
        print(out_log)
    return out_log


def load_startup_data():
    """
    加载启动数据
    :return:
    """
    """
    {'id': 11, 'git_server': '1', 'project_name': '仓库系统', 'branches': 'master', 'tags': '', 
    'program_language': 'java', 'docker_registry_id': '1', 'update_datetime': {'$date': 1605035741000}, 
    'create_datetime': {'$date': 1605035741000}, 'repo_path': 'http://git.xxx.com/wms/wms_service'}
    """
    with open(cur_executor_path + "/" + "data_data.json") as f:
        global startup_data
        startup_data = json.loads(f.read())
    with open(root_path + "/" + "data_data" + "/" + "docker_registry.json") as f:
        global docker_registry_data
        docker_registry_data = json.loads(f.read())
    with open(root_path + "/" + "data_data" + "/" + "git_server.json") as f:
        global git_server_data
        git_server_data = json.loads(f.read())


def load_project_source_code():
    """
    加载项目源码
    :return:
    """
    # 判断git指令是否有安装
    out_log = execute_shell("git", False)
    if "command not found" in out_log:
        print(out_log)
        execute_shell("yum install -y git")
    # 判断docker是否有安装
    # 创建目录
    code_path = root_path + "/" + "cache" + "/" + "code"  # 源码目录
    repo_path = startup_data["repo_path"]
    branches = startup_data["branches"]
    repo_path_path = (repo_path[repo_path.find("//") + 2:]).replace(".", "_")  # 仓库目录
    branches_path = "branches" + "/" + branches
    global finally_project_code_path
    global finally_project_build_path
    finally_project_code_path = code_path + "/" + repo_path_path + "/" + branches_path + "/" + "source"
    finally_project_build_path = code_path + "/" + repo_path_path + "/" + branches_path + "/" + "build"
    execute_shell("mkdir -p " + finally_project_code_path)
    execute_shell("mkdir -p " + finally_project_build_path + " && chmod 777 " + finally_project_build_path)
    # 项目路径目录
    username = git_server_data["robot_username"]
    password = git_server_data["robot_password"]
    auth_username_password = username + ":" + password + "@"
    repo_path_list = list(repo_path)
    repo_path_list.insert(repo_path.find("//") + 2, auth_username_password)
    command_repo_path = "".join(repo_path_list) + ".git"
    # git clone http://<username>:<password>@git_server_url/repo_path.git -b <分支名> --single--branch
    switch_path_command = "cd " + finally_project_code_path + " && "
    # 如果仓库中有.git文件夹的话则进行增量更新, 反之进行全量拉取
    git_metadata_dir_path = finally_project_code_path + "/" + '.git'
    if os.path.exists(git_metadata_dir_path) or os.path.isdir(git_metadata_dir_path):  # 如果仓库中有.git文件夹的话则进行增量更新
        command = "git pull origin"
    else:  # 全量拉取
        # TODO 清理全量拉取目录
        command = "git clone " + " -b " + branches + " --single-branch " + command_repo_path + " ./"

    command = switch_path_command + command
    print(command.replace(auth_username_password, ""))
    execute_shell(command)


def load_business():
    project_program_language = startup_data["program_language"]
    # 依赖库
    dependency_path = root_path + "/" + "cache" + "/" + "dependency" + "/" + project_program_language
    execute_shell("mkdir -p " + dependency_path)
    global business_hyper_fusion_path
    business_hyper_fusion_path = root_path + "/" + "business_hyper_fusion" + "/" + project_program_language
    execute_shell("chmod +x " + business_hyper_fusion_path)
    do_build_project_path = business_hyper_fusion_path + "/" + "do_build_project.sh"
    with open(do_build_project_path) as f:
        build_project_sh_template = f.read()
        build_project_sh_path = business_hyper_fusion_path + "/" + "build_project.sh"
        with open(build_project_sh_path)as build_project_sh_file:
            build_project_sh_lines = build_project_sh_file.readlines()
        build_project_sh = " && ".join(build_project_sh_lines).strip()
        do_build_project_sh = build_project_sh_template.format(**{
            "execute_id": executor_id,
            "finally_project_code_path": finally_project_code_path,
            "finally_project_build_path": finally_project_build_path,
            "build_project_sh": build_project_sh,
        })
        execute_shell("chmod +x " + business_hyper_fusion_path)
        execute_shell(do_build_project_sh)


def execute_business():
    # do_build_project
    # build_project
    # clean_build_project
    # startup
    # Dockerfile
    # do_build_docker
    # build_docker
    # clean_build_docker
    pass


if __name__ == '__main__':
    load_startup_data()
    load_project_source_code()
    load_business()
