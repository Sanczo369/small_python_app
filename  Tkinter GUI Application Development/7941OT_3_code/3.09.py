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

    def reconstruct_pattern(self, pattern_num, bpu, units):
        self.widget_drum_file_name = [0] * MAX_DRUM_NUM
        try:
            self.df = self.pattern_list[pattern_num]['df']
            for i in range(len(self.df)):
                file_name = self.df[i]
                if file_name == 0:
                    self.widget_drum_name[i].delete(0, END)
                    continue
                self.widget_drum_file_name.insert(i, file_name)
                drum_name = os.path.basename(file_name)
                self.widget_drum_name[i].delete(0, END)
                self.widget_drum_name[i].insert(0, drum_name)
        except:
            for i in range(MAX_DRUM_NUM):
                try:
                    self.df
                except:
                    self.widget_drum_name[i].delete(0, END)
        try:
            bpu = self.pattern_list[pattern_num]['bpu']
            units = self.pattern_list[pattern_num]['units']
        except:
            return
        self.bpu_widget.delete(0, END)
        self.bpu_widget.insert(0, bpu)
        self.units_widget.delete(0, END)
        self.units_widget.insert(0, units)
        self.create_right_pad()
        c = bpu * units
        self.create_right_pad()
        try:
            for i in range(MAX_DRUM_NUM):
                for j in range(c):
                    if self.pattern_list[pattern_num]['bl'][i][j] == 'active':
                        self.button[i][j].config(bg='green')
        except:
            return

    def play_in_thread(self):
        self.thread = threading.Thread(None,self.play, None, (), {})
        self.thread.start()

    def play(self):
        self.keep_playing = True
        while self.keep_playing:
            for i in range(len(self.button[0])):
                for item in self.button:
                    try:
                        if item[i].cget('bg') == 'green':
                            if not self.widget_drum_file_name[self.button.index(item)]:continue
                            sound_filename = self.widget_drum_file_name[self.button.index(item)]
                            self.play_sound(sound_filename)
                            #self.root.update() # a rather inelegant hack
                    except:continue
                time.sleep(1/8.0)
                if self.loop == False: self.keep_playing = False

    def play_sound(self, sound_filename):
        try:
            self.s = wave.open(sound_filename, 'rb')
            sample_rate = self.s.getframerate()
            channels = self.s.getnchannels()
            frmt = sound.AFMT_S16_LE
            self.snd = sound.Output(sample_rate, channels, frmt)
            s = self.s.readframes(300000)
            self.snd.play(s)
        except:
            pass
    def stop_play(self):
        self.keep_playing = False
        return

    def loop_play(self, xval):
        self.loop = xval

    def drum_load(self, drum_no):
        def callback():
            self.current_drum_no = drum_no
            try:
                file_name = tkFileDialog.askopenfilename(defaultextension=".wav",filetypes=[("Wave Files", "*.wav"), ("OGG Files", "*.ogg")])
                if not file_name: return
                try:
                    del self.widget_drum_file_name[drum_no]
                except:pass
                self.widget_drum_file_name.insert(drum_no, file_name)
                drum_name = os.path.basename(file_name)
                self.widget_drum_name[drum_no].delete(0, END)
                self.widget_drum_name[drum_no].insert(0, drum_name)
            except:
                tkMessageBox.showerror('Invalid', "Error loading drum samples")
        return callback

    def button_clicked(self,i,j,bpu):
            def callback():
                btn = self.button[i][j]
                color = 'grey55' if (j/bpu)%2 else 'khaki'
                new_color = 'green' if btn.cget('bg') != 'green' else color
                btn.config(bg=new_color)
            return callback

    def create_play_bar(self):
        playbar_frame = Frame(self.root, height=15)
        ln = MAX_DRUM_NUM + 10
        playbar_frame.grid(row=ln, columnspan=13, sticky=W + E, padx=15, pady=10)
        button = Button(playbar_frame, text='Play', command=self.play_in_thread)
        button.grid(row=ln, column=1, padx=1)
        button = Button(playbar_frame, text='Stop', command=self.stop_play)
        button.grid(row=ln, column=3, padx=1)
        loop = BooleanVar()
        loopbutton = Checkbutton(playbar_frame, text='Loop', variable=loop, command=lambda: self.loop_play(loop.get()))
        loopbutton.grid(row=ln, column=16, padx=1)


# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()

