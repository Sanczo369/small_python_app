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

def on_find():
    t2 = Toplevel(root)
    t2.title('Find')
    t2.geometry('262x65+200+250')
    t2.transient(root)
    Label(t2, text="Find All:").grid(row=0, column=0, sticky='e')
    v = StringVar()
    e = Entry(t2, width=25, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    e.focus_set()
    c = IntVar()
    Checkbutton(t2, text='Ignore Case', variable=c).grid(row=1, column=1, sticky='e', padx=2, pady=2)
    Button(t2, text="Find All", underline=0, command=lambda: search_for(v.get(), c.get(), textPad, t2, e)).grid(
        row=0, column=2, sticky='e' + 'w', padx=2, pady=2)
    def close_search():
        textPad.tag_remove('match', '1.0', END)
        t2.destroy()
    t2.protocol('WM_DELETE_WINDOW', close_search)  # override close button

def search_for(needle, cssnstv, textPad, t2, e):
    textPad.tag_remove('match', '1.0', END)
    count = 0
    if needle:
        pos = '1.0'
        while True:
            pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
            if not pos: break
            lastpos = '%s+%dc' % (pos, len(needle))
            textPad.tag_add('match', pos, lastpos)
            count += 1
            pos = lastpos
        textPad.tag_config('match', foreground='red', background='yellow')

    e.focus_set()
    t2.title('%d matches found' % count)


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