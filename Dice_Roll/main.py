import random
from customtkinter import *

root = CTk()
root.title("Dice Roll")
root.geometry('700x450+300+200')
root.resizable(False, False)
root.iconbitmap('logo.ico')
set_appearance_mode("dark")
def roll():
    number=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    x1=random.choice(number)
    x2=random.choice(number)
    l1 = CTkLabel(master=root, text=f'{x1}{x2}', font=("Arial", 270), text_color="#FFCC70")
    l1.place(relx= 0.5, rely = 0.2, anchor = "n")

b1=CTkButton(master=root, text="lets roll...",font=("Arial", 30), corner_radius=32, fg_color="#4158D0", hover_color="#4158D0", command=roll)
b1.place(relx= 0.5, rely = 0.1, anchor = "n")



root.mainloop()