"""
    itertools提供了非常有用的用于操作迭代对象的函数
"""
# "无限"迭代器
"""
    count(n) :无限数自然数,间隔为n
    cycle(str) :无限重复str
    repeat(t, n) :重复t n次
"""
import itertools
natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 使用takewhile()函数截取有限序列
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

"""Chain()将一组迭代对象*串联*起来，形成一个更大的迭代器"""
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

"""groupby()把迭代器中相邻的重复元素挑出来放在一起"""
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))   # 将相同的元素当作一组

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

"""

itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator
只有用for循环迭代的时候才真正计算。


"""