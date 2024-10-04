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

        self.msg = Label(text='', fg='red')
        self.msg.grid(row=3, column=1, sticky=W)

        self.tree = ttk.Treeview(height=5, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=W)
        self.tree.heading(2, text='Phone Number', anchor=W)

        delbtn = ttk.Button(text="Delete Selected", command = self.delete_record)
        delbtn.grid(row=5, column=0, sticky=W)

        updtbtn = ttk.Button(text="Modify Selected", command = self.open_modify_window)
        updtbtn.grid(row=5, column=1, sticky=W)
        #self.view_records()

    def create_record(self):
        name = self.namefield.get()
        num = self.numfield.get()
        if name == "":
            self.msg["text"] = "Please Enter name"
            return
        if num == "":
            self.msg["text"] = "Please Enter Number"
            return
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts VALUES(NULL,?, ?)", (name, num))
        conn.commit()
        c.close()
        self.namefield.delete(0, END)
        self.numfield.delete(0, END)
        self.msg["text"] = "Phone Record of %s Added" % name
        self.view_records()

    def view_records(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        list = c.execute("SELECT * FROM contacts ORDER BY name desc")
        for row in list:
            self.tree.insert("", 0, text=row[1], values=row[2])
        c.close()

    def delete_record(self):
            self.msg["text"] = ""
            conn = sqlite3.connect('phonebook.db')
            c = conn.cursor()
            name = self.tree.item(self.tree.selection())['text']
            query = "DELETE FROM contacts WHERE name = '%s';" %name
            c.execute(query)
            conn.commit()
            c.close()
            self.msg["text"] = "Phone Record for %s Deleted" %name
            self.view_records()


