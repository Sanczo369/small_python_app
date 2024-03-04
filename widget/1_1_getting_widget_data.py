import tkinter as tk
from tkinter import ttk

def button_func():
	# get the content of the entry
	entry_text = entry.get()

	# update the label
	# label.configure(text = 'some other text')
	label['text'] = entry_text
	entry['state'] = 'disabled'
	# print(label.configure())

# window
window = tk.Tk()
window.title('Getting and setting widgets')


# run
window.mainloop()