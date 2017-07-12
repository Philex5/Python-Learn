import numpy as np
"""
关键字列表:
  array:创建数组
  dtype:指定数据类型
  zeros:填充数据为0
  ones:填充数据为1
  empty:创建数据接近0
  arrange:按指定范围创建数据
  linspace:创建线段

"""

"""创建数组"""
a=np.array([2,23,4])
print (a)

b=np.array([2,23,4],dtype=np.int)
print(b.dtype)
#int 64

c=np.array([2,23,4],dtype=np.int32)
print(c.dtype)
#int 32

"""创建特定数据"""
"""2d矩阵 2x3"""
a=np.array([[2,23,4],[2,32,4]])
print(a)

"""创建全0数组"""
"""注意是双括号"""
zero=np.zeros((3,4))
print(zero)

"""创建全1数组并指定数据类型"""
one=np.ones((3,5),dtype=float)
print(one)

"""创建全空数组，其中每个值都是接近于0得数"""
emp=np.empty((4,4))
print(emp)

"""用arrange创建连续数组"""
"""10-19的数据，2步长"""
aran=np.arange(10,20,2)
print(aran)

"""使用reshape改变数据的形状"""
re_a=np.arange(12)
re_b=re_a.reshape((3,4))
print(re_a)
print(re_b)

"""利用linspace创建线段型数据"""
"""开始端1,结束端10,且分割成20个数据，生成线段"""
lin=np.linspace(1,10,30)
print(lin.reshape(10,3))

