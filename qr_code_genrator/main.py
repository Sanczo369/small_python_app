import qrcode
from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")
root.overrideredirect(True)

img = qrcode.make("Hello World! This is Qrcode")
img.save("mycode.png")

if __name__ == '__main__':
    root.mainloop()