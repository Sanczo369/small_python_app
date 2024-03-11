import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

# Combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

# run
window.mainloop()