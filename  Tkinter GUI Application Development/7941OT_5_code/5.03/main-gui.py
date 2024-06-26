'''
METHODS ADDED
--------------------------------
next_track
prev_track

METHODS MODIFIED
--------------------------------
create_button_frame - added all control buttons
'''
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os
import player
class GUI:
    alltracks = []
    indx = 0
    currentTrack = ''
    timer = [0, 0]  # corresponding to minutes and seconds
    timepattern = '{0:02d}:{1:02d}'
    loopchoices = [("No Loop", 1), ("Loop Current", 2), ("Loop All", 3)]
    selectedloopchoice = 3  # deafult 'no loop'
    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk()
        self.create_button_frame()
        self.create_list_frame()
        self.create_bottom_frame()
        self.root.mainloop()
