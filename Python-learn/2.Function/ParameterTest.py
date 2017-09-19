#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n=n-1
        s=s*x
    return s

#默认参数应设置为不变值，以免在不断的调用中发生变化


#可变参数
def calc1(numbers):
#numbers 为turple or list
    sum=0
    for i in numbers:
        sum=sum+i
    return sum


def calc2(*numbers):
#将传入的值组装成一个turple
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

numbers=(1,2,3)
calc1(numbers)

calc2(1,2,3)

#将turple转化为可变参数传入
calc2(*numbers)


#关键字参数
def person(name,age,**kw):
    print('name',name,'age:',age,'other:',kw)






#输入格式为key=value,将传入参数组合为一个dict
person('jack','20',city='New York')
extra={'city':'Beijing','job':'Engineer'}
person('Tom','21',**extra)

#关键字参数可以拓展函数功能，在必需的信息之外还能获得用户可以选择提供的信息，例如用户注册功能


#命名关键字参数
#命名关键字参数用来限制关键字参数的名字
#筛出可选信息中的可用部分？有名字的可选信息
#之前有可变参数可以省略×号

def person(name,age,*,city,job):
    print(name,age,city,job)

person('jack','20',city='Beijing',job='Engineer')

#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

f1(1,2)
f1(1,2,3,1,2,3,job='OL')
f2(1,2,d='jack',ext=None)

args=(1,2,3,4)
args1=(1,2,3)
kw={'d':99,'x':'w'}
f1(*args,**kw)
f2(*args1,**kw)

#任意函数都可以通过类似func(*args,**kw)的形式调用
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。