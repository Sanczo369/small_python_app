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

    #  element
    tilte_label=Label(root, text='GRA "PAPIER, KAMIEŃ, NOŻYCZKI"', font=("Comic Sans MS", 20, "bold"))
    choose_label=Label(root,text="PROSZĘ, WYBIERZ:", font=("Arial", 10))
    frame= LabelFrame(root, pady=10, padx=10)
    pick1=Button(frame, image=img1,borderwidth=1, relief="solid", bg="white", command=lambda:player_pick("papier"))
    pick2=Button(frame, image=img2,borderwidth=1, relief="solid", bg="white", command=lambda:player_pick("kamien"))
    pick3=Button(frame, image=img3,borderwidth=1, relief="solid", bg="white", command=lambda:player_pick("nozyczki"))

    tilte_label.grid(row=0, columnspan=2, sticky=N)
    choose_label.grid(row=1, columnspan=2)
    frame.grid(row=2,columnspan=2)
    pick1.grid(row=1, column=1)
    pick2.grid(row=1, column=2)
    pick3.grid(row=1, column=3)


    root.mainloop()
if __name__ == '__main__':
    main()