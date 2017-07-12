import numpy as np
"""
 "="赋值会使array有相关性（同一地址），一变皆变
 要使用np.copy()
"""
a=np.arange(12)
b=a
c=a
d=b
a[10]=23
print(d)

e=a.copy()
a[3]=12
print(e)
