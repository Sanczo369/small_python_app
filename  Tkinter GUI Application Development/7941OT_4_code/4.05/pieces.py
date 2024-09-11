"""
Code illustration: 4.05

--> No changes done here from the previous iteration



Tkinter GUI Application Development Hotshot
"""

import sys

SHORT_NAME = { 'R':'Rook', 'N':'Knight', 'B':'Bishop', 'Q':'Queen', 'K':'King', 'P':'Pawn'}

def create_piece(piece, color='white'):
    ''' Takes a piece name or shortname and returns the corresponding piece instance '''
    if piece in (None, ' '): return
    if piece.isupper(): color = 'white'
    else: color = 'black'
    piece = SHORT_NAME[piece.upper()]
    module = sys.modules[__name__]
    return module.__dict__[piece](color)

class Piece(object):
    def __init__(self, color):
        if color == 'black':
            self.shortname = self.shortname.lower()
        elif color == 'white':
            self.shortname = self.shortname.upper()
        self.color = color

    def ref(self, board):
        ''' Get a reference of chess board instance'''
        self.board = board


    def moves_available(self, pos, diagonal, orthogonal, distance):
        board = self.board
        allowed_moves = []
        orth  = ((-1,0),(0,-1),(0,1),(1,0))
        diag  = ((-1,-1),(-1,1),(1,-1),(1,1))
        piece = self

