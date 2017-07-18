"""
    filter(func, Iterable)用于过滤序列，func返回值决定是否舍弃Iterable中的元素
"""


def is_odd(n):
    return n % 2 == 0

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9 ])))


def not_empty(s):   # 删除一个序列中的空字符串
    return s and s.strip()

print(list(filter(not_empty,['A', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break



# Exsercise:利用filter()过滤非回数

def is_palindrome(n):
    s = str(n)
    l = len(s)
    i = 0
    while i < l//2:
        if s[i] != s[l-i-1]:
            return False
        i = i + 1
    return True


print(list(filter(is_palindrome, [1234, 12321, 909,345,67876])))

print(list(filter((lambda n : str(n)==str(n)[::-1]), [1234, 12321, 909,345,67876])))

# get str逆置新写法：[::-1]
# 列表生成式实在是太强大！

