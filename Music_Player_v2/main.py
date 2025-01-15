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

        # Create the controls frame
        controls_frame = tk.Frame(self.window)
        controls_frame.pack()

        # Create the play button
        self.play_button = tk.Button(controls_frame, text="Play", command=self.play)
        self.play_button.grid(row=0, column=0, padx=10)

        # Create the pause button
        self.pause_button = tk.Button(controls_frame, text="Pause", command=self.pause)
        self.pause_button.grid(row=0, column=1, padx=10)