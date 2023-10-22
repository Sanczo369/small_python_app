from tkinter import  *
import random
root=Tk()
root.title("Snake Game")

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
score = 0
direction = "down"
GAME_HEIGHT = 700
GAME_WIDTH = 700



# Klasy
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
# Funkcje
def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    del snake.coordinates[-1]

    canvas.delete(snake.squares[-1])

    del snake.squares[-1]

    root.after(SPEED, next_turn, snake, food)
def change_direction(new_direction):
    pass
def check_collisions():
    pass
def game_over():
    pass

top_label=Label(root, text="Score:{}".format(score), font=("consolas", 40))
top_label.pack()

canvas = Canvas(root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int(screen_width/2) - int(window_width/2)
y = int(screen_height/2) - int(screen_height/2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


snake=Snake()
food=Food()

next_turn(snake, food)

root.mainloop()