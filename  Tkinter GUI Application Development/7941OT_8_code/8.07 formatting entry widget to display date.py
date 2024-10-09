"""
Code illustration: 8.07
Formatting Entry Widget
Tkinter GUI Application Development Hotshot
"""
from tkinter import *
class FormatEntryWidgetDemo:
    def __init__(self, root):
        Label(root, text='Date(MM/DD/YYYY)').pack()
        self.entereddata = StringVar()
        self.dateentrywidget = Entry(textvariable=self.entereddata)
        self.dateentrywidget.pack(padx=5, pady=5)
        self.dateentrywidget.focus_set()
        self.slashpositions = [2, 5]
        root.bind('<Key>', self.format_date_entry_widget)

    def format_date_entry_widget(self, event):
        entrylist = [c for c in self.entereddata.get() if c != '/']
        for pos in self.slashpositions:
            if len(entrylist) > pos:
                entrylist.insert(pos, '/')
        self.entereddata.set(''.join(entrylist))
