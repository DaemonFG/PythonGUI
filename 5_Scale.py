import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def print_selection(v):
    l.config(text='You have selected ' + v)


l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
