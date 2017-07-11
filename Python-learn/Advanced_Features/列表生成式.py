#List Comprehensions
import os

print(list(range(1,11)))

print([x*x for x in range(1,11)])
print([x*x for x in range(1,20) if x%2==0])
print([m+n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('/home/philex/SegNet')])

d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k+'='+v)

print([k+'='+v for k,v in d.items()])
L=['HEllo','World','IBM','APPLE']
print([s.lower() for s in L])

L1=['Hello','World',18,'Apple',None]
L2=[]
for l in L1:
    if isinstance(l,str):
        L2.append(l.lower())
    else:
        continue

print(L2)

#使用列表生成式简介太多了，厉害！
print([l.lower() for l in L1 if isinstance(l,str)])
