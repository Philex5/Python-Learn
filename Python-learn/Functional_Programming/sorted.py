from operator import itemgetter

list = [36, 5, -12, 9, -21]
print(sorted(list))
print(sorted(list, key=abs))

StrList = ['bob', 'about', 'Zoo', 'Credit', 'Credit']
print(sorted(StrList))
print(sorted(StrList, key=str.lower))
print(sorted(StrList, key=str.lower, reverse=True))

# Exsercise 1:
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('List', 88)]




L2 = sorted(L, key = itemgetter(0))
print(L2)
print(sorted(L, key = lambda t : t[1]))
print(sorted(L, key = itemgetter(1), reverse=True))

