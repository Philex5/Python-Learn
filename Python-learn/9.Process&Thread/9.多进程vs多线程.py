"""
     实现多任务，通常采用Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。

     如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

     如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

     - 多进程比较稳定，只要主进程不挂(只分配任务，挂掉概率低)，程序就不会挂，但开销巨大（特别是没有fork的windows下）
     - 多线程比多进程快一点，但存在致命缺点：一个线程挂，整个程序就挂掉了


"""