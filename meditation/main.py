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

        # Tkinter Frame
        self.frame = Frame(self.window, bg=st.color1, \
        width=800, height=450)
        self.frame.place(x=0, y=0)

        # Default values
        self.inhale = True
        self.exhale = False
        self.onHomePage = False
        self.defaultTime = st.baseTime

        # Calling Home Page
        self.HomePage()

    # Manage the Home/Welcoming Window
    def HomePage(self):
        self.Reset()
        self.ClearScreen()
        self.BgImage(st.bgImage1)
        self.StartButton()
        self.TimeButton()
        self.RemainingTime(self.defaultTime)

    # Function to reset the default values
    def Reset(self):
        self.onHomePage = True
        self.inhale = True
        self.exhale = False
        self.defaultTime = st.baseTime

    # Clear all widgets from the Tkinter Frame
    def ClearScreen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

   # Displays the background image
    def BgImage(self, img):
        image = Image.open(img)
        resizedImg = image.resize((st.width, st.height))
        self.img1 = ImageTk.PhotoImage(resizedImg)

        label = Label(self.frame, image=self.img1)
        label.pack()

    # Button to Start Meditation
    def StartButton(self):
        image = Image.open(st.startBtn)
        resizedImg = image.resize((130,130))
        self.img2 = ImageTk.PhotoImage(resizedImg)

        self.button = Button(self.frame, image=self.img2, \
        bg=st.color2, border=0, cursor='hand2', \
        command=self.MeditationPage)
        self.button.place(x=320, y=120)

    # Button for setting the duration of mediation
    def TimeButton(self):
        image = Image.open(st.setTimeBtn)
        resizedImg = image.resize((130,40))
        self.img3 = ImageTk.PhotoImage(resizedImg)

        self.button = Button(self.frame, image=self.img3, \
        bg=st.color2, border=0, cursor='hand2', \
        command=self.SecondWindow)
        self.button.place(x=320, y=270)


    # Label to show the remaining time of mediation
    def RemainingTime(self, rTime):
        mins, secs = divmod(rTime, 60)
        self.timeLabel = Label(self.frame, text=f"{mins}:{secs}", \
        bg=st.color2, fg=st.color3 ,font=(st.font3, 15))
        self.timeLabel.place(x=727, y=25)

    # A different window for setting the mediation period
    def SecondWindow(self):
        self.newWindow = Tk()
        self.newWindow.title("Set Time")
        self.newWindow.geometry(st.resolution)

        self.totalTime = IntVar()

        self.chosenTime = ttk.Combobox(self.newWindow, \
        textvariable=self.totalTime, values=st.timeList, \
        font=(st.font3, 20), width=8)
        self.chosenTime.set(1)
        self.chosenTime.place(x=160, y=110)

        setTimeBtn = Button(self.newWindow, text="Set Time", \
        font=(st.font4, 11), bg=st.color5, fg=st.color2, \
        cursor='hand2', command=self.GetTime)
        setTimeBtn.place(x=185, y=150)