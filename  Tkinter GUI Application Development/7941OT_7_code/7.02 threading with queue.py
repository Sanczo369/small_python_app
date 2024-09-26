"""
Code illustration: 7.02

Threading with Queue Simple Demo

Tkinter GUI Application Development Hotshot
"""



import Queue
import threading

class Worker(threading.Thread):
   def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

   def run(self):
       while True:
           job = self.queue.get()
           self.taskHandler(job)

