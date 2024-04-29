"""
Code illustration: 2.02
Text Editor Code
Step 3: Adding  Menu items to each menu
Step 4: Adding labels to hold shortcut toolbar and line number
@Tkinter GUI Application Development Hotshot
"""
from Tkinter import *
root = Tk()
#
# Step 2 & Step 3: Adding Menu Bar and adding menu drop down choices
#

#defining icons for compund menu demonstration
newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')
menubar = Menu(root)

# File menu,for open,save,save as and quit
filemenu = Menu(menubar, tearoff=0 )
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT, image=newicon, underline=0  )
filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, image=openicon, underline =0)
filemenu.add_command(label="Save", accelerator='Ctrl+S',compound=LEFT, image=saveicon,underline=0)
filemenu.add_command(label="Save as",accelerator='Shift+Ctrl+S')
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator='Alt+F4')
menubar.add_cascade(label="File", menu=filemenu)

#Edit menu - Undo, Redo, Cut, Copy and Paste
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",compound=LEFT,  image=undoicon, accelerator='Ctrl+Z')
editmenu.add_command(label="Redo",compound=LEFT,  image=redoicon, accelerator='Ctrl+Y')
editmenu.add_separator()
editmenu.add_command(label="Cut", compound=LEFT, image=cuticon, accelerator='Ctrl+X')
editmenu.add_command(label="Copy", compound=LEFT, image=copyicon,  accelerator='Ctrl+C')
editmenu.add_command(label="Paste",compound=LEFT, image=pasteicon, accelerator='Ctrl+V')
editmenu.add_separator()
editmenu.add_command(label="Find",underline= 0, accelerator='Ctrl+F')
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator='Ctrl+A')
menubar.add_cascade(label="Edit", menu=editmenu)

