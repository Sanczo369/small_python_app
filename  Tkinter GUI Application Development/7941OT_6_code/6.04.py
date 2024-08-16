"""
Code illustration: 6.04
Adding TopBar to display options for each of the selected buttons


ATTRIBUTED ADDED HERE:
arrow='none'
width=1.0
dash = None
fill = 'red'
outline = 'black'


METHODS MODIFIED:
selected_tool_bar_item
draw_line
draw_rectangle
draw_oval
draw_brush


NEW METHODS ADDED:
fill_options_combobox / set_fill
OutlineOpt / set_outline
width_options_combobox / set_width
arrow_options_combobox / set_arrow
dash_options_combobox  /set_dash



Tkinter GUI Application Development Hotshot
"""

from tkinter import *
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
    all_toolbar_functions = ('draw_line', 'draw_rectangle', 'draw_oval', 'draw_brush')
    selected_toolbar_func_index = 0  # draw_line

    arrow = 'none'
    width = 1.0
    dash = None
    fill = 'red'
    outline = 'black'

    def __init__(self, root):
       self.root = root
       self.create_menu()
       self.create_top_bar()
       self.create_tool_bar()
       self.create_drawing_canvas()

    def create_menu(self):
        self.menubar = Menu(self.root)
        self.menuitems = (
                       'File- &New/Ctrl+N/self.new_file, &Open/Ctrl+O/self.open_file, Save/Ctrl+S/self.save, SaveAs//self.save_as, Sep, Exit/Alt+F4/self.close',
                       'Edit- Undo/Ctrl+Z/self.undo, Sep',
                       'About- About//self.about'
                       )
        self.build_menu()
        self.root.config(menu=self.menubar)
