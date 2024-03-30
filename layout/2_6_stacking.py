import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Stacking order')
window.geometry('400x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(window, text = 'Label 2', background = 'red')
label3 = ttk.Label(window, text = 'Label 3', background = 'blue')
# run
window.mainloop()