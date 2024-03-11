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

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# run
window.mainloop()