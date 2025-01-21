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