from tkinter import *
import datetime
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo

root = tk.Tk()
root.title("Simpli Video Player")
root.geometry("800x700+290+10")
frame = tk.Frame(root)
frame.pack()

def update_duration(event):
    """ updates the duration after finding the duration """
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration

def update_scale(event):
    """ updates the scale value """
    progress_value.set(vid_player.current_duration())

def load_video():
    """ loads the video """
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)

        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "Play"
        progress_value.set(0)

root.mainloop()