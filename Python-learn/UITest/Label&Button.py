import tkinter as tk

#define a window
window=tk.Tk()
window.title=('my window')
#window's width&height
window.geometry('200x100')

var=tk.StringVar()
#define a label on window
label=tk.Label(window,
               textvariable=var,
               bg='green',
               font=('Arial',10),
               width=15,
               height=2)
label.pack()
#label.place(5,0)

on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        var.set('Gakki ga daisukidesu!')
        on_hit=True
    else:
        on_hit=False
        var.set('')

#define a button
button=tk.Button(window,
                 text='hit me',
                 width=10,
                 height=1,
                 command=hit_me)
button.pack()

#keep fresh
window.mainloop()