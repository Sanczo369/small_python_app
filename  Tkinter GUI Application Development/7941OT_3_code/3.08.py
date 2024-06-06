"""
Code illustration: 3.08
Adding Support For Multiple beat patterns
@Tkinter GUI Application Development Hotshot
"""

from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import os


#modules for playing sounds
import time
import wave
import pymedia.audio.sound as sound

import threading

#constants
MAX_DRUM_NUM = 5


class DrumMachine():
    def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0] * MAX_DRUM_NUM
        self.current_drum_no = 0
        self.keep_playing = True
        self.loop = False
        self.pattern_list = [None] * 10


# ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()


