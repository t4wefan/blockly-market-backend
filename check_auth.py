import requests

url = 'https://auth.t4wefan.pub//token/check'


def check_auth(token_id, token_content):
    auth = requests.get(f'{url}?token_id={token_id}&token={token_content}')
    return auth.json()
