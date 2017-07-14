import matplotlib.pyplot as plt
import numpy as np

n = 1024  # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

"""
生成1024个呈标准正态分布的二维数据组 (平均数是0，方差为1) 作为一个数据集
并图像化这个数据集。每一个点的颜色值用T来表示
"""
T = np.arctan2(Y, X)

"""size=75 alpha透明度"""
plt.scatter(X, Y, s=75, c=T, alpha=.5)
plt.xlim(-1.5,1.5)
plt.xticks(())
plt.ylim(-1.5,1.5)
plt.yticks(())
plt.show()