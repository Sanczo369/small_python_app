"""
Code illustration: 2.11
Adding infoBar at bottom
Adding Color Theme
@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import tkFileDialog
import os
import tkMessageBox

root = Tk()
root.geometry('350x350')


def show_info_bar():
    val = showinbar.get()
    if val:
        infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')
    elif not val:
        infobar.pack_forget()


# About menu - Aboutus, Help
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command=about)
aboutmenu.add_cascade(label="Help", command=help_box)
menubar.add_cascade(label="About",  menu=aboutmenu)


#creating icon toolbar
icons = ['new_file' ,'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo','on_find', 'about']
for i, icon in enumerate(icons):
    tbicon = PhotoImage(file='icons/'+icon+'.gif')
    cmd = eval(icon)
    toolbar = Button(shortcutbar, image=tbicon, command=cmd)
    toolbar.image = tbicon
    toolbar.pack(side=LEFT)



shortcutbar.pack(expand=NO, fill=X)

lnlabel = Label(root,  width=2,  bg = 'antique white')
lnlabel.pack(side=LEFT,  fill=Y)


#
# Adding Text Widget & ScrollBar widget
#

textPad = Text(root, wrap=WORD, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll=Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT,fill=Y)

########################################


#Creating Info Bar // widget within text widget
infobar = Label(textPad, text='Line: 1 | Column: 0')
infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')

#Add events
textPad.bind("<Any-KeyPress>", update_line_number)
textPad.tag_configure("active_line", background="ivory2")

root.mainloop()