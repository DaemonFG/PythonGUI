import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def print_selection():
    value = lb.get(lb.curselection())  # 获取当前选中文本
    var1.set(value)


var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

b1 = tk.Button(window, text='point selection', width=15, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # 为变量设置值
lb = tk.Listbox(window, listvariable=var2)  # 创建listbox

list_item = ['大头','二恒','曹三狗']
for item in list_item:
    lb.insert('end',item)

lb.insert(1,'first')
lb.delete(1)

lb.pack()

window.mainloop()
