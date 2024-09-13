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

    def __init__(self, parent, chessboard):
        self.chessboard = chessboard
        self.parent = parent
        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.square_clicked)
