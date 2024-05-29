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


# ======================================================================

if __name__ == '__main__':
    dm = DrumMachine()

    dm.app()
