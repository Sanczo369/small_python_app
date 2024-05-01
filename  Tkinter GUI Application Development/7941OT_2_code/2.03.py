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

######################################################################
# defining icons for compund menu demonstration
newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')
menubar = Menu(root)


root.mainloop()
