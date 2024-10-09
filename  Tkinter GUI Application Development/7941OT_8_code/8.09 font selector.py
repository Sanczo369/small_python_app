"""
Code illustration: 8.09
Font Selector
Tkinter GUI Application Development Hotshot
"""
from tkinter import *
import ttk
import tkFont

class FontSelectorDemo():

   def __init__(self):
      self.currentfont     = tkFont.Font(font=('Times New Roman', 12))
      self.family          = StringVar(value='Times New Roman')
      self.fontsize        = StringVar(value='12')
      self.fontweight      = StringVar(value=tkFont.NORMAL)
      self.slant           = StringVar(value=tkFont.ROMAN)
      self.underlinevalue  = BooleanVar(value=False)
      self.overstrikevalue = BooleanVar(value=False)
      self.gui_creator()
