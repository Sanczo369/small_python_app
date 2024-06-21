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

class ChessError(Exception): pass