import copy
a=[1,2,[3,4,5]]
#ShallowCopy
b = a
print(id(a))
print(id(b))
a[1]=22
print(a)
print(b)

# copy 方法深拷贝一层list
c = copy.copy(a)
print(id(a)==id(c))
print(id(a[2])==id(c[2]))


# DeepCopy
d=copy.deepcopy(a)
print(id(a) == id(d))
print(id(a[2]) == id(d[2]))
