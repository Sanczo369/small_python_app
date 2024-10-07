"""
Code illustration: 8.03

Validation Modes Demo

Tkinter GUI Application Development Hotshot
"""

import tkinter as tk

class ValidateModeDemo():
    def __init__(self):
        self.root = tk.Tk()
        vcmd = (self.root.register(self.validate), '%V')

        # validate = none mode - will not call validate method ever.
        tk.Label (text='None').pack()
        tk.Entry(self.root, validate="none", validatecommand=vcmd).pack()

        # validate = focus mode - will call validate method on focusin and focusout
        tk.Label (text='Focus').pack()
        tk.Entry(self.root, validate="focus", validatecommand=vcmd).pack()

        # validate = Key mode - will call validate method only when you type something or edit the entry
        tk.Label (text='key').pack()
        tk.Entry(self.root, validate="key", validatecommand=vcmd).pack()

        # validate = all mode - will call validate method on focus and key events
        tk.Label (text='all').pack()
        tk.Entry(self.root, validate="all", validatecommand=vcmd).pack()
