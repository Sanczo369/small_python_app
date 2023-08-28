from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image


# Function to show the author info window
def show_author_info():
    author_info_window = Toplevel(root)
    author_info_window.title("Author Information")
    author_info_window.geometry("300x100")

    author_label = Label(author_info_window, text="Autor: Arkadiusz Sanecki", font=label_font)
    author_label.pack(pady=20)

    back_button = Button(author_info_window, text="Wróć", command=author_info_window.destroy)
    back_button.pack()


root = Tk()
root.iconbitmap('logo.ico')
root.title("Tic Tac Toe")
root.geometry("400x400")

# Make the window resizable false
root.resizable(False, False)
logo = ImageTk.PhotoImage(Image.open("logo1.png"))
button_font = font.Font(family='Comic Sans MS', size=12)
label_font = font.Font(family='Comic Sans MS', size=16)

# LabelFrame
framettt = Label(root, height=2, width=12, text="Tic Tac Toe",bg='#000000', fg='#ffffff', font=label_font)
logo0_label = Label(root, image=logo)
# Define Elements
btn_1 = Button(root, height=2, width=30, text="Start",
               bg='#45b592', fg='#ffffff', bd=0, font=button_font)
btn_2 = Button(root, height=2, width=30, text="Autor",
               bg='#45b592', fg='#ffffff', bd=0, font=button_font, command=show_author_info)
btn_3 = Button(root, height=2, width=30, text="Koniec",
               bg='#45b592', fg='#ffffff', bd=0, font=button_font)

# Position
logo0_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
framettt.grid(row=0, column=2, columnspan=2, padx=50, pady=15)

btn_1.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
btn_2.grid(row=2, column=0, columnspan=4, padx=50, pady=15)
btn_3.grid(row=3, column=0, columnspan=4, padx=50, pady=15)

if __name__ == '__main__':
    root.mainloop()