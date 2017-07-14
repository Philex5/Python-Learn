import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=2*x+1

plt.figure(num=1,figsize=(8,5))
plt.plot(x,y)

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0+1
"""(x0,0)->(x0,y0)"""
plt.plot([x0, x0], [0,y0],'k--',linewidth=2.5,)
"""set dot styles"""
plt.scatter([x0, ], [y0, ],s=50,color='b')

"""
标注方式1：使用annotate
   xycoords='data' 是说基于数据的值来选位置,
   xytext=(+30, -30)  xy 偏差值
   textcoords='offset points' 对于标注位置的描述 
    arrowprops是对图中箭头类型的一些设置.



"""
plt.annotate(r'$2x+1=%s$'% y0, xy=(x0,y0),xycoords='data',
             xytext=(+30,-30),textcoords='offset points',
             fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

"""标注方式2：使用text"""
plt.text(-3.7,3,r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'green'})

plt.show()