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

    def create_console_frame(self):
        cnslfrm = Frame(self.root)
        photo = PhotoImage(file='../icons/glassframe.gif')
        self.canvas = Canvas(cnslfrm, width=370, height=90)
        self.canvas.image = photo
        self.canvas.grid(row=1)
        self.console = self.canvas.create_image(0, 10, anchor=NW, image=photo)
        self.clock = self.canvas.create_text(32, 34, anchor=W, fill='#CBE4F6', font="DS-Digital 20",
                                             text="00:00")
        self.songname = self.canvas.create_text(115, 37, anchor=W, fill='#9CEDAC', font="Verdana 10",
                                                text='\"Currently playing: none [00.00] \"')

        self.progressBar = ttk.Progressbar(cnslfrm, length=1, mode="determinate")
        self.progressBar.grid(row=2, columnspan=10, sticky='ew', padx=5)

        cnslfrm.grid(row=1, pady=1, padx=0)

    def create_button_frame(self):
        buttonframe = Frame(self.root)
        previcon = PhotoImage(file='../icons/previous.gif')
        prevbtn=Button(buttonframe, image=previcon, borderwidth=0, padx=0, command=self.prev_track)
        prevbtn.image = previcon
        prevbtn.grid(row=3, column=1, sticky='w')

