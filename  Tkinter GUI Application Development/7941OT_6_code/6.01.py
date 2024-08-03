"""
Code illustration: 6.01

Creating the Overall Structure for our Drawing Program

Tkinter GUI Application Development Hotshot
"""



from tkinter  import *
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

    def __init__(self, root):
        self.root = root
        self.create_menu()
        self.create_top_bar()
        self.create_tool_bar()
        self.create_drawing_canvas()
