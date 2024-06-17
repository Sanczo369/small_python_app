#!/usr/bin/env python
"""
Code illustration: 3.12
Finalizing our Drum Machine
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
import pickle

import tkinter.ttk

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

    def about(self):
        tkinter.messagebox.showinfo("About","Tkinter GUI Application\n Development Hotshot")

    def exit_app(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()


    def save_project(self):
        self.record_pattern()#make sure the last pattern is recorded before save
        file_name = tkinter.filedialog.asksaveasfilename(filetypes=[('Drum Beat File','*.bt')] , title="Save project as...")
        pickle.dump( self.pattern_list, open( file_name, "wb" ) )
        self.root.title(os.path.basename(file_name) + " - DrumBeast")

    def load_project(self):
        file_name = tkinter.filedialog.askopenfilename(filetypes=[('Drum Beat File','*.bt')], title='Load Project')
        if file_name == '':return
        self.root.title(os.path.basename(file_name) + " - DrumBeast")
        fh = open(file_name,"rb") # open the file in reading mode
        try:
            while True: # load from the file until EOF is reached
                self.pattern_list = pickle.load(fh)
        except EOFError:
            pass
        fh.close()
        try:
            self.reconstruct_pattern(0, self.pattern_list[0]['bpu'], self.pattern_list[0]['units'])# reconstruct the first pattern
        except:tkinter.messagebox.showerror("Error","An unexpected error occurred trying to reconstruct patterns")


# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()


