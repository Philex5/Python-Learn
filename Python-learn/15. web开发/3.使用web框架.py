from flask import Flask
from flask import request

# 使用传说中的Flask框架
# WSGI的处理函数要针对每个HTTP请求进行相应，但如果URL过多且每个URL对应的请求有多种，写起来就很复杂。
# 使用web框架在WSGI接口上进一步抽象，使用web框架只需不断地编写函数

# Flask通过Python的装饰器在内部自动把URL和函数关联起来

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return """
             <form action="/signin" method="post">
             <p><input name="username"></p>
             <p><input name="password"></p>
             <P><button type="submit">Sign In</p>
             </form>
           """

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request 对象读取表单内容
    if request.form['username']=='add' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password. </h3>'


if __name__ == '__main__':
    app.run()

"""
   Other frames:
       - Django： 全能型web框架
       - web.py：一个小巧的web框架
       - Bottle：和Flask类似的web框架
       - Tornado：Facebook的开源异步web框架

"""
# 注：func_name.route(path, method)
# 目录可以代表网址的分级
# 根据方法来返回html语法的字符串
# flask使用request.form[name]来读取表单内容
