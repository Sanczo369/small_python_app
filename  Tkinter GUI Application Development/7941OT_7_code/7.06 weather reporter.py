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
