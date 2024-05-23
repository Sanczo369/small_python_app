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

#######################################################################
def new_file(event=None):
    root.title("Untitled")
    global filename
    filename = None
    textPad.delete(1.0,END)
    update_line_number()

def open_file(event=None):
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

# Defining save method

def save(event=None):
    global filename
    try:
        f = open(filename, 'w')
        letter = textPad.get(1.0, 'end')
        f.write(letter)
        f.close()
    except:
        save_as(event=None)

#Defining save_as method
def save_as(event=None):
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

#########################################################################
#demo of indexing and tagging features of text widget
def select_all(event=None):
        textPad.tag_add('sel', '1.0', 'end')
        return


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

    Button(t2, text="Find All", underline=0, command=lambda: search_for(v.get(), c.get(), textPad, t2, e)).grid(row=0,
                                                                                                                column=2,
                                                                                                                sticky='e' + 'w',
                                                                                                                padx=2,
                                                                                                                pady=2)

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


root.mainloop()