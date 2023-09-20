from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

root=Tk()
root.title("Data Entry")
root.geometry('700x400+300+200')
root.resizable(False, False)
root.configure(bg="#326273")
# root.iconbitmap('logo.ico')

Label(root, text="Proszę o wypełnienie formularza zgłoszeniowego", font="arial 13", bg="#326273", fg="#fff").place(x=20,y=20)




root.mainloop()