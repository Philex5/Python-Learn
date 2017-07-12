#numpy的属性
#维度：ndim
#行数和列数：shape
#元素个数：size

import numpy as np

#列表化为矩阵
array=np.array([[1,2,3],[2,3,4]])
print(array)

#查看属性：
print("number of dim:",array.ndim)
print("shape:",array.shape)
print("size:",array.size)