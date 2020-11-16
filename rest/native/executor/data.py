"""
执行器 执行业务

暂时为硬编码实现业务
后续改为流通数据到业务中, 执行业务
"""
import json
import threading

from bson.json_util import dumps
from flask import Blueprint

from business_hardcode.build_project import build_project
from component import form
from component import mymysql
from rest.native.executor import context

app = Blueprint('native_executor_execute', __name__,
                url_prefix='/native/executor/data')

business_hardcode_pool = {
    "1": build_project.build_project,
}
business_id_2_name = {
    "1": "build_project"
}


@app.route('/insert', methods=['POST'])
def insert():
    """
    执行业务, 向执行队列中添加一个执行任务
    :return:
    """
    request_data = form.check(['business_id', "data_id", "data_data_id"])  # 校验是否传入 业务id, 数据模型数据id
    business_id = request_data["business_id"]
    data_id = request_data["data_id"]
    data_data_id = request_data["data_data_id"]
    data_data_data = context.select_data_by_data_id__data_data_id(data_id, data_data_id)[0]
    # 持久化到数据库中
    business_name = business_id_2_name[business_id]
    # 执行器数据id, 后续包含: 执行日志、执行状态 等等
    executor_data_id = mymysql.execute("""
            insert into executor_data(business_id, business_name, data_id,
             data_data_id,data_data_data,create_by) 
             values (%(business_id)s, %(business_name)s, %(data_id)s,%(data_data_id)s,%(data_data_data)s,%(create_by)s )
        """, {
        "business_id": business_id,
        "business_name": business_name,
        "data_id": data_id,
        "data_data_id": data_data_id,
        "data_data_data": dumps(data_data_data),
        "create_by": 'tristan',
    })
    context.log(
        "执行器启动中: data_id: %s data_data_id: %s data_data_data: %s" % (data_id, data_data_id, str(data_data_data)),
        executor_data_id)
    threading.Thread(target=business_hardcode_pool[business_id],
                     args=(executor_data_id, data_data_data,)).start()
    context.log("执行器已启动", executor_data_id)
    return json.dumps({
        "executor_data_id": executor_data_id
    })
