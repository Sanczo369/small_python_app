import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Place')
window.geometry('400x600')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
button = ttk.Button(window, text = 'Button')

# run
window.mainloop()