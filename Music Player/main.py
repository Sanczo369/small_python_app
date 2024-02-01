#!/usr/bin/python3
# Music Player Tkinter
#

import os,sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from pygame import mixer,error

class Music_Player(Tk):
    def __init__(self):
        super(Music_Player,self).__init__()
        event = None
        self.title("Music Player")
        self.geometry("300x200+500+95")
        self.resizable(0,0)
        icon = PhotoImage(file="./icon/music-player-icon.png")
        self.iconphoto(False,icon)
        menu = Menu(self)
        self.configure(menu=menu)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label="Open File",accelerator="Ctrl+O",command=lambda: self.open_file(event))
        filemenu.add_separator()
        filemenu.add_command(label="Exit",accelerator="Alt+F4",command=self.quit)
        menu.add_cascade(label="File",menu=filemenu)
        play_btn = Button(self,text="Play",width=5,height=2,foreground="#fff000",background="#333",command=self.play_music).pack(padx=3,pady=3)
        pause_btn = Button(self,text="Pause",width=5,height=2,foreground="#fff000",background="#333",command=self.pause_music).pack(padx=3,pady=3)
        stop_btn = Button(self,text="Stop",width=5,height=2,foreground="#fff000",background="#333",command=self.stop_music).pack(padx=3,pady=3)
        self.bind("<Control-o>",lambda event: self.open_file(event))
        self.configure(background="black")
def main():
    window = Music_Player()
    window.mainloop()

if __name__ == "__main__":
    main()