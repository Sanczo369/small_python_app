"""
Code illustration: 2.05
A demonstration of different types of top-level window
@Tkinter GUI Application Development Hotshot
"""
from Tkinter import *
root = Tk()

#top level window
root.title('Toplevel Window')
root.geometry('300x300')
Label(root, text='I am the Main Toplevel window\n All other windows here are my children').pack()


root.mainloop()