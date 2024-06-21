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


class ChessError(Exception): pass