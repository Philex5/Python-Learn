import numpy as np
import pandas as pd

"""
    常用选择数据的方法：
      - 简单的筛选
      - 根据标签： loc
      - 根据序列： iloc
      - 根据混合的这两种: ix
      - 通过判断的筛选
    
"""
df=pd.DataFrame(np.arange(24).reshape(6,4),
                index=pd.date_range('20170623',periods=6),
                columns=['A','B','C','D'])

print(df)

"""简单筛选"""
#print(df['A'])
print(df.A)
"""      按行选择"""
print(df[0:2])
print(df['20170623':'20170625'])


"""按标签选择"""
print(df.loc['20170624'])

"""        : 表示所有行"""
print(df.loc[:,['A','B']])
print(df.loc['20170625',['A','B']])


"""位置选择iloc"""
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])
print(df.iloc[[2,4,5],1:4])


"""混合选择"""
print(df.ix[:3,['A','C']])

"""使用判断"""
print(df[df.A>8])
