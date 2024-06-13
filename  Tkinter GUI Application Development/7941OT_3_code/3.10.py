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



Label(root, text= 'Tkinter    Versus').grid(row=0, columnspan=2, sticky='ew')
ttk.Label(root, text='ttk').grid(row=0, column=1)


Button(root, text='tk Button').grid(row=1, column=0)
ttk.Button(root, text='ttk Button').grid(row=1, column=1)

Checkbutton(root, text='tk CheckButton').grid(row=2, column=0)
ttk.Checkbutton(root, text='ttk CheckButton').grid(row=2, column=1)


n = ttk.Notebook(root)
n.grid(row=12, column=1)
f1 = ttk.Frame(n); # you can embed other widgets into these frames
f2 = ttk.Frame(n);
n.add(f1, text='Tab One')
n.add(f2, text='Tab Two')

ttk.Progressbar(root, length = 140,value=65).grid(row=13, column=0)

ttk.Sizegrip(root).grid(row=14, column=1)# small triangular thing that can be gripped to resize the window


mytree = ttk.Treeview(root, height=2, columns=2)
mytree.grid(row=14, columnspan=2)
mytree.heading('#0', text='Column A', anchor=W)
mytree.heading(2, text='Column B', anchor=W)
mytree.column(2, stretch=0, width=70)


root.mainloop()