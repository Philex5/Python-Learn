import tkinter as tk

#frame 用于布局
window=tk.Tk()
window.title('my window ')
window.geometry('300x300')

tk.Label(window,text="on the window",
               width=20,
               ).pack()

#主框架
frame=tk.Frame(window)

frame1=tk.Frame(frame)
frame2=tk.Frame(frame)

frame.pack()
frame1.pack(side='left')
frame2.pack(side='right')

tk.Label(frame1,
         text="on the frame 1",
               width=20,
               ).pack()

tk.Label(frame2,
         text="on the frame 2",
               width=20,
               ).pack()

window.mainloop()