"""
Code illustration: 7.07

Phonebook Application

Tkinter GUI Application Development Hotshot
"""

from Tkinter import *
import ttk
import sqlite3


class PhoneBook:
    def __init__(self, master):
        photo = PhotoImage(file='icons/phonebookicon.gif')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0)
