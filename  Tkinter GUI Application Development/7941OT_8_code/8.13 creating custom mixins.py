"""
Code illustration: 8.13
Creating Custom Mixins
Tkinter GUI Application Development Hotshot
"""

from tkinter import *

def frame(parent,  row, col):
    widget = Frame(parent)
    widget.grid(row= row, column=col)
    return widget

def label(parent,  row, col, text):
    widget = Label(parent, text=text)
    widget.grid(row= row, column=col,  sticky='w', padx=2)
    return widget
