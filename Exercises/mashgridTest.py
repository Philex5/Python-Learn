import numpy as np

x = [3, 4, 5]
y = [6, 7, 8, 9]
nx, ny = np.meshgrid(x, y)
new = np.array([nx.ravel(), ny.ravel()]).T
print(nx)
print(ny)
print(new)