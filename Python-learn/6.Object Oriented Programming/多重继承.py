"""
     MixIn设计模式：在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
                  而不是设计多层次的复杂的继承关系。
     MixIn:强调“组合”，有功能类
     多重继承，强调同中有异的逻辑关系。

"""

class Animal(object):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 大类
class Manmal(Animal):
    pass


class Bird(Animal, Flyable):
    pass


# 各种动物
class Dog(Manmal, Runnable):
    pass


class Bat(Manmal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass
