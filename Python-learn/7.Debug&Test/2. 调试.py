import logging
"""
    print打印出像确认状态的变量，只适用于简单代码
"""

"""
   断言 assert
     python3 - 0  name.py（关闭断言）
"""
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    foo('0')
"""
    logging
    指定logging的级别
        它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
        当我们指定level=INFO时，logging.debug就不起作用了
        同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
"""

logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10/n)


"""
  python调试器：pdb
  我有IDE
"""