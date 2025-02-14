import os
import shutil
from tkinter import *
from threading import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

file_types={
   'Documents' : ('.pdf','.doc','.xls','txt','.csv','.xml','.zip', '.docx', '.DOCX', '.odt'),
   'Pictures' : ('.jpg','.jpeg','.png','.JPG', '.webp'),
   'Videos' : ('.mp4','.mkv','.3gp','.flv','.mpeg'),
   'Music' : ('.mp3','.wav','.m4a','.webm'),
   'Programs' : ('.py','.cpp','.c','.sh','.js'),
   'Apps' : ('.exe','.apk'),
}

class File_Organizer:
    def __init__(self, root):
        # Setting the Tkinter main window
        self.window = root
        self.window.geometry("720x500")
        self.window.title('File Organizer - PySeek')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg='gray90')
        self.selected_dir = ''
        self.browsed = False
        # Frame 1: For the Logo
        self.frame_1 = Frame(self.window,bg='gray90',
        width=280, height=70)
        self.frame_1.pack()
        self.frame_1.place(x=20, y=20)
        self.display_logo()
        # About Button
        About_Btn = Button(self.window, text="About",
        font=("Kokila", 10, 'bold'), bg="dodger blue",
        fg="white", width=5, command=self.about_window)
        About_Btn.place(x=600, y=20)
        # Exit Button
        Exit_Btn = Button(self.window, text="Exit",
        font=("Kokila", 10, 'bold'), bg="dodger blue",
        fg="white", width=5, command=self.exit_window)
        Exit_Btn.place(x=600, y=60)
        # Frame 2: For the Main Page Widgets
        self.frame_2 = Frame(self.window, bg="white",
        width=720,height=480)
        self.frame_2.place(x=0, y=110)
        self.main_window()

    def display_logo(self):
        image = Image.open('Images/logo.png')
        resized_image = image.resize((280, 70))
        self.logo = ImageTk.PhotoImage(resized_image)
        label = Label(self.frame_1, bg='gray90',image=self.logo)
        label.pack()