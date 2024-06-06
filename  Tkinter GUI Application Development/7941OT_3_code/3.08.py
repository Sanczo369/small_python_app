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

    def record_pattern(self):
        pattern_num, bpu, units = self.patt.get(), self.bpu.get(), self.units.get()
        self.pat_name.config(state='normal')
        self.pat_name.delete(0, END)
        self.pat_name.insert(0, 'Pattern %s' % pattern_num)
        self.pat_name.config(state='readonly')
        prevpval = self.prevpatvalue
        self.prevpatvalue = pattern_num
        c = bpu * units
        self.buttonpickleformat = [[0] * c for x in range(MAX_DRUM_NUM)]
        for i in range(MAX_DRUM_NUM):
            for j in range(c):
                if self.button[i][j].config('bg')[-1] == 'green':
                    self.buttonpickleformat[i][j] = 'active'
        self.pattern_list[prevpval] = {'df': self.widget_drum_file_name, 'bl': self.buttonpickleformat, 'bpu': bpu,
                                       'units': units}
        self.reconstruct_pattern(pattern_num, bpu, units)


# ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()


