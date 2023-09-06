from tkinter import *

running = False
hours, minutes, seconds = 0, 0, 0

def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        clock.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:
        clock.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    clock.config(text='00:00:00')


def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    clock.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    global update_time
    update_time = clock.after(1000, update)

root = Tk()
root.title('stopwatch')
root.geometry("400x600")
root.config(bg='black')
root.iconbitmap('logo.ico')


button_style = {
    "height": 2,
    "width": 10,
    "font": ('arial', 12, 'bold'),
    "fg": '#ffffff',
    "bd": 0,
}

clock = Label(root, background='black', foreground='white', font=('arial', 40, 'bold'))
start_btn = Button(root, text="Start", bg="#4169E1", **button_style, command=start)
stop_btn = Button(root, text="Stop", bg="#ff0000", **button_style, command=pause)
reset_btn = Button(root, text="Reset", bg="#222222", **button_style, command=reset)

clock.grid(row=0, columnspan=3, padx=50, pady=15)
start_btn.grid(row=1, column=0, padx=10, pady=15)
stop_btn.grid(row=1, column=1, padx=10, pady=15)
reset_btn.grid(row=1, column=2, padx=10, pady=15)

root.mainloop()
