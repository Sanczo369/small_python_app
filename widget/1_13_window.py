import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('More on the window')
# window.geometry('600x400+100+200')
window.iconbitmap('python.ico')

# exercise:
# start window in the middle of the screen
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()


# run
window.mainloop()