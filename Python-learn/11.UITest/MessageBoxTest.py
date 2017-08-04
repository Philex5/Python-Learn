import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title('my window ')
window.geometry('300x300')

def pop_up():
   # 提示框
   #messagebox.showinfo(title='Hi',message='lalalalalalalal')
   #警告框
   #messagebox.showwarning(title='warning',message='大事不好了！')
   #异常框
   # messagebox.showerror(title='Error',message='A error cause the stopping!')
   #询问框,return yes or no
   #print(messagebox.askquestion(title='Asking',message='Are you a man?'))
   #return True or False
   #print(messagebox.askyesno(title='Asking', message='Are you a man?'))
   #return True or False
   print(messagebox.askretrycancel(title='Asking', message='Are you a man?'))
   #return True or False
   print(messagebox.askokcancel(title='Asking', message='Are you a man?'))

button=tk.Button(window,
                 text="Pop-Up",
                 width=20,
                 command=pop_up)
button.pack()

window.mainloop()