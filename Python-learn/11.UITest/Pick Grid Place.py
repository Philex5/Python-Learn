import tkinter as tk

window=tk.Tk()
window.title('my window ')
window.geometry('200x200')
#pack
# frame=tk.Frame(window)
# frame1=tk.Frame(frame).pack(side='top')
# frame2=tk.Frame(frame).pack(side='bottom')
# tk.Label(window,text=1).pack(side='top')
# tk.Label(frame1,text=2).pack(side='bottom')

#grid
# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i,column=j,padx=10,pady=10)
#

#place
tk.Label(window,text=1).place(x=10,y=100,anchor='sw')


window.mainloop()