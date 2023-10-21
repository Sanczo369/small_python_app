from tkinter import  *
import random
root=Tk()
root.title("Snake Game")
root.geometry("700x700+300+100")
root.resizable(False,False)
img_logo=PhotoImage(file="logo.png")
root.iconphoto(False, img_logo)

# Zmienne
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


# Klasy
class Snake:
    pass
class Food:
    pass

# Funkcje
def next_turn():
    pass
def change_direction(new_direction):
    pass
def check_collisions():
    pass
def game_over():
    pass

root.mainloop()