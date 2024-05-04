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

#transient window
t = Toplevel(root)
Label(t, text='I am a transient window of root\n I always stay on top of my parent\n I get hidden if my parent window is minimized').pack()
t.transient(root)

root.mainloop()