"""
   强大的工具
   generator:一边循环一边计算的机制
"""

"""
Way1:把列表生成式的[]改成()
"""
g=(x*x for x in range(10))
print(g)


"""
how to print generator
 for i in range(10):
    print(next(g))

不需要用next函数，避免抛出StopIteration错误
"""

for n in g:
    print(n)

"""
way2:使用关键字yield
"""

def fib(max):
    n, a, b =0, 0, 1
    while n<max:
        # print(b)
        yield b
        a, b=b, a+b
        n = n+1
    return 'done'

f = fib(7)
print(f)
"""
 f 是一个generator
 执行next()每次执行到yield停止，下一次在从这里继续执行
 返回值只能通过StopIteration抓取
"""
while True:
    try:
        x=next(f)
        print('f',x)

    except StopIteration as e:
        print('Generator return value:',e.value)
        break



for j in f:
    print(j)


def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield (3)
    print("step 3")
    yield (5)

o = odd()
next(o)
next(o)
next(o)

"""
Excercises:杨辉三角
"""

def triangles():
    i = 1
    list=[]
    newlist=[]
    newlist.append(1)
    newlist.append(1)
    list.append(1)
    yield list
    i = i+1
    list.append(1)
    yield list
    i = i+1
    while True:
        for j in range(i-2):
            newlist[j+1] = list[j]+list[j+1]
        newlist.append(1)
        i = i+1
        #必须用copy否则就是代表同一个list，会一起变化
        list = newlist.copy()
        yield newlist

n = 0
for t in triangles():
    print(t)
    n = n+1
    if n == 10:
        break