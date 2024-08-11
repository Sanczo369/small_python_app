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

    def create_menu(self):
        self.menubar = Menu(self.root)
        self.menuitems = (
            'File- &New/Ctrl+N/self.new_file, &Open/Ctrl+O/self.open_file, Save/Ctrl+S/self.save, SaveAs//self.save_as, Sep, Exit/Alt+F4/self.close',
            'Edit- Undo/Ctrl+Z/self.undo, Sep',
            'About- About//self.about'
        )
        self.build_menu()
        self.root.config(menu=self.menubar)

    def create_top_bar(self):
        self.topbar = Frame(self.root, height=25, relief=RAISED)
        self.topbar.pack(fill=X, side=TOP, pady=2)

    def create_tool_bar(self):
        self.toolbar = Frame(self.root, width=50, relief=RAISED)
        self.toolbar.pack(fill=Y,side=LEFT, pady=3)
        self.create_tool_bar_buttons()
        self.create_color_pallete()
        self.curcoordlabel = Label(self.toolbar, text = 'x: 0  \ny: 0 ')
        self.curcoordlabel.grid(row=13, column=1, columnspan=2, pady=5, padx=1, sticky='w')


