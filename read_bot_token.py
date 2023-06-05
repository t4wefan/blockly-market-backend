import os

def read_bot_token():
    users_dir = "users"
    token_file_path = os.path.join(users_dir, "bot_token")
    
    if os.path.exists(token_file_path):
        with open(token_file_path, "r") as f:
            token = f.read().strip()
        return token
    else:
        return ''