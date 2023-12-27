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

def one_grid(row):
    global grid,entry_list
    g1 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    entry_list[0].append(g1)
    g1.place(x = 5,y = 5)
    g2 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    entry_list[0].append(g2)
    g2.place(x = 52,y = 5)
    g3 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g3.place(x = 102,y = 5)
    entry_list[0].append(g3)
    g4 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g4.place(x = 5,y = 52)
    entry_list[1].append(g4)
    g5 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g5.place(x = 52,y = 52)
    entry_list[1].append(g5)
    g6 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g6.place(x = 102,y = 52)
    entry_list[1].append(g6)
    g7 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g7.place(x = 5,y = 102)
    entry_list[2].append(g7)
    g8 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g8.place(x = 52,y = 102)
    entry_list[2].append(g8)
    g9 = Entry(row,textvariable=var,width = 2, fg="white", font="Geneva 30 bold",bg="#373737",justify=CENTER)
    g9.place(x = 102,y = 102)
    entry_list[2].append(g9)


def display_val():
    global entry_list
    u = 0
    for a in entry_list:
        a_splited = [a[x:x + 9] for x in range(0, len(a), 9)]
        for y in range(9):
            if (grid[u][y] != 0):
                a_splited[0][y].insert(0, grid[u][y])
        u += 1
    u = 3
    for a in entry_list:
        a_splited = [a[x:x + 9] for x in range(0, len(a), 9)]
        for y in range(9):
            if (grid[u][y] != 0):
                a_splited[1][y].insert(0, grid[u][y])
        u += 1

    u = 6
    for a in entry_list:
        a_splited = [a[x:x + 9] for x in range(0, len(a), 9)]
        for y in range(9):
            if (grid[u][y] != 0):
                a_splited[2][y].insert(0, grid[u][y])
        u += 1


def scramble():
    global grid
    clear()
    for a in entry_list:
        for b in a:
            b.delete(first=0, last=100)
    amount = 20

    for i in range(amount):
        y = random.randint(0, len(grid) - 1)
        x = random.randint(0, len(grid) - 1)
        num = random.randint(1, len(grid))
        allow = 0
        for e in range(len(grid)):
            if num not in grid[x] and num != grid[e][y]:
                allow += 1
        grid[x][y] = num
        tempo = grid
        tempo = rearrange(tempo)

        for e in range(len(grid)):
            if (duplicate_checker(tempo[e])):
                allow = 0
        if allow != len(grid):
            grid[x][y] = 0

    display_val()

root.mainloop()