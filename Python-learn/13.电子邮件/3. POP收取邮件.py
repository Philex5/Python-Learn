"""
    收取邮件分两步:
        1. 用poplib把邮件的原始文本下载到本地
        2. 用email解析原始文本，还原为邮件对象

"""
# POP下载邮件
import poplib

# 输入邮件地址，口令和POP3 服务器地址
email = '15156866015@sina.cn'
password = '7575818wf'
pop3_server = 'pop.sina.cn'

# 连接到POP3服务器：
server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
# 打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

# 身份验证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Message: %s.Size: %s' % server.stat())

# list()返回所有邮件的编号
resp, mails, octets = server.list()

# 可以

