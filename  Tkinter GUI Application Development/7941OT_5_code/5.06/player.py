"""
Code illustration: 5.06

Adding Contextual Menus

NO changes Here

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

    def play_media(self):
        try:
            self.myplayer = pyglet.media.Player()
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
        if self.parent.loopv.get()  == 1:
            # No Loop
            return None
        if self.parent.loopv.get()  == 2:
            # Loop current
            self.parent.launch_play()
        if self.parent.loopv.get()  == 3:
            # Loop All
            self.fetch_next_track()

    def fetch_next_track(self):
        #next_trackindx = next((i+1 for i, x in enumerate(self.parent.alltracks) if x == self.parent.currentTrack ), -1)
        try:
            next_trackindx = self.parent.alltracks.index(self.parent.currentTrack) +1
            self.parent.currentTrack = self.parent.alltracks[next_trackindx]
            self.parent.launch_play()
        except:
            print 'end of list'
