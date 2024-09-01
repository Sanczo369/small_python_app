"""
Code illustration: 4.02
#no changes

Tkinter GUI Application Development Hotshot
"""

from tkinter import *


class GUI(dict):
    rows = 8
    columns = 8
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    dim_square = 64
    images = {}

    def __init__(self, parent, chessboard):
        self.parent = parent
        self.chessboard = chessboard
        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
