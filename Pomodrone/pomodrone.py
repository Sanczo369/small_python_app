import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time

class Pomodoro:
	def __init__(self, root):
		self.root = root

    def work_break(self, timer):
        # common block to display minutes
        # and seconds on GUI
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)

        def work(self):
            timer = 25 * 60
            while timer >= 0:
                pomo.work_break(timer)
                if timer == 0:
                    # once work is done play
                    # a sound and switch for break
                    playsound("sound.ogg")
                    messagebox.showinfo(
                        "Good Job", "Take A Break, \
        				nClick Break Button")
                timer -= 1
