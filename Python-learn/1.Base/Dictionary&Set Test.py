a_list=[1,3,34,45,65,]
#List可以说是一种key为有序数列的字典
#key:value
#dic的查找速度极快，因为可以由key计算得到value的内存地址(hash算法)，根据地址直接取出value
#但会耗费大量的内存，是以空间换时间的一种方法

dic={'apple':1,'pear':2,'orange':3}
dic2={1:'a','c':'b'}

#remove element
del dic['pear']
dic.pop('orange')

#add element
dic['b']=20
print(dic)

#dictionary can contain a lot of element
dic3={'a':[1,2,3],'b':{'c':4}}
print(dic3)

#Set也是key：value
#Set中无重复元素
#set和dict的唯一区别仅在于没有存储对应的value
s=set([1,1,1,3,34,2,2,34])
print(s)

s.add(4)
s.remove(4)

#set可以看成是数学意义上的无序和无重复元素得集合，因此，两个set可以做数学意义上得交集及、并集等操作：
s1=set([1,2,3])
s2=set([2,3,4])

print(s1&s2)
#求并集
print(s1|s2)

#set中的key值也不可变，所以不可以是list
#turple是不可变对象
s3=set([(1,2,3),5])
dic={(1,2,3):3,'df':2}

#带list的turple是可变对象
dic={(1,[2,3]):5,'dr':3}
#s3=set([1,2,[3,5]])