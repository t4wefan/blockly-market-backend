import os

def read_user_token1(userid):
    users_dir = "users"
    filename = f"{userid}.json"
    token_file_path = os.path.join(users_dir, filename)
    
    if os.path.exists(token_file_path):
        with open(token_file_path, "r") as f:
            token = f.read().strip()
        return token
    else:
        return ''