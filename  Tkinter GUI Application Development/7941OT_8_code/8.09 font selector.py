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

      # Font Sizes
      Label(text='Font Size').grid(row=0, column=2)
      sizeList = ttk.Combobox(textvariable=self.fontsize)
      sizeList.bind('<<ComboboxSelected>>', self.on_value_change)
      sizeList.grid(row=1, column=2, columnspan=2, sticky=N+S+E+W, padx=10)
      allfontsizes = range(6,70)
      sizeList['values'] =  allfontsizes

   def on_value_change(self, event=None):
      try:
         self.currentfont.config(family=self.family.get(), size=self.fontsize.get(), weight=self.fontweight.get(),
                                 slant=self.slant.get(), underline=self.underlinevalue.get(),
                                 overstrike=self.overstrikevalue.get())
         self.text.tag_config('fontspecs', font=self.currentfont)
      except ValueError as e:
         print(e)
         pass  ### invalid entry - ignored for now. You can use a tkMessageBox dialog to show an error
