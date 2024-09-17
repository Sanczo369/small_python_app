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

    def __init__(self, pat = None):
        self.show(START_PATTERN)

    def is_in_check_after_move(self, p1, p2):
        tmp = deepcopy(self)
        tmp.move(p1,p2)
        return tmp.king_in_check(self[p1].color)

 def shift(self, p1, p2):
        p1, p2 = p1.upper(), p2.upper()
        piece = self[p1]
        try:
            dest  = self[p2]
        except:
            dest = None
        if self.player_turn != piece.color:
            raise NotYourTurn("Not " + piece.color + "'s turn!")
        enemy = ('white' if piece.color == 'black' else 'black' )
        moves_available = piece.moves_available(p1)
        if p2 not in moves_available:
            raise InvalidMove
        if self.all_moves_available(enemy):
            if self.is_in_check_after_move(p1,p2):
                raise Check
        if not moves_available and self.king_in_check(piece.color):
            raise CheckMate
        elif not moves_available:
            raise Draw
        else:
            self.move(p1, p2)
            self.complete_move(piece, dest, p1,p2)

    def move(self, p1, p2):
        piece = self[p1]
        try:
            dest  = self[p2]
        except:
            pass
        del self[p1]
        self[p2] = piece


    def complete_move(self, piece, dest, p1, p2):
        enemy = ('white' if piece.color == 'black' else 'black')
        if piece.color == 'black':
            self.fullmove_number += 1
        self.halfmove_clock += 1
        self.player_turn = enemy
        abbr = piece.shortname
        if abbr == 'P':
            abbr = ''
            self.halfmove_clock = 0
        if dest is None:
            movetext = abbr + p2.lower()
        else:
            movetext = abbr + 'x' + p2.lower()
            self.halfmove_clock = 0
        self.history.append(movetext)






