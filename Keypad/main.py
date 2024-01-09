import tkinter as tk

Keyboard_App = tk.Tk()

keys = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'DEL',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '!', 'TAB',
    'SPACE',
]

curBut = [-1,-1]
buttonL = [[]]
entry = tk.Text(Keyboard_App, width=97, height=8)
entry.grid(row=0, columnspan=15)

varRow = 1
varColumn = 0

Keyboard_App.mainloop()