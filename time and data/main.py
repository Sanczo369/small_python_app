from tkinter import *

root = Tk()
root.title('time and data')
root.geometry("400x400")
root.config(bg='black')



clock = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
calendar = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
clock.grid(column=0, row=0)
calendar.grid(column=0, row=1)
root.mainloop()
