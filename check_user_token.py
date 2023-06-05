from read_user_token import read_user_token1 as read_user_token1
from check_user import check_user

def check_user_token(token_id, token_content):
        status = "ok"
        
        if check_user(userid=token_id) == False:
            status = 'error'
            info = 'user do not exists'
            token = ''
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