"""
    进程间通信是通过Queue Pipes等实现的
"""
# 以Queue为例
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待pw结束：
    pw.join()
    # pr进程是死循环(不停查看queue，有数据则读出)，无法等待其结束，只能强制中止
    pr.terminate()
