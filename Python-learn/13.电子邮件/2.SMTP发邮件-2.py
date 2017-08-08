"""
    邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，
    所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib


def _format_addr(s):   # 格式化一个邮件地址,注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令：
from_addr = 'philexwoo@163.com'
password = '7575818wf'
# 输入收件人地址
to_addr = '15156866015@sina.cn'
# 输入SMTP服务器地址
smtp_server = 'smtp.163.com'

"""发送文本"""
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
"""发送HTML"""
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#                '<p>send by  <a href="http://www.python.org">Python</a>...</p>' +
#                '</body></html>', 'html', 'utf-8')

""" 发送附件
带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
所以，可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
再继续往里面加上表示附件的MIMEBase对象即可：
"""
msg = MIMEMultipart()

# 邮件的正文是MIMEText
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
"""发送图片
要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
"""
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>'
                    + '</body></html>', 'html', 'utf-8'))


# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('./kaer.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型
    mime = MIMEBase('image', 'jpg', filename='kaer.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='kaer.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment', '0')

    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


"""发送文本和Html
msg = MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

"""

msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....', 'utf-8').encode()  # 含有中文要进行编码

"""加密SMTP
实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件，Gmail必须加密传输
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

"""

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

"""
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
"""