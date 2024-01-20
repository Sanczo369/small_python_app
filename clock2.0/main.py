import tkinter
import time
from tkinter import scrolledtext

if __name__ == "__main__":

    window = tkinter.Tk()
    frame = tkinter.Frame(window, width=800, height=800)
    frame.pack()

    tkinter.Label(frame, text="Current time: ").pack()

    text = scrolledtext.ScrolledText(frame, height=10)
    text.pack()

    clock1 = Clock(frame)
    clock1.pack()
    clock1.configure(bg='white', fg='black', font=("helvetica", 65))

    tkinter.Label(frame, text=" ").pack()

    b = tkinter.Button(frame, text='Quit', command=quit)
    b.pack(side=tkinter.RIGHT)
    b2 = tkinter.Button(frame, text='Current Time', command=lambda :text.insert("end", time.strftime("%I:%M:%S")+'\n'))
    b2.pack(side=tkinter.LEFT)

    window.mainloop()