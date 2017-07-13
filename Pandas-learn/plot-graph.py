import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
    Series 可视化
"""
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()
#plt.plot(x=,y=)
data.plot()
plt.show()


"""
    Dataframe 可视化
"""
data=pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list("ABCD"),)
data=data.cumsum()
data.plot()
plt.show()

ax=data.plot.scatter(x='A',y='B',color='DarkBlue',label='class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='class2',ax=ax)
plt.show()