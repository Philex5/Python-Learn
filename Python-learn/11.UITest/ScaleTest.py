import tkinter as tk

window=tk.Tk()
window.title('scale test')
window.geometry('200x200')

label=tk.Label(window,
               bg='yellow',
               text='  ',
               font=('Arial',15),
               width=10
               )


def print_selection(v):
    label.config(text=v)

var=tk.StringVar()
scale=tk.Scale(window,
               label='try me',
               #not from
               from_=5,
               to=11,
               orient=tk.HORIZONTAL,
               length=200,
               showvalue=1,
               variable=var,
               tickinterval=2,
               resolution=0.01,
               command=print_selection)
               #自动将数值传到命令函数

label.pack()
scale.pack()

window.mainloop()