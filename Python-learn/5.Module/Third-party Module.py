"""
  导入本地非当前目录文件的三种方法：
  1. 写入sys，本次有效
  2. 写入PATH环境变量，永久有效
  3. 在下级目录中添加__init__.py文件，生成包，用包名.模块名方式调用
"""

import sys
import Mod.mm.test

sys.path.append('MyDir')


print(test.abs1(-3))