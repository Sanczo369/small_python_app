from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import names

root  = tk.Tk()
root.geometry('400x200')
root.title("Name Generators")


def search():
    Gender = gender.get()
    Type = types.get()

    if Gender == 'Male' and Type == "Full Name":
        name = names.get_full_name(gender="male")
        text.insert('end', name)
    elif Gender == 'Male' and Type == "First Name":
        name = names.get_first_name()
        text.insert('end', name)
    elif Gender == 'Male' and Type == "Last Name":
        name = names.get_last_name()
        text.insert('end', name)

    elif Gender == 'Female' and Type == "Full Name":
        name = names.get_full_name(gender="female")
        text.insert('end', name)
    elif Gender == 'Female' and Type == "First Name":
        name = names.get_first_name()
        text.insert('end', name)
    elif Gender == 'Female' and Type == "Last Name":
        name = names.get_last_name()
        text.insert('end', name)