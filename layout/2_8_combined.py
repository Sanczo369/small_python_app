import tkinter as tk
import ttkbootstrap as ttk
# from tkinter import ttk

# window
window = ttk.Window(themename = 'lumen')
window.title('Combined layout')
window.geometry('600x600')
window.minsize(600,600)

# main layout widgets
menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

# main place layout
menu_frame.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
# run
window.mainloop()