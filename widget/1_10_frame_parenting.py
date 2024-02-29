import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')


# frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

# run
window.mainloop()