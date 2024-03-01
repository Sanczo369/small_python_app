import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title("Tab Widget")

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab 1')
button1.pack()


# run
window.mainloop()