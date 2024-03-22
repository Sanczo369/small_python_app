import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Extra(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.title('extra window')
		self.geometry('300x400')
		ttk.Label(self, text = 'A label').pack()
		ttk.Button(self, text = 'A button').pack()
		ttk.Label(self, text = 'another label').pack(expand = True)

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')


# run
window.mainloop()