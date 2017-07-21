#a=True
#while a:
while True:
    b=input('type something')
    if b=='1':
        #a=False
        break
    else:
        #pass
        continue

print('finish run')

sum=0
for i in range(101):
    sum=sum+i
print(sum)

L=['Bart','Lisa','Adam']
for name in L:
    print('Hello,%s !'%name)
    print('hello,',name,'l')

