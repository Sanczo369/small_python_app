"""
Code illustration: 4.04
Enforcing Piece Related Rules

New Method Added:
moves_available() in class Piece.

Classes Modified Here:

class King(Piece)
class Queen(Piece)
class Rook(Piece)
class Knight(Piece)
class Bishop(Piece)
class Pawn(Piece)



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

class Piece():
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
        orth = ((-1, 0), (0, -1), (0, 1), (1, 0))
        diag = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        piece = self

        beginningpos = board.num_notation(pos.upper())
        if orthogonal and diagonal:
            directions = diag + orth
        elif diagonal:
            directions = diag
        elif orthogonal:
            directions = orth

        for x, y in directions:
            collision = False
            for step in range(1, distance + 1):
                if collision: break
                dest = beginningpos[0] + step * x, beginningpos[1] + step * y
                if self.board.alpha_notation(dest) not in board.occupied('white') + board.occupied('black'):
                    allowed_moves.append(dest)
                elif self.board.alpha_notation(dest) in board.occupied(piece.color):
                    collision = True
                else:
                    allowed_moves.append(dest)
                    collision = True

        allowed_moves = filter(board.is_on_board, allowed_moves)
        return map(board.alpha_notation, allowed_moves)

class King(Piece):
    shortname = 'k'
    def moves_available(self,pos):
        return super(King, self).moves_available(pos.upper(), True, True, 1)

class Queen(Piece):
    shortname = 'q'
    def moves_available(self,pos):
        return super(Queen, self).moves_available(pos.upper(), True, True, 8)