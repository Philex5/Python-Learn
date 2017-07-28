"""
    序列化： 把变量从内存中编程可存储或传输的过程
           Python中叫pickling,Java中叫serialization,其他还有marshalling、 flattening
    序列化后，就可以把序列化后的内通写入磁盘，后者通过网络传输到其他机器
"""
"""
    使用Pickle
    并且可能不同版本的Python彼此都不兼容
    因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
"""
# pickle.dumps()方法把任意对象序列化成一个bytes
# pickle.dump()直接把对象序列化后写入一个file-like Object
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('philex1.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('philex1.txt', 'rb')
d = pickle.load(f)
f.close()
print(d, '\n')

"""
    使用JSON
    在不同编程语言中传递对象，就必须把对象序列化为标准格式,比如xml,
    但JSON是更好的方法，因为JSON表示出来就是一个字符串，可以被任何语言读取
    而且JSON速度比XML快、还能直接在Web界面中读取，十分方便
"""
# python -> json
import json
d = dict(name='Bob', age=20,score=88)
dj = json.dumps(d)
print(dj)

# json -> python
json_str = '{"age":20, "score":18, "name":"Bob"}'
print(json.loads(json_str))

# Python 的dict对象直接可以序列化为JSON的{}，list->[], int ,double ,str均可直接序列化

# JSON序列化class对象

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s)) Error:无法直接序列化为JSON的对象

# 先将Student实例转化为dict


def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

print(json.dumps(s, default=student2dict))

# 还可以利用class实例的__dict__属性(除定义了__slots__属性)
# print(json.dumps(s, default=lambda obj:obj.__dict__))


# class实例反序列化


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = ' {"name": "ayase", "age": 20, "score": 95}'
print(json.loads(json_str, object_hook=dict2student))

