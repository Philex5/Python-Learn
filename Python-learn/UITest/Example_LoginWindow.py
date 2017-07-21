import tkinter as tk
from tkinter import messagebox
import pickle

window=tk.Tk()
window.title("Welcome to Philex's Homepage ")
window.geometry("400x350")

canvas=tk.Canvas(window,height=200,width=500)
image_file=tk.PhotoImage(file="/home/philex/图片/welcome.gif")
image=canvas.create_image(0,0,anchor="nw",image=image_file)
canvas.pack(side='top')

#user information
tk.Label(window,text='UserName:').place(x=50,y=210)
tk.Label(window,text='Password:').place(x=50,y=250)

var_usr_name=tk.StringVar()
var_usr_name.set('example@python.com')
var_usr_password=tk.StringVar()
var_usr_password.set("sfdfasdfafd")
entry_name=tk.Entry(window,textvariable=var_usr_name)
entry_name.place(x=160,y=210)
entry_passw=tk.Entry(window,textvariable=var_usr_password,show='*')
entry_passw.place(x=160,y=250)


#Login 2.Function
def usr_login():
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_password.get()
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb')as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
        if usr_name in usrs_info:
            if usr_pwd==usrs_info[usr_name]:
                tk.messagebox.showinfo(title="Welcome",message="Login Success!")
            else:
                tk.messagebox.showinfo(title="Error", message="Login Success!")

        else:
            is_sign_up=messagebox.askyesno('Welcome',message="you have not sign up!")
            if is_sign_up:
                usr_sign_up()


#Sign up 2.Function
def usr_sign_up():
    def sign_to_python():
        np = new_pwd.get()
        npf = new_pwd_comf.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_comf = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm Password: ').place(x=10, y=90)
    entry_usr_pwd_comf= tk.Entry(window_sign_up, textvariable=new_pwd_comf, show='*')
    entry_usr_pwd_comf.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_python)
    btn_comfirm_sign_up.place(x=150, y=130)


btn_login=tk.Button(window,text="Login",command=usr_login)
btn_login.place(x=170,y=300)

btn_sign_up=tk.Button(window,text="Sign Up",command=usr_sign_up)
btn_sign_up.place(x=240,y=300)

window.mainloop()
