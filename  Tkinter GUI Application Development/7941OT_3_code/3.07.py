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

#constants
MAX_DRUM_NUM = 5


class DrumMachine():
    def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0]*MAX_DRUM_NUM
        self.current_drum_no = 0
        self.keep_playing = True
        self.loop = False


    def play_in_thread(self):
        self.start_button.config(state='disabled')
        self.thread = threading.Thread(None, self.play, None, (), {})
        self.thread.start()

    def play(self):
        self.keep_playing = True
        while self.keep_playing:
            for i in range(len(self.button[0])):
                for item in self.button:
                    try:
                        if item[i].cget('bg') == 'green':
                            if not self.widget_drum_file_name[self.button.index(item)]: continue
                            sound_filename = self.widget_drum_file_name[self.button.index(item)]
                            self.play_sound(sound_filename)
                            # self.root.update() # a rather inelegant hack
                    except:
                        continue
                time.sleep(1 / 8.0)  # change this to modify the tempo
                if self.loop == False: self.keep_playing = False
        self.start_button.config(state='normal')

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