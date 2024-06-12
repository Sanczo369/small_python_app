#!/usr/bin/env python
"""
Code illustration: 3.10.py
1. tkinter versus ttk Themed Widgets
2. new widgets introduced in ttk

@Tkinter GUI Application Development Hotshot
"""

from tkinter import *
from tkinter.ttk import *

root= Tk()

style = ttk.Style()
print(style.theme_names())
#style.theme_use('clam')

mytree = ttk.Treeview(root, height=2, columns=2)
mytree.grid(row=14, columnspan=2)
mytree.heading('#0', text='Column A', anchor=W)
mytree.heading(2, text='Column B', anchor=W)
mytree.column(2, stretch=0, width=70)


root.mainloop()