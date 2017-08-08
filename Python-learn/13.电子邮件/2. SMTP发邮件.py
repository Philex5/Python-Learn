from email.mime.text import MIMEText
import smtplib
import time

msg = MIMEText('hello, send by Python 为什么要拒收我的邮件啊？？', 'plain', 'utf-8')

# 输入Email地址和口令：
from_addr = 'philexwoo@163.com'
password = '7575818wf'
# 输入收件人地址
to_addr = '15156866015@sina.cn'
# 输入SMTP服务器地址
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)                # 打印与SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()