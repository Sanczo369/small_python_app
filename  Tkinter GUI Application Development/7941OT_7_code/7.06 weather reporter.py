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
