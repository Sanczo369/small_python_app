import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
	def __init__(self, start_size):
		super().__init__()
		self.title('Responsive layout')
		self.geometry(f'{start_size[0]}x{start_size[1]}')

		self.frame = ttk.Frame(self)
		self.frame.pack(expand = True, fill = 'both')


        SizeNotifier(
            self,
            {
                600: self.create_medium_layout,
                300: self.create_small_layout,
                1200: self.create_large_layout
            })
		self.mainloop()


# exercise
# create a a third layout where the widgets are next to each other (I used grid)
# make it appear once the window is wider than 1200 pixels


app = App((400,300))