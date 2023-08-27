from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Tic Tac Toe")
root.geometry("300x300")

# Make the window resizable false
root.resizable(False, False)


# Define Element

# LabelFrame "Calculator"
framettt = Label(root, text="Tic Tac Toe", padx=5, pady=5)
btn_1 = Button(root, height=2, width=30, padx=5, pady=5, text="Start")
btn_2 = Button(root, height=2, width=30, padx=5, pady=5, text="Autor")
btn_3 = Button(root, height=2, width=30, padx=5, pady=5, text="Koniec")

# Position
framettt.grid(row=0, column=0)
btn_1.grid(row=1, column=0)
btn_2.grid(row=2, column=0)
btn_3.grid(row=3, column=0)


if __name__ == '__main__':
    root.mainloop()