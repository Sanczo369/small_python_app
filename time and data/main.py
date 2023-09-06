from tkinter import *
from datetime import date
import time

root = Tk()
root.title('time and data')
root.geometry("400x400")
root.config(bg='black')


def update():
    calendar.config(text=date.today().strftime("%d/%m/%Y"))
    clock.config(text=time.strftime("%H:%M:%S"))
    clock.after(1000, update)

clock = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
calendar = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
clock.grid(column=0, row=0)
calendar.grid(column=0, row=1)
update()
root.mainloop()
