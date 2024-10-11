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
