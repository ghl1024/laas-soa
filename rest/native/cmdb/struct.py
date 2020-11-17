import json

from flask import Blueprint

from component import form
from component import mymysql

app = Blueprint('native_cmdb_struct', __name__,
                url_prefix='/native/cmdb/struct')


@app.route('/select', methods=['POST'])
def select():
    request_data = form.check(["did"])
    return json.dumps(mymysql.execute("""
                select id, code, meaning, reference_type, is_open_data, data_type, default_value
                from designer_data_struct
                where did = %(did)s
    """, request_data))


@app.route('/insert', methods=['POST'])
def insert():
    request_data = form.check(["did", "code", "meaning", "reference_type"])
    code = request_data['code']
    # insert column to data data
    mymysql.execute(
        'ALTER TABLE designer_data_data_%(did)s ADD COLUMN ' + code + ' VARCHAR(255) DEFAULT NULL COMMENT %(meaning)s;',
        request_data)

    return json.dumps(mymysql.execute("""
                insert into designer_data_struct(did, code, meaning, reference_type
                , is_open_data, data_type, default_value) 
                values (%(did)s, %(code)s, %(meaning)s, %(reference_type)s
                , %(is_open_data)s, %(data_type)s, %(default_value)s)
    """, request_data))


@app.route('/update', methods=['POST'])
def update():
    request_data = form.check(
        ["did", "code", "meaning", "reference_type", "is_open_data", "data_type", "default_value"])
    old_code = request_data['code']
    code = request_data['code']
    if request_data.__contains__("old_code"):
        old_code = request_data['old_code']
    # update column to data data
    mymysql.execute(
        'ALTER TABLE designer_data_data_%(did)s change ' + old_code + ' ' + code
        + ' VARCHAR(255) DEFAULT NULL COMMENT %(meaning)s;',
        request_data)
    return json.dumps(mymysql.execute("""
                update designer_data_struct 
                set code = %(code)s 
                    ,meaning = %(meaning)s 
                    ,reference_type = %(reference_type)s 
                    ,is_open_data = %(is_open_data)s
                    ,data_type = %(data_type)s
                    ,default_value = %(default_value)s
                where id = %(id)s
    """, request_data))


@app.route('/delete', methods=['POST'])
def delete():
    request_data = form.check(["id"])
    code = request_data['code']
    # delete column to data data
    mymysql.execute(
        'ALTER TABLE designer_data_data_%(did)s drop ' + code,
        request_data)

    return json.dumps(mymysql.execute("""
                delete from designer_data_struct
                where id = %(id)s
    """, request_data))
