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


# ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()


