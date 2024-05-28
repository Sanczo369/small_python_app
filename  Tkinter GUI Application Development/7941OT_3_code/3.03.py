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


    # ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()


