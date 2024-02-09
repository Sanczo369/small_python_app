import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet

# set colours
bg_colour = "#3d6466"

# initiallize app with basic settings
root = tk.Tk()
root.title("Recipe Picker")
# create a frame widgets
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)



# run app
root.mainloop()