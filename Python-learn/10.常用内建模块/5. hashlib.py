import hashlib
"""
    hashlib提供了常见的摘要算法，如MD5,SHA1等、
    什么是摘要算法呢？
    摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串-摘要digest（通常用16进制的字符串表示）
"""

# 计算一个字符串的MD5值
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to ust sha1 in'.encode('utf-8'))
sha1.update('python hashlib'.encode('utf-8'))
print(sha1.hexdigest())

"""
    摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
    只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
"""

# Exercise 用户登录验证
import re, json

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

print(get_md5('wf19951005'))



def register(username, password):
    try:
        with open(r'./data.txt', 'r') as f:
            db = json.load(f)
    except:
        db = {}
    dbr = db
    if not re.match('^\w+$', username):
        print('username is invalid')
        return
    elif not re.match('^\w+$', password):
        print('password is invalid')
        return
    elif username in dbr.keys():
        print('user has registered')
        return
    else:
        dbr[username] = get_md5(password + username + 'the-Salt')
    with open('./data.txt', 'w') as f:
        json.dump(dbr, f)
        print('register success!')
    return


def login(user, password):
    db = {}
    try:
        with open('./data.txt', 'r') as f:
            db = json.load(f)
    except:
        print('Dict do not exist.')
        return
    if user not in db:
        print('user has not registered')
        return
    if db[user] == get_md5(password + user + 'the-Salt'):
        print('login in success!')
    else:
        print('login in failed!')
    return

register(' ', 'dfsfdas')
login('philex', 'wf19951005')
register('philex', '19951005')
register('michael', '12345678')
login('philex', '19951005')
login('michael', 'helloworld')
login('mi', 'helloworld')



