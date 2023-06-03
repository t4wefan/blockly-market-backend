import json
import os
import time


def save_token(userid, token):
    path = "users"
    if not os.path.exists(path):
        os.makedirs(path)

    filename = f"{userid}.json"
    status = "success"

    data = {
        "preset_id": userid,
        "content": token,
        "create_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        
    }

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        json.dump(data, f,)
        result = json.dumps(data,)
        print( result )
        return data
        
