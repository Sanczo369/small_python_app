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


def create_small_layout(self):
    self.frame.pack_forget()
    self.frame = ttk.Frame(self)
    ttk.Label(self.frame, text='Label 1', background='red').pack(expand=True, fill='both', padx=10, pady=5)
    ttk.Label(self.frame, text='Label 2', background='green').pack(expand=True, fill='both', padx=10, pady=5)
    ttk.Label(self.frame, text='Label 3', background='blue').pack(expand=True, fill='both', padx=10, pady=5)
    ttk.Label(self.frame, text='Label 4', background='yellow').pack(expand=True, fill='both', padx=10, pady=5)
    self.frame.pack(expand=True, fill='both')

# exercise
# create a a third layout where the widgets are next to each other (I used grid)
# make it appear once the window is wider than 1200 pixels


app = App((400,300))