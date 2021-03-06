"""
    TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据
    相比TCP,UDP则是面向无连接的协议

     使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
    虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

"""
import socket
# 使用UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
    # 接收数据

    data, addr = s.recvfrom(1024)
    print('Received from %s:%s. ' % addr)
    # 使用UDP,发送要用sendto，而且还要指明地址
    s.sendto(b'hello, %s' % data, addr)

"""
    UDP与TCP的端口不冲突，可以各自绑定！
"""
