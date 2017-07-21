"""
    当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数
    这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
    这个函数就是偏函数！
    可以用来固定常用的参数，比如某些属性
"""
import functools

print(int('12345'))

# 八进制转十进制
print(int('12345', base=8))

print(int('12345', 16))

# 定义一个函数传入base，后面转化就不必每次都要加base


def int2(x, base=2):
    return int(x, base)

print(int2('1011010'))
print(int2('100000'))

p_int2 = functools.partial(int, base=2)
print(p_int2('11110000'))

max2 = functools.partial(max, 10)
# 最大值为之前固定住的10，有点意思
print(max2(1, 5, 6, 8))