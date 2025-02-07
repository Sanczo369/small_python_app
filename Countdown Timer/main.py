import time
from tkinter import *
import multiprocessing
from tkinter import ttk, messagebox
from playsound import playsound
from threading import *

# Hour list
hour_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24]

# Minute List
min_sec_list = [0, 1, 2, 3, 4, 5, 6, 7, 8,
9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
53, 54, 55, 56, 57, 58, 59,]

class CountDown:
    def __init__(self, root):
        self.window = root
        self.window.geometry("480x320+0+0")
        self.window.title('CountDown Timer')
        # Tkinter window background color
        self.window.configure(bg='gray35')
        # Fixing the Window length constant
        self.window.resizable(width=False, height=False)

        # Declaring a variable to pause the countdown time
        self.pause = False

        # The Start and Pause buttons are placed
        # inside this frame
        self.button_frame = Frame(self.window, bg="gray35", \
        width=240, height=40)
        self.button_frame.place(x=230, y=150)
        # This frame is used to show the countdown time label
        self.time_frame = Frame(self.window, bg="gray35", \
        width=480, height=120).place(x=0, y=210)

        # Tkinter Labels
        time_label = Label(self.window, text="Set Time",
        font=("times new roman",20, "bold"), bg='gray35',fg='yellow')
        time_label.place(x=180, y=30)

        hour_label = Label(self.window, text="Hour",
                           font=("times new roman", 15), bg='gray35', fg='white')
        hour_label.place(x=50, y=70)

        minute_label = Label(self.window, text="Minute",
                             font=("times new roman", 15), bg='gray35', fg='white')
        minute_label.place(x=200, y=70)

        second_label = Label(self.window, text="Second",
                             font=("times new roman", 15), bg='gray35', fg='white')
        second_label.place(x=350, y=70)
        # ===========================================

        # Tkinter Comboboxes
        # Combobox for hours
        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self.window, width=8,
                                          height=10, textvariable=self.hour,
                                          font=("times new roman", 15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=50, y=110)

        # Combobox for minutes
        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.window, width=8,
        height=10, textvariable=self.minute,
        font=("times new roman",15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=200,y=110)

        # Combobox for seconds
        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.window, width=8,
        height=10, textvariable=self.second,
        font=("times new roman",15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=350,y=110)
        # ===========================================

        # Tkinter Buttons
        # Cancel button
        cancel_button = Button(self.window, text='Cancel',
        font=('Helvetica',12), bg="white", fg="black",
        command=self.Cancel)
        cancel_button.place(x=70, y=150)

        # Set Time Button
        # When the user presses this button
        # the 'Start' and 'Pause' button will
        # show inside the 'self.button_frame' frame
        set_button = Button(self.window, text='Set',
        font=('Helvetica',12), bg="white", fg="black",
        command=self.Get_Time)
        set_button.place(x=160, y=150)

        def Cancel(self):
            self.pause = True
            self.window.destroy()