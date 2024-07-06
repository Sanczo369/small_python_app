"""
Code illustration: 5.04

NEW METHODS ADDED HERE:
-------------------------
song_len() - to calculate the total length of the song
current_time() - to calculate the current duration of play

METHODS MODIFIED:
-----------------------
start_play_thread - added a call to song_len to get the song length

@Tkinter GUI Application Development Hotshot
"""


import pyglet
from threading import Thread
import time

FWDREWNDTIME = 20

class Player():
    parent = None
    metadata ={} #mp3 artist title year genre in dictionary form.
    song_length = 0 #in seconds
    paused = False
    stopped = False
    current_time = 0
    vol = 0.0

    def play_media(self):
        try:
            self.myplayer = pyglet.media.Player()
            self.source = pyglet.media.load(self.parent.currentTrack)
            self.myplayer.queue(self.source)
            self.myplayer.play()
            pyglet.app.run()
        except:
            pass


