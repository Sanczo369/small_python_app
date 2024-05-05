"""
Code illustration: 2.06
A demonstration of tkFileDialog
@Tkinter GUI Application Development Hotshot
"""



from Tkinter import *
import tkFileDialog

root = Tk()

def askopenfile():
    tkFileDialog.askopenfile(mode='r')

def askopenfilename():
    tkFileDialog.askopenfilename()

def asksaveasFile():
    tkFileDialog.asksaveasfile()

def asksaveasfilename():
    tkFileDialog.asksaveasfilename()

def askDirectory():
    tkFileDialog.askdirectory()


root.mainloop()