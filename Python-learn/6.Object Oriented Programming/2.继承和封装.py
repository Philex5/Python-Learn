class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)

"""
    多态性：静态语言(JAVA) vs 动态语言(Python）
    JAVA: 必须是Animal及其子类的实例
    Python: 有run方法即可
            动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
"""
