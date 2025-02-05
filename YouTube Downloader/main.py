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

    # This function displays all the widgets in the Main Page
    def Main_Window(self):
        self.URL = Entry(self.frame_3, \
        font=("Helvetica", 18), width=41)
        self.URL.place(x=20,y=20)

        # Paste URL Button
        paste_btn = Button(self.frame_3, text="Paste URL", \
        command=self.Paste_URL)
        paste_btn.place(x=580,y=20)

        # Resolution Label
        resolution_lbl = Label(self.frame_3, \
        text="Download Quality", \
        font=("Times New Roman", 13, 'bold'))
        resolution_lbl.place(x=150, y=70)

        self.quality = StringVar()
        # Combo Box for showing the available video resolution
        # and  Audio download options
        self.quality_combobox = ttk.Combobox(self.frame_3, \
        textvariable=self.quality, font=("times new roman",13))
        self.quality_combobox['values'] = download_quality
        self.quality_combobox.current(0)
        self.quality_combobox.place(x=310,y=70)

        # Save To Button: Where the downloaded file will be stored
        save_to_btn = Button(self.frame_3, text="Save To", \
        font=("Kokila", 10, 'bold'), bg="gold", width=6, \
        command=self.Select_Directory)
        save_to_btn.place(x=150, y=110)

        # Tkinter Label sor showing the Save To location path
        # on the window
        self.loc_label = Label(self.frame_3, \
        text=self.save_to_loc, font=("Helvetica", 12), \
        fg='blue', bg='white')
        self.loc_label.place(x=240, y=116)

        status_lbl = Label(self.frame_3, text="Status", \
        font=("Times New Roman", 13, 'bold'))
        status_lbl.place(x=150, y=160)