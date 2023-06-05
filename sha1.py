import hashlib

def sha1(text):
    # 创建 SHA1 哈希对象
    sha1 = hashlib.sha1()

    # 更新哈希对象的输入
    sha1.update(text.encode('utf-8'))

    # 返回 SHA1 哈希值的十六进制表示形式
    return str(sha1.hexdigest())