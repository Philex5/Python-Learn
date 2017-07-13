import numpy as np
import pandas as pd
"""

   Merge 主要用于有两组key column的数据
   -依据一组key合并
   -依据两组key合并
   -Indicator
   -依据index合并
   -解决overlapping的问题
"""
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})

"""根据key合并"""
print(pd.merge(left,right,on='key'))

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
res = pd.merge(left, right, on=['key1', 'key2'], how='outter')
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
res = pd.merge(left, right, on=['key1', 'key2'], how='right')
