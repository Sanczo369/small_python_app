import tkinter
from tkinter import *
import random
guess = str()
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

root = Tk()
root.title("Sudoku")
root.minsize(width=500, height=635)
root.attributes("-alpha", 0.90)
root.configure(background="#282828")

title = Label(root, text='Sudoku', fg="#382888", font="Geneva 30", bg="#282828")
title.pack()

box = Canvas(root, width=435, height=435, background="#282828", bd=6, highlightthickness=6)
box.pack()

entry_list = [[], [], []]
var =[]
done = False


root.mainloop()