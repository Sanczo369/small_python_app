import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')

# pack
# label1.pack(side = 'left', expand = True, fill = 'y')
# label2.pack(side = 'left', expand = True, fill = 'both')

# run
window.mainloop()