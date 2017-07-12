import numpy as np

a=np.array((10,20,30,40))
print(a)
b=np.arange(2,10,2)
print(b)
print(a-b)
"""+ - * / // **"""
print(10*np.sin(a))
print(b<3)

"""二维计算"""
a_2d=np.array([[1,2],[3,4]])
b_2d=np.arange(4).reshape(2,2)
print(a_2d)
print(b_2d)

"""二维数组乘法
1. 对应位置元素相乘
2. 线性代数-矩阵相乘
"""
print(a_2d*b_2d)
print(np.dot(a_2d,b_2d))

"""sum() min() max() TEST"""

ran=np.random.random((2,4))*10
print(ran)
print(np.sum(ran))
print(np.max(ran))
print(np.min(ran))

"""
  对指定行列进行操作
  axis=1: 以行作为查找单元
  axis=0: 以列作为查找单元
"""
print("sum =",np.sum(ran ,axis=1))
print("max =",np.max(ran,axis=0))
print("min =",np.min(ran,axis=1))


"""
  argmin(): 矩阵中最小元素索引
  argmax(): 矩阵中最大元素索引
  mean(): 求解均值
  average(): 求解均值
  median(): 求解中位数
  cumsum():累加函数（累加：从起始项到该项的元素和）
  diff():累差函数后一项与前一项之差
  sort():对每一行从小到大排序
  transpose():矩阵转置操作
  
"""
A=np.arange(2,14).reshape((3,4))
print(np.argmin(A))
print(np.argmax(A))
print(A.cumsum())
print(np.transpose(A))

