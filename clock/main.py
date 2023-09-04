from tkinter import *
import time

root= Tk()
root.title('clock')
root.geometry("400x600")
root.config(bg='black')

def update():
    clock.config(text=time.strftime("%H:%M:%S"))
    clock.after(1000,update)


clock = Label(root, background = 'black',foreground = 'white', font = ('arial', 40, 'bold'))
clock.pack()
update()
root.mainloop()