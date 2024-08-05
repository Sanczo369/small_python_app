"""
Code illustration: 6.02
Handling Mouse Events

ATTRIBUTED ADDED HERE:
currentobject = None
startx = 0
starty = 0
lastx = 0
lasty = 0

METHODS MODIFIED:
create_drawing_canvas - added event bindings for tracking mouse movements and mouse click
NEW METHODS ADDED:
mouse_down
mouse_down_motion
mouse_up
show_current_coordinates
Tkinter GUI Application Development Hotshot
"""
from tkinter import *
import tkFileDialog
import tkMessageBox
import Image
import ImageTk
from tkColorChooser import askcolor
import framework


class GUI(framework.GUIFramework):
    background = 'white'
    foreground = 'red'
    currentobject = None
    filename = 'untitled'
    currentobject = None
    startx = 0
    starty = 0
    lastx = 0
    lasty = 0