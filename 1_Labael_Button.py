import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

# here are contents of window
l1 = tk.Label(window,
              text='OMG! this is Tk!',  # text of label
              bg='green',  # color of background
              font=('Arial', 12),  # font size & type
              width=15, height=2)  # width ang height of label
l1.pack()

var = tk.StringVar()
on_hit = False  # Fasle first


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me!')
    else:
        on_hit = False
        var.set('')


l2 = tk.Label(window,
              textvariable=var,  # textvariabel can be changed
              bg='pink',
              font=('Arial', 12),
              width=15, height=2)
l2.pack()

b = tk.Button(window,
              text='hit me',
              width=15, height=2,
              command=hit_me)  # command after hitting the button)
b.pack()

window.mainloop()
