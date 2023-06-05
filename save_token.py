import os


def save_token(userid, token):
    path = "users"
    if not os.path.exists(path):
        os.makedirs(path)

    filename = f"{userid}.json"

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        f.write(token)
        print(f"Token {token} saved to file {filename}")
