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

def leftKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [0,10]
        buttonL[0][10].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [curBut[0], (curBut[1]-1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def upKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 0:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]-1)%5, 0]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]-1)%5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]-1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def downKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 3:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]+1)%5, 0]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]+1)%5, 5]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]+1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def select(value, x, y):
    if curBut != [-1,-1]:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        buttonL[curBut[0]][curBut[1]].configure(highlightcolor='#d9d9d9')
    curBut[:] = [x,y]
    buttonL[x][y].configure(highlightbackground='red')
    buttonL[x][y].configure(highlightcolor='red')
    if value == "DEL":
        input_val = entry.get("1.0", 'end-2c')
        entry.delete("1.0", "end")
        entry.insert("1.0", input_val, "end")
    elif value == "SPACE":
        entry.insert("insert", ' ')
    elif value == "TAB":
        entry.insert("insert", '   ')
    else:
        entry.insert("end", value)

Keyboard_App.mainloop()