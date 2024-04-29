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


