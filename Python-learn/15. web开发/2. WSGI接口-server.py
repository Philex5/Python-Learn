from wsgiref.simple_server import make_server
# 导入之前编写的application函数
from hello import application
import sys
sys.path.append('./')

# 创建一个服务器，IP地址为空，端口为8000， 处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()