"""
    计算机网络就是把各个计算机连接到一起，让网络中的计算机可以互相通信。
    网络编程就是如何在程序中实现两台计算机的通信
    网络通信实质是两个进程之间在通信
"""
"""
   IP协议负责把数据从一台计算机通过网络发送到另一个计算机

   TIP协议建立在IP协议之上，TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
   TCP协议会通过握手建立连接，然后对每个IP包编号，确保对方按顺序收到，如果有包丢到了，就自动重发。

   许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

    一个IP包除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。

    端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。

    一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。

"""