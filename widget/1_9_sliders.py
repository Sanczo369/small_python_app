import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('Sliders')

# slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(
	window,
	command = lambda value: progress.stop(),
	from_ = 0,
	to = 25,
	length = 300,
	orient = 'horizontal',
	variable = scale_float)
scale.pack()


# run
window.mainloop()