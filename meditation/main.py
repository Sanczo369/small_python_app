'''A Meditation Application in Python - Tkinter Project
- developed by Subhankar Rakshit.
'''
import time
import settings as st
from tkinter import *
from threading import *
import multiprocessing as mp
from PIL import ImageTk, Image
from playsound import playsound
from tkinter import ttk, messagebox

class Meditation:
    def __init__(self, root):
        # Window Settings
        self.window = root
        self.window.geometry(f"{st.width}x{st.height}")
        self.window.title('Meditation App')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg=st.color2)