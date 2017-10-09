"""
    协程，又称微线程，纤程。英文名Coroutine
    协程相当于线程中的子线程，类似于程序与子程序的关系，但是不同之处在于协程可以中断运行跳到其他协程之后在回来继续执行
    这一点子程序无法做到。
    使用协程效率极高，也没有多进程中锁机制的烦扰。
    子程序就是协程的一种特例
    Python中的协程通过generator实现
"""


def consumer():
    r = ''
    while True:
        n = yield r  # 返回r 接收n
        # if not n:
        #     return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 启动生成器,第一次yield
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s..' % n)
        r = c.send(n)     # 切换到consumer
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
"""
  整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务
"""
