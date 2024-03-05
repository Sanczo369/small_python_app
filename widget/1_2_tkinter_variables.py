import tkinter as tk
from tkinter import ttk

def button_func():
	print(string_var.get())
	string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')



# run
window.mainloop()