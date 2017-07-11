import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

#定义一个输入框，以×显示show='*'
entry=tk.Entry(window)

text=tk.Text(window,
             height=2)

def insert_point():
    var=entry.get()
    #insert 插入到指针的位置
    text.insert('insert',var)

def insert_end():
    var=entry.get()
    #insert 插入到尾部
    text.insert('end',var)

def insert_position():
    var=entry.get()
    #insert 插入到第一行第三位
    text.insert(2.2,var)

button1=tk.Button(window,
                  text='insert point',
                  width=10,
                  height=1,
                  command=insert_point)

button2=tk.Button(window,
                  text='insert end',
                  width=10,
                  height=1,
                  command=insert_end)
button3=tk.Button(window,
                  text='insert position',
                  width=10,
                  height=1,
                  command=insert_position())


entry.pack()
button1.pack()
button2.pack()
button3.pack()
text.pack()

window.mainloop()
