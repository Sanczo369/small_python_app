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


    def __init__(self, parent, chessboard):
        self.chessboard = chessboard
        self.parent = parent
        #Adding Top Menu
        self.menubar = Menu(parent)
        self.filemenu = Menu(self.menubar, tearoff=0 )
        self.filemenu.add_command(label="New Game", command=self.new_game )
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        # Adding Frame
        self.btmfrm = Frame(parent, height=64)
        self.info_label = Label(self.btmfrm, text="   White to Start the Game  ", fg=self.color2)
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.btmfrm.pack(fill="x", side=BOTTOM)

        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.square_clicked)

    def new_game(self):
        self.chessboard.show(chessboard.START_PATTERN)
        self.draw_board()
        self.draw_pieces()
        self.info_label.config(text="   White to Start the Game  ", fg='red')

    def square_clicked(self, event):
        col_size = row_size = self.dim_square
        selected_column = event.x / col_size
        selected_row = 7 - (event.y / row_size)
        pos = self.chessboard.alpha_notation((selected_row, selected_column))
        try:
            piece = self.chessboard[pos]
        except:
            pass
        if self.selected_piece:
            self.shift(self.selected_piece[1], pos)
            self.selected_piece = None
            self.focused = None
            self.pieces = {}
            self.draw_board()
            self.draw_pieces()
        self.focus(pos)
        self.draw_board()

    def shift(self, p1, p2):
        piece = self.chessboard[p1]
        try:
            dest_piece = self.chessboard[p2]
        except:
            dest_piece = None
        if dest_piece is None or dest_piece.color != piece.color:
            try:
                self.chessboard.shift(p1,p2)
            except chessboard.ChessError as error:
                self.info_label["text"] = error.__class__.__name__
            else:
                turn = ('white' if piece.color == 'black' else 'black')
                self.info_label["text"] = '' + piece.color.capitalize() +"  :  "+ p1 + p2 + '    ' + turn.capitalize() + '\'s turn'
