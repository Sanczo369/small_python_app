import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Stacking order')
window.geometry('400x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(window, text = 'Label 2', background = 'red')
label3 = ttk.Label(window, text = 'Label 3', background = 'blue')

# label1.lift()
# label2.lower()

button1 = ttk.Button(window, text = 'raise label 1', command = lambda: label1.lift(aboveThis = label2))
button2 = ttk.Button(window, text = 'raise label 2', command = lambda: label2.tkraise())
button3 = ttk.Button(window, text = 'raise label 3', command = lambda: label3.tkraise())
# run
window.mainloop()