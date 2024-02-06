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
def start_countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(time_display, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, start_countdown, count - 1)
    else:
        start_timer()
        engines = ''
        work_sess = math.floor(repetition/2)
        for item in range(work_sess):
            engines += '⚙'
        checkmark_label.config(text=engines)

# --- UI FUNCTIONS: Timer Reset --- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_display, text='00:00')
    title_task_label.config(text="& tasks")
    checkmark_label.config(text='')
    global repetition
    repetition = 0

# --- UI FUNCTIONS: Add/Remove tasks --- #

def add_button_click():
    listbox_label.insert(tkinter.END, entry_task.get())


def remove_button_click():
    listbox_label.delete(tkinter.ANCHOR)

# --- UI FUNCTIONS: Set work and long break variables --- #

def set_work_timer():
    global WORK_MIN
    work_minutes = int(work_entry.get())
    if type(work_minutes) != int:
        WORK_MIN = 25
    else:
        WORK_MIN = work_minutes
    return WORK_MIN

def set_long_break():
    global LONG_BREAK_MIN
    long_break = int(long_break_entry.get())
    if type(long_break) != int:
        LONG_BREAK_MIN = 20
    else:
        LONG_BREAK_MIN = long_break
    return LONG_BREAK_MIN
