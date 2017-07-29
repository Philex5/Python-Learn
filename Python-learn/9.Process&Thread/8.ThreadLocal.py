import threading

"""
  每个线程都有的对应的同名局部变量，不共享。
  通过ThreadLocal对象来获取每个线程对应的该变量

  一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
   ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
"""

"""
    Lock解决了线程间的全局变量修改问题
    ThreadLocal解决了线程内部函数之间参数传递问题
"""


#  创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程相关的student：
    std = local_school.student
    print('hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Philex',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Jack',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

