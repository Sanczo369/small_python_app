#!/usr/bin/env python
"""
Code illustration: 3.04
Loading Drum Samples
@Tkinter GUI Application Development Hotshot
"""

from tkinter import *
import tkFileDialog
import tkMessageBox
import os

class DrumMachine():
    def __init__(self):
        self.widget_drum_name = []
        self.widget_drum_file_name = [0]*MAX_DRUM_NUM
        self.current_drum_no = 0

    def drum_load(self, drum_no):
        def callback():
            self.current_drum_no = drum_no
            try:
                file_name = tkFileDialog.askopenfilename(defaultextension=".wav",
                                                        filetypes=[("Wave Files", "*.wav"), ("OGG Files", "*.ogg")])
                if not file_name: return
                try:
                    del self.widget_drum_file_name[drum_no]
                except:
                    pass
                self.widget_drum_file_name.insert(drum_no, file_name)
                drum_name = os.path.basename(file_name)
                self.widget_drum_name[drum_no].delete(0, END)
                self.widget_drum_name[drum_no].insert(0, drum_name)
            except:
                tkMessageBox.showerror('Invalid', "Error loading drum samples")
        return callback

    def button_clicked(self, i, j, bpu):
        def callback():
            btn = self.button[i][j]
            color = 'grey55' if (j / bpu) % 2 else 'khaki'
            new_color = 'green' if btn.cget('bg') != 'green' else color
            btn.config(bg=new_color)
        return callback

    def create_play_bar(self):
        playbar_frame = Frame(self.root, height=15)
        ln = MAX_DRUM_NUM + 10
        playbar_frame.grid(row=ln, columnspan=13, sticky=W + E, padx=15, pady=10)
        button = Button(playbar_frame, text='Play')
        button.grid(row=ln, column=1, padx=1)
        button = Button(playbar_frame, text='Stop')
        button.grid(row=ln, column=3, padx=1)
        loop = BooleanVar()
        loopbutton = Checkbutton(playbar_frame, text='Loop', variable=loop)
        loopbutton.grid(row=ln, column=16, padx=1)

        # ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()

    dm.app()
