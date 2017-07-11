
a_list=[12,34,54,15,6,12]

# for content in a_list:
#     print(content)
#
# for index in range(len(a_list)):
#     print('index',index,'number in list=',a_list[index])

#tuple is unchangeble but list is not
a_list.append(0)
a_list[0]=1
#删除指定元素
a_list.remove(34)
#删除指定位置元素pop，无参时删除末尾元素
print(a_list.pop())
print(a_list.pop(3))

print(a_list)
#print the last one
print(a_list[-1])

a_list.insert(1,89)


#find index
print(a_list.index(12))

#sort(default:from small to big)
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)

#tuple元素不可变，但若含有list元素
# 可以通过更改list元素来实现tuple的变化
tuple1=(1,)
tuple2=(1,2,[3,4])
print(tuple2[2][1])
tuple2[2][1]='Y'
print(tuple2[2][1])
#list&tuple二维表示均为[2][1]

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
