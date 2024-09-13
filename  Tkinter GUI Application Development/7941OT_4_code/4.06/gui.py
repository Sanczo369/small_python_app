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

    def square_clicked(self, event):
        col_size = row_size = self.dim_square
        selected_column = event.x / col_size
        selected_row = 7 - (event.y / row_size)
        pos = self.chessboard.alpha_notation((selected_row, selected_column))
        try:
            piece = self.chessboard[pos]
        except:
            pass
        if self.selected_piece:
            self.shift(self.selected_piece[1], pos)
            self.selected_piece = None
            self.focused = None
            self.pieces = {}
            self.draw_board()
            self.draw_pieces()
        self.focus(pos)
        self.draw_board()

    def shift(self, p1, p2):
        piece = self.chessboard[p1]
        try:
            dest_piece = self.chessboard[p2]
        except:
            dest_piece = None
        if dest_piece is None or dest_piece.color != piece.color:
            try:
                self.chessboard.shift(p1,p2)
            except:
                pass

    def focus(self, pos):
        try:
            piece = self.chessboard[pos]
        except:
            piece=None
        if piece is not None and (piece.color == self.chessboard.player_turn):
            self.selected_piece = (self.chessboard[pos], pos)
            self.focused = map(self.chessboard.num_notation, (self.chessboard[pos].moves_available(pos)))
