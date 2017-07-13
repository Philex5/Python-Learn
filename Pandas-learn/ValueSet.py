import numpy as np
import pandas as pd

df=pd.DataFrame(
                np.arange(24).reshape((6,4)),
                index=pd.date_range("20140405",periods=6),
                columns=['A','B','C','D']
               )

df.loc['20140406','B']=26
df.iloc[2,3]=234
print(df)

df.B[df.A>4]=0
print(df)
df['F']=np.arange(1,7)
df['G']=pd.Series([5,5,5,5,5,5],index=pd.date_range('20140405',periods=6))
print(df)


"""处理丢失数据"""

df.iloc[0,1]=np.nan
df.iloc[4,2]=np.nan
print(df)

"""  
    去掉有NaN的行或列，使用dropna
"""

df.dropna(
    axis=0,   #0:对行进行操作   1：对列进行操作
    how='any' #any:只要存在NaN就drop掉   all：必须全是NaN
)
"""
    将NaN用其他值代替
"""
df.fill(value=0)

"""
    判断是否有缺失数据NaN
"""
df.isnull()