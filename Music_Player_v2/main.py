import os
import vlc
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Music Player")
        self.window.geometry("500x340")

        # Create the playlist
        self.playlist = tk.Listbox(self.window, width=50)
        self.playlist.pack(pady=10)