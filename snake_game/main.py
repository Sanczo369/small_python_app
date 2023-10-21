from tkinter import  *
import random
root=Tk()
root.title("Snake Game")
root.geometry("600x600+300+100")
root.resizable(False,False)
img_logo=PhotoImage(file="logo.png")
root.iconphoto(False, img_logo)


# Klasy
class Snake:
    pass
class Food:
    pass

# Funkcje
def next_turn():
    pass
def change_direction():
    pass
def check_collisions():
    pass
def game_over():
    pass

root.mainloop()