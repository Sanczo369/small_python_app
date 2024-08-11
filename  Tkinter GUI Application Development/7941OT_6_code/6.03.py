"""
Code illustration: 6.03
Drawing Basic Shapes on the Canvas
ATTRIBUTED ADDED HERE:
all_toolbar_functions
selected_toolbar_func_index
METHODS MODIFIED:
mouse_down_motion
mouse_up
selected_tool_bar_item
NEW METHODS ADDED:
draw_line
draw_oval
draw_rectangle
drawPolygon
draw_brush
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
    all_toolbar_functions = ('draw_line', 'draw_rectangle', 'draw_oval', 'draw_brush')
    selected_toolbar_func_index = 0 # draw_line

    def __init__(self, root):
        self.root = root
        self.create_menu()
        self.create_top_bar()
        self.create_tool_bar()
        self.create_drawing_canvas()
