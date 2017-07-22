"""
    面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的执行。为了简化程序设计，
                      面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统复杂度。
    面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接受其他对象发过来的消息，并
                      处理这些消息。计算机程序的执行就是一系列消息在各个对象之间传递。

"""
#  定义一个Student类，继承于object类


class Student(object):
    def __init__(self, name, score):
        self._name = name           # '_'表示变量为'private',但还是可以从外界访问的，自由的python
        self._score = score

    # 数据封装，避免从外界直接访问属性；
    # 数据和逻辑被封装起来，也便于调用，不需要知道内部实现的细节
    def print_score(self):
        print('%s: %s' % (self._name, self._score))

    def get_score(self):
        if self._score >= 90:
            return 'A'
        if self._score >= 60:
            return 'B'
        else:
            return 'C'

    # getter and setter
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_score(self, score):
        if 0<= score <= 100:
            self._score = score
        else:
            return ValueError('bad score')

# 类的实例化
bart = Student('Bart Simpson', 60)
print(bart.print_score())
print(bart.get_score())

# Python允许对实例变量绑定任何数据，也就是说，同为一个类的实例，属性可能会不同
mary = Student('lisa', 79)
mary.age = 12
print(mary.age)

# 类属性和实例属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student1(object):
    def __init__(self, name):
        self.name = name
s = Student1('Bob')
s.score = 90


class Student2(object): # 类属性
    name = 'Student'

# 实例属性与类属性同名会覆盖类属性，自身不能再访问