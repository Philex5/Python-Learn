"""SQLite 与 MySQL
   SQlite的特点是轻量级、可嵌入、但不呢个承受高并发访问，是和桌面和移动应用
   而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite
"""
# 导入MySql驱动
import pymysql

conn = pymysql.connect(user='root', password='123456', database=+'test')
cursor = conn.cursor()
#cursor.execute(r"insert into test values(02, 'lebron')")
print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from test where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
