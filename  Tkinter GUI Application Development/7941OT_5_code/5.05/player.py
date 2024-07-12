"""
Code illustration: 5.05

METHODS MODIFED
play_media (added a call back event on end of a song - calls what_next method)


METHODS ADDED
what_next (decides wether a next song is to be played or not)
fetch_next_track (if next song is to be played this method fetches the next track from the playlist for play)





@Tkinter GUI Application Development Hotshot
"""


import pyglet
from threading import Thread
import time

FWDREWNDTIME = 20

class Player():
    parent = None
    metadata ={} #mp3 artist title year genre in dictionary form.
    song_len = 0 #in seconds
    paused = False
    stopped = False
    current_time = 0
    vol = 0.0
