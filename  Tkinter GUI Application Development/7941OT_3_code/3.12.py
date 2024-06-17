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
    pass



# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()


