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