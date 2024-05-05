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


def open_file():
    global filename
    filename = tkFileDialog.askopenfilename(defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filename == "":  # If no file chosen.
        filename = None  # Absence of file.
    else:
        root.title(os.path.basename(filename) + " - pyPad")  # Returning the basename of 'file'
        textPad.delete(1.0, END)
        fh = open(filename, "r")
        textPad.insert(1.0, fh.read())
        fh.close()


# Defining save method

def save():
    global filename
    try:
        f = open(filename, 'w')
        letter = textPad.get(1.0, 'end')
        f.write(letter)
        f.close()
    except:
        save_as()


root.mainloop()