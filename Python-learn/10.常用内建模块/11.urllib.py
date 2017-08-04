"""
    urllib提供了一系列用于操作URL的功能
"""
"""
    request模块可以很方便的抓取URL内容：也就是发送一个GET请求到指定界面，然后返回HTTP的响应
"""
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

