"""
全局鉴权
"""
import time

import requests
from flask import request

import config
from exception import MyServiceException

SOA_TOKEN_STR = "Laas-Soa-Token"

local_memory_token_record = {}


def record_2_local_memory(token, user_id):
    global local_memory_token_record
    local_memory_token_record[token] = {"timestamp": (time.time()), "user_id": user_id}


def query_token_by_remote(token):
    # 请求授权接口
    oauth_url = config.app_conf["oauth"]["url"]
    resp = requests.get(oauth_url + "/permission/verification_token", {
        "token": token
    })
    result = resp.json()
    if not result or len(result) < 1:
        raise MyServiceException("请求令牌查询失败, 请重新登录")
    for item in result:
        record_2_local_memory(token, item["user_id"])
        break


def do_auth():
    if SOA_TOKEN_STR not in request.headers:
        raise MyServiceException("未登录的请求")
    token = request.headers[SOA_TOKEN_STR]
    # url_root = request.url_root # 请求的根路径, 包含请求协议、域名、端口
    if token in local_memory_token_record:
        local_memory_token_record_value = local_memory_token_record[token]
        if int(time.time()) < local_memory_token_record_value["timestamp"] - 7 * 24 * 60 * 60:
            return
    query_token_by_remote(token)


def wrap_authentication():
    do_auth()
