from tkinter import *

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

colors=Canvas(root, bg="#ffffff", width=40, height=300, bd=0)
colors.place(x=42, y=55)

root.mainloop()