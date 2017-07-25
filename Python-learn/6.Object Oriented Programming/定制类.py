"""
    __str__ ：修改类实例的直接输出
    __repr__ : __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串

"""
class Student(object):
    def __init__(self, name):
        self.name = name

    #相当于修改java的toString方法
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__
print(Student('Philex'))
s = Student('Philex')
print(s)

"""
    __iter__:返回一个迭代对象，使类能够像list或turple一样用于for...in循环
             Python的for循环会不断调用该迭代对象的__next__()方法拿到循环的下一值，
             知道遇到StopIteration错误推出循环。
"""

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self    # 实例本身就是

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

"""
    通过__itter()__，可以让类实例像list那样使用for循环，但不能像list[index]取任意位置数据
    而通过__getitem()__可以做到。
    
    
"""


class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a

        # 使用切片
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L



print(Fib1()[5])
print(Fib1()[5:8])

"""
    __getattr__ : 动态返回一个属性
    
"""
class Student(object):
    def __init__(self):
        self.name = 'Philex'

    # 属性不存在是自动调用 __getattr__()
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\' ' % attr)

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print(Chain().status.user.timeline.list)