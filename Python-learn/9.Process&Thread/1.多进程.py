"""
    对操作系统来说，一个任务就是一个进程，比如打开一个浏览器就是启动一个浏览器进程，打开两个记事本就是启动了两个进程。
    有些进程不知同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，
    就要同时运行多个“子任务”，我们把进程内的这些子任务成为“线程”

"""
"""
    多任务的三种实现方式：
        - 多进程模式
        - 多线程模式
        - 多进程+多线程模式  

"""
import os

#
# fork()函数调用一次返回两次
# 当前进程（父进程）返回子进程ID
# 子进程永远返回0
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

print('Process (%s) start ...' % os.getpid())
pid = os.fork()

if pid == 0:
    print('I am child process(%s) and my parent is %s'% (os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process(%s).' % (os.getpid(), pid))



