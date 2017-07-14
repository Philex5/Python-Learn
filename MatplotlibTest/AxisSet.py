import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
l1 = plt.plot(x,y2,label='up')
l2 = plt.plot(x,y1,color='green',linewidth=1.0,linestyle='--',label='down')

"""
   使用plt.xlim设置x坐标轴范围：(-1, 2)
   使用plt.ylim设置y坐标轴范围：(-2, 3) 
   使用plt.xlabel设置x坐标轴名称：’I am x’
   使用plt.ylabel设置y坐标轴名称：’I am y’；
   
"""
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')

"""
   使用xticks设置x轴刻度
   使用yticks设置y轴刻度
"""

new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)

plt.yticks([-3,-2,-1,1.22,3],[r'$really\ bad$', r'$bad$',
                                r'$normal$',r'$good$'
                                r'$really\ good$'])
"""
   使用plt.gca获取当前坐标轴信息
   使用.spines设置边框
   使用.set_color设置边框颜色：默认黑色
 
"""
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('blue')


ax.xaxis.set_ticks_position('bottom')

ax.yaxis.set_ticks_position('left')

"""
使用.spines设置边框：y轴
使用.set_position设置边框位置:x=0的位置
（位置所有属性：outward，axes，data）
"""

ax.spines['left'].set_position(('data',0))


plt.legend(loc='upper right')
plt.show()




