import matplotlib.pyplot as plt
import numpy as np
import time

x = np.linspace(-10,10,40)
y1 = x**2+4
y2 = 3*x+5

""" 定义一个图像窗口"""

plt.figure()
plt.plot(x,y1)
plt.show()
time.sleep(3)
plt.close()


plt.figure(num=3,figsize=(8,5),)
plt.plot(x, y1)
plt.plot(x, y2,color='red',linewidth=1.0,linestyle="--")
plt.show()


