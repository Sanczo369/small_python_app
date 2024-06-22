"""
Code illustration: 5.01
Creating GUI to Load and play a song
Tkinter GUI Application Development Hotshot
"""

from tkinter  import *
import tkinter.filedialog
import player


class GUI:
    currentTrack = ''
    def __init__(self, player):
        self.player = player
        player.parent = self
        self.root = Tk()
        self.create_button_frame()
        self.create_bottom_frame()
        self.root.mainloop()
