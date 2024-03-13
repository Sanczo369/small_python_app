import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# run
window.mainloop()