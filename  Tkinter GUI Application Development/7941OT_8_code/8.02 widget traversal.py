"""
Code illustration: 8.02

Widget Traversal
Tkinter GUI Application Development Hotshot
"""
from Tkinter import *


class TraversalDemo:
    def __init__(self, root):
        topframe = Frame(root, takefocus=1, highlightthickness=2, highlightcolor='red')
        en = Entry(topframe, width=25)
        en.grid(row=0, column=4, sticky=W)
        en.insert(END, 'Tabs jumps to next widget')
        topframe.pack(fill=X, expand=1)
        topframe.focus_force()
