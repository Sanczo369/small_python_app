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