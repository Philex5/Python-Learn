# text="""This is my first test
# This is next line
# This is last line
# """
# append_text='\nThis is appended file!'
#
# #打开文件
# my_file=open('my file.txt','w')
# #内容写入
# my_file.write(text)
# #内容追加
# my_file.write(append_text)
#
# #关闭文件
# my_file.close()

file=open('my file.txt','r')
content=file.readlines()
line=file.readline()
print(content)
