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

    def create_button_frame(self):
        buttonframe = Frame(self.root)
        previcon = PhotoImage(file='../icons/previous.gif')
        prevbtn=Button(buttonframe, image=previcon, borderwidth=0, padx=0, command=self.prev_track)
        prevbtn.image = previcon
        prevbtn.grid(row=3, column=1, sticky='w')

        del_selectedicon = PhotoImage(file='../icons/del_selected.gif')
        del_selectedbtn=Button(bottomframe,image=del_selectedicon,borderwidth=0,padx=0, text='Delete', command=self.del_selected)
        del_selectedbtn.image = del_selectedicon
        del_selectedbtn.grid(row=5, column=2 )
