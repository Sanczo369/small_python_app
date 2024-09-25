"""
Code illustration: 7.01

Screensaver

Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
from random import randint


# A class to generate balls with random attributes

class RandomBall:

    def __init__(self, canvas, scrnwidth, scrnheight):
        self.canvas = canvas
        self.xpos = randint(10, int(scrnwidth))
        self.ypos = randint(10, int(scrnheight))
        self.xvelocity = randint(6, 12)
        self.yvelocity = randint(6, 12)
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        self.radius = randint(40, 70)
        r = lambda: randint(0, 255)  ### create a random number from 0-255
        self.color = '#%02x%02x%02x' % (r(), r(), r())
