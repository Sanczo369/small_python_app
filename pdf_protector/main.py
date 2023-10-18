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

root.mainloop()