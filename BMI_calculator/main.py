from tkinter import *
from tkinter import ttk
import tkinter as tk

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

Height=StringVar()
Weight=StringVar()
height=Entry(root, textvariable=Height, width=4, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=52,y=145)
#Height.set(get_current_value())
weight=Entry(root, textvariable=Weight, width=4, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=272,y=145)
#Weight.set(get_current_value2())




# Slider 1
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

slider= ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=236)


# Slider 2
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

slider2= ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=236)


Button(root,text="Raport", width=15,height=2,font="arial 10 bold", bg="#1f6e68", fg="white").place(x=280,y=340)


scale=PhotoImage
root.mainloop()