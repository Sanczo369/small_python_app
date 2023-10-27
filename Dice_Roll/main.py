import random
from tkinter import *

root=Tk()
root.title("Dice Roll")
root.geometry('700x450+300+200')
root.resizable(False, False)
root.iconbitmap('logo.ico')

def roll():
    number=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    x1=random.choice(number)
    x2=random.choice(number)
    l1.config(text=f'{x1}{x2}')
    l1.pack()


l1=Label(root, font=("times", 200))
b1=Button(root, text="lets roll...", command=roll)
b1.place(x=330,y=0)


mainloop()