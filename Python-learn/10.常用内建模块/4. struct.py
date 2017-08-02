"""
    struct :解决bytes和其他二进制数据类型的转换
"""
# Python中，将一个32位无符号整数变成字节，也就是4个长度的bytes
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >>8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# 使用struct
import struct
struct.pack('>I', 1024009)
