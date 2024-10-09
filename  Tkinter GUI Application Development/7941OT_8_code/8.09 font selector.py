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

   def gui_creator(self):
      #font family selector combobox
      Label(text='Font Family').grid(row=0, column=0)
      fontList = ttk.Combobox(textvariable=self.family)
      fontList.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W, padx=10)
      fontList.bind('<<ComboboxSelected>>', self.on_value_change)
      allfonts = list(tkFont.families())
      allfonts.sort()
      fontList['values'] =  allfonts
