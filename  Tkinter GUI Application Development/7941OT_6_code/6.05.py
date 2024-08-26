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

    def __init__(self, root):
       self.root = root
       self.create_menu()
       self.create_top_bar()
       self.create_tool_bar()
       self.create_drawing_canvas()

    def delete_object(self,x0,y0,x1,y1):
        self.canvas.delete(self.selected_objected)

    def delete_object_options(self):
        pass

    def fill_object(self,x0,y0,x1,y1):
        if self.selected_objected == self.canvas:
            self.canvas.config(bg=self.fill)
        else:
            self.canvas.itemconfig(self.selected_objected, fill=self.fill)

    def fill_object_options(self):
        self.fill_options_combobox()

    def move_to_top(self,x0,y0,x1,y1):
        self.canvas.tag_raise(self.selected_objected)

    def move_to_top_options(self):
        pass

    def drag_item(self,x0,y0,x1,y1):
        if not self.all_toolbar_functions[self.selected_toolbar_func_index] == 'drag_item':
            self.canvas.bind( "<Button1-Motion>", self.mouse_down_motion)
            return
        self.currentobject = self.canvas.move(self.selected_objected, x1-x0,y1-y0)
        self.canvas.bind("<B1-Motion>", self.drag_item_update_xy)

    def drag_item_update_xy(self, event):
        self.startx, self.starty = self.lastx, self.lasty
        self.lastx, self.lasty = event.x, event.y
        self.drag_item(self.startx, self.starty,self.lastx, self.lasty)

    def drag_item_options(self):
        pass

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
        self.toolbar.pack(fill=Y,side=LEFT, pady=3)
        self.create_tool_bar_buttons()
        self.create_color_pallete()
        self.curcoordlabel = Label(self.toolbar, text = 'x: 0  \ny: 0 ')
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
        self.colorpallete = Canvas(self.toolbar, height=55, width =55)
        self.colorpallete.grid(row=10, column=1, columnspan=2, pady=5, padx=3)
        self.backgroundpallete = self.colorpallete.create_rectangle(15, 15,48, 48,tags="backgroundpallete", outline=self.background, fill=self.background)
        self.foregroundpallete = self.colorpallete.create_rectangle(1, 1,33, 33,tags="foregroundpallete", outline=self.foreground, fill=self.foreground)
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
        try:self.set_fill()
        except:pass
        try:self.set_outline()
        except:pass
        self.colorpallete.itemconfig(self.foregroundpallete,outline=self.foreground, fill=self.foreground)

    def show_selected_tool_icon_in_topbar(self):
        Label(self.topbar,text='Selected Tool:').pack(side=LEFT)
        photo = PhotoImage(file='icons/'+self.all_toolbar_functions[self.selected_toolbar_func_index]+'.gif')
        label = Label(self.topbar, image=photo)
        label.image = photo
        label.pack(side=LEFT)

    def remove_options_from_topbar(self):
        for child in self.topbar.winfo_children():
            child.destroy()

