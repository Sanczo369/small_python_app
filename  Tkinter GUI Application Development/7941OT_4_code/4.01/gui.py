"""
Code illustration: 4.01
1) Creating the View File
2) Drawing Chess Board With the Canvas Widget
Tkinter GUI Application Development Hotshot
"""
from tkinter import *


class GUI():
    rows = 8
    columns = 8
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    dim_square = 64

    def __init__(self, parent):
        self.parent = parent
        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()



def main():
    root = Tk()
    root.title("Chess")
    root.mainloop()

if __name__ == "__main__":
    main()

