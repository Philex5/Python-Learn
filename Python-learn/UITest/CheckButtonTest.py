import tkinter as tk

window=tk.Tk()
window.title('CheckButton')
window.geometry('200x200')

var1=tk.IntVar()
var2=tk.IntVar()

label=tk.Label(window,
               bg="green",
               text='',
               width=20)

def print_selection():
    label.config(text=var1.get())
    if var1.get()==1&var2.get()==1:
        label.config(text="I love both!")
    elif var1.get()==1&var2.get()!=1:
        label.config(text="I love only Python!")
    elif var1.get()!=1&var2.get()==1:
        label.config(text="I love only C++!")
    else:
        label.config(text="I do not love either! ")

cb1=tk.Checkbutton(window,
                  text='Python',
                  #多选框，设置变量的方式(variable=onvalue/offvalue)
                  # 与单选框Radiobutton不同(variable=value)
                  variable=var1,
                  onvalue=1,   #if choosen set variable=1
                  offvalue=0,
                  command=print_selection)
cb2=tk.Checkbutton(window,
                   text='C++',
                   variable=var2,
                   onvalue=1,  # if choosen set variable=1
                   offvalue=0,
                   command=print_selection
                   )



label.pack()
cb1.pack()
cb2.pack()

window.mainloop()