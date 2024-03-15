import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')

# run
window.mainloop()