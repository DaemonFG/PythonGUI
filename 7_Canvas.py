import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def move_it():
    canvas.move(rect, 0, 2)  # 横坐标移动1位，纵坐标移动2位


canvas = tk.Canvas(window, bg='blue', height=100, width=200)  # 画布
canvas.pack()

b = tk.Button(window, text='move it', width=15, height=2, command=move_it)
b.pack()

image_file = tk.PhotoImage(file='ins.gif')  # 图片文件
image = canvas.create_image(10, 10,  # 距离两侧分别为10
                            anchor='nw',  # 以左上角为基准，north west?
                            image=image_file)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)  # 坐标(50,50)到(80,80)画一条直线

oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  # 创建一个红色圆

arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30,  # 创建一个扇形
                        start=0, extent=180, fill='yellow')  # 0°-180°

rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20, fill='green')  # 创建一个矩形

window.mainloop()
