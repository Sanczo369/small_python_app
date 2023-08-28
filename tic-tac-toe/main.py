from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.iconbitmap('logo.ico')
root.title("Tic Tac Toe")
root.geometry("300x300")

# Make the window resizable false
root.resizable(False, False)

# Define font
button_font = font.Font(family='Comic Sans MS', size=12)
label_font = font.Font(family='Comic Sans MS', size=16)

# Define Element
logo = ImageTk.PhotoImage(Image.open("logo1.png"))

# LabelFrame "TTT"
framettt = Label(root, text="Tic Tac Toe", padx=5, pady=5, font=label_font)
btn_1 = Button(root, height=2, width=30, padx=5, pady=5, text="Start", font=button_font)
btn_2 = Button(root, height=2, width=30, padx=5, pady=5, text="Autor", font=button_font)
btn_3 = Button(root, height=2, width=30, padx=5, pady=5, text="Koniec", font=button_font)

# Position
framettt.grid(row=0, column=0)
btn_1.grid(row=1, column=0)
btn_2.grid(row=2, column=0)
btn_3.grid(row=3, column=0)


if __name__ == '__main__':
    root.mainloop()