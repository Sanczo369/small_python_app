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

    def create_tool_bar_buttons(self):
        for i, item in enumerate(self.all_toolbar_functions):
            tbicon = PhotoImage(file='icons/'+item+'.gif')
            self.button = Button(self.toolbar, image=tbicon, command=lambda i=i: self.selected_tool_bar_item(i))
            self.button.grid(row=i/2, column=1+i%2, sticky='nsew')
            self.button.image = tbicon

    def selected_tool_bar_item(self, i):
        self.selected_toolbar_func_index = i

    def create_color_pallete(self):
        self.colorpallete = Canvas(self.toolbar, height=55, width =55)
        self.colorpallete.grid(row=10, column=1, columnspan=2, pady=5, padx=3)
        self.backgroundpallete = self.colorpallete.create_rectangle(15, 15,48, 48,tags="backgroundpallete", outline=self.background, fill=self.background)
        self.foregroundpallete = self.colorpallete.create_rectangle(1, 1,33, 33,tags="foregroundpallete", outline=self.foreground, fill=self.foreground)
        self.colorpallete.tag_bind(self.backgroundpallete, "<Button-1>", self.set_background_color)
        self.colorpallete.tag_bind(self.foregroundpallete, "<Button-1>", self.set_foreground_color)

    def set_background_color(self, event=None):
        self.background = askcolor()[-1]
        self.colorpallete.itemconfig(self.backgroundpallete, outline=self.background, fill=self.background)

    def set_foreground_color(self, event=None):
        self.foreground = askcolor()[-1]
        self.colorpallete.itemconfig(self.foregroundpallete,outline=self.foreground, fill=self.foreground)

    def create_drawing_canvas(self):
        cnvsframe=Frame(self.root,width=900,height=900)
        cnvsframe.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.canvas = Canvas(cnvsframe, background="white", width=500,height=500,scrollregion=(0,0,800,800))
        hbar=Scrollbar(cnvsframe,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(cnvsframe,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.canvas.bind( "<Button-1>", self.mouse_down)
        self.canvas.bind( "<Button1-Motion>", self.mouse_down_motion)
        self.canvas.bind( "<Button1-ButtonRelease>", self.mouse_up)
        self.canvas.bind( "<Motion>", self.show_current_coordinates)

    def mouse_down(self, event):
        self.currentobject = None
        self.lastx = self.startx = self.canvas.canvasx(event.x)
        self.lasty = self.starty = self.canvas.canvasy(event.y)
