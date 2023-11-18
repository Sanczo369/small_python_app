import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

app = tk.Tk()
app.title('Youtube Downloader')
app.geometry("500x400")
window.iconbitmap('yt.ico')
app.configure(background='#cccccc')

# Browse Button
browse = tk.Button(app, text="Browse",command=browse_location,fg='black'  ,bg="DarkGoldenrod1"  ,width=11 ,height=1 , activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=600, y=270)

# Decision Buttons
clearButton = tk.Button(app, text="Clear",command=clear,fg="black" ,bg="dark turquoise" ,width=10 ,height=2 , activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=180, y=350)

down = tk.Button(app, text="Download",command=download_file,fg="black" ,bg="yellow green" ,width=10 ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
down.place(x=390, y=350)

app.mainloop()