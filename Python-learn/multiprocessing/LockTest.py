import multiprocessing as mp
def job_P1(v,num1,l):
   l.acquire()
   for i in range(10):
       v.value+=num1
       print('job1:',v.value)
   l.release()

def job_P2(v,num2,l):
    l.acquire()
    for j in range(10):
        v.value+=num2
        print('job2:',v.value)
    l.release()

if __name__=='__main__':
    l=mp.Lock()
    #shared_variable is like a object,not the ValueType
    v=mp.Value('i',0)
    p1=mp.Process(target=job_P1,args=(v,1,l))
    p2=mp.Process(target=job_P2,args=(v,10,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()



