import numpy as np
import pandas as pd

"""
   基本合并方式concat
     -axis: 合并方向
     -ignore_index: 重置index
     -join： 合并方式（只留下共有or全留下）
     -join_axes： 依照axes合并
     -append： 添加数据

"""
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['d','f','g','h'])

"""
cancat纵向合并(axis=0)
ignore_index=True,重置index

"""
res=pd.concat([df1,df2,df3],axis=0)
print(res)

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)


print(pd.concat([df1,df3],axis=0))
print(pd.concat([df1,df3],axis=1,join_axes=[df1.index]))

"""只留下共有的"""
print(pd.concat([df1,df3],axis=0,join="inner"))

print(df1.append(df2,ignore_index=True))
