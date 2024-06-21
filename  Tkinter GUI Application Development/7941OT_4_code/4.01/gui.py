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




def main():
    root = Tk()
    root.title("Chess")
    root.mainloop()

if __name__ == "__main__":
    main()

