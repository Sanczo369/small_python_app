import random
import turtle as t

t.bgcolor('yellow')
t.title('Snake Game')
snake = t.Turtle()
snake.shape('square')
snake.color('red')
snake.speed(0)
snake.penup()
snake.hideturtle()

food = t.Turtle()
food.color('green')
food.shape('square')
food.speed(0)
food.penup()
food.hideturtle()

welcome_text = t.Turtle()
welcome_text.write('Press SPACE to Start', align='center', font=('Helvetica', 20, 'bold'))
welcome_text.hideturtle()

score_text = t.Turtle()
score_text.hideturtle()

def game_over():
    snake.color('yellow')
    food.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Helvetica', 40, 'bold'))

def boundary():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2

    (x, y) = snake.pos()
    boundary = (x<=left_wall or x>=right_wall or y<=bottom_wall or y>=top_wall)
    return boundary