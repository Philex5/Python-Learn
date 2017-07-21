def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(100))

#过深的调用会导致栈溢出
#print(fact(1000))


#练习：汉诺塔问题
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4,'A','B','C')
#神奇的汉诺塔问题啊，我自己还是写不出来，难受想哭
#