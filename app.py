
from fastapi import FastAPI
from pydantic import BaseModel
from upload import Item_upload
from typing import Union
from check_user_token import check_user_token
from generate_token import generate_token
from check_user import check_user
from upload import upload
import uvicorn

# lets start
app = FastAPI()

class Item_create(BaseModel):
    token_id: int
    source: Union[bool, None] = None
class Item_check(BaseModel):
    token_id: int
    token: str
@app.post('/token/create')
def generate_token_api(item:Item_create):
    token_id = item.token_id
    source = item.source
    if_user_exists = check_user(userid=token_id)
    if if_user_exists == True:
        status = 'error'
        info = 'user already exists'
        token = ''
        return {"info": info, "status": status, "token": token, }
    else:
        return generate_token(token_id, source, )

@app.post('/token/check')
def check_token_api(item:Item_check):
    token_id = item.token_id
    token = item.token
    return check_user_token(token_id=token_id, token_content=token)

@app.post('/upload')
def upload(item:Item_upload):
    return upload(item)

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0', port=7860)
