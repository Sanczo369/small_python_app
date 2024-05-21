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

def show_info_bar():
    val = showinbar.get()
    if val:
        infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')
    elif not val:
        infobar.pack_forget()

#Displaying Line Numbers
def update_line_number(event=None):
    txt = ''
    if showln.get():
        endline, endcolumn = textPad.index('end-1c').split('.')
        txt = '\n'.join(map(str, range(1, int(endline))))
    lnlabel.config(text=txt, anchor='nw')


root.mainloop()