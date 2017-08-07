"""
    Socket是网络编程的一个抽象概念。
    通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
"""
import socket

"""客户端："""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:IPv4 AF    AF_INET:IPv6
# SOCK_STREAM： 面向流的TCP协议

s.connect(('www.sina.com.cn', 80))

"""
    由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
    其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。
    端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
    
"""

# 发送数据
s.send(b'GET / HTTP/1.1\rnHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')

# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

buffer = []
while True:
    # 每次最多接收1K字节：
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)


"""  服务器端： """
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection....')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % (sock, addr))


while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()





