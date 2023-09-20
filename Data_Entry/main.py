from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
# import openpyxl, xlrd
# from openpyxl import Workbook
import pathlib

root=Tk()
root.title("Data Entry")
root.geometry('700x400+300+200')
root.resizable(False, False)
root.configure(bg="#326273")
# root.iconbitmap('logo.ico')

Label(root, text="Proszę o wypełnienie formularza zgłoszeniowego", font="arial 13", bg="#326273", fg="#fff").place(x=20,y=20)

Label(root, text="Imię", font=23, bg="#326273", fg="#fff").place(x=50,y=100)
Label(root, text="Numer Kontaktowy", font=23, bg="#326273", fg="#fff").place(x=50,y=150)
Label(root, text="Wiek", font=23, bg="#326273", fg="#fff").place(x=50,y=200)
Label(root, text="Płeć", font=23, bg="#326273", fg="#fff").place(x=370,y=200)
Label(root, text="Address", font=23, bg="#326273", fg="#fff").place(x=50,y=250)

name_value = StringVar()
contact_value = StringVar()
age_value = StringVar()

name_entry = Entry(root,textvariable=name_value, width=45, bd=2, font=20)
contact_entry = Entry(root,textvariable=contact_value, width=45, bd=2, font=20)
age_entry = Entry(root,textvariable=age_value, width=45, bd=2, font=20)
gender_combobox= Combobox(root,values=['M','K'], font="arial 14", state='r', width=14)
address_entry= Text(root, width=50, height=4, bd=4)

name_entry.place(x=200,y=100)
contact_entry.place(x=200,y=150)
age_entry.place(x=200,y=200)
gender_combobox.place(x=440,y=200)
address_entry.place(x=200,y=250)


root.mainloop()