"""
Code illustration: 5.02
Adding Playlist with Listbox widget

NEW ATTRIBUTES ADDED HERE
----------------------------
alltracks = [] - to track all items in the playlist


NEW METHODS ADDED HERE:
-------------------------
list_frame()
add_dir()
del_selected()
clear_list()
identify_track_to_play()

METHODS MODIFIED:
-----------------------
__init__: added newly defined list_frame method to be intiailized within the mainloop
create_bottom_frame() - added 3 new buttons: delete file, add directory & delete all

@Tkinter GUI Application Development Hotshot
"""
from Tkinter  import *
import tkFileDialog
import os
import time
import player

class GUI:
    alltracks = []
    currentTrack = ''


if __name__ == '__main__':
    playerobject = player.Player()
    app = GUI(playerobject)
