import time
from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
from playsound import playsound
import multiprocessing
from datetime import datetime
from threading import *

hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24']

minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59']

ringtones_list = ['mom_calling', 'nice_wake_up', 'romantic', 'twirling_intime', 'wakeup_alarm_tone']

ringtones_path = {
    'mom_calling': 'Ringtones/mom_calling.mp3',
    'nice_wake_up': 'Ringtones/nice_wake_up.mp3',
    'romantic': 'Ringtones/romantic.mp3',
    'twirling_intime': 'Ringtones/twirling_intime.mp3',
    'wakeup_alarm_tone': 'Ringtones/wakeup_alarm_tone.mp3'
}

class AlarmClock:
    def __init__(self, root):
        self.window = root
        self.window.geometry("680x420+0+0")
        self.window.title("PyClock")
        self.window.resizable(width = False, height = False)

        # Background image of the first window.
        self.bg_image = ImageTk.PhotoImage(file="Images/image_1.jpg")
        self.background = Label(self.window, image=self.bg_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Display Label shows the current time in the
        # first window
        self.display = Label(self.window, font=('Helvetica', 34),
        bg = 'gray8', fg = 'yellow')
        self.display.place(x=100,y=150)

        self.show_time()

        set_button = Button(self.window, text="Set Alarm",
        font=('Helvetica',15), bg="green", fg="white",
        command=self.set_alarm)
        set_button.place(x=270, y=220)

    # Method to show the current time in the first window
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
        # Placing the time format level.
        self.display.config(text = current_time)
        self.display.after(100, self.show_time)

    def set_alarm(self):
        self.alarm_window = Tk()
        self.alarm_window.title("Set Alarm")
        self.alarm_window.geometry("680x420+200+200")

        # Hour Label
        hours_label = Label(self.alarm_window, text="Hours",
                            font=("times new roman", 20))
        hours_label.place(x=150, y=50)

        #  Minute Label
        minute_label = Label(self.alarm_window, text="Minutes",
                             font=("times new roman", 20))
        minute_label.place(x=450, y=50)

        # Hour Combobox
        self.hour_var = StringVar()
        self.hour_combo = ttk.Combobox(self.alarm_window,
                                       width=10, height=10, textvariable=self.hour_var,
                                       font=("times new roman", 15))
        self.hour_combo['values'] = hours_list
        self.hour_combo.current(0)
        self.hour_combo.place(x=150, y=90)

        # Minute Combobox
        self.minute_var = StringVar()
        self.minute_combo = ttk.Combobox(self.alarm_window,
        width=10, height=10, textvariable=self.minute_var,
        font=("times new roman",15))
        self.minute_combo['values'] = minutes_list
        self.minute_combo.current(0)
        self.minute_combo.place(x=450,y=90)

        # Ringtone Label.
        ringtone_label = Label(self.alarm_window, text="Ringtones",
        font=("times new roman",20))
        ringtone_label.place(x=150, y=130)

        # Ringtone Combobox(Choose the ringtone).
        self.ringtone_var = StringVar()
        self.ringtone_combo = ttk.Combobox(self.alarm_window,
        width=15, height=10, textvariable=self.ringtone_var,
        font=("times new roman",15))
        self.ringtone_combo['values'] = ringtones_list
        self.ringtone_combo.current(0)
        self.ringtone_combo.place(x=150,y=170)

        # Create an entry for setting a message
        message_label = Label(self.alarm_window, text="Message",
        font=("times new roman",20))
        message_label.place(x=150, y=210)

        self.message_var = StringVar()
        self.message_entry = Entry(self.alarm_window,
        textvariable=self.message_var, font=("times new roman",14), width=30)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(x=150, y=250)

