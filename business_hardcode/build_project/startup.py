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
repo_path = None
repo_path_path = None
docker_registry_path = None
# 加载数据
startup_data = None
docker_registry_data = None
git_server_data = None
# 项目
branches = None
# 加载源码
finally_project_code_path = None
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
    'create_datetime': {'$date': 1605035741000}, 'repo_path': 'http://git.xxx.com/wms/wms_service'},
     'module_path': 'wms-service/wms-server'}
    """
    with open(cur_executor_path + "/" + "data_data.json") as f:
        global startup_data
        startup_data = json.loads(f.read())
    global docker_registry_path
    docker_registry_path = root_path + "/" + "data_data" + "/" + "docker_registry.json"
    with open(docker_registry_path) as f:
        global docker_registry_data
        docker_registry_data = json.loads(f.read())
    with open(root_path + "/" + "data_data" + "/" + "git_server.json") as f:
        global git_server_data
        git_server_data = json.loads(f.read())
    # 顺便初始化一些数据
    project_program_language = startup_data["program_language"]
    # 依赖库
    dependency_path = root_path + "/" + "cache" + "/" + "dependency" + "/" + project_program_language
    if not os.path.exists(dependency_path):
        execute_shell("mkdir -p " + dependency_path)
    global business_hyper_fusion_path
    business_hyper_fusion_path = root_path + "/" + "business_hyper_fusion" + "/" + project_program_language
    global repo_path
    repo_path = startup_data["repo_path"]
    global repo_path_path
    repo_path_path = (repo_path[repo_path.find("//") + 2:]).replace(".", "_")  # 仓库目录
    global branches
    branches = startup_data["branches"]
    global finally_project_code_path
    code_path = root_path + "/" + "cache" + "/" + "code"  # 源码目录
    finally_project_code_path = code_path + "/" + repo_path_path + "/" + "branches" + "/" + branches


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
    if not os.path.exists(finally_project_code_path):
        execute_shell("mkdir -p " + finally_project_code_path)
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
        # TODO 清理全量拉取目录???
        command = "git clone " + " -b " + branches + " --single-branch " + command_repo_path + " ./"

    command = switch_path_command + command
    print(command.replace(auth_username_password, ""))
    execute_shell(command)


def build_project():
    """
    构建项目
    :return:
    """
    # 加载项目源码
    load_project_source_code()
    # 构建项目
    execute_shell("chmod +x " + business_hyper_fusion_path)
    do_build_project_path = business_hyper_fusion_path + "/" + "do_build_project.sh"
    with open(do_build_project_path) as f:
        build_project_sh_template = ""
        for item in f.readlines():
            item = item.strip().replace("\n", "").replace("\r", "")
            if "" == item:
                continue
            build_project_sh_template += item + " && "
        build_project_sh_template = build_project_sh_template[:-4]
        build_project_sh_path = business_hyper_fusion_path + "/" + "build_project.sh"
        with open(build_project_sh_path)as build_project_sh_file:
            build_project_sh_lines = build_project_sh_file.readlines()
        build_project_sh = " && ".join(build_project_sh_lines).strip()
        do_build_project_sh = build_project_sh_template.format(**{
            "execute_id": executor_id,
            "finally_project_code_path": finally_project_code_path,
            "build_project_sh": build_project_sh,
        })
        execute_shell("chmod +x " + business_hyper_fusion_path)
        execute_shell(do_build_project_sh)


def build_docker():
    # 生成docker登录密码文件
    docker_registry_password_path = docker_registry_path + "_password"
    if not os.path.exists(docker_registry_password_path):
        with open(docker_registry_password_path, "w") as f:
            f.write(docker_registry_data["password"])
    build_docker_sh_path = business_hyper_fusion_path + "/" + "build_docker.sh"
    # 加载构建镜像脚本
    with open(build_docker_sh_path)as build_docker_sh_file:
        build_docker_sh_template = ""
        for item in build_docker_sh_file.readlines():
            build_docker_sh_template += item.strip().replace("\n", "").replace("\r", "") + " && "
        build_docker_sh_template = build_docker_sh_template[:-8]
        registry_url = docker_registry_data["registry_url"]
        registry_username = docker_registry_data["username"]
        image_id = registry_url + "/tristan/" + \
                   repo_path_path[repo_path_path.find("/") + 1:].replace("/", "_") + ":" + str(executor_id)

        finally_project_build_path = finally_project_code_path
        project_dockerfile_path = finally_project_build_path + "/" + "Dockerfile"
        dockerfile_path = business_hyper_fusion_path + "/" + "Dockerfile"
        if not os.path.exists(project_dockerfile_path):
            execute_shell("cp " + dockerfile_path + " " + project_dockerfile_path)
        build_docker_sh = build_docker_sh_template.format(**{
            "docker_registry_password_path": docker_registry_password_path,
            "registry_url": registry_url,
            "registry_username": registry_username,
            "finally_project_build_path": finally_project_build_path,
            "image_id": image_id,
        })
    out_log = execute_shell(build_docker_sh, False)
    print(out_log.replace(registry_username, "xxx"))


def execute_business():
    build_project()
    build_docker()


if __name__ == '__main__':
    load_startup_data()
    execute_business()
