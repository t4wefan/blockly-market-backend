import base64
from sha1 import sha1
from read_bot_token import read_bot_token
from check_user import check_user
from save_token import save_token

def generate_token(token_id, source,):
    status = "ok"
    bot_id = read_bot_token()
    token_exists = check_user(userid=token_id)
    
    if token_exists == True:
        status = 'error'
        info = 'user already exists'
        token = ''
        print("token id:" + token_id)
        print("status:" + status)
        print("info:" + info)
        print("token:" + token)
        return {"info": info, "status": status}
    
    if source == '':
        status = 'error'
        info = 'source is required'
        token = 'denied'
        print("token id:" + token_id)
        print("status:" + status)
        print("info:" + info)
        print("token:" + token)
        return {"info": info, "status": status}
    
    elif source == bot_id:
        info = 'successfully created'
        token_0pass = bot_id + str(int(token_id) + 114514)
        token_1pass = token_0pass
        token_2pass = base64.b64encode(str(token_1pass).encode()).decode() 
        token = sha1(token_2pass)
        print("token id:" + token_id)
        print("status:" + status)
        print("info:" + info)
        print("token:" + token)
        save_token(userid=token_id, token=token)
        return {"info": info, "status": status, "token": token}

    
    else:
        status = 'error'
        info = 'unexpected error'
        token = ''
        print("token id:" + token_id)
        print(bot_id)
        print("status:" + status)
        print("info:" + info)
        print("token:" + token)
        print(token_exists)
        return {"info": info, "status": status}
    






    



