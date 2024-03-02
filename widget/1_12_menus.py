import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command = lambda: print('New file'))
file_menu.add_command(label = 'Open', command = lambda: print('Open file'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)


# run
window.mainloop()