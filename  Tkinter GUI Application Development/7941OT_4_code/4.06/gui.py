"""
Code illustration: 4.06


ATTRIBUTES ADDED
pieces = {}
selected = None
selected_piece = None
focused = None


METHOD MODFIED
Class GUI
__init__ (click event added)
draw_board modified to handle clicks

NEW METHODS ADDED
sqaureclicked
shift
focus


Tkinter GUI Application Development Hotshot
"""
import chessboard
import pieces
from Tkinter import *
from PIL import ImageTk

class GUI():
    pieces = {}
    selected_piece = None
    focused = None
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    highlightcolor ="khaki"
    rows = 8
    columns = 8
    dim_square = 64
