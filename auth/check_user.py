import os

def check_user(userid):
    filename = f"{userid}.json"
    status = True if os.path.isfile(filename) else False
    return status