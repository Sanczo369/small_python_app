import os
import glob
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk, filedialog

# File Extensions: You can modify it as per your requirements
file_types = ['.jpg', 'jpeg', '.png', '.mp3', '.mp4', '.pdf']


class File_Renamer:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("720x500")
        self.window.title('File Renamer - PySeek')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg='gray90')