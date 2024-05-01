"""
Code illustration: 2.03
Leveraging power of text widget built-in options
@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
root = Tk()
root.geometry('350x350')

########################################################################
# Levaraging built in text widget functionalities

def undo():
    textPad.event_generate("<<Undo>>")

def redo():
    textPad.event_generate("<<Redo>>")

def cut():
    textPad.event_generate("<<Cut>>")

def copy():
    textPad.event_generate("<<Copy>>")

def paste():
    textPad.event_generate("<<Paste>>")


root.mainloop()
