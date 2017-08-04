import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

var=tk.StringVar()
label=tk.Label(window,
               text='   ',
               bg='yellow',
               width=20,
               )

def print_selection():
    #config方法更改text属性
    label.config(text='you have selected'+var.get())

button=tk.Button(window,
                 height=2

                 )
#set variable=value
rb1=tk.Radiobutton(window,
                  text='Option A',
                  variable=var,
                  value='A',
                  command=print_selection)


rb2=tk.Radiobutton(window,
                  text='Option B',
                  variable=var,
                  value='B',
                  command=print_selection)


rb3=tk.Radiobutton(window,
                 text='Option C',
                  variable=var,
                  value='C',
                  command=print_selection)

label.pack()
rb1.pack()
rb2.pack() 

window.mainloop()



