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

topLabel = Label(root, text="PDF Protector",font=("arial",40,"bold"))
topLabel.pack(pady=(40,0))

source=StringVar()
Label(frame, text="Source PDF File:", font="arial 10 bold", fg='#4c4542').place(x=30, y=50)
entry1= Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry1.place(x=150, y=48)

Button_Source=PhotoImage(file="btn.png")
Button(frame,image=Button_Source, width=35, height=24, bg="#d3cdcd").place(x=500, y=47)

target=StringVar()
Label(frame, text="Target PDF File:", font="arial 10 bold", fg='#4c4542').place(x=30, y=100)
entry2= Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
entry2.place(x=150, y=100)

password=StringVar()
Label(frame, text="Set User Password:", font="arial 10 bold", fg='#4c4542').place(x=15, y=150)
entry3= Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
entry3.place(x=150, y=150)

Button_icon=PhotoImage(file="btn.png")
Protect=Button(root,text="     Protect PDF File",compound=LEFT, image=Button_icon, width=230, height=50, bg="#bfb9b9",font="arial 10 bold")
Protect.pack(side=BOTTOM, pady=40)

root.mainloop()