"""
Code illustration: 4.06

NEW CLASSES ADDED HERE:
class Check(ChessError)
class InvalidMove(ChessError)
class CheckMate(ChessError)
class Draw(ChessError)
class NotYourTurn(ChessError)


NEW ATTRIBUTES ADDED HERE:
captured_pieces = { 'white': [], 'black': [] }
player_turn = None
halfmove_clock = 0
fullmove_number = 1
history = []


NEW METHODS ADDED HERE:
shift() # to code pre-move validations and rules
move() # to execute actual move
is_in_check_after_move() # to check if a king is in check after a move
complete_move # to finalize move and to modify records as a result of the move


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
