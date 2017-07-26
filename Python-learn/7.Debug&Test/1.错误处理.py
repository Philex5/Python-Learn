import logging
"""
    try机制
"""
try:
    print('try....')
    r = 10 / 0
    print('result', r)
except ZeroDivisionError as e:
    print('ZeroDivisionError: ', e)
except ValueError as e:
    print('ValueError:', e)
else:
    print('no error')
finally:     # 不管抛不抛出错误，finally后的语句始终执行
    print('finally...')
print('END')

"""
    调用堆栈
    如果不捕获错误，错误不会不断上抛到Python解释器，再由解释器打印出错误堆栈
    
    记录错误： logging
"""

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

"""
    抛出错误： raise
            捕获错误更多是为了记录，而抛出错误是为了让更上层的调用者去处理
"""

class FooError(ValueError):
    pass

def foo1(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo1('0')