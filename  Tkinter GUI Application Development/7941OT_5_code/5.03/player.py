"""
Code illustration: 5.03
Adding Functionality of Next, Forward, Previous, Rewind Mute & Volume
NEW METHODS ADDED HERE:
-------------------------
fast_fwd
rewind
mute
unmute

METHODS MODIFIED:
-----------------------
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
