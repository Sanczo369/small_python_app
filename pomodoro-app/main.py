import tkinter
import math

# ----- CONSTANTS ----- #

PINK = "#e2979c"
RED = "#C84B31"
GREEN = "#dce0cd"
GREEN_MSG = "#125C13"
YELLOW = "#ECDBBA"
FONT_NAME = "Lucida Console"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None


# --- UI FUNCTIONS: Countdown Clock --- #

def start_timer():
    global repetition
    global title_task_label
    repetition += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetition % 8 == 0:
        title_task_label.config(text="long break", font=(FONT_NAME, 30), bg=GREEN, fg=GREEN_MSG)
        start_countdown(long_break_sec)
    elif repetition % 2 == 0:
        start_countdown(short_break_sec)
        title_task_label.config(text="short break", font=(FONT_NAME, 20), bg=GREEN, fg=PINK)
    else:
        title_task_label.config(text="work and focus", font=(FONT_NAME, 20), bg=RED, fg=PINK)
        start_countdown(work_sec)