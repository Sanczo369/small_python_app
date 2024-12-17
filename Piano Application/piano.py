from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from playsound import playsound
root = tk.Tk()
root.geometry('700x300')
root.title("piano")
root.maxsize(700,300)
root.minsize(700,300)
root['bg']="white"
icon = ImageTk.PhotoImage(Image.open('piano.png'))
icon_label = Label(root,image=icon)
icon_label.place(x=295,y=10)
frame1 = Frame(root,width=700,height=198,bg="white")
frame1.place(x=0,y=100)


class piano():
    def PianoSound(self, sound):
        playsound(f'Piano{sound}.mp3')