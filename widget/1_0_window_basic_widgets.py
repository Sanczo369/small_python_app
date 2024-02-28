import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# run
window.mainloop()