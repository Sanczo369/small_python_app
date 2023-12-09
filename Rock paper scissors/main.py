from tkinter import *
def main():
    root=Tk()
    root.title('GRA "PAPIER, KAMIEŃ, NOŻYCZKI"')
    root.iconbitmap("logo.ico")
    root.geometry("692x522")
    root.resizable(False,False)

    img1 = ImageTk.PhotoImage(Image.open("papier.jpg"))
    img2 = ImageTk.PhotoImage(Image.open("kamien.jpg"))
    img3 = ImageTk.PhotoImage(Image.open("nozyczki.jpg"))
    var = StringVar()



    root.mainloop()
if __name__ == '__main__':
    main()