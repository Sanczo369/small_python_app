import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')


# Exercise
# use event binding to create a basic paint app
def draw_on_canvas(event):
	x = event.x
	y = event.y
	canvas.create_oval((x - brush_size / 2,y - brush_size / 2, x + brush_size / 2,y + brush_size / 2), fill = 'black')
# run
window.mainloop()