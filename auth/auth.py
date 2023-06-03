from flask import Flask, request, jsonify
from token import generate_token
from read_bot_token import read_bot_token


app = Flask(__name__)

@app.route('/token', methods=['GET'])
def make_token():
    token_id = request.args.get('token_id', '')
    source = request.args.get('source', '')

    result = generate_token(token_id, source, )
    return jsonify(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)