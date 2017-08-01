"""
    Base64 是一种用64个字符来表示任意二进制数据的方法
        Base64的原理很简单，首先，准备一个包含64个字符的数组：
        ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
        然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit（2^6=64正好表示一个字符）：
        Base64编码把3字节的二进制数据转变成了4字节的文本数据
        如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
        Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
"""
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

"""
    由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数， 
    所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
"""
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

"""
Summary:
  Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
"""

# Exercise

# 加上被处理掉的'='


def safe_base64_decode(s):
    return base64.b64decode(s+b'='*(len(s) % 4))

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
