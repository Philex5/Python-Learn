import numpy as np

x=np.array([[[[3,4],[4,5],[8,9]]],[[[1,2],[3,4],[8,9]]]])
print(np.shape(x))
print(x)
b=np.squeeze(x[1,:,:,:])
print(np.shape(b))
print(b)
