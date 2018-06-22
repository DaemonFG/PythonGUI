import tkinter as tk
from tkinter import messagebox
import pickle

window = tk.Tk()
window.title('Welcome')
window.geometry('500x300')


def usr_login():
    # get user_name and user_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    # 匹配用户名和密码正确性
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usr_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usr_info = {'admin': 'admin'}
            pickle.dump(usr_info, usr_file)

    # 匹配后的相应弹窗
    if usr_name in usr_info:
        if usr_pwd in usr_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are u? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not sign up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()
        else:
            window.quit()


def usr_sign_up():
    # sign up window
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('320x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd)
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password:').place(x=10, y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm)
    entry_new_pwd_confirm.place(x=150, y=90)

    def sign_to_FG():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

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

    btn_confirm_sin_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_FG)
    btn_confirm_sin_up.place(x=150, y=130)


# welcome image
canvas = tk.Canvas(window, height=200, width=500)  # 创建画布
image_file = tk.PhotoImage(file='welcome.gif')  # 加载图片文件
image = canvas.create_image(30, 5, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name:').place(x=115, y=150)
tk.Label(window, text='Password:').place(x=115, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('exmple@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=225, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=225, y=190)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=235)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=235)

window.mainloop()