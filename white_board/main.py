from tkinter import *
from tkinter.colorchooser import  askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('White Board')
root.geometry("1050x570+150+50")
root.config(bg='#f2f3f5')
root.resizable(False,False)
root.iconbitmap('logo.ico')



color_box=PhotoImage(file="color_section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser=PhotoImage(file="rubber_96712.png")
Button(root, image=eraser, bg='#f2f3f5').place(x=45, y=400)

colors=Canvas(root, bg="#ffffff", width=40, height=310, bd=0)
colors.place(x=42, y=55)

canvas =Canvas(root, width=900, height=510, background='white', cursor="hand2")
canvas.place(x=130, y=20)

def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,"Button-1", lambda x: show_color("black"))

    id = colors.create_rectangle((10,40,30,60),fill="grey")
    colors.tag_bind(id,"Button-1", lambda x: show_color("grey"))

    id = colors.create_rectangle((10,70,30,90),fill="brown")
    colors.tag_bind(id,"Button-1", lambda x: show_color("brown"))

    id = colors.create_rectangle((10,100,30,120),fill="red")
    colors.tag_bind(id,"Button-1", lambda x: show_color("red"))

    id = colors.create_rectangle((10,130,30,150),fill="orange")
    colors.tag_bind(id,"Button-1", lambda x: show_color("orange"))

    id = colors.create_rectangle((10,160,30,180),fill="yellow")
    colors.tag_bind(id,"Button-1", lambda x: show_color("yellow"))

    id = colors.create_rectangle((10,190,30,210),fill="green")
    colors.tag_bind(id,"Button-1", lambda x: show_color("green"))

    id = colors.create_rectangle((10,220,30,240),fill="blue")
    colors.tag_bind(id,"Button-1", lambda x: show_color("blue"))

    id = colors.create_rectangle((10,250,30,270),fill="purple")
    colors.tag_bind(id,"Button-1", lambda x: show_color("purple"))

    id = colors.create_rectangle((10,280,30,300),fill="pink")
    colors.tag_bind(id,"Button-1", lambda x: show_color("pink"))
display_pallete()

canvas.bind('<Button-1>')
canvas.bind('<B1-Motion>')
root.mainloop()