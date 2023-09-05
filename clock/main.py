from tkinter import *
import time

running = False
hours, minute, seconds = 0, 0, 0

def start():
    global running
    if not running:
        update()
        running = True

root = Tk()
root.title('clock')
root.geometry("400x600")
root.config(bg='black')
root.iconbitmap('logo.ico')

def update():
    clock.config(text=time.strftime("%H:%M:%S"))
    clock.after(1000, update)

button_style = {
    "height": 2,
    "width": 10,
    "font": ('arial', 12, 'bold'),
    "fg": '#ffffff',
    "bd": 0,
}

clock = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
start_btn = Button(root, text="Start", bg="#4169E1", **button_style)
stop_btn = Button(root, text="Stop", bg="#ff0000", **button_style)
reset_btn = Button(root, text="Reset", bg="#222222", **button_style)

clock.grid(row=0, columnspan=3, padx=50, pady=15)
start_btn.grid(row=1, column=0, padx=10, pady=15)
stop_btn.grid(row=1, column=1, padx=10, pady=15)
reset_btn.grid(row=1, column=2, padx=10, pady=15)

update()
root.mainloop()
