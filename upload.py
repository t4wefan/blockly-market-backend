import os
from pydantic import BaseModel
from check_user_token import check_user_token
from json import load as js_load, dump as js_dump
class Item_upload(BaseModel):
    token: str
    token_id: int
    name: str
    desc: str
    version: str
    code: str
    body: str
    author: str
    contact: str

def upload(item:Item_upload):
    status = check_user_token(token_id=item.token_id, token_content=item.token)
    if status.status !='ok':
        return status
    # 从文件中读取插件的信息
    filepath = os.path.join('data', 'plugin_data.json')
    with open(filepath,'r',encoding='utf-8') as f:
        plugin_data: dict = js_load(f)
    enable_data = plugin_data[item.name]
    if enable_data:
        # 判断是否为插件作者
        if enable_data['collaborator'] != item.token_id:
            return {"status":'error',"info":'Not author or plugin_name error!'}
        if enable_data['version'] == item.version:
            return {"status":'error',"info":'version error!'}
        plugin_data[item.name]['version'].append(item.version)
    else:
        plugin_data[item.name]={"collaborator": item.token_id,"versions": [item.version]}
    # 更新版本信息
    plugin_data[item.name]['latest']=item.version
    with open(filepath,'w') as f:
        js_dump(plugin_data,f)
    code_path = os.path.join('data', item.name,item.version)
    with open(code_path,'w') as f:
        js_dump(item,f)
    return {"status":'ok',"info":'upload success'}