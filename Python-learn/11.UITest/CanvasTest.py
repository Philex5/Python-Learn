import tkinter as tk

window = tk.Tk()
window.title('my window ')
window.geometry('500x500')

canvas=tk.Canvas(window,
                 bg='blue',
                 height=400,
                 width=400,
                 )

#只能显示gif文件,why?
image_file = tk.PhotoImage(file='/home/philex/图片/cat.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
#form(x0,y0)to(x1,y1)
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='green')
#画一个扇形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)


def moveit():
    canvas.move(oval, 0, 4)

b = tk.Button(window,
              text='move',
              command=moveit
              )

canvas.pack()
b.pack()

window.mainloop()