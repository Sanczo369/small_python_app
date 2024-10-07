"""
Code illustration: 8.04

Demonstration of percent substitutions in data validation
Tkinter GUI Application Development Hotshot
"""

import Tkinter as tk

class PSubDemo():
    def __init__(self):
        self.root = tk.Tk()
        tk.Label(text='Type Something Below').pack()
        vcmd = (self.root.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        tk.Entry(self.root, validate="all", validatecommand=vcmd).pack()
        self.root.mainloop()
