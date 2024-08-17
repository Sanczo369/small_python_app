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

    def create_top_bar(self):
        self.topbar = Frame(self.root, height=25, relief=RAISED)
        self.topbar.pack(fill=X,side=TOP, pady=2)

    def create_tool_bar(self):
        self.toolbar = Frame(self.root, width=50, relief=RAISED)
        self.toolbar.pack(fill=Y, side=LEFT, pady=3)
        self.create_tool_bar_buttons()
        self.create_color_pallete()
        self.curcoordlabel = Label(self.toolbar, text='x: 0  \ny: 0 ')
        self.curcoordlabel.grid(row=13, column=1, columnspan=2, pady=5, padx=1, sticky='w')

    def create_tool_bar_buttons(self):
        for i, item in enumerate(self.all_toolbar_functions):
            tbicon = PhotoImage(file='icons/'+item+'.gif')
            self.button = Button(self.toolbar, image=tbicon, command=lambda i=i: self.selected_tool_bar_item(i))
            self.button.grid(row=i/2, column=1+i%2, sticky='nsew')
            self.button.image = tbicon

    def selected_tool_bar_item(self, i):
            self.selected_toolbar_func_index = i
            self.remove_options_from_topbar()
            self.show_selected_tool_icon_in_topbar()
            opt = self.all_toolbar_functions[self.selected_toolbar_func_index]+'_options'
            fnc = getattr(self, opt)
            fnc()

    def create_color_pallete(self):
        self.colorpallete = Canvas(self.toolbar, height=55, width=55)
        self.colorpallete.grid(row=10, column=1, columnspan=2, pady=5, padx=3)
        self.backgroundpallete = self.colorpallete.create_rectangle(15, 15, 48, 48, tags="backgroundpallete",
                                                                    outline=self.background, fill=self.background)
        self.foregroundpallete = self.colorpallete.create_rectangle(1, 1, 33, 33, tags="foregroundpallete",
                                                                    outline=self.foreground, fill=self.foreground)
        self.colorpallete.tag_bind(self.backgroundpallete, "<Button-1>", self.set_background_color)
        self.colorpallete.tag_bind(self.foregroundpallete, "<Button-1>", self.set_foreground_color)

    def set_background_color(self, event=None):
        self.background = askcolor()[-1]
        try:self.set_fill()
        except:pass
        try:self.set_outline()
        except:pass
        self.colorpallete.itemconfig(self.backgroundpallete, outline=self.background, fill=self.background)

    def set_foreground_color(self, event=None):
        self.foreground = askcolor()[-1]
        try:
            self.set_fill()
        except:
            pass
        try:
            self.set_outline()
        except:
            pass
        self.colorpallete.itemconfig(self.foregroundpallete, outline=self.foreground, fill=self.foreground)
