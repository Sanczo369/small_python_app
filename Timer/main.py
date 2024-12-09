from tkinter import *
import math
import os
import pygame


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

reps = 0
timer = None
is_paused = False
remaining_time = 0

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00:00")
    canvas.itemconfig(progress_bar, fill="green")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps, is_paused, remaining_time
    reps = 0
    is_paused = False
    remaining_time = 0
    pause_button.config(text="Pause")