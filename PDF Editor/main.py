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