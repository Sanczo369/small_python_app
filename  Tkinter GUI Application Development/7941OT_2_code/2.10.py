"""
Code illustration: 2.10
Adding Shortcut icon toolbar
Displaying Line Numbers
Highlighting Current Line

@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import tkFileDialog
import os
import tkMessageBox
root = Tk()
root.geometry('350x350')


# Displaying Line Numbers
def update_line_number(event=None):
    txt = ''
    if showln.get():
        endline, endcolumn = textPad.index('end-1c').split('.')
        txt = '\n'.join(map(str, range(1, int(endline))))
    lnlabel.config(text=txt, anchor='nw')


root.mainloop()
