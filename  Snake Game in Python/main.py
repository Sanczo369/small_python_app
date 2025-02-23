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