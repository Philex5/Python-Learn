"""
   可迭代对象(Iterable)：可以直接作用于for循环的数据类型
   包括：
      - 集合数据类型，如list tuple dict set str
      - generator，() and generator function(yield)
"""
from collections import Iterable
from collections import Iterator

"""判断一个对象是否是Iterable对象"""
print(isinstance((x for x in range(10)), Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(100, Iterable))

"""判断一个对象是否是Iterator"""
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(100, Iterator))

""" 
    能够直接使用for循环是 Iterable
    能够调用next()函数是 Iterator
    
list dict str 是Irerable，但不是Iterator
可以通过调用iter()使它们变成Iterator  
   for循环本质就是先iter(Iterable),再不断调用next(i)
"""
print(isinstance(iter({}),Iterator))





