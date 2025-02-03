import pyperclip
from tkinter import *
from threading import *
from tkinter import ttk
from pytube import YouTube
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox, ttk

# Resolution Options(Audio Option is also available)
download_quality = ['144p', '360p', '720p', 'Audio Only']

class Yt_Downloader:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("700x480")
        self.window.title('YouTube Video and Audio Downloader')
        self.window.resizable(width=False, height=False)

        self.save_to_loc = ''

        # Frame 1: For YouTube Logo
        self.frame_1 = Frame(self.window, width=220, height=80)
        self.frame_1.pack()
        self.frame_1.place(x=20, y=20)

        # Frame 2: For Download Logo
        self.frame_2 = Frame(self.window, width=50, height=50)
        self.frame_2.pack()
        self.frame_2.place(x=235, y=40)

        self.show_yt_logo()
        self.show_dn_logo()