import tkinter as tk
from tkinter import ttk


def create_segment(parent, label_text, button_text):
	frame = ttk.Frame(master = parent)

	# grid layout
	frame.rowconfigure(0, weight = 1)
	frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')

	# widgets
	ttk.Label(frame, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
	ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

	return frame

# window
window = tk.Tk()
window.title('Widgets and return')
window.geometry('400x600')

# run
window.mainloop()