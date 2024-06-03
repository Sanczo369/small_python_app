#!/usr/bin/env python
"""
Code illustration: 3.07
Tkinter and Threading
@Tkinter GUI Application Development Hotshot
"""

from tkinter import *
import tkFileDialog
import tkMessageBox
import os

#modules for playing sounds
import time
import wave
import pymedia.audio.sound as sound

import threading

class DrumMachine():
        def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0]*MAX_DRUM_NUM
        self.current_drum_no = 0
        self.keep_playing = True
        self.loop = False



    def app(self):
        self.root = Tk()
        self.root.title('Drum Beast')
        self.create_top_bar()
        self.create_left_pad()
        self.create_play_bar()
        self.root.mainloop()

# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()