"""
Code illustration: 7.10

Bar Graph

Tkinter GUI Application Development Hotshot
"""

import Tkinter
import random

root = Tkinter.Tk()


cwidth = 250
cheight = 220
barWidth = 20


canv = Tkinter.Canvas(root, width=cwidth, height=cheight, bg= 'white')
canv.pack()
