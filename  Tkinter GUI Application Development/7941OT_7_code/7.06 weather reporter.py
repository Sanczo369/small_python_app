"""
Code illustration: 7.06

Weather Reporter

Tkinter GUI Application Development Hotshot
"""
# -*- coding: utf-8 -*-

from Tkinter import *
import ttk
import urllib
import datetime
import json
from PIL import ImageTk
import tkMessageBox


class WeatherReporter:
    def __init__(self, root):
        self.root = root
        self.top_frame()
        self.display_frame()

    def top_frame(self):
        topfrm = Frame(self.root)
        topfrm.grid(row=1, sticky='w')
        Label(topfrm, text='Enter Location').grid(row=1, column=2, sticky='w')
        self.enteredlocation = StringVar()
        Entry(topfrm, textvariable=self.enteredlocation).grid(row=1, column=3, sticky='w')
        ttk.Button(topfrm, text='Show Weather Info', command= self.show_weather_button_clicked).grid(row=1, column=4, sticky='w')

    def display_frame(self):
        displayfrm = Frame(self.root)
        displayfrm.grid(row=2, sticky='ew', columnspan=5)
        self.canvas = Canvas(displayfrm, height='410', width='300', background='black', borderwidth=5)
        self.canvas.create_rectangle( 5, 5,305,415, fill='#F6AF06')
        self.canvas.grid(row=2, sticky='w', columnspan=5)
