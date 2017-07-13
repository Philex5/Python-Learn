import pandas as pd
import numpy as np

"""
   Numpy与Pandas的比较：
     以python的列表和字典来作比较:
       Numpy： 列表形式，没有数值标签
       Pandas： 字典形式.
     Pandas是基于Numpy构建的，让Numpy为中心得应用变得更加简单
"""

"""
   Pandas的两大数据结构：
      Series
      DataFrame
      
"""

"""
   Series:
     字符串表现形式为：index value
     如果没有手动创建，python会自动创建0-(n-1)的整数型索引
"""
series=pd.Series({3:1,4:4,5:6,'4':np.nan,'5':44,'6':1})
print(series)

"""
   DataFrame:
       表格型的数据结构，它包含一组有序得列，每列可以是不同的值类型，
       行索引：index 
       列索引：column
       行列索引可以自动生成(0 -- n-1)
"""
DataIndex=pd.date_range('20170101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=DataIndex,columns=['a','b','c','d'])
print(df)
print(df['b'])


df1=pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

"""自定义每列的内容"""
df2=pd.DataFrame({'A':np.arange(1,5),
                  'B':pd.Timestamp('20120102'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(["test","train","test","train"]),
                  'F':'foo'
                  })

print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
"""axis=1:横轴排序，axis=0:纵轴排序"""
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_values(by='A'))

df3=pd.DataFrame({
                 "Name":np.array(['LeBron','Curry','WestBrook','Durant']),
                 "Age":np.arange(27,31),
                 "Salary":np.array([30]*4,dtype='int64'),
                 "Birthday":pd.date_range('19841230',periods=4)
                 })
print(df3)






