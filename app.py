
from flask import Flask, request, jsonify
from check_user_token import check_user_token
from generate_token import generate_token
from check_user import check_user

# lets start
app = Flask(__name__)

def is_int(id):
    if isinstance(id, int):
        return True
    else:
        return False


@app.route('/token/create', methods=['GET', "POST"])
def generate_token_api():
    token_id = request.args.get('token_id', '')
    source = request.args.get('source', '')
    if_user_exists = check_user(userid=token_id)
    if is_int(token_id) == False:
        status = 'error'
        info = 'token_id should be a integar'
        token = ''
        return jsonify({"info": info, "status": status, "token": token}) 

    if if_user_exists == True:
        status = 'error'
        info = 'user already exists'
        token = ''
        return jsonify({"info": info, "status": status, "token": token}) 
    else:
        result = generate_token(token_id, source, )

        return jsonify(result)


@app.route('/token/check', methods=['GET', 'POST'])
def check_token_api():
    token_id = request.args.get('token_id', '')
    
    if is_int(token_id) == False:
        status = 'error'
        info = 'token_id should be a integar'
        return jsonify({"info": info, "status": status, })
    else:
        token = request.args.get('token', '')
        result = check_user_token(token_id=token_id, token_content=token)
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
