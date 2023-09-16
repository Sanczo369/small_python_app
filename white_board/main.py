from tkinter import *

root = Tk()
root.title('White Board')
root.geometry("1050x570+150+50")
root.config(bg='#f2f3f5')
root.resizable(False,False)
root.iconbitmap('logo.ico')



color_box=PhotoImage(file="color_section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

root.mainloop()