"""
Code illustration: 5.07

Adding Tooltips (Balloon Widget) using PMW extension


METHODS MODIFIED:
__init__ method
create_button_frame
create_bottom_frame
tootip addded for each button in both these frames


@Tkinter GUI Application Development Hotshot
"""
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import ttk
import os
import time

import Pmw

import player

class GUI:
    alltracks = []
    indx = 0
    currentTrack = ''
    timer = [0, 0]  # corresponding to minutes and seconds
    timepattern = '{0:02d}:{1:02d}'

    # new attributes added here
    loopchoices = [("No Loop", 1), ("Loop Current", 2), ("Loop All", 3)]
    selectedloopchoice = 3  # deafult 'no loop'

