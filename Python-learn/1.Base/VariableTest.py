
#Python 中数据类型：
#1.整型
a=100
b=0xff00
#   python中除法是精确的
c=33
print(a/c)
print(a//c)
#地板除结果为整数

#2.浮点数

#3.字符串
str='lalala'
str1="hahahh"
#字符串中有引号使用转义字符\
hello='I\'m\"OK\""'
HELLO=r'I am "OK"'

#4.布尔值 True False

#字符串编码
print(ord('A'))
#print(ord('中文'))
print(chr(66))

#!/usr/bin/python3
# _*_ coding: utf-8 _*_

print('hello %s,my name is %s'%('bob','jack'))

print('growth rate is %d %%'%7)

s1=72
s2=85
r=(85-72)/72

#控制浮点数的小数点位数
print('%.5f'%r)

s='中文-python'
print(s)
b=s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
