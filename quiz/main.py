from tkinter import *

root = Tk()
root.title('Quiz')
root.geometry("400x400")
root.iconbitmap('logo.ico')

# Zdefiniowanie Elementów
nazwa_label = Label(root, text="Quiz")
btn_1 = Button(root, text="Start")
btn_2 = Button(root, text="Autor")
btn_3 = Button(root, text="Koniec")


# Pozycja Elementów
nazwa_label.grid(row=0, column=0, columnspan=2, padx=20, pady=15)
btn_1.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
btn_2.grid(row=2, column=0, columnspan=4, padx=50, pady=15)
btn_3.grid(row=3, column=0, columnspan=4, padx=50, pady=15)

root.mainloop()