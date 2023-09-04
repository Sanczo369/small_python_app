from tkinter import *
import time



root = Tk()
root.title('clock')
root.geometry("400x600")
root.config(bg='black')


def update():
    clock.config(text=time.strftime("%H:%M:%S"))
    clock.after(1000, update)


clock = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
start_btn = Button(root, text="Start")
stop_btn = Button(root, text="Stop")
reset_btn = Button(root, text="Reset")

clock.grid(row=0, column=0, columnspan=4, padx=50, pady=15)
start_btn.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
stop_btn.grid(row=1, column=1, columnspan=4, padx=50, pady=15)
reset_btn.grid(row=1, column=2, columnspan=4, padx=50, pady=15)

update()
root.mainloop()
