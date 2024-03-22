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

# https://docs.python.org/3/library/tkinter.messagebox.html
def ask_yes_no():
	# answer = messagebox.askquestion('Title', 'Body')
	# print(answer)
	messagebox.showerror('Info title', 'Here is some information')


def create_window():
	global extra_window
	extra_window = Extra()
	# extra_window = tk.Toplevel()
	# extra_window.title('extra window')
	# extra_window.geometry('300x400')
	# ttk.Label(extra_window, text = 'A label').pack()
	# ttk.Button(extra_window, text = 'A button').pack()
	# ttk.Label(extra_window, text = 'another label').pack(expand = True)

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')


# run
window.mainloop()