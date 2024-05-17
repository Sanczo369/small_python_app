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

#theme choice

def theme(event=None):
        global bgc,fgc
        val = themechoice.get()
        clrs = clrschms.get(val)
        fgc, bgc = clrs.split('.')
        fgc, bgc = '#'+fgc, '#'+bgc
        textPad.config(bg=bgc, fg=fgc)

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

def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()


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