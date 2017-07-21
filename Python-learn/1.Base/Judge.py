# condition=1
# while condition<10:
#     print(condition)
#     condition=condition+1
#
# #while True:
# #    print("I'm True!")

example_list=[1,2,3,4,5,6,7,32,3423,65]
example_list[0]=3
for i in example_list:
    print(i)

for i in range(3,20,2):
    print(i)

x=4
y=2
z=3
if x>y:
    print("x>y")
elif x>z:
    print()
else:
    print("")

height=1.80
weight=80.5
bmi=weight/(height**2)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')
