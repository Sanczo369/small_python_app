from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather_App")
root.geometry('900x500+300+200')
root.resizable(False,False)

#search box
textfield = tk.Entry(root, justify='center', width=17, font=("poppins", 25, "bold"), bg="#404040", fg="white")
textfield.place(x=50, y=40)
textfield.focus()
#search icon
myimage_icon = Button(borderwidth=0, cursor="hand2", bg="#404040")
myimage_icon.place(x=400, y=34)
root.mainloop()

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file='box.png')
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)