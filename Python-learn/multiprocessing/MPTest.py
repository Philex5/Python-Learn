#多进程
import multiprocessing as mp
#多线程
import threading as td
import time

def job(q):
    result=0
    for i in range(100000):
        result+=i+i**2+i**3
    q.put(result)

#效率对比多进程vs多线程
def multicore():
  q=mp.Queue()
  p1=mp.Process(target=job,args=(q,))
  p2=mp.Process(target=job,args=(q,))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  res1=q.get()
  res2=q.get()
  print("This is the multiCore:",res1+res2)

def Normal_Work():
    result=0
    for i in range(2):
        for i in range(100000):
            result+=i+i**2+i**3


def multithread():
    q=mp.Queue()
    t1=td.Thread(target=job,args=(q,))
    t2=td.Thread(target=job,args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1=q.get()
    res2=q.get()
    print("This is the multiThread:",res1+res2)

if __name__=='__main__':
    st=time.time()
    Normal_Work()
    st1=time.time()
    print("normal cost time:",st1-st)
    multithread()
    st2=time.time()
    print("multithread cost time:",st2-st1)
    multicore()
    st3=time.time()
    print("multicore cost time:",st3-st2)

#Running_Time: 多进程 < 普通 < 多线程