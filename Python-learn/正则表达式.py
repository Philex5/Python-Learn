"""
    正则表达式是一种用来匹配字符串的强有力的武器
    正则表达式的设计思想是：用一种描述性的语言来给字符串定义一个规则，
    凡是符合规则的字符串，我们就认为它‘匹配’了。否则就是不合法的。
"""
"""
    正则表达式匹配规则：
    
        - \d :匹配一个数字
        - \w :匹配一个字母或者数字
              eg. '\w\w\d' -> 'py3'
        - . :可以匹配任何字符
        - * :表示任意个(包括0)字符
        - + :表示至少一个字符
        - ? :表示0个或1个字符
        - {n} :表示n个字符
        - {n,m} :表示n-m个字符
    
    eg. \d{3}\s+\d{3,8}: \s+ 表示匹配至少一个空格
                          010  12345678
        \d{3}\-\d{3,8}: \表示转义
                          010-12345678 
"""
"""
    进阶：
        - [] :表示范围 [0-9] [a-z] [A-Z]
             - [0-9a-zA-Z\_] :可以匹配一个数字、字母或者下划线
             - [0-9a-zA-Z\_]+ :可以匹配至少由一个数字、字母或者下划线组成的字符串
             - [a-zA-Z\_][0-9a-zA-Z]* :可以匹配由任意字母或下划线开头，后接任意数字、字母和下划线组成的字符串
                                       即Python合法的变量
             - [a-zA-z\_][0-9a-zA-Z]{0-19}限制变量长度为1-20个字符串
             - A|B ：可以匹配A或B   (P|p)ython可以匹配的'python' or "Python'
             - ^ 表示行的开头，^\d表示必须以数字开头
             - $ 表示行的结束，$\d表示必须以数字结束
               ^philex$ ：整行匹配，只能匹配philex

"""
"""
    re模块：包含所有正则表达式的功能
           
"""
import re


# python自身和正则表达式一样，使用\转义
s = 'ABC\\-001'
print(s)
# 为避免混淆，进来使用python的r前缀表示正则表达式
s = r'ABC\-001'
print(s)


""" 判断是否匹配 """
print(re.match(r'^\d{3}-\d{3,8}$', '123-343235'))
print(re.match(r'^\d{3}-\d{3,8}$', '010 324234'))
# 匹配正确则返回match对象，否则返回None，故一般自己用if在print信息


"""   切分字符串  """
# 正常切分，无法分别连续字符
print('a,b    c'.split(' '))
print(re.split(r'\s+', 'a,b   c'))
print(re.split(r'[\s,]+', 'a,b c   d'))
print(re.split(r'[\s,;]*', 'a,b;c   d,e'))

""" 分组 ()"""
# ^(\d{3})-(\d{3,8})$ 给号码分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '012-323433')
print(m)
print(m.group(0))  # group(0)是原始字串
print(m.group(1))
print(m.group(2))
# 还可以提取子串
# 提取时间
t = '19:05:30'
m =re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

"""  贪婪匹配 ：正则匹配默认是匹配尽可能多的字符  """
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# \d+?采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

""" 编译 
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：

       1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

       2.用编译后的正则表达式去匹配字符串。
"""
# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-23423').groups())
print(re_telephone.match('010-20923').groups())


# Exercise:验证邮件地址格式


def valid(ema):

    m = re.match(r'^<(\w*\s+\w*)>([a-zA-Z]+?\w{1,20})@(\w{3,9}).([a-zA-Z]{3})$', ema)
    if m:
        print("%s@%s.%s" % (m.group(2), m.group(3), m.group(4)))
    else:
        print('incorrect format !')

valid('philexwoo@gmail.com')
valid('sdjklfkd\dfsf')
valid('<philex  woo>philexwoo@gmail.com')

