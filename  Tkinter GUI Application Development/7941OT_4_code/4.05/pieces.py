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
