import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():
    tk.messagebox.showwarning(title='Hi', message='hahahahaha!')
    # tk.messagebox.showerror(title='Hi', message='hahahahaha!')
    # tk.messagebox.showwarning(title='Hi', message='hahahahaha!')
    # tk.messagebox.showinfo(title='Hi', message='hahahahaha!')

    print(tk.messagebox.askquestion())  # return yes or no
    """  return True or False
    print(tk.messagebox.askyesno())
    print(tk.messagebox.askretrycancel())
    print(tk.messagebox.askokcancel())
    """


tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
