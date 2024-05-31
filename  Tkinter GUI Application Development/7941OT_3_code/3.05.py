#!/usr/bin/env python
"""
Code illustration: 3.05
Playing Sound Files with pymedia module

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

class DrumMachine():
    def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0] * MAX_DRUM_NUM
        self.current_drum_no = 0

    def play(self):
        for i in range(len(self.button[0])):
            for item in self.button:
                try:
                    if item[i].cget('bg') == 'green':
                        if not self.widget_drum_file_name[self.button.index(item)]: continue
                        sound_filename = self.widget_drum_file_name[self.button.index(item)]
                        self.play_sound(sound_filename)
                except:
                    continue
            time.sleep(3 / 4.0)  # corresponds to 80 beats per minute (80 BPM)(60/80)

    def play_sound(self, sound_filename):
        try:
            self.s = wave.open(sound_filename, 'rb')
            sample_rate = self.s.getframerate()
            channels = self.s.getnchannels()
            frmt = sound.AFMT_S16_LE
            self.snd= sound.Output(sample_rate, channels, frmt)
            s = self.s.readframes(300000)
            self.snd.play(s)
        except:
            pass

# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()
