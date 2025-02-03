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