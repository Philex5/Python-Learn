import os
# 输出系统名字
print(os.name)
# 输出详细系统信息
print(os.uname())
# 环境变量
print(os.environ)
print(os.environ.get('PATH'))


print(os.path.abspath('.'))

# 合成路径
di = os.path.join('/home/philex/Experiments/Experiment1/', 'testdir')
print(di)
os.mkdir(di)
