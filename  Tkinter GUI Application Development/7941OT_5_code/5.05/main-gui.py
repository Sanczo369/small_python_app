"""
Code illustration: 5.05
ATRRIBUTES ADDED:
loopchoices ( a dictionary of name and assigned raio button value)
selectedloopchoice (1,2 or 3)
METHODS MODIFIED:
create_bottom_frame () -  #radio buttons added
@Tkinter GUI Application Development Hotshot
"""
from Tkinter import *
import tkFileDialog
import tkMessageBox
import ttk
import os
import time
import player


class GUI:
    alltracks = []
    indx = 0
    currentTrack = ''
    timer = [0, 0]  # corresponding to minutes and seconds
    timepattern = '{0:02d}:{1:02d}'

    # new attributes added here
    loopchoices = [("No Loop", 1), ("Loop Current", 2), ("Loop All", 3)]
    selectedloopchoice = 3  # deafult 'no loop'

    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk()
        self.root.title('Media Player')
        self.root.iconbitmap('../icons/mp.ico')
        self.create_console_frame()
        self.create_button_frame()
        self.create_list_frame()
        self.create_bottom_frame()
        self.root.mainloop()
