import sys
import os
from flask import Flask, request, jsonify

# get path
script_dir = os.path.dirname(os.path.abspath(__file__))
# make path
relative_path = os.path.join(script_dir, "auth")

# add path
sys.path.append(relative_path)

# import modules
from token_ import check_token
from token_ import generate_token

# lets start
app = Flask(__name__)


@app.route('/token/create', methods=['GET', "POST"])
def generate_token_api():
    token_id = request.args.get('token_id', '')
    source = request.args.get('source', '')
    result = generate_token(token_id, source, )
    return jsonify(result)


@app.route('/token/check', methods=['GET', 'POST'])
def check_token_api():
    token_id = request.args.get('token_id', '')
    token = request.args.get('token', '')
    result = check_token(token_id, token_content=token)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
