#zip将任意序列合并返回一个tuple
a=[1,2,3]
b=[4,5,6]
#return a zip object
print(zip(a,b))
#normalization
print(list(zip(a,b)))
for i,j in zip(a,b):
    print(i/2,j*2)
print(list(zip(a,a,b)))

#lambda实现一个简单的函数，实现简化代码的功能(有点内联函数的意思inline)
def fun1(a,b):
    return a+b

fun2=lambda x,y:x+y
print(fun1(2,3))
print(fun2(3,4))

#map用来将函数与参数绑定
print(map(fun1,[1],[2]))
print((list)(map(fun1,[1,3],[2,4])))

