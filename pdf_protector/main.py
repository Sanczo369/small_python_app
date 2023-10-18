from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
root=Tk()
root.title("PDF Protector")
root.geometry("600x430+300+100")
root.resizable(False,False)

img_logo=PhotoImage(file="logo.png")
root.iconphoto(False, img_logo)

frame=Frame(root, width=580, height=290, bd=6, relief=GROOVE)
frame.place(x=10, y=130)

source=StringVar()
Label(frame, text="Source PDF File:", font="arial 10 bold", fg='#4c4542').place(x=30, y=50)
entry1= Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry1.place(x=150, y=48)




root.mainloop()