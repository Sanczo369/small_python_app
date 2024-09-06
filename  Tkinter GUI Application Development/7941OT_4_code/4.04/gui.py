"""
Code illustration: 4.03
Displaying the Pieces

--> No changes from the previous iteration

Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import chessboard
from PIL import ImageTk

class GUI(dict):
    rows = 8
    columns = 8
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    dim_square = 64
    images = {}

