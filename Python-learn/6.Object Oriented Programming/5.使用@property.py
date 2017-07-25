"""
直接使用属性：
     s.score = 90
     print(s.score)
     很方便但无法检查参数

传统的方法：
     setter: s.set_score(90) (包括参数检查)
     getter: s.get_score()

使用@property： 既能检查参数， 又可以用类似属性这样简单的方式访问类的变量

"""

class Student(object):

    @property
    def score(self):
        return self._score      # 相当于getter()

    @score.setter
    def score(self, value):     # 相当于setter
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

s1 = Student()
s1.score = 90
print(s1.score)

"""  声明只读变量:
           @property
           def calc(self):
               return  self._score*2

"""
# Exercise
class Rectangle():
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must is a in')
        if value < 0:
            raise ValueError('width must > 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must is a in')
        if value < 0:
            raise ValueError('height must > 0')
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

r = Rectangle()
# r.width = -10
r.width = 10
r.height =10
print(r.width)
print(r.resolution)