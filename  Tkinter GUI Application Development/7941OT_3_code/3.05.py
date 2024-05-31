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
    pass


# ======================================================================
if __name__ == '__main__':
    dm = DrumMachine()
    dm.app()
