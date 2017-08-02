"""
namedtuple
    创建一个自定义的tuple对象，并且规定了tuple元素的个数。
    很方便的定义一个数据类型，它具备tuple的不变性，还能使用属性访问

"""
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))

"""
deque
    list线性存储，索引很快，插入删除效率低
    deque是能够高校实现插入和删除操作的双向列表，适合用于对列和栈

"""
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)

"""
defaultdict
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
"""
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

"""
OrderedDict
  使用dict时，key是无序的，在迭代时无法确定key的顺序。
  要保持dict的顺序使用OrderedDict
"""
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# OrderedDict的key按插入的顺序排列，不是根据key本身
od1 = OrderedDict()
od1['z'] = 1
od1['y'] = 2
od1['z'] = 3
print(list(od.keys()))

"""
Counter
    简单的计数器
"""
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)






