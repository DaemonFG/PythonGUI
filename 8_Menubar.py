import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

counter = 0


def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter += 1


menubar = tk.Menu(window)  # 在窗口上方创建一个菜单栏

filemenu = tk.Menu(menubar,  # 定义一个空菜单单元
                   tearoff=0)  # 能否被分开
menubar.add_cascade(label='File', menu=filemenu)  # 将上面定义的空菜单命名为File，放在菜单栏中
filemenu.add_cascade(label='New', command=do_job)  # 加入下拉小菜单
filemenu.add_cascade(label='Open', command=do_job)
filemenu.add_cascade(label='Save', command=do_job)

filemenu.add_separator()  # 菜单的分割线

filemenu.add_cascade(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar,  # 定义一个空菜单单元
                   tearoff=0)  # 能否被分开
menubar.add_cascade(label='Edit', menu=editmenu)  # 将上面定义的空菜单命名为Edit，放在菜单栏中
editmenu.add_cascade(label='Copy', command=do_job)  # 加入下拉小菜单
editmenu.add_cascade(label='Cut', command=do_job)
editmenu.add_cascade(label='Paste', command=do_job)

submenu = tk.Menu(editmenu)
editmenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu1', command=do_job)

l = tk.Label(window, bg='yellow', text='')
l.pack()

window.config(menu=menubar)

window.mainloop()
