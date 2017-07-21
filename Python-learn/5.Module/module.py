"""
   一个文件中的代码越写越长会不容易维护
   为了写出可维护的代码，把函数进行分组，分别放到不同的文件中，每个文件包含的代码就相对较少。
   每一个.py文件都是一个模块(Module)
   使用模块的好处：
        - 提高了代码的可维护性
        - 避免了函数名和变量冲突，不同的模块可以有相同的函数名和变量名，不用担心冲突
   需要避免的冲突：
        - 与内置函数名的冲突
        - 与python自带的模块名的冲突
        - 相同模块名的冲突：
            放在不同的包下即可，在目录下新建一个__init__.py(可以为空)文件即可让当前目录成为一个包
            可以通过backpageName.ModuleName来调用模块
             __init__.py也是一个模块，它的名字是包名
"""

""" 使用模块化"""
__author__ = 'Philex Wu'
import sys


def test():
    args = sys.argv  # argv:用list存储了命令行的所有参数，至少含有1个参数(该py文件的名称)
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments')

if __name__ == '__main__':
    test()

"""
   作用域：
       不希望被引用的非公开函数和变量：_xxx
       封装private性质的函数，隐藏实现细节
          def func1()
          def func2
          def interface():
              return  state, fun1,func2 
"""