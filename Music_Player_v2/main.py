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

        # Create the stop button
        self.stop_button = tk.Button(controls_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=2, padx=10)

        # Create the add button
        self.add_button = tk.Button(controls_frame, text="Add", command=self.add_to_playlist)
        self.add_button.grid(row=1, column=0, pady=10)

        # Create the remove button
        self.remove_button = tk.Button(controls_frame,text="Remove",command=self.remove_song)
        self.remove_button.grid(row=1, column=1, pady=10)

        # Create the vlc player instance
        self.player = vlc.Instance()
        self.media_player = self.player.media_player_new()

        # Set the end event
        the_event = vlc.EventType.MediaPlayerEndReached
        self.media_player.event_manager().event_attach(the_event, self.next_song)

    def play(self):
        selected_song = self.playlist.get(tk.ACTIVE)
        media = self.player.media_new(selected_song)
        self.media_player.set_media(media)
        self.media_player.play()

    def pause(self):
        self.media_player.pause()

