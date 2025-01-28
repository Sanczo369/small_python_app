import os
import io
import random
import string
import numpy as np
import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from Crypto.Hash import SHA256, HMAC

class ImageEncryption:
    def __init__(self, root):
        self.window = root
        self.window.geometry("920x520")
        self.window.title('IMAGE ENCRYPTION APP')
        self.window.resizable(width = False, height = False)

        # ==============Start Menubar===============
        self.menubar = Menu(self.window, bg="#5956BA", fg="white", font=("Montserrat", 9))
        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='OPEN', menu=edit)
        edit.add_command(label='ENCRYPT',command=self.open_image_for_encryption)
        edit.add_command(label='DECRYPT',command=self.open_image_for_decryption)

        about = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='ABOUT', menu=about)
        about.add_command(label='ABOUT', command=self.about)

        # Exit the Application
        _exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='EXIT', menu=_exit)
        _exit.add_command(label='EXIT', command=self.window.destroy)

        # Configuring the menubar
        self.window.config(menu=self.menubar)
        # ===================End of menubar=======================

        # ===================Start of frames====================
        self.frame1 = Frame(self.window, bg='white')
        self.frame1.place(x=0, y=0, width=720, height=420)

        self.frame2 = Frame(self.window, bg='white')
        self.frame2.place(x=0, y=420, width=720, height=100)

        self.frame3 = Frame(self.window, bg='yellow')
        self.frame3.place(x=720, y=0, width=200, height=520)
        # ==================End of frames======================

        sidebar_image = Image.open("Images/sidebar.png")
        footer_image = Image.open("Images/footer.png")
        encrypt_img = PhotoImage(file='Images/encrypt.png')
        decrypt_img = PhotoImage(file='Images/decrypt.png')
        self.browse_iv_img = PhotoImage(file='Images/browse_iv.png')

        # Displaying sidebar image
        self.img1 = ImageTk.PhotoImage(sidebar_image)
        label1 = Label(self.frame3, image=self.img1)
        label1.pack()

        # Displaying footer image
        self.img2 = ImageTk.PhotoImage(footer_image)
        label2 = Label(self.frame2, image=self.img2)
        label2.pack()

        # Encryption Button
        btn_1 = Button(self.frame3, image=encrypt_img, border=0, cursor="hand2", command=self.pre_encryption)
        btn_1.place(x=35, y=70)

        encrypt_btn = customtkinter.CTkButton(master=self.frame3, image=encrypt_img)
        encrypt_btn.pack(padx= 20, pady=20)

        # Decryption Button
        btn_2 = Button(self.frame3, image=decrypt_img, border=0, cursor="hand2", command=self.pre_decryption)
        btn_2.place(x=35, y=125)

        decrypt_btn = customtkinter.CTkButton(master=self.frame3, image=decrypt_img)
        decrypt_btn.pack(padx= 20, pady=20)

        self.default_values()

    def default_values(self):
        self.encryption_status = False
        self.decryption_status = False
        self.image_path = ''
        self.iv_path = ''

    # Resizing the image
    def resize_image(self, image_path):
        image = Image.open(image_path)
        width, height = image.size

        # Determine image type and calculate resize dimensions
        if width > height:  # Landscape
            new_width = self.frame1.winfo_width()
            new_height = int(height * (new_width / width))
        elif width < height:  # Portrait
            new_height = self.frame1.winfo_height()
            new_width = int(width * (new_height / height))
        else:  # Square
            new_width = 400
            new_height = 400

        return new_width, new_height

    # Displays the original image before encryption
    def display_original_image(self, image_path):
        image = Image.open(image_path)
        self.clear_screen()
        self.width, self.height = self.resize_image(self.image_path)
        resized_image = image.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.image = ImageTk.PhotoImage(resized_image)

        # Create a new inner frame for the resized image
        inner_frame = Frame(self.frame1, width=self.width, height=self.height)
        inner_frame.pack()

        # Create a label to display the image
        image_label = Label(inner_frame, image=self.image)
        image_label.pack()

        # Displays the image information
        self.image_information_1()

    # Displays the decryprted image after decryption operation
    def display_decrypted_image(self, image_path):
        self.clear_screen()

        image = Image.open(image_path)
        self.width, self.height = self.resize_image(image_path)
        resized_image = image.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.image = ImageTk.PhotoImage(resized_image)

        # Create a new inner frame for the resized image
        inner_frame = Frame(self.frame1, width=self.width, height=self.height)
        inner_frame.pack()

        # Create a label to display the image
        image_label = Label(inner_frame, image=self.image)
        image_label.pack()

        self.file_name_label.config(text=f"Image: {os.path.basename(image_path)}")
        self.file_status_label.config(text=f"Decrypted Image", bg="green")

        self.key_entry.destroy()
        self.btn_3.destroy()

        # Displays a dummy image
    def display_placeholder_image(self):
        self.clear_screen()
        image = Image.open("Images/sample_encrypted_image.png")

        # Create an object of tkinter ImageTk
        self.image = ImageTk.PhotoImage(image)

        # Create a new inner frame for the resized image
        inner_frame = Frame(self.frame1, width=720, height=420)
        inner_frame.pack()

        # Create a label to display the image
        image_label = Label(inner_frame, image=self.image)
        image_label.pack()

        # Displays the image information
        self.image_information_1()


    # Displays the decryprted image after decryption operation
    def display_decrypted_image(self, image_path):
        self.clear_screen()

        image = Image.open(image_path)
        self.width, self.height = self.resize_image(image_path)
        resized_image = image.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.image = ImageTk.PhotoImage(resized_image)