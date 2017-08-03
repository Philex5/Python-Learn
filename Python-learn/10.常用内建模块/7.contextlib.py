"""
  with open('/path/file', 'r') as f: 能够简略的使用资源
  并不是只有open()函数能够使用with语句
  只要实现了上下文管理的方法__enter__和__exit即可
"""


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(selfself, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

"""
    一种更简单的方法，使用contextlib
"""
from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    # @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
    print('End')


with create_query('Bob') as q:
    q.query()

"""
    使用@contextmanager,在某段代码执行前后自动执行特定代码
"""
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)

with tag("h1"):
    print('hello')
    print('world')
# 先执行yield之前的代码，在执行with内部代码，最后执行yield后面的代码

"""
    @closing 将没有实现上下文的对象变为上下文对象
"""
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print('line')

@contextmanager
def clossing(thing):
    try:
        yield  
    finally:   
        thing.close()


"""
   想在某些代码执行前后搞点事（打开/关闭文件），就找@contextlib！
"""
