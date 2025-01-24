import os
import io
import random
import string
import numpy as np
import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto.Hash import SHA256, HMAC

class ImageEncryption:
    def __init__(self, root):
        self.window = root
        self.window.geometry("920x520")
        self.window.title('IMAGE ENCRYPTION APP')
        self.window.resizable(width = False, height = False)

        # ==============Start Menubar===============
        self.menubar = Menu(self.window, bg="#5956BA", fg="white", font=("Montserrat", 9))
        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='OPEN', menu=edit)
        edit.add_command(label='ENCRYPT',command=self.open_image_for_encryption)
        edit.add_command(label='DECRYPT',command=self.open_image_for_decryption)

        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ABOUT', menu=about)
        about.add_command(label='ABOUT', command=self.about)

        # Exit the Application
        _exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='EXIT', menu=_exit)
        _exit.add_command(label='EXIT', command=self.window.destroy)