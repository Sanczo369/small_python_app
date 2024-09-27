import threading
import Queue
import random
import time
from Tkinter import *

class GUI(Tk):
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False
        self.canvas = Canvas(self, width=495, height=305, bg='#FF75A0')
        self.canvas.pack()
        self.snake = self.canvas.create_line((0, 0), (0,0), fill='#FFCC4C', width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(455, 15, fill='white', text='Score: 0')
        self.queue_handler()

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)
                if task.has_key('game_over'):
                    self.game_over()
                elif task.has_key('move'):
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake, *points)
                elif task.has_key('food'):
                    self.canvas.coords(self.food, *task['food'])
                elif task.has_key('points_earned'):
                    self.canvas.itemconfigure(self.points_earned , text='Score: {}'.format(task['points_earned']))
                self.queue.task_done()
        except Queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill='white', text='Game Over')
        quitbtn = Button(self, text='Quit', command = self.destroy)
        self.canvas.create_window(200, 180, anchor='nw', window=quitbtn)

class Food():
    def __init__(self, queue):
        self.queue = queue
        self.generate_food()
