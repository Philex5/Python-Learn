"""
    收取邮件分两步:
        1. 用poplib把邮件的原始文本下载到本地
        2. 用email解析原始文本，还原为邮件对象

"""

# POP下载邮件
import poplib
from collections import namedtuple
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 输入邮件地址，口令和POP3 服务器地址
email = 'philexwoo@163.com'
password = '7575818wf'
pop3_server = 'pop.163.com'

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

# 可以查看返回的列表类似[b'1 82923', b'2 2194',...]
print(mails)

# 获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index) # 循环使用可以拿到每一封邮件内容

# 可以根据邮件索引号直接冲服务器删除邮件
# server.dele(index)

# lines 存储了邮件的原始文本每一行，可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')

""" 解析邮件"""
# 将邮件内容解析为Message对象
msg = Parser().parsestr(msg_content)


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):  # 检测编码，否则非UTF-8编码的邮件都无法正常显示
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# Message对象可能是MIMEMutipart对象，包含嵌套的其他MIMEBase对象
# 嵌套可能还不止一层，所以要递归地打印出Message对象
# indent 用于缩进显示
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From ', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s　<%s>' % (name, addr)
            print('%s%s: %s' %  (' ' * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s------------------------' % ('  '* indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type =='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment:%s' % ('  '*indent, content_type))

print_info(msg)
# 关闭连接
server.quit()





