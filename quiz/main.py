from tkinter import *

root = Tk()
root.title('Quiz')
root.geometry("400x400")
root.iconbitmap('logo.ico')


button_style = {
    "height": 2,
    "width": 30,
    "font": ('Comic Sans MS', 12),
}

# Zdefiniowanie Elementów
nazwa_label = Label(root, text="Quiz")
btn_1 = Button(root, text="Start", **button_style)
btn_2 = Button(root, text="Autor", **button_style)
btn_3 = Button(root, text="Koniec", **button_style)


# Pozycja Elementów
nazwa_label.grid(row=0, column=0, columnspan=2, padx=20, pady=15)
btn_1.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
btn_2.grid(row=2, column=0, columnspan=4, padx=50, pady=15)
btn_3.grid(row=3, column=0, columnspan=4, padx=50, pady=15)

root.mainloop()