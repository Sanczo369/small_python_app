import os
import cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

class Image_Rotator:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x600")
        self.window.title('Image Rotator')
        self.window.resizable(width=False, height=False)

        self.img = img
        self.rot_image = rot_image
        self.image_name = image_name
        self.Image_Path = image_path

        self.width = 740
        self.height = 480

        # Creating Menubar
        self.menubar = Menu(self.window)

        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.open_image)

        # Adding About Menu
        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=about)
        about.add_command(label='About', command=self.about)