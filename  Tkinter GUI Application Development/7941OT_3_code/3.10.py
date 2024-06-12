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

n = ttk.Notebook(root)
n.grid(row=12, column=1)
f1 = ttk.Frame(n); # you can embed other widgets into these frames
f2 = ttk.Frame(n);
n.add(f1, text='Tab One')
n.add(f2, text='Tab Two')


mytree = ttk.Treeview(root, height=2, columns=2)
mytree.grid(row=14, columnspan=2)
mytree.heading('#0', text='Column A', anchor=W)
mytree.heading(2, text='Column B', anchor=W)
mytree.column(2, stretch=0, width=70)


root.mainloop()