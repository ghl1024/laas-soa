from business_hardcode.update_project_config.nacos import Nacos

# 修改文件内容
if __name__ == '__main__':
    project_name = "tristan"
    env = "dev"
    file_path = "configs/application.yaml"
    file_content = "configs/application.yaml"
    nacos = Nacos()
    # 同步nacos数据到soa
    # 查询nacos的项目列表
    # project_list = nacos.select_project_list()
    # print(project_list)
    # 查询nacos的文件列表
    # 查询nacos的文件内容
    # for item in project_list:
    #     file_list = nacos.select_file_list(item["project_id"])
    #     print(file_list)
    #     break
    # 新增项目
    # insert_project_result = nacos.insert_project(project_name)
    # print(insert_project_result)

    # 修改项目名
    # 删除项目
    # delete_project_result = nacos.delete_project(project_name")
    # print(delete_project_result)

    # 新增文件
    insert_file_result = nacos.insert_file(project_name, env, file_path, file_content)
    print(insert_file_result)
    # 修改文件名
    # 删除文件
    delete_file_result = nacos.delete_file(project_name, env, file_path)
    print(delete_file_result)
