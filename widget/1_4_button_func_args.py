import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
	print('a button was pressed')
	print(entry_string.get())


# setup
window = tk.Tk()
window.title('buttons, functions and arguments')


# run
window.mainloop()