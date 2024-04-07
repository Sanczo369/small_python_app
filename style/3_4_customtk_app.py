# import tkinter as tk
# from tkinter import ttk
import customtkinter as ctk

# exercise:
# convert the app to use ctk

class App(ctk.CTk):
    def __init__(self, title, size):
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()