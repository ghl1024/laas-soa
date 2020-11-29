import json

import requests

"""
托管nacos
"""
nacos_base_url = "http://192.168.90.232:8848"

access_token_pool = {}


class Nacos(object):
    def __init__(self, base_url="http://192.168.90.232:8848", username="nacos", password="nacos"):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.max_page_size = 99999
        self.access_token = self.select_access_token()

    # 获取令牌
    def select_access_token(self):
        request_url = self.base_url + "/nacos/v1/auth/users/login"
        request_data = {
            "username": self.username,
            "password": self.password,
        }
        resp = requests.post(request_url, data=request_data)
        result_text = resp.text
        try:
            result = json.loads(result_text)
        except Exception as e:
            print(result_text)
            raise e + result_text
        access_token = result["accessToken"]
        print("access_token: ", access_token)
        global access_token_pool
        access_token_pool[nacos_base_url] = access_token
        return access_token

    # #####项目
    # 查询项目列表
    def select_project_list(self):
        request_url = self.base_url + "/nacos/v1/console/namespaces"
        request_params = {
            "accessToken": self.access_token,
            "pageNo": 1,
            "pageSize": self.max_page_size,
        }
        resp = requests.get(request_url, params=request_params)
        result_text = resp.text
        try:
            result = json.loads(result_text)
        except Exception as e:
            print(result_text)
            raise e + result_text
        resp_data = result["data"]
        project_list = []
        for resp_data_item in resp_data:
            project_id = resp_data_item["namespace"]
            project_name = resp_data_item["namespaceShowName"]
            project_list.append({
                "project_id": project_id,
                "project_name": project_name,
            })
        return project_list

    # 新增项目
    def insert_project(self, project_name):
        request_url = self.base_url + "/nacos/v1/console/namespaces"
        request_params = {
            "accessToken": self.access_token,
        }
        request_data = {
            "customNamespaceId": project_name,
            "namespaceName": project_name,
            "namespaceDesc": project_name,
        }
        resp = requests.post(request_url, params=request_params, data=request_data)
        if "true" == resp.text:
            return True
        return False

    # 修改项目
    def update_project(self):
        pass

    # 删除项目
    def delete_project(self, project_id):
        request_url = self.base_url + "/nacos/v1/console/namespaces"
        request_params = {
            "accessToken": self.access_token,
        }
        request_data = {
            "namespaceId": project_id,
        }
        resp = requests.delete(request_url, params=request_params, data=request_data)
        if "true" == resp.text:
            return True
        return False

    # #####文件
    # 查询文件列表
    def select_file_list(self, project_id):
        request_url = self.base_url + "/nacos/v1/cs/configs"
        request_params = {
            "accessToken": self.access_token,
            "pageNo": 1,
            "pageSize": self.max_page_size,

            "tenant": project_id,
            "dataId": "",
            "group": "",
            "search": "accurate",
        }
        request_data = {

        }
        resp = requests.get(request_url, params=request_params, data=request_data)
        result_text = resp.text
        try:
            result = json.loads(result_text)
        except Exception as e:
            print(result_text)
            raise e + result_text
        resp_data = result["pageItems"]
        file_list = []
        for resp_data_item in resp_data:
            file_path = resp_data_item["dataId"]
            file_content = resp_data_item["content"]
            file_list.append({
                "file_path": file_path,
                "file_content": file_content,
            })
        return file_list

    # 新增文件
    def insert_file(self, project_id, env, file_path, file_content):
        file_path = file_path.replace("/", "-")
        request_url = self.base_url + "/nacos/v1/cs/configs"
        request_params = {
            "accessToken": self.access_token,
        }
        request_data = {
            "tenant": project_id,
            "group": "DEFAULT_GROUP",
            "dataId": file_path + "-" + env,
            "content": file_content,
        }
        resp = requests.post(request_url, params=request_params, data=request_data)
        if "true" == resp.text:
            return True
        return False

    # 修改文件名
    def update_file(self):
        pass

    # 删除文件
    def delete_file(self, project_id, env, file_path):
        file_path = file_path.replace("/", "-")
        request_url = self.base_url + "/nacos/v1/cs/configs"
        request_params = {
            "accessToken": self.access_token,
        }
        request_data = {
            "tenant": project_id,
            "group": "DEFAULT_GROUP",
            "dataId": file_path + "-" + env,
        }
        resp = requests.delete(request_url, params=request_params, data=request_data)
        if "true" == resp.text:
            return True
        return False

    # #####文件内容
    # 查询nacos的文件内容
    def select_file_content(self):
        pass

    # 修改文件内容
    def update_file_content(self):
        pass
