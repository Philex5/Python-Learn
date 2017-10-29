import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as np

mat1 = '/media/philex/Data/fMRI_MT/train_data_1/t_1_9.mat'
data = sio.loadmat(mat1)
m = data['nii_img_u16_sqz']

# count = 0
# for i in range(90):
#     for j in range(109):
#         for k in range(90):
#             if m[i][j][k] > 0:
#                 print(m[i][j][k])
#                 count = count + 1
#
# print(count)

"""不能画出，这里的xyz是坐标值，不是三个特征值"""
# x, y, z = m[:, 0], m[:, 1], m[:, 2]
# print(np.shape(x))
# print(np.shape(y))
# print(np.shape(z))
#
# fig = plot.figure()
# ax = Axes3D(fig)
#
# ax.scatter(x, y, z, c='g')
#
# ax.set_zlabel('Z')
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plot.show()
