"""
   多线程与多进程最大的不同在于：
       多进程中，同一变量，各有一分拷贝存在于每个进程中，互补应吸纳该
       多线程中，所有变量由所有线程共享，任何一个变量都可以被任何一个线程修改
"""
import time,threading
balance = 0


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):  # 保证执行次数够多
        change_it(n)



"""
  修改balance需要多条语句，而执行这几条语句时，线程可能中断
  初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8
"""
# 给change_it()上锁，保证一个线程修改变量之后其他线程才能访问该变量
lock = threading.Lock()

def run_thread1(n):
    for i in range(10000):
        # 先要获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

"""
  Python的线程是真正的线程，但解释器执行代码时，
  有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
  然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
  这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
  所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
  执行与cpu核数相同的死循环也只能跑满一个核，
  而其他语言比如C\C++或Java能把全部核心跑满

def deadloop(x):
    while True:
        x = x ^ 1

t1 = threading.Thread(target=deadloop, args=(5,))
t2 = threading.Thread(target=deadloop, args=(6,))
t3 = threading.Thread(target=deadloop, args=(9,))
t4 = threading.Thread(target=deadloop, args=(4,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()


Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
多线程的并发在Python中就是一个美丽的梦
但多进程可以使用多核
"""