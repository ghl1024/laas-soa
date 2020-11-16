import json

from flask import Blueprint

from component import mymysql

app = Blueprint('change_workflow_data', __name__,
                url_prefix='/change/workflow/struct')
"""
流程模板(结构)
"""


@app.route('/select', methods=['POST'])
def select():
    """
    查询流程模板
    :return:
    """
    data = mymysql.execute("""
    select service_type, workflow
    from workflow_struct ws
    where ws.id in (select max(id)
                    from workflow_struct
                    group by service_type)
    """)
    return json.dumps({
        'data': data,
    })


@app.route('/insert', methods=['POST'])
def insert():
    """
    新增流程模板
    :return:
    """
    return {}


@app.route('/update', methods=['POST'])
def update():
    """
    修改流程模板
    :return:
    """
    return {}


@app.route('/delete', methods=['POST'])
def delete():
    """
    删除流程模板
    :return:
    """
    return {}
