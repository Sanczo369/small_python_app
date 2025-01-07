import os
import PyPDF2
import os.path
from tkinter import *
from functools import partial
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from tkinter import ttk, messagebox
from PyPDF2.pdf import PdfFileWriter

class PDF_Editor:
    def __init__(self, root):
        self.window = root
        self.window.geometry("740x480")
        self.window.title('PDF Editor')

        # Color Options
        self.color_1 = "white"
        self.color_2 = "gray30"
        self.color_3 = "black"
        self.color_4 = 'orange red'

        # Font Options
        self.font_1 = "Helvetica"
        self.font_2 = "Times New Roman"
        self.font_3 = "Kokila"

        self.saving_location = ''

        # ================Menubar Section===============
        self.menubar = Menu(self.window)