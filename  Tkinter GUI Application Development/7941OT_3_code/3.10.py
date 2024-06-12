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

root.mainloop()