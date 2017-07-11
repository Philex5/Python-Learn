import math
def function():
    print("This is a script!")
    a=1+2
    print(a)

def function(a,b):
    c=a*b
    print(a)
    print('the c is ',c)


def sale_car(price,brand,color='red',is_second_hand=True):
    print('price',price,
          "brand",brand,
          "color",color,
          "is_second_hand",
          is_second_hand
          )
def my_abs(x):
    #参数检查
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

#函数返回多个值(返回一个turple)
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

def quadraitc(a,b,c):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2

sale_car(1000000,'BMW','blue')
print(my_abs(-3.6))
x,y=move(100,100,60,math.pi/6)
r=move(100,100,60,math.pi/6)
print(r)
print(x,y)

print(quadraitc(1,5,6))