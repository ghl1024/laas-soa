import os
import time

# read target server config
target_server_list = []
target_server_file_name = "target_server"
password_file_name = "password"
with open(target_server_file_name) as f:
    original_target_server_list = f.readlines()
    for item in original_target_server_list:
        if not item or "" == item:
            continue
        item = item.strip().replace("\n", "").replace("\t", "")
        target_server_list.append(item)

with open(password_file_name) as f:
    password = f.read()
os.system("echo target_server: %s \n password:%s" % (str(target_server_list), password))

# install sshpass
os.system("apt-get install sshpass")
time.sleep(1)


def exec_remote_shell(remote_host, remote_password, shell):
    command = """ sshpass -p %s ssh root@%s "%s" """ % (remote_password, remote_host, shell)
    os.system("""echo "command is: %s" """ % command)
    os.system(command)
    time.sleep(1)


def transfer_remote_file(remote_host, remote_password, local_filepath, remote_filepath):
    command = """sshpass -p %s scp %s root@%s:%s""" % (remote_password, local_filepath, remote_host, remote_filepath)
    os.system("""echo "command is: %s" """ % command)
    os.system(command)
    time.sleep(2)


os.system("echo send script file to target server")
for item in target_server_list:
    transfer_remote_file(item, password, "node_exporter", "node_exporter")
    exec_remote_shell(item, password, "chmod +x node_exporter")
    exec_remote_shell(item, password, "nohup  ~/node_exporter > node_exporter.log 2>&1 &")
    exec_remote_shell(item, password, "curl http://localhost:9100/metrics")
os.system(""" echo "all right done, thank you for use this script" """)
