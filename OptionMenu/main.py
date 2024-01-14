from tkinter import OptionMenu
import tkinter as Tkinter
class GasGen(Tkinter.Tk):
	def __init__(self):
		super().__init__()
		self.vars = []
		self.initialize()
		self.grid()


if __name__ == "__main__":
	app = GasGen()
	app.title('Gas mixture generator')
	app.configure(background = "slate gray")
	app.mainloop()