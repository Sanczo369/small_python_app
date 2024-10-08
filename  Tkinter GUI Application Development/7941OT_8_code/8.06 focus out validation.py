"""
Code illustration: 8.06
validate='focusout' demo
Tkinter GUI Application Development Hotshot
"""
import tkinter as tk
import re


class FocusOutValidationDemo():
    def __init__(self):
        self.master = tk.Tk()
        self.errormsg = tk.Label(text='', fg='red')
        self.errormsg.pack()
        tk.Label(text='Enter Email Address').pack()
        vcmd = (self.master.register(self.validate_email), '%P')
        invcmd = (self.master.register(self.invalid_email), '%P')
        self.emailentry = tk.Entry(self.master, validate="focusout", validatecommand=vcmd, invalidcommand=invcmd)
        self.emailentry.pack()
        tk.Button(self.master, text="Login").pack()
        tk.mainloop()
