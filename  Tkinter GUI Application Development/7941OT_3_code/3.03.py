#!/usr/bin/env python
"""
Code illustration: 3.03
Drum Program Editor Code
Creating the Right Drum Pad or the Pattern Editor

@Tkinter GUI Application Development Hotshot
"""

from tkinter import *


class DrumMachine():

    def button_clicked(self, i, j, bpu):
        def callback():
            btn = self.button[i][j]
            color = 'grey55' if (j / bpu) % 2 else 'khaki'
            new_color = 'green' if btn.cget('bg') != 'green' else color
            btn.config(bg=new_color)
        return callback

    def create_play_bar(self):
        playbar_frame = Frame(self.root, height=15)
        ln = MAX_DRUM_NUM+10
        playbar_frame.grid(row=ln, columnspan=13,sticky=W+E,padx=15, pady=10)
        button = Button( playbar_frame, text ='Play')
        button.grid(row= ln, column=1, padx=1)
        button = Button( playbar_frame, text ='Stop')
        button.grid(row= ln, column=3,padx=1)
        loop = BooleanVar()
        loopbutton = Checkbutton(playbar_frame, text='Loop', variable=loop)
        loopbutton.grid(row=ln, column=16,padx=1)

    def create_left_pad(self):
        '''creating actual pattern editor pad'''
        left_frame = Frame(self.root)
        left_frame.grid(row=10, column=0, columnspan=6,sticky=W+E+N+S)
        tbicon = PhotoImage(file='images/openfile.gif')
        for i in range(0, MAX_DRUM_NUM):
            button = Button(left_frame, image=tbicon)
            button.image = tbicon
            button.grid(row=i, column=0,  padx=5,pady=2)
            self.drum_entry = Entry(left_frame)
            self.drum_entry.grid(row=i, column=4, padx=7,pady=2)


    # ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()


