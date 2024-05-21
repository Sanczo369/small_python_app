"""
Code illustration: 2.12.py
Features Added:
1.	Event Handling
2.	Contextual Menu
3.      Add TitleBar Icon
@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import tkFileDialog
import os
import tkMessageBox

root = Tk()
root.geometry('350x350')
root.iconbitmap('icons/pypad.ico')

def popup(event):
    cmenu.tk_popup(event.x_root, event.y_root, 0)


root.mainloop()