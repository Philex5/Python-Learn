#存储进程结果Queue
#进程不能直接返回一个值
import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)

def multithreading():
    q=Queue()
    threads=[]
    data=[[1,3,4],[3,5,6],[2,8,4],[7,6,1]]
    for i in range(4):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results=[]
    for i in range(4):
        results.append(q.get())
    print(results)


if __name__=='__main__':
    multithreading()
