import threading
from time import *

def T1_job():
    print("T1 start \n")
    for i in range(10):
        sleep(0.1)
    print("T1 finished \n")
def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

def main():

    thread1=threading.Thread(target=T1_job,name='T1')
    thread2=threading.Thread(target=T2_job,name="T2")
    thread1.start()
    #thread1.join()
    thread2.start()
    print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())

    #join到主线程#
    #执行完thread再执行之后的操作
    thread1.join()
    thread2.join()
    print('all done\n')


if __name__=='__main__':
    main()