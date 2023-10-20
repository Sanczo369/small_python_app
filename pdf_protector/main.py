from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
root=Tk()
root.title("PDF Protector")
root.geometry("600x430+300+100")
root.resizable(False,False)

def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Wybierz plik obrazu", filetypes=(("PDF file", "*.pdf"), ("All files", ".")))
    entry1.insert(END, filename)

def Protect():
    mainfile=source.get()
    protectfile=target.get()
    code=password.get()

    if mainfile=="" and protectfile=="" and password.get()=="":
        messagebox.showerror("Invalid", "All entries are empty!")
    elif mainfile=="":
        messagebox.showerror("Invalid", "Please Type Souce PDF Filename")
    elif protectfile=="":
        messagebox.showerror("Invalid", "Please Type Target PDF Filename")
    elif password.get()=="":
        messagebox.showerror("Invalid", "Please Type Password")
    else:
        try:
            out=PdfFileWriter()
            file= PdfFileReader(filename)
            num = file.numPages

            for idx in range(num):
                page=file.getPage(idx)
                out.addPage(page)
            out.encrypt(code)

            with open(protectfile, "wb") as f:
                out.write(f)

            source.set("")
            target.set("")
            password.set("")

            messagebox.showinfo("info", "Successfully done!!!")

        except:
            messagebox.showerror("Invalid", "Invalid Entry!!!")

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

Button_Source=PhotoImage(file="file_select.png")
Button(frame,image=Button_Source, width=35, height=24, bg="#d3cdcd", command=browse).place(x=500, y=47)

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