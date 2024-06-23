"""
Code illustration: 5.01
Basic implemetation of pyglet player class
Tkinter GUI Application Development Hotshot
"""
import pyglet
from threading import Thread


class Player():
    parent = None

    def play_media(self) :
        try:
            self.myplayer= pyglet.media.Player()
            self.source = pyglet.media.load(self.parent.currentTrack)
            self.myplayer.queue(self.source)
            self.myplayer.play()
            pyglet.app.run()
        except:
            pass


if __name__ == '__main__':

    print('a pyglet player class implementation')
