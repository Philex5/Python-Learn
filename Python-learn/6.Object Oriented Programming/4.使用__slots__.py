from types import MethodType

class Student(object):
    pass

# 创建一个类实例后，我们可以为这个实例绑定任何属性和方法
s = Student()
s.name = 'jack'


def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 但这对其他实例是不起作用的
s2 = Student()
# s2.set_age(23)  error

# 为了给所有实例绑定方法，可以给class绑定方法
Student.set_age = set_age
s2.set_age(23)
print(s2.age)

# 动态绑定允许我们在程序运行的过程中动态给类加上功能

"""
   使用__slots__可以限制实例能添加的属性
   只对当前类有效，对其子类无效
"""


class student(object):
    __slots__ = ('name', 'age')

s3 = student()
s3.name = 'philex'
s3.age = 25
# s3.score = 90 has error

