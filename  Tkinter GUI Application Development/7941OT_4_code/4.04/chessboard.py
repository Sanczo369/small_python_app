"""
Code illustration: 4.04

--> No changes from the previous iteration

Tkinter GUI Application Development Hotshot
"""
import pieces
import re

START_PATTERN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w 0 1'


class Board(dict):
    y_axis = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    x_axis = (1, 2, 3, 4, 5, 6, 7, 8)

    def __init__(self, patt=None):
        self.process_notation(START_PATTERN)

    def alpha_notation(self,xycoord):
        if not self.is_on_board(xycoord): return
        return self.y_axis[xycoord[1]] + str(self.x_axis[xycoord[0]])
