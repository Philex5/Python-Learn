import numpy as np
"""
    np.split(): 等量分割，axis=1,纵向 axis=0 横向
    np.array_split() 不等量分割
    np.vsplit()：横向分割
    np.hsplit(): 纵向分割

"""

A=np.arange(12).reshape(3,4)
print(A)

print(np.split(A,2,axis=1))
print(np.split(A,3,axis=0))

print(np.array_split(A,3,axis=1))
print(np.hsplit(A,2))
print(np.vsplit(A,3))
