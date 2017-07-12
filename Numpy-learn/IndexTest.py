import numpy as np
A=np.arange(3,15)
print(A[3])

a=[3,5,6,4,7,8,9,10]
print(a[4])

"""
永远记住范围表达式包括左边不包括右边
"""
B=np.arange(4,16).reshape((3,4))
print(B)
print(B[1,1:3])
"""list必须要用两个[]，而numpy.array可以只用一个[]"""
a=[[3,5,6],[4,7,8,9,10]]
print(a[1][0:3])

"""
  for循环默认逐行打印
  逐列打印可以先转置矩阵
"""
for row in B:
    print(row)

"""B.T 等价于 B.transpose()"""
for column in B.T:
    print(column)

"""
   flatten()将多维矩阵展开为1列
"""
C=B.flatten()
print(C)