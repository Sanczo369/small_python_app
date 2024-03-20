import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling')

text_list = [('label', 'button'),('thing', 'click'),('third', 'something'),('label1', 'button'),('label2', 'button'),('label3', 'button'),('label4', 'button')]
list_frame = ListFrame(window, text_list, 100)

# run
window.mainloop()