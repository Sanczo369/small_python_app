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

        # Tkinter Frame
        self.frame = Frame(self.window, bg=st.color2, width=st.width, height=st.height)
        self.frame.place(x=0, y=0)

        # Calling the function, startWindow()
        self.startWindow()

    def startWindow(self):
        # A Tkinter Label to display the title
        titleLabel = Label(self.frame, text="Typing Speed Test", bg=st.color2, fg=st.color1 ,font=(st.font3, 35, "bold"))
        titleLabel.place(x=175, y=80)

        startButton = Button(self.frame, text="Start Here", border=0, cursor='hand2' ,fg=st.color2, bg=st.color1, font=(st.font4, 18), command=self.startTest)
        startButton.place(x=320, y=215)