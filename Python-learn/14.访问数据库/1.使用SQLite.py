"""SQLite是一个嵌入式数据库，它的数据库就是一个文件。
   由于SQLite本身是C写的，而且体积很小，
   所以，经常被集成到各种应用程序中，甚至在IOS和Android的APP中都可以集成
"""
# 导入驱动
import sqlite3
# 连接到SQLite数据库，数据库是test.db文件
conn = sqlite3.connect('test.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
#cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user(id,name) values (\'1\',\'Michael\')')
print(cursor.rowcount)
cursor.execute('select * from user where id=?', ('1',))
values= cursor.fetchall()
print(values)
cursor.close()
conn.close()
