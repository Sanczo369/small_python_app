import qrcode
from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("QR CODE GENERATOR")
root.geometry("400x400")

# Zablokowanie zmiany rozmiaru okna
root.resizable(False, False)

#root.overrideredirect(True)

# img = qrcode.make("Hello World! This is Qrcode")
# img.save("mycode.png")


# Elementy
content_label = Label(root, text="Wpisz co ma zawierać kod QR")
name_label = Label(root, text="Podaj nazwe dla kodu QR (pliku png)")
content_entry = Entry(root)
name_entry = Entry(root)
generate_btn = Button(root, text="Generuj")
# Pozycja elementów
content_label.grid(row=0, column=0)
content_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
generate_btn.grid(row=2, columnspan=2)
if __name__ == '__main__':
    root.mainloop()