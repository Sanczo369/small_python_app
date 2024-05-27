#!/usr/bin/env python
"""
Code illustration: 3.02
Drum Program Editor Code
Setting up Widgets
@Tkinter GUI Application Development Hotshot
"""

from Tkinter import *

class DrumMachine():

    def create_play_bar(self):
        playbar_frame = Frame(self.root, height=15)
        ln = MAX_DRUM_NUM + 10
        playbar_frame.grid(row=ln, columnspan=13, sticky=W + E, padx=15, pady=10)
        button = Button(playbar_frame, text='Play')
        button.grid(row=ln, column=1, padx=1)
        button = Button(playbar_frame, text='Stop')
        button.grid(row=ln, column=3, padx=1)
        loop = BooleanVar()
        loopbutton = Checkbutton(playbar_frame, text='Loop', variable=loop)
        loopbutton.grid(row=ln, column=16, padx=1)

    def create_left_pad(self):
        left_frame = Frame(self.root)
        left_frame.grid(row=10, column=0, columnspan=6,sticky=W+E+N+S)
        tbicon = PhotoImage(file='images/openfile.gif')
        for i in range(0, MAX_DRUM_NUM):
            button = Button(left_frame, image=tbicon)
            button.image = tbicon
            button.grid(row=i, column=0,  padx=5,pady=2)
            self.drum_entry = Entry(left_frame)
            self.drum_entry.grid(row=i, column=4, padx=7,pady=2)

    def create_right_pad(self):
        right_frame = Frame(self.root)
        right_frame.grid(row=10, column=6,sticky=W+E+N+S, padx=15, pady=2)
        self.button = [[0 for x in range(4)] for x in range(MAX_DRUM_NUM)]
        for i in range(MAX_DRUM_NUM):
            for j in range(4):
                self.button[i][j] = Button(right_frame, bg='grey55')
                self.button[i][j].grid(row=i, column=j)

# ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()


