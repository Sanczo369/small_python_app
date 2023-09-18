from tkinter import *

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")
root.iconbitmap('logo.ico')

top=PhotoImage(file="top.png")
top_image=Label(root, image=top, background="#f0f1f5")
top_image.place(x=50,y=0)





root.mainloop()