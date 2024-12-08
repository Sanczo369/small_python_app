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

def start_timer():
    global reps, remaining_time
    reps += 1

    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())

    count = hours * 3600 + minutes * 60 + seconds

    if remaining_time > 0:
        count_down(remaining_time)
        title_label.config(text="Work", fg=GREEN)
        remaining_time = 0
    elif count > 0:
        count_down(count)
        title_label.config(text="Work", fg=GREEN)

def pause_timer():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
        start_timer()

def play_tick_sound():
    pygame.mixer.music.load(resource_path("./assets/tick.wav"))
    pygame.mixer.music.play()

def play_finish_sound():
    pygame.mixer.music.load(resource_path("./assets/finish.wav"))
    pygame.mixer.music.play()