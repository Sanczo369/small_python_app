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