import qrcode
from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("QR CODE GENERATOR")
root.geometry("400x400")

# Zablokowanie zmiany rozmiaru okna
root.resizable(False, False)

root.overrideredirect(True)

img = qrcode.make("Hello World! This is Qrcode")
img.save("mycode.png")

if __name__ == '__main__':
    root.mainloop()