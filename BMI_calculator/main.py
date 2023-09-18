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

Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

box=PhotoImage(file="box.png")
Label(root,image=box).place(x=40,y=100)
Label(root,image=box).place(x=260,y=100)
root.mainloop()