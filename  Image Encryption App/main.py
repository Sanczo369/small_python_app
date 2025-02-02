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

    # Displays the original image information
    def image_information_1(self):
        image = Image.open(self.image_path)
        width, height = image.size

        self.image_name_label = Label(self.frame2, text=f"Image Name: {os.path.basename(self.image_path)}", font=("Montserrat", 8), bg="#03226F", fg="white")
        self.image_name_label.place(x=20, y=17)

        self.image_size_label = Label(self.frame2, text=f"Image Size: {width}x{height}", font=("Montserrat", 8), bg="#03226F", fg="white")
        self.image_size_label.place(x=20, y=42)

        self.status_label = Label(self.frame2, text="Image is Opened", font=("Montserrat", 8), bg="#03226F", fg="white")
        self.status_label.place(x=20, y=67)

    # Displays the encrypted image information
    def image_information_2(self):
        self.clear_screen()

        self.key_var = StringVar(value='')
        self.key_entry = Entry(self.frame3, textvariable=self.key_var, font=("Montserrat", 8), width=15)
        self.key_entry.place(x=81, y=222)

        self.btn_3 = Button(self.frame3, image=self.browse_iv_img, border=0, cursor="hand2",
                            command=self.browse_IV_file)
        self.btn_3.place(x=35, y=350)

        self.browse_iv_btn = customtkinter.CTkButton(master=self.frame3, image=self.browse_iv_img)
        self.browse_iv_btn.pack(padx=20, pady=20)

        self.file_name_label = Label(self.frame2, text=f"Image Name: {os.path.basename(self.image_path)}",
                                     font=("Montserrat", 8), bg="#03226F", fg="white")
        self.file_name_label.place(x=20, y=17)

        self.file_status_label = Label(self.frame2, text="Image is Opened", font=("Montserrat", 8), bg="#03226F",
                                       fg="white")
        self.file_status_label.place(x=20, y=42)

    # Opens the filedialog to select a directory for saving resulting image
    def choose_directory(self):
        chosen_dir = filedialog.askdirectory()
        if chosen_dir:
            return chosen_dir
    # Generates random key values
    def generate_random_text(self):
        # Available length options: 16, 24, or 32 (You can modify here)
        length = 32
        # Define the character pool containing all desired characters
        char_pool = string.ascii_uppercase + string.ascii_lowercase + string.digits

        random_text = ''.join(random.sample(char_pool, length))
        return random_text

    # Performs encryption on images
    def encrypt_image(self, image_path, output_image_path, iv_path, key):
        image = Image.open(image_path)

        # Generate a random IV
        iv = get_random_bytes(AES.block_size)

        # Get a unique identifier from the filename
        image_hash = SHA256.new(os.path.basename(image_path).encode("utf-8")).hexdigest()

        # Combine key-specific value with random string (nonce) using HMAC
        key_specific = HMAC.new(key, msg=image_hash.encode("utf-8"), digestmod=SHA256).digest()
        unique_iv = HMAC.new(key_specific, msg=os.urandom(16), digestmod=SHA256).digest()[:16]

        # Convert the image to bytes
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format=image.format)
        img_bytes = img_byte_array.getvalue()

        # Initialize AES cipher
        cipher = AES.new(key, AES.MODE_CBC, unique_iv)

        # Encrypt the image data with padding
        padded_data = pad(img_bytes, AES.block_size)
        encrypted_data = iv + cipher.encrypt(padded_data)

        # Write the encrypted data with IV to the output image file
        with open(output_image_path, 'wb') as f:
            f.write(encrypted_data)

        # Saving the iv file
        with open(iv_path, 'wb') as f:
            f.write(unique_iv)

        self.decryption_status = False

    # Performs pre-encryprion tasks
    def pre_encryption(self):
        if self.image_path == '':
            tk.messagebox.showerror(title="Image Missing", message="Please select an image")
        else:
            key = self.generate_random_text()
            key = bytes(key, encoding="utf-8")
            key_str = key[0:].decode("utf-8")

            chosen_dir = self.choose_directory()
            filename = os.path.basename(self.image_path)
            image_name = filename.split('.')[0]
            output_image_path = f"{chosen_dir}/{image_name}_encrypted.jpg"
            iv_path = f"{chosen_dir}/{image_name}_encrypted.iv"

            self.encrypt_image(self.image_path, output_image_path, iv_path, key)

            self.status_label.config(text="Image is encrypted", bg="green")

            self.key_label_var = StringVar()
            self.key_label = Entry(self.frame2, textvariable=self.key_label_var, font=("Montserrat", 8), width=20,
                                   bg="#03226F", fg="white")
            self.key_label.insert(0, f"{key_str}")
            self.key_label.place(x=180, y=17)

            self.clear_screen()
            self.image_path = ''

    # Selecting the iv file (secret file)
    def browse_IV_file(self):
        self.iv_path = filedialog.askopenfilename(title="Select the IV File", filetypes=(("IV File", "*.iv"),))

  # Performs decryption on images
    def decrypt_image(self, input_image_path, output_image_path, key, iv_path):
        self.output_image_path = output_image_path

        # Read the IV from the separate file
        with open(iv_path, 'rb') as f:
            unique_iv = f.read()

        # Read the encrypted data
        with open(input_image_path, 'rb') as f:
            encrypted_data = f.read()

        try:
            # Separate the IV from the encrypted data
            iv = encrypted_data[:AES.block_size]
            encrypted_data = encrypted_data[AES.block_size:]

            # Initialize AES cipher
            cipher = AES.new(key, AES.MODE_CBC, unique_iv)

            # Decrypt the image data
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)