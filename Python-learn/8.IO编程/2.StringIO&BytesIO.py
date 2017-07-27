"""
    StringIO: 在内存中读写str
"""
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())

# 初始化SringIO
f2 = StringIO('hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())


"""
   BytesIO:在内存中读写二进制数据
"""

from io import BytesIO

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())

b2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b2.read())