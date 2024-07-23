"""
Code illustration: 5.07

Adding Tooltips (Balloon Widget) using PMW extension


METHODS MODIFIED:
__init__ method
create_button_frame
create_bottom_frame
tootip addded for each button in both these frames


@Tkinter GUI Application Development Hotshot
"""
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import ttk
import os
import time

import Pmw

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
        self.balloon = Pmw.Balloon(self.root)
        self.create_console_frame()
        self.create_button_frame()
        self.list_frame()
        self.create_bottom_frame()
        self.context_menu()
        self.root.protocol('WM_DELETE_WINDOW', self.close_player)
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
        self.balloon.bind(prevbtn, 'Previous Song')

        rewindicon = PhotoImage(file='../icons/rewind.gif')
        rewindbtn = Button(buttonframe, image=rewindicon, borderwidth=0, padx=0, command=self.player.rewind)
        rewindbtn.image = rewindicon
        rewindbtn.grid(row=3, column=2, sticky='w')
        self.balloon.bind(rewindbtn, 'Go Back')

        self.playicon = PhotoImage(file='../icons/play.gif')
        self.stopicon = PhotoImage(file='../icons/stop.gif')
        self.playbtn=Button(buttonframe, text ='play', image=self.playicon, borderwidth=0, padx=0, command=self.toggle_play_pause)
        self.playbtn.image = self.playicon
        self.playbtn.grid(row=3, column=3)
        self.balloon.bind(self.playbtn, 'Play Song')

        fast_fwdicon = PhotoImage(file='../icons/fast_fwd.gif')
        fast_fwdbtn=Button(buttonframe, image=fast_fwdicon, borderwidth=0, padx=0, command=self.player.fast_fwd)
        fast_fwdbtn.image = fast_fwdicon
        fast_fwdbtn.grid(row=3, column=4)
        self.balloon.bind(fast_fwdbtn, 'Fast Forward')

        nexticon = PhotoImage(file='../icons/next.gif')
        nextbtn=Button(buttonframe, image=nexticon,borderwidth=0,padx=0, command=self.next_track)
        nextbtn.image = nexticon
        nextbtn.grid(row=3, column=5)
        self.balloon.bind(nextbtn, 'Next Song')



