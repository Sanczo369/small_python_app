import pyperclip
from tkinter import *
from threading import *
from tkinter import ttk
from pytube import YouTube
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox, ttk

# Resolution Options(Audio Option is also available)
download_quality = ['144p', '360p', '720p', 'Audio Only']

class Yt_Downloader:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("700x480")
        self.window.title('YouTube Video and Audio Downloader')
        self.window.resizable(width=False, height=False)

        self.save_to_loc = ''

        # Frame 1: For YouTube Logo
        self.frame_1 = Frame(self.window, width=220, height=80)
        self.frame_1.pack()
        self.frame_1.place(x=20, y=20)

        # Frame 2: For Download Logo
        self.frame_2 = Frame(self.window, width=50, height=50)
        self.frame_2.pack()
        self.frame_2.place(x=235, y=40)

        self.show_yt_logo()
        self.show_dn_logo()

        # About Button
        about_btn = Button(self.window, text="About", \
        font=("Kokila", 10, 'bold'), bg="dodger blue", \
        fg="white", width=5, command=self.About_Window)
        about_btn.place(x=600, y=30)

        # Exit Button
        exit_btn = Button(self.window, text="Exit", \
        font=("Kokila", 10, 'bold'), bg="dodger blue", \
        fg="white", width=5, command=self.Exit_Window)
        exit_btn.place(x=600, y=70)

        # Frame 3: For the Main Page Widgets
        self.frame_3 = Frame(self.window, bg="white", \
                             width=700, height=480)
        self.frame_3.place(x=0, y=130)

        # Calling the Main_Window() Function
        self.Main_Window()

    # This function displays the YouTube Logo
    def show_yt_logo(self):
        # Opening the YouTube logo image
        image = Image.open('Images/YouTube_logo.png')
        # Resizing the image
        resized_image = image.resize((220, 80))

        # Create an object of tkinter ImageTk
        self.img_1 = ImageTk.PhotoImage(resized_image)

        # Create a Label Widget to display the text or Image
        label = Label(self.frame_1, image=self.img_1)
        label.pack()

    # This Function displays the Download logo
    def show_dn_logo(self):
        # The image Path(Opening the image)
        image = Image.open('Images/Download_Button.png')
        resized_image = image.resize((50, 50))

        # Create an object of tkinter ImageTk
        self.img_2 = ImageTk.PhotoImage(resized_image)

        # Create a Label Widget to display the text or Image
        label = Label(self.frame_2, image=self.img_2)
        label.pack()