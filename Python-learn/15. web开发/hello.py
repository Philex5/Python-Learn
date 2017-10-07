"""
    WSGI: Web Server Gateway Interface
    要求一个web开发者实现一个函数，就可以相应HTTP请求
    使我们专注于生成HTML文档，不用接触到TCP连接、HTTP原始请求和响应格式
"""


def application(environ, start_response):
    start_response('200 OK', [('ContentType', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# environ: 一个包含所有HTTP请求信息的dict对象
# start_response: 一个发送HTTP相应的函数


"""
无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
HTTP请求的所有输入信息都可以通过environ获得
HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
"""








