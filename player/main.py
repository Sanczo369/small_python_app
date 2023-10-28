from tkinter import *

root = Tk()
root.title("Media Player")
root.geometry('485x700+290+10')
root.resizable(False, False)
root.iconbitmap('logo.ico')
root.config(bg="#333333")


lower_farme = Frame(root, bg ="#ffffff", width=485, height=180)
lower_farme.place(x=0, y=400)
mainloop()
