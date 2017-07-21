"""
    装饰器(Decorator):在代码运行期间动态增加功能的方式
    相当于为已有函数添加功能（比如打印日志），相当于添加装饰
    decorator 是一个返回函数的高阶函数
"""

import functools
# 定义一个能打印日志的decorator


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
# 相当于执行了: now = log(now)
def now():
    print('2015-3-25')

now()


# 如果decorator本身需要传入参数
# 那就需要编写一个返回decorator的高阶函数
# 三层嵌套

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
# 相当于： now = log('execute')(now)
def now():
    print('2015-3-25')

now()
# 名字改变了？
print(now.__name__)


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log3
def now():
    print('2015-3-25')

now()
print(now.__name__)

# Exercise


def logE(text=' '):
    def decorator(func):
        def wrapper(*args, **kw):
            functools.wraps(func)
            print('begin call !')
            if text == '':
                print('call'+'%s()' % func.__name__)
            else:
                print('%s %s()' % (text, func.__name__))
            print('end call !')
            return func(*args, **kw)
        return wrapper
    return decorator


@logE()
def now():
    print("2017-7-20")


@logE('Execute')
def nowT():
    print("2017-7-20")

now()

nowT()