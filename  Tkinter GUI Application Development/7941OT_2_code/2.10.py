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

##########################################################################

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

#######################################################################

def new_file():
    root.title("Untitled")
    global filename
    filename = None
    textPad.delete(1.0,END)
    update_line_number()

def open_file():
    global filename
    filename = tkFileDialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if filename == "": # If no file chosen.
        filename = None # Absence of file.
    else:
        root.title(os.path.basename(filename) + " - pyPad") # Returning the basename of 'file'
        textPad.delete(1.0,END)
        fh = open(filename,"r")
        textPad.insert(1.0,fh.read())
        fh.close()
    update_line_number()


root.mainloop()
