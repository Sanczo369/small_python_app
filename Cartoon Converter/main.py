import cv2
import pathlib
import pyautogui
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

class Image_Cartoonify:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x560")
        self.window.title('Cartoonify')
        self.window.resizable(width = False, height = False)

        self.width = 740
        self.height = 480

        self.Image_Path = ''

        # Creating Menubar
        self.menubar = Menu(self.window)

        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.open_image)

        # Menu widget to cartoonify the image
        cartoonify = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Cartoonify', menu=cartoonify)
        cartoonify.add_command(label='Create Cartoon', command=self.cartoonify)

        # Exit the Application
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=exit)
        exit.add_command(label='Exit', command=self._exit)