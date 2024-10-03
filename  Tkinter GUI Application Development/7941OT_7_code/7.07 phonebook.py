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

        fr = LabelFrame(master, text= 'Create New Record')
        fr.grid(row=0, column=1, padx=8,pady=8, sticky='ew')


        Label(fr, text='Name:').grid(row=1, column=1, sticky=W, pady=2)
        self.name= StringVar()
        self.namefield = Entry(fr, textvariable= self.name)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        Label(fr, text='Contact Number:').grid(row=2, column=1,sticky=W,  pady=2)
        self.num= IntVar()
        self.numfield = Entry(fr, textvariable= self.num)
        self.numfield.grid(row=2, column=2, sticky=W,padx=5, pady=2)
        ttk.Button(fr, text= 'Add Record', command=self.create_record).grid(row=3, column=2, sticky=E,padx=5, pady=2)
        showbtn = ttk.Button(text="Show Records", command = self.view_records)
        showbtn.grid(row=3, column=0, sticky=W)
