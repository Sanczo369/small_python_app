"""
Code illustration: 5.06

METHODS MODIFIED:
create_list_frame - added event handler for right click to call a method show_context_menu

NEW METHODS ADDED HERE
create_context_menu
show_context_menu
close_player


@Tkinter GUI Application Development Hotshot
"""
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import os
import time

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
