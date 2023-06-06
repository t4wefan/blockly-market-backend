import os
import datetime
from pydantic import BaseModel
from check_auth import check_auth
from json import load as js_load, dump as js_dump


class ItemUpload(BaseModel):
    token: str
    token_id: int
    name: str
    desc: str
    version: str
    code: str
    body: str
    author: str


plugin_index: list
index_path = os.path.join('data', 'index.json')
with open(index_path, 'r', encoding='utf-8') as f:
    plugin_index = js_load(f)

plugin_data: dict
filepath = os.path.join('data', 'plugin_data.json')
with open(filepath, 'r', encoding='utf-8') as f:
    plugin_data = js_load(f)


def plugin_uploader(item: ItemUpload):
    # status = check_auth(token_id=item.token_id, token_content=item.token)
    # if status.status != 'ok':
    #     return {"result": status, "index": plugin_index, "data": plugin_data}

    # 从文件中读取插件的信息

    if item.name in plugin_data:
        enable_data = plugin_data[item.name]
        # 判断是否为插件作者
        if enable_data['collaborator'] != item.token_id:
            return {"result": {"status": 'error', "info": 'Not author or plugin_name error!'}, "index": plugin_index, "data": plugin_data}
        if item.version in enable_data['versions']:

            return {"result": {"status": 'error', "info": 'version error!'}, "index": plugin_index, "data": plugin_data}

        plugin_data[item.name]['versions'].append(item.version)
        for i in range(len(plugin_index) - 1):
            if plugin_index[i]['name'] == item.name:
                plugin_index[i] = {
                    "name": item.name,
                    "version": item.version,
                    "desc": item.desc,
                    "author": item.author,
                    "date": str(datetime.datetime.now())
                }
    else:
        plugin_data[item.name] = {"collaborator": item.token_id, "versions": [item.version]}
        plugin_index.append({
            "name": item.name,
            "version": item.version,
            "desc": item.desc,
            "author": item.author,
            "date": str(datetime.datetime.now())
        })
    # 更新版本信息
    plugin_data[item.name]['latest'] = item.version
    code_path = os.path.join('data', item.name)
    if not os.path.exists(code_path):
        os.makedirs(code_path)
    try:
        with open(f'{code_path}\\{item.version}.json', 'w') as f:
            js_dump({
                "name": item.name,
                "desc": item.desc,
                "version": item.version,
                "code": item.code,
                "body": item.body,
                "author": item.author
            }, f)
        with open(filepath, 'w') as f:
            js_dump(plugin_data, f)
        with open(index_path, 'w') as f:
            js_dump(plugin_index, f)
        return {"result": {"status": 'ok', "info": 'upload success'}, "index": plugin_index, "data": plugin_data}
    except FileNotFoundError :
        return {"result": {"status": 'error', "info": 'FileNotFoundError'}, "index": plugin_index, "data": plugin_data}
    except:
        return {"result": {"status": 'error', "info": 'Unknown Error'}, "index": plugin_index, "data": plugin_data}
