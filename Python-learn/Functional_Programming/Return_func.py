def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


"""
返回的不是求和结果，而是求和函数
"""
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(*(1, 3, 5))
print(f)

print(f())

"""
  当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
"""
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


"""
   闭包：外部函数调用内部函数时，相关参数和变量都保存在返回的内部函数中
"""


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
    # 返回三个函数f
        fs.append(f)
    return fs

f1, f2, f3 = count()

# 调用f时，i已经变成了3
print(f1())
print(f2())
print(f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

"""返回一个函数时，牢记该函数并未执行，
   返回函数中不要引用任何可能会变化的变量"""