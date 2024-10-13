from tkinter import *
from PIL import Image,ImageTk

class LCD_CNN:
    def __init__(self,root):
        self.root=root
        #window size
        self.root.geometry("1006x500+0+0")
        self.root.resizable(False, False)
        self.root.title("Lung Cancer Detection")

        img4=Image.open(r"Images\Lung-Cancer-Detection.jpg")
        img4=img4.resize((1006,500),Image.ANTIALIAS)
        #Antialiasing is a technique used in digital imaging to reduce the visual defects that occur when high-resolution images are presented in a lower resolution.
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=50,width=1006,height=500)

        # title Label
        title_lbl=Label(text="Lung Cancer Detection",font=("Bradley Hand ITC",30,"bold"),bg="black",fg="white",)
        title_lbl.place(x=0,y=0,width=1006,height=50)

        #button 1
        self.b1=Button(text="Import Data",cursor="hand2",command=self.import_data,font=("Times New Roman",15,"bold"),bg="white",fg="black")
        self.b1.place(x=80,y=130,width=180,height=30)

        #button 2
        self.b2=Button(text="Pre-Process Data",cursor="hand2",command=self.preprocess_data,font=("Times New Roman",15,"bold"),bg="white",fg="black")
        self.b2.place(x=80,y=180,width=180,height=30)
        self.b2["state"] = "disabled"
        self.b2.config(cursor="arrow")

        #button 3
        self.b3=Button(text="Train Data",cursor="hand2",command=self.train_data,font=("Times New Roman",15,"bold"),bg="white",fg="black")
        self.b3.place(x=80,y=230,width=180,height=30)
        self.b3["state"] = "disabled"
        self.b3.config(cursor="arrow")