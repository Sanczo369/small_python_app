"""
Code illustration: 4.07
METHODS ADDED
new_game (to start a new game)
METHODS MODIFIED
__init__ (menu bar and info frame added)
shift (to change the info label after every move)
Tkinter GUI Application Development Hotshot
"""
import chessboard
import pieces
from Tkinter import *
from PIL import ImageTk
class GUI():
    pieces = {}
    selected_piece = None
    focused = None
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    highlightcolor ="khaki"
    rows = 8
    columns = 8
    dim_square = 64