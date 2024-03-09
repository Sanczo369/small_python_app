import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
	print('a button was pressed')
	print(entry_string.get())

def outer_func(parameter):
	def inner_func():
		print('a button was pressed')
		print(parameter.get())
	return inner_func


# setup
window = tk.Tk()
window.title('buttons, functions and arguments')


# run
window.mainloop()