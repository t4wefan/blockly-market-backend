import base64
from sha1 import sha1
from read_bot_token import read_bot_token
from read_user_token import read_user_token as read_user_token1
from check_user import check_user

def generate_token(token_id, source,):
    status = "ok"
    bot_id = read_bot_token()
    token_exists = check_user()
    
    if token_exists == True:
        status = 'error'
        info = 'user already exists'
        token = None
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
        return {"info": info, "status": status, "token": token}
    
    else:
        status = 'error'
        info = 'unexpected error'
        return {"info": info, "status": status}
    

def check_token(token_id, token_content):
        status = "ok"
        
        if check_user() == False:
            status = 'error'
            info = 'user do not exists'
            token = None
            print("token id:" + token_id)
            print("status:" + status)
            print("info:" + info)
            print("token:" + token)
            return {"info": info, "status": status}
        
        else:
            user_token = read_user_token1(userid=token_id)
            token = user_token
            if token_content == user_token:
                status = 'ok'
                info = 'token check passed'
                print("token id:" + token_id)
                print("status:" + status)
                print("info:" + info)
                print("token:" + token)
                return {"info": info, "status": status}
            else:
                status = 'error'
                info = 'token check not passed'
                print("token id:" + token_id)
                print("status:" + status)
                print("info:" + info)
                print("token:" + token)
                return {"info": info, "status": status}




    



