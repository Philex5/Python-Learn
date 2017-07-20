"""
   使用lambda关键字定义简单的函数
"""
print(list(map(lambda x: x*x, [1, 3, 5, 7, 9])))

def build(x, y):
    return lambda: x * x + y * y
