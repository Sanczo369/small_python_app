import tkinter as tk
from tkinter import ttk, font

# window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

style.configure('new.TButton', foreground = 'green', font = ('Jokerman', 20))
style.map('new.TButton',
	foreground = [('pressed', 'red'),('disabled', 'yellow')],
	background = [('pressed', 'green'), ('active', 'blue')])
style.configure('TFrame', background = 'pink')

# run
window.mainloop()