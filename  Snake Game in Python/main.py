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