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

    def play_media(self) :
        try:
            self.myplayer= pyglet.media.Player()
            self.myplayer.push_handlers(on_eos=self.what_next)
            self.source = pyglet.media.load(self.parent.currentTrack)
            self.myplayer.queue(self.source)
            self.myplayer.play()
            pyglet.app.run()
        except:
            pass

    def what_next(self):
        if self.stopped:
            self.stopped = False
            return None
        if self.parent.selectedloopchoice == 1:
            # No Loop
            return None
        if self.parent.selectedloopchoice == 2:
            # Loop current
            self.parent.launch_play()
        if self.parent.selectedloopchoice == 3:
            # Loop All
            self.fetch_next_track()

    def fetch_next_track(self):
        try:
            next_trackindx = self.parent.alltracks.index(self.parent.currentTrack) +1
            self.parent.currentTrack = self.parent.alltracks[next_trackindx]
            self.parent.launch_play()
        except:
            print 'end of list'
