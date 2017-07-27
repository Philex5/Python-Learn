"""
    读文件
"""
try:
    f = open('file.txt', 'r')
    for i in range(13):
        s = f.read(1)
        print(s)
finally:
    if f:
        f.close()

# 简便写法： with open('file.txt', 'r') as f

"""
   read(): 一次性读取全部
   read(size): 一次读取size字节内容，return list
   read(line): 一次读取一行，用来读取配置文件比较方便
"""

"""
file-like Object

像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
除了file外，还可以是内存的字节流，网络流，自定义流等等。
file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
"""

"""
    二进制文件:图片、视频等
"""
fb = open('dogy.jpg', 'rb')
print(fb.read())

"""
     字符编码
     f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore' )
     print(f.read())
     
"""


"""
    写文件：'r'->'w' 'read'->'write'
"""