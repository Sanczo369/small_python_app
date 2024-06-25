"""
Code illustration: 5.02
No changes here in this iteration
@Tkinter GUI Application Development Hotshot
"""
import pyglet
from threading import Thread
import time

class Player():
    parent = None
    metadata ={} #mp3 artist title year genre in dictionary form.
    song_length = 0 #in seconds
    paused = False
    stopped = False
    current_time = 0
    vol = 0.0
