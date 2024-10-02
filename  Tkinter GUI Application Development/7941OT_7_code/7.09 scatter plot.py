"""
Code illustration: 7.09

Scatter Plot

Tkinter GUI Application Development Hotshot
"""

import tkinter
import random
root = tkinter.Tk()

c = tkinter.Canvas(root, width=350, height=280, bg='white')
c.grid()


#create x-axis
c.create_line(50,250,300,250, width=3)
for i in range(12):
    x = 50 + (i * 20)
    c.create_text(x,255,anchor='n', text='%d'% (20*i) )


#y-axis
c.create_line(50,250,50,20, width=3)
for i in range(12):
    y = 250 - (i * 20)
    c.create_text(45,y, anchor='e', text='%d'% (20*i))
