"""
    Pool(进程池)：批量创建子进程
"""
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Start Parent precess %s' % os.getpid())
    p = Pool()    # 默认值为cpu核数4
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print("Waitting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")