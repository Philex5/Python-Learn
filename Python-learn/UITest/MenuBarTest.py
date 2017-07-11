import tkinter as tk

# 窗口选项条MenuBar
window=tk.Tk()
window.title('my window ')
window.geometry('500x500')

menubar=tk.Menu(window)

def do_job():
 label.config(text='do it')
#tearoff 是否可以拆分
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Quit',command=window.quit)

EditMenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=EditMenu)
EditMenu.add_command(label='Cut',command=do_job)
EditMenu.add_command(label='Copy',command=do_job)
EditMenu.add_command(label='Paste',command=do_job)

second=tk.Menu(EditMenu,tearoff=0)
EditMenu.add_cascade(label='Second',menu=second)
second.add_command(label="test1",command=do_job)
second.add_separator()
second.add_command(label="test2",command=do_job)

label=tk.Label(window,
               bg='yellow',
               width=20,
               text="")

window.config(menu=menubar)
label.pack()

window.mainloop()