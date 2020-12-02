# coding: utf-8
import os
# import threading
import time

# read target server config
target_server_list = []
password = None
# 目标服务器ip文件, 使用时需要修改内容
target_server_file_name = "target_server"
# 服务器密码文件, 使用时需要修改内容
password_file_name = "password"

if not os.path.exists("logs"):
    os.mkdir("logs")


def log(filename, log_content):
    print(filename, log_content)
    return
    file_open_mode = "a"
    log_file_name = "logs/" + str(filename)
    if not os.path.exists(log_file_name):
        file_open_mode = "w"
    with open(log_file_name, file_open_mode) as f:
        f.write(log_content)


def do_init():
    with open(target_server_file_name) as f:
        original_target_server_list = f.readlines()
        for item in original_target_server_list:
            if not item or "" == item:
                continue
            item = item.strip().replace("\n", "").replace("\t", "")
            target_server_list.append(item)

    with open(password_file_name) as f:
        global password
        password = f.read().strip()


def exec_remote_shell(remote_host, remote_password, shell):
    command = ' sshpass -p %s ssh -o "StrictHostKeyChecking no" root@%s "%s" ' % (
        remote_password, remote_host, shell)
    log(remote_host, "command is: %s" % command)
    log(remote_host, os.popen(command).read())
    time.sleep(1)


def transfer_remote_file(remote_host, remote_password, local_filepath, remote_filepath):
    command = ' sshpass -p %s scp -o "StrictHostKeyChecking no" %s root@%s:%s ' % (
        remote_password, local_filepath, remote_host, remote_filepath)
    log(remote_host, "command is: %s" % command)
    log(remote_host, os.popen(command).read())
    time.sleep(2)


def setup(item):
    # 加载数据
    # 分发执行
    # 关闭node_exporter进程
    exec_remote_shell(item, password, "kill $(ps aux | grep 'node_exporter' | awk '{print $2}')")
    # 传输node_exporter并授予权限
    transfer_remote_file(item, password, "node_exporter", "node_exporter")
    exec_remote_shell(item, password, "chmod +x node_exporter")
    # 传输系统化node_exporter指令文件并授予权限
    transfer_remote_file(item, password, "systemctl_node_exporter.sh", "systemctl_node_exporter.sh")
    exec_remote_shell(item, password, "chmod +x systemctl_node_exporter.sh && /root/systemctl_node_exporter.sh")
    # 查看node_exporter状态及访问情况
    exec_remote_shell(item, password, "ps aux|grep node_exporter")
    exec_remote_shell(item, password, "curl http://localhost:9100")
    log(item, "setup finish")


if __name__ == '__main__':
    do_init()
    print("send script file to target server")
    for item in target_server_list:
        # threading.Thread(target=setup, args=(item,)).start()
        setup(item)
        time.sleep(5)
    print("all right done, thank you for use this scrip")
