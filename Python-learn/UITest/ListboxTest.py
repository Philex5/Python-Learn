import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

var1=tk.StringVar()

label=tk.Label(window,
               textvariable=var1,
               bg='yellow',
               width=4)

def print_selection():
    value=listbox.get(listbox.curselection())
    var1.set(value)


button=tk.Button(window,
                 text='print selection',
                 width=15,
                 height=1,
                 command=print_selection)

varlist=tk.StringVar()
varlist.set((11,22,33,44))
listbox=tk.Listbox(window,listvariable=varlist)
list_items=[1,2,3,4]
for item in list_items:
    listbox.insert('end',item)

listbox.insert(1,'first')
listbox.insert(2,'second')
listbox.delete(2)






label.pack()
button.pack()
listbox.pack()
window.mainloop()
