import cv2
import pathlib
import pyautogui
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

class Image_Cartoonify:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x560")
        self.window.title('Cartoonify')
        self.window.resizable(width = False, height = False)

        self.width = 740
        self.height = 480

        self.Image_Path = ''

        # Creating Menubar
        self.menubar = Menu(self.window)

        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.open_image)

        # Menu widget to cartoonify the image
        cartoonify = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Cartoonify', menu=cartoonify)
        cartoonify.add_command(label='Create Cartoon', command=self.cartoonify)

        # Exit the Application
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=exit)
        exit.add_command(label='Exit', command=self._exit)

        # Configuring the menubar
        self.window.config(menu=self.menubar)
        # ===================End=======================

        # Creating a Frame
        self.frame = Frame(self.window,
        width=self.width,height=self.height)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        # Open an Image through filedialog
    def open_image(self):
        self.clear_screen()
        self.Image_Path = filedialog.askopenfilename(title="Select an Image",
                                                     filetypes=(("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            self.show_image(self.Image_Path)
    # Display the Image
    def show_image(self, Img):
        # Opening the image
        image = Image.open(Img)
        # resize the image, so that it fits to the screen
        resized_image = image.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(resized_image)

        # A Label Widget for displaying the Image
        label = Label(self.frame, image=self.img)
        label.pack()