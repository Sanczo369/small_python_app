import os
import cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

class Image_Rotator:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x600")
        self.window.title('Image Rotator')
        self.window.resizable(width=False, height=False)

        self.img = img
        self.rot_image = rot_image
        self.image_name = image_name
        self.Image_Path = image_path

        self.width = 740
        self.height = 480

        # Creating Menubar
        self.menubar = Menu(self.window)

        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.open_image)

        # Adding About Menu
        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=about)
        about.add_command(label='About', command=self.about)

        # Exit the Application
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=exit)
        exit.add_command(label='Exit', command=self.Exit)

        # Configuring the menubar
        self.window.config(menu=self.menubar)
        # ===================End=======================


        left_btn = Button(self.window, text="Left",
        font=("Helvetica", 15, 'bold'), command=self.rotate_left)
        left_btn.place(x=15,y=270)

        right_btn = Button(self.window, text="Right",
        font=("Helvetica", 15, 'bold'), command=self.rotate_right)
        right_btn.place(x=865,y=270)

        # Creating a Frame
        self.frame_1 = Frame(self.window,
        width=self.width,height=self.height)
        self.frame_1.pack()
        self.frame_1.place(anchor='center', relx=0.5, rely=0.5)

    # Onen an Image
    def open_image(self):
        self.clear_screen()
        self.Image_Path =
        filedialog.askopenfilename(title = "Select an Image",
        filetypes = (("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            self.image_name = os.path.basename(self.Image_Path)
            if self.image_name != '':
                self.show_image()

    # Show the selected Image
    def show_image(self):
        image = Image.open(self.Image_Path)
        resized_image = image.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(resized_image)

        # Create a Label Widget to display the text or Image
        label = Label(self.frame_1, image=self.img)
        label.pack()

    # Method to rotate the image 90-degree clockwise
    def rotate_right(self):
        if self.image_name == None:
            pass
        else:
            data = cv2.imread(self.Image_Path)
            self.rot_image = cv2.rotate(data, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(self.Image_Path, self.rot_image)
            self.clear_screen()
            self.show_image()

    # Method to rotate the image 90-degree anti-clockwise
    def rotate_left(self):
        if self.image_name == None:
            pass
        else:
            data = cv2.imread(self.Image_Path)
            self.rot_image = cv2.rotate(data, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(self.Image_Path, self.rot_image)
            self.clear_screen()
            self.show_image()