from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("ENCRYPTION","Input Password")
    elif password!="1234":
        messagebox.showerror("ENCRYPTION","Invalid Paasword")
