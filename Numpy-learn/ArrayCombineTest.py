import numpy as np
"""
   vstack() : vertical stack 上下合并
   hstack() : horizontal  stack 左右合并
   concatenate() :多个矩阵合并，axis=1 左右合并为 axis=0 上下合并
"""
A = np.array([1,1,1])
B = np.array([2,2,2])

"""限定形状要加一层()"""
print(np.vstack((A, B)))
print(np.hstack((A, B)))


"""将只有一行的array转置"""
"""nupmy.newaxis 为ndarray增加一个轴(3,)->(1,3)"""
print(A[np.newaxis, :])
print(A.shape)
print(A[np.newaxis, :].shape)

print(A[:, np.newaxis])
print(A[:, np.newaxis].shape)


A = A[:, np.newaxis]
B = B[:, np.newaxis]
C = np.concatenate((A,B,B,A),axis=0)
print(C)
D = np.concatenate((A,B,B,A),axis=1)
print(D)

