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