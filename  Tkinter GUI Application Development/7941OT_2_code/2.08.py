"""
Code illustration: 2.08
A demonstration of tkMessageBox
@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import tkMessageBox

root = Tk()
fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side':LEFT, 'padx': 2, 'pady': 3}


fr1.pack()
fr2.pack()

root.mainloop()
