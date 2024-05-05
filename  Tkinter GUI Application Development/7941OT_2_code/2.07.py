"""
Code illustration: 2.07

Adding
File>New,
File>Open,
File>Save
File>Save As
functionality

@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import tkFileDialog
import os
root = Tk()
root.geometry('350x350')
#######################################################################

def new_file():
    root.title("Untitled")
    global filename
    filename = None
    textPad.delete(1.0,END)



root.mainloop()