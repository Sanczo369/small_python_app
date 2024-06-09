#!/usr/bin/env python
"""
Code illustration: 3.09
Object Persistence: pickling and unpickling
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

#constants
MAX_DRUM_NUM = 5


class DrumMachine():
    def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0]*MAX_DRUM_NUM
        self.current_drum_no = 0
        self.keep_playing = True
        self.loop = False
        self.pattern_list = [None]*10

    def about(self):
        tkMessageBox.showinfo("About", "Tkinter GUI Application\n Development Hotshot")

    def exit_app(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def save_project(self):
        self.record_pattern()#make sure the last pattern is recorded before save
        file_name = tkFileDialog.asksaveasfilename(filetypes=[('Drum Beat File','*.bt')] , title="Save project as...")
        pickle.dump( self.pattern_list, open( file_name, "wb" ) )
        self.root.title(os.path.basename(file_name) + " - DrumBeast")

    def load_project(self):
        file_name = tkFileDialog.askopenfilename(filetypes=[('Drum Beat File','*.bt')], title='Load Project')
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
        except:tkMessageBox.showerror("Error","An unexpected error occurred trying to reconstruct patterns")

    def record_pattern(self):
        pattern_num, bpu, units = self.patt.get(),self.bpu.get(), self.units.get()
        self.pat_name.config(state='normal')
        self.pat_name.delete(0, END)
        self.pat_name.insert(0, 'Pattern %s'%pattern_num)
        self.pat_name.config(state='readonly')
        prevpval = self.prevpatvalue
        self.prevpatvalue = pattern_num
        c = bpu*units
        self.buttonpickleformat = [[0] * c for x in range(MAX_DRUM_NUM)]
        for i in range(MAX_DRUM_NUM):
            for j in range(c):
                if self.button[i][j].config('bg')[-1] == 'green':
                    self.buttonpickleformat[i][j] = 'active'
        self.pattern_list[prevpval] = {'df': self.widget_drum_file_name, 'bl': self.buttonpickleformat, 'bpu':bpu, 'units':units}
        self.reconstruct_pattern(pattern_num, bpu, units)






# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()

