import multiprocessing as mp
#pool:进程池，Python 自动分配任务到每个核实现多进程
def job(x):
    return x*x

def multicore():
    pool=mp.Pool()
    #map函数自动分配任务CPU核
    res=pool.map(job,range(10000))
    print(res)
    #apply_async()只能传递一个值，只会放入一个核进行计算，可迭代
    res=pool.apply_async(job,(2,))
    #用get方法获取返回值
    print(res.get())
    #返回list对象
    multi_res=[pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res])
    #print(type(multi_res))


if __name__=='__main__':
    multicore()
