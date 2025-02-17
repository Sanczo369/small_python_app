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

    def startTest(self):
        # Clearing the previous screen
        self.clearScreen()

        # Getting the total time allocated for the test
        self.totalTime = st.totalTime

        # Choosing a random paragraph from the list of several choices
        self.paragraph = random.choice(self.textList)

        # A Label widget for showing the remainning time
        self.timeLabel = Label(self.frame, text="1:00", bg=st.color2, fg=st.color1, font=(st.font1, 15))
        self.timeLabel.place(x=20, y=15)

        # A Tkinter Text widget to display the paragraph
        textBox = Text(self.frame, width=65, height=10, bg=st.color1, font=(st.color2, 13))
        textBox.place(x=40, y=80)

        # Inserting the text into the Text widget
        textBox.insert(END, self.paragraph)
        textBox.config(state='disabled')

        # A Tkinter Entry widget to get input from the user
        self.inputEntry = Entry(self.frame, fg=st.color2, bg=st.color1, width=35, font=(st.font4, 20))
        self.inputEntry.place(x=100, y=360)

        # Define the on press to capture key pressing
        ls = Listener(on_press=self.listener)
        # Starting a different thread for this task
        ls.start()

    def listener(self, key):
        self.key = str(key)

        # If any key is pressed, a different thread will create
        # to Count Down the remaining time.
        if self.key != None:
            self.typingStarted = True
            self.multiThreading()

        # Returning False to stop the thread created to
        # capture key pressing.
        return False

    def multiThreading(self):
        x = Thread(target=self.countDown)
        x.start()