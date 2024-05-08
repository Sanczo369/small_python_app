"""
Code illustration: 2.09
Adding About, Help Functionality
Adding 'Really Quit ?' Prompt  to exit button
@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import tkFileDialog
import os
import tkMessageBox

root = Tk()

root.geometry('350x350')

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

def new_file():
    root.title("Untitled")
    global filename
    filename = None
    textPad.delete(1.0,END)


def open_file():
    global filename
    filename = tkFileDialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
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

#Defining save_as method

def save_as():
    try:
        # Getting a filename to save the file.
        f = tkFileDialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        fh = open(f, 'w')
        textoutput = textPad.get(0.0, END)
        fh.write(textoutput)
        fh.close()
        root.title(os.path.basename(f) + " - pyPad") # Setting the title of the root widget.
    except:
        pass
        #tkMessageBox.showwarning("Cancelled", "Save Cancelled")


#########################################################################
# demo of indexing and tagging features of text widget
def select_all():
    textPad.tag_add('sel', '1.0', 'end')


root.mainloop()