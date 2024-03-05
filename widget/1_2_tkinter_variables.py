import tkinter as tk
from tkinter import ttk

def button_func():
	print(string_var.get())
	string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise
# create 2 entry fields and 1 label, they should all be connected via a StringVar
# set a start value of 'test'

exercise_var = tk.StringVar(value = 'test')
# exercise_var.set('test')

# run
window.mainloop()