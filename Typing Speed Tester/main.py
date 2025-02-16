import time
import random
import text as tt
from tkinter import *
import settings as st
from threading import *
from PIL import Image, ImageTk
from pynput.keyboard import Listener

class TypingTest:
    def __init__(self, root):
        # Window Settings
        self.window = root
        self.window.geometry(f"{st.width}x{st.height}")
        self.window.title('Typing Tester')
        self.window.resizable(width=False, height=False)
        self.window.configure(bg=st.color2)

        # Declaring some variables
        self.key = None
        self.typingStarted = False

        # Text for using as a paragraph
        self.textList = [tt.text1, tt.text2, tt.text3, tt.text4, tt.text5]