import tkinter as tk
from tkinter import ttk


# exercise
# create a scrollbar
class ListFrame(ttk.Frame):
	def __init__(self, parent, text_data, item_height):
		super().__init__(master = parent)
		self.pack(expand = True, fill = 'both')

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height


        # canvas
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill='both')


        # display frame
        self.frame = ttk.Frame(self)


        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both', pady=4, padx=10)
# setup
window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling')

text_list = [('label', 'button'),('thing', 'click'),('third', 'something'),('label1', 'button'),('label2', 'button'),('label3', 'button'),('label4', 'button')]
list_frame = ListFrame(window, text_list, 100)

# run
window.mainloop()