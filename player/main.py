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


# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)

image_icon = PhotoImage(file="logo png.png")
root.iconphoto(False, image_icon)

frameCnt = 30
frames = [PhotoImage(file='aa1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]


lower_farme = Frame(root, bg ="#ffffff", width=485, height=180)
lower_farme.place(x=0, y=400)
mainloop()
