# 使用for循环来遍历ist或tuple,称之为迭代（Iteration）
from collections import Iterable

list = [1, 2, 3, 4]
for i in list:
    print(i)

tuple = (1, 2, 3, 4)
for i in tuple:
    print(i)

for ch in 'ABC':
    print(ch)

# 判断一个对象是否可迭代
print(isinstance('abc',Iterable))

# 遍历输出下标
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x,y in [(1, 1),(2,2),(3,3),(4,4)]:
    print(x, y)