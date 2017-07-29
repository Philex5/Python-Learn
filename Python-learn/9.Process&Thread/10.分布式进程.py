"""
   在Thread和Process中，应当优选Process，因为Process更稳定，而且可以分布到多台机器上
   而Thread最多只能分布到同一台机器的多个CPU上

   Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
   一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
   由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

   通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了
"""

