"""
Code illustration: 6.05

Adding Features of 'delete_object', 'fill_object', 'move_to_top', 'drag_item'

ATTRIBUTED ADDED HERE:
selected_objected

ATTRIBUTES MODIFIED HERE:
all_toolbar_functions (added 4 new items to the tuple- 'delete_object', 'fill_object', 'move_to_top', 'drag_item')


METHODS MODIFIED:
mouse_down


NEW METHODS ADDED:
fill_object
fill_object_options
delete_object
delete_object_options
move_to_top
move_to_top_options
drag_item
drag_item_update_xy
drag_item_options

Tkinter GUI Application Development Hotshot
"""



from tkinter  import *
import tkFileDialog
import tkMessageBox
import Image
import ImageTk
from tkColorChooser import askcolor

import ttk

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
    all_toolbar_functions = (
    'draw_line', 'draw_rectangle', 'draw_oval', 'draw_brush', 'delete_object', 'fill_object', 'move_to_top',
    'drag_item')
    selected_toolbar_func_index = 0  # draw_line
    arrow = 'none'
    width = 1.0
    dash = None
    fill = 'red'
    outline = 'black'

    selected_objected = None
