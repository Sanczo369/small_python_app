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
