import tkinter as tk

win = tk.Tk()
tk.Button(win, text='Show Values', command=show_values).grid(columnspan=2)

win.mainloop()