import os
# 输出系统名字
print(os.name)
# 输出详细系统信息
print(os.uname())
# 环境变量
print(os.environ)
print(os.environ.get('PATH'))


print(os.path.abspath('.'))

# 合成路径,使用join函数能避免不同操作系统路径分隔符问题(ubuntu:/,win:\
di = os.path.join('/home/philex/Experiments/Experiment1/', 'testdir')
print(di)
os.mkdir(di)
os.rmdir(di)

# 拆分路径
print(os.path.split('/home/philex/djfkls/ksjfkl/lala.txt'))
# 得到文件拓展名
print(os.path.splitext('/path/to/file.txt'))
# 对路经的合并和拆分操作并要求目录和文件真实存在，它们只对字符串进行操作

# 文件操作
# os.rename('file.txt', 'file.py')
# os.remove('file.py')


"""列出当前目录下所有文件和目录："""
print([x for x in os.listdir('.')])
"""列出当前目录下所有目录："""
print([x for x in os.listdir('.') if os.path.isdir(x)])
"""列出所有.py文件"""
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


# Exercise
def find(di, s, path):
    if os.path.isfile(di):
        if s in os.path.split(di)[1]:
            print(path)
        return
    else:
        dirs = [os.path.abspath(x) for x in os.listdir(path)]
        for fod in dirs:
            path1 = ('%s/%s' % (path, os.path.split(fod)[1]))
            find(fod, s, path1)


def findfile(s):
    dirs = [os.path.abspath(x) for x in os.listdir('.')]

    for fod in dirs:
        if os.path.isfile(fod):
            if s in os.path.split(fod)[1]:
                print("./%s" % os.path.split(fod)[1])
            else:
                continue
        else:
            path = ('./%s' % os.path.split(fod)[1])
            find(fod, s, path)

findfile('philex')

# dirs = [x for x in os.listdir('.')]
# print('3' in (os.path.split(dirs[1])[-1]))