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

#line highlighting
def highlight_line(interval=100):
    textPad.tag_remove("active_line", 1.0, "end")
    textPad.tag_add("active_line", "insert linestart", "insert lineend+1c")
    textPad.after(interval, toggle_highlight)


def undo_highlight():
    textPad.tag_remove("active_line", 1.0, "end")

def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()

##########################################################
#Defining about method
def about(event=None):
    tkMessageBox.showinfo("About","Tkinter GUI Application\n Development Hotshot")

#Defining help method
def help_box(event=None):
    tkMessageBox.showinfo("Help","For help refer to book:\n Tkinter GUI Application\n Development Hotshot", icon='question')

def exit_editor(event=None):
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', exit_editor) # override close button and redirect to exit_editor





root.mainloop()