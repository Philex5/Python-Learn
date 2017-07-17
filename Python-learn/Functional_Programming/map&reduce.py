"""
   Iterator=map(func, Iterable)
"""
from functools import reduce


def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# int->str
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

"""
   reduce(f,[x1, x2, x3, x4]) = f(f(f(x1,x2),x3),x4)
"""


def add(x, y):
    return x+y

print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x*10+y

print(reduce(fn, [1, 3, 5, 7, 9]))


def str2int(s):
    def fn(x, y):
        return x*10+y

    def char2num(s):
        return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('4568456'))

# return list[(int)]
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int1(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))


""" 练习 """

# Qustion 1
def normalize(name):
    L = ''
    # i = 0
# L.append(name[i].upper())
# append会使str断开,使用str的+操作

    # L = L + name[i].upper()
    # while i < len(name)-1:
    #     i = i + 1
    #     L=L + name[i].lower()
    L = L + name[0].upper()
    L = L + name[1:].lower()
    return L


L1 = ['adam', 'jACk', 'berT']
print(list(map(normalize, L1)))

# Qustion 2


def prod(L):

    return reduce(lambda x, y: x*y, map(char2num, L))

print(prod('235'))

# Qustion 3


def str2float(s):
    s1 = s.split('.')
    def char2int1(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def minus_mul(m):
        re = 0
        count = 0
        for i in m:
            re = re + i * pow(10, -(count+1))
            count = count + 1
        return re

    flo = reduce(lambda x, y: x*10+y, map(char2int1, s1[0]))
    flo = flo + minus_mul(map(char2int1, s1[1]))
    return flo

print(str2float('123.456'))
