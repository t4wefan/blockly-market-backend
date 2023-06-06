import datetime
import os.path
from fastapi import FastAPI
from upload import ItemUpload, plugin_uploader
import uvicorn
from json import load as js_load

app = FastAPI()

plugin_index: list
index_path = os.path.join('data', 'index.json')
with open(index_path, 'r', encoding='utf-8') as f:
    plugin_index = js_load(f)

plugin_data: dict
filepath = os.path.join('data', 'plugin_data.json')
with open(filepath, 'r', encoding='utf-8') as f:
    plugin_data = js_load(f)


@app.post('/upload')
def upload_(item: ItemUpload):
    global plugin_index, plugin_data
    res = plugin_uploader(item)
    plugin_index = res["index"]
    plugin_data = res["data"]
    return res["result"]


@app.get("/index")
def get_index():
    global plugin_index
    return {"time": str(datetime.datetime.now()), "index": plugin_index}


@app.get("/version/{name}")
def get_index(name: str):
    global plugin_data
    return plugin_data[name]["versions"]

@app.get("/usage")
async def usage():
    return '欢迎使用blockly-registry, 在这里可以分享blockly插件, 项目仅供学习交流使用，严禁用于任何商业用途和非法行为,'


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7860)
