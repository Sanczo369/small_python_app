"""
Code illustration: 4.07

NO CHANGES IN THIS ITERATION

@Tkinter GUI Application Development Hotshot
"""
from copy import deepcopy
import re

import pieces




START_PATTERN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w 0 1'

class Board(dict):

    y_axis = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    x_axis = (1, 2, 3, 4, 5, 6, 7, 8)
    captured_pieces = { 'white': [], 'black': [] }
    player_turn = None
    halfmove_clock = 0
    fullmove_number = 1
    history = []

    def __init__(self, pat = None):
        self.show(START_PATTERN)

    def is_in_check_after_move(self, p1, p2):
        tmp = deepcopy(self)
        tmp.move(p1,p2)
        return tmp.king_in_check(self[p1].color)
