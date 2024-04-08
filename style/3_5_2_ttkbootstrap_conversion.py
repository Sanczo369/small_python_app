import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self, title, size):
        # main setup
        super().__init__(themename='custom')
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()

class Menu(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

		self.create_widgets()

class Main(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
		Entry(self, 'Entry 1','Button 1','green')
		Entry(self, 'Entry 2','Button 2','blue')