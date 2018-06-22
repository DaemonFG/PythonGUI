import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# pack
"""
tk.Label(window, text='1').pack(side='top')
tk.Label(window, text='1').pack(side='bottom')
tk.Label(window, text='1').pack(side='left')
tk.Label(window, text='1').pack(side='right')
"""

# grid
"""
for r in range(4):
    for c in range(3):
        tk.Label(window, text=2).grid(row=r, column=c,
                                      padx=10,  # 左右间距
                                      pady=10)  # 上下间距
"""

# place
tk.Label(window, text=3).place(x=20, y=10, anchor='nw')

window.mainloop()
