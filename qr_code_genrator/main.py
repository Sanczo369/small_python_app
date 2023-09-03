import qrcode
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image


root = Tk()
# konfiguracja okna
root.iconbitmap('logo.ico')
root.title("QR CODE GENERATOR")
root.geometry("450x630")

# Funkcja generująca kod QR
def gen(x, y):
    img = qrcode.make(x)
    img.save(f'{y}.png')
    display_qr_code(f'{y}.png')

# Funkcja wyswietlajaca kod qr
def display_qr_code(image_path):
    code_png = ImageTk.PhotoImage(Image.open(image_path))
    if hasattr(root, 'qr_code_label'):
        root.qr_code_label.configure(image=code_png)
        root.qr_code_label.image = code_png
    else:
        root.qr_code_label = Label(root, image=code_png)
        root.qr_code_label.grid(row=5, column=0, padx=50)

# Zablokowanie zmiany rozmiaru okna
root.resizable(False, False)

# Style
label_font = font.Font(family='Roboto', size=14)
button_style = {
    "height": 2,
    "width": 30,
    "font": ('Comic Sans MS', 12),
    "bg": "#e67e22",
    "fg": '#ecf0f1',
    "activebackground": "#45b592",
    "borderwidth": 1,
    "relief": "solid"
}

# Elementy
content_label = Label(root, text="Wpisz co ma zawierać kod QR", font=label_font)
content_entry = Text(root, height=3, width=40)

name_label = Label(root, text="Podaj nazwę dla kodu QR (pliku png)", font=label_font)
name_entry = Text(root, height=1, width=20)

generate_btn = Button(root, text="Generuj", command=lambda: gen(content_entry.get("1.0", "end-1c"), name_entry.get("1.0", "end-1c")), **button_style)

# Pozycja elementów
content_label.grid(row=0, column=0, padx=0, pady=5)
content_entry.grid(row=1, column=0, padx=10, pady=5)
name_label.grid(row=2, column=0, padx=70, pady=5)
name_entry.grid(row=3, column=0, padx=70, pady=20)
generate_btn.grid(row=4,column=0, padx=50)

if __name__ == '__main__':
    root.mainloop()
