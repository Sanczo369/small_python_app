import tkinter as tk

win = tk.Tk()

def show_values():
    a = " ".join([str(i.get()) for i in values])
    tk.Label(win, text=a).grid()

tk.Button(win, text='Show Values', command=show_values).grid(columnspan=2)

win.mainloop()