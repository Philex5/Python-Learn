#Gloal Variable
APPLE=100
a=None
#define a glogal variable in function body
def fun():
    global a
    a=APPLE-90
    return a+100

print("old_a",a)
print(fun())
print("new_a",a)
print(APPLE)



