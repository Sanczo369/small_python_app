#!/usr/bin/env python
"""
Code illustration: 3.11.py
tttk widgets styling and theming explained
@Tkinter GUI Application Development Hotshot
"""
from tkinter import *
import tkinter.ttk
root= Tk()
x = tkinter.ttk.Style()
x.configure('.', font='Arial 14', foreground='brown', background='yellow')
x.configure('danger.TButton', font='Times 12',foreground='red', padding=1)




root.mainloop()


