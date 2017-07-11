#generator:一边循环一边计算的机制

#Way1:把列表生成式的[]改成()
g=(x*x for x in range(10))
print(g)

#how to print generator
for i in range(10):
    print(next(g))

#不需要用next函数，避免抛出StopIteration错误

