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

def seek(value):
    """ used to seek a specific timeframe """
    vid_player.seek(int(value))

def skip(value: int):
    """ skip seconds """
    vid_player.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get() + value)

def play_pause():
    """ pauses and plays """
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"

def video_ended(event):
    """ handle video ended """
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)


#ButtonPlay = PhotoImage(file="play1.png")
#Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,
#       command=load_video).place(x=0, y=0)

load_btn = tk.Button(root, text="Browse",bg="#FFFFFF", font=("calibri",
      12, "bold"), command=load_video)
load_btn.pack(ipadx=12, ipady=4, anchor=tk.NW)

#ButtonPlay = PhotoImage(file="play11.png")
#Playbutton = tk.Button(root, image=ButtonPlay, bd=0, height = 60, width =60,
#       command=lambda: play_pause).pack(ipadx=12, ipady=4, anchor=tk.NW)

#vid_player = TkinterVideo(scaled=True, master=root)
#vid_player.pack(expand=True, fill="both")

vid_player = TkinterVideo(root, scaled=True)
vid_player.pack(expand=True, fill="both")

root.mainloop()