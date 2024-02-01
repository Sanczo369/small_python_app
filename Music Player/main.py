#!/usr/bin/python3
# Music Player Tkinter
#

import os,sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from pygame import mixer,error

def main():
    window = Music_Player()
    window.mainloop()

if __name__ == "__main__":
    main()