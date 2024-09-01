"""
Code illustration: 4.02
ChessBoard Model Based on FEN notation

New clasess defined here
Board
ChessError(Exception)
InvalidColor(ChessError)


Tkinter GUI Application Development Hotshot
"""
import pieces
import re

START_PATTERN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w 0 1'


class Board(dict):
    y_axis = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    x_axis = (1, 2, 3, 4, 5, 6, 7, 8)
