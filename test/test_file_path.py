from rest.native.executor import context

local_executor_root_path = r'D:\projects\github\laashub-soa\laas-soa\business_hardcode\build_project'
remote_basic_dir = "/data/tristan/1"

if __name__ == '__main__':
    local_files = context.get_local_files(local_executor_root_path + "/data_data")
    print(local_files)
    print("-" * 100)
    remote_files = context.convert_local_files_2_remote_files(local_files, local_executor_root_path, remote_basic_dir)
    # print(remote_files)
    for item in local_files:
        if item.endswith("/"):
            item = item[:-1]
            print(item)
