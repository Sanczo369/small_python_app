import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


root = Tk()
root.title("Media Player")
root.geometry('485x700+290+10')
root.resizable(False, False)
root.iconbitmap('logo.ico')
root.config(bg="#333333")

def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


lower_farme = Frame(root, bg ="#ffffff", width=485, height=180)
lower_farme.place(x=0, y=400)
mainloop()
