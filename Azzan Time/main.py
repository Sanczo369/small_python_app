from datetime import datetime, timedelta
from time import strftime
import requests
from tkinter import Frame, Label, Tk, messagebox, PhotoImage
from base64 import b64decode
from os import remove

WIDTH = 400
HEIGHT = 380



if __name__ == "__main__":
    root = Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (WIDTH / 2))
    y_cordinate = int((screen_height / 2) - (HEIGHT / 2))

    root.resizable(0, 0)

    root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x_cordinate, y_cordinate))
    root.title("Azzan times | Made by Omar Hosam")

    MainApplication(root)

    root.mainloop()