class Calculator:
    name = 'Great Wall'
    price = 18
    # init function
    def __init__(self,name,price,height,width,weight=20):
        self.n = name
        self.p = price
        self.h = height
        self.wid = width
        self.wei = weight
        self.add(2, 3)
    # self uses own properties
    def add(self, x, y):
        print(self.n)
        print(x+y)
    def minus(self,x,y):
        print(x-y)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

cal = Calculator("good", 18, 17, 8)
print(cal.p)


