import types
# type
print(type(123))
print(type(abs))
print(type(123) == int)


def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

# isinstance 判断继承关系
# isinstance(classA, classB)
print(isinstance('sdf', str))

# dir: 获得一个对象的所有属性和方法
# return list

print(dir('ABC'))
# __name__ :内置方法
# len('ABC') = 'ABC'.__len__()


class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

# getattr() setattr() hasattr()直接操纵一个对象的属性


class MyObject(object):
    def __init__(self):
        self.x = 0

    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
hasattr(obj, 'y')
print(getattr(obj, 'y'))
print(obj.y)

# 传入一个default参数，属性不存在返回默认值
getattr(obj, 'z', 404)

# 获得对象的方法
setattr(obj, 'x', 10)
fn = getattr(obj, 'power')
print(fn())