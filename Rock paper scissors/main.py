from tkinter import *

def player_pick(pick):
    if pick == "papier":
        pick1.config(bg ="red")
        pick2.config(bg ="white")
        pick3.config(bg ="white")
        playerHand = "papier"


    elif pick == "kamien":
        pick1.config(bg ="white")
        pick2.config(bg ="red")
        pick3.config(bg ="white")
        playerHand = "kamien"


    else:
        pick1.config(bg ="white")
        pick2.config(bg ="white")
        pick3.config(bg ="red")
        playerHand = "nozyczki"

    player_pick_label = Label(result, text="Twój wybór:" + playerHand)
    player_pick_label.grid(row=0, column=0)

    def ai_pick():
        tab = ['papier', 'kamien', 'nozyczki']
        i = random.randint(0, len(tab) - 1)
        aiHand = tab[i]
        return aiHand

    def checkResult(pick, numbers):
        numbers += 1
        player = player_pick(pick)
        ai = ai_pick()
        if player == ai:
            aiHand = 'draw'
            winer_label = Label(result, text="Remis", font=("Arial", 15))
            winer_label.grid(row=2, column=0)
        elif (player == 'papier' and ai == 'kamien') or (player == 'kamien' and ai == 'nozyczki') or (
                player == 'nozyczki' and ai == 'papier'):
            aiHand = "win"
            winer_label = Label(result, text="Zwycięzca gry:Gracz", font=("Arial", 15))
            winer_label.grid(row=2, column=0)
        else:
            aiHand = 'loss'
            winer_label = Label(result, text="Zwycięzca gry:AI", font=("Arial", 15))
            winer_label.grid(row=2, column=0)
        ai_pick_label = Label(result, text="Wybór komputera:" + ai)
        ai_pick_label.grid(row=1, column=0)

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

    # play button
    play_btn = Button(frame, text="PLAY", font=("Arial", 20, "bold"), borderwidth=2, relief="solid", padx=100, pady=5,
                      command=lambda: checkResult(playerHand, numbers))
    play_btn.grid(row=3, columnspan=4, pady=20)

    # score element
    score = LabelFrame(root, text="AKTUALNE WYNIKI", pady=10, padx=10)
    game_label = Label(score, text="liczba gier:" + str(numbers))
    win_label = Label(score, text="wygranych:" + str(wins))
    lose_label = Label(score, text="przegranych:" + str(losses))
    draw_label = Label(score, text="remisów:" + str(draws))
    # score element position
    score.grid(row=4, column=1, sticky=E)
    game_label.grid(row=0, column=0, sticky=W)
    win_label.grid(row=1, column=0, sticky=W)
    lose_label.grid(row=2, column=0, sticky=W)
    draw_label.grid(row=3, column=0, sticky=W)

    # game result element
    result = LabelFrame(root, text="WYNIKI GRY", pady=10, padx=190)
    player_pick_label = Label(result, text="Twój wybór:" + playerHand)
    ai_pick_label = Label(result, text="Wybór komputera:" + aiHand)
    winer_label = Label(result, text="Zwycięzca gry:", font=("Arial", 15))
    # game result position
    result.grid(row=4, column=0, sticky=W)
    player_pick_label.grid(row=0, column=0)
    ai_pick_label.grid(row=1, column=0)
    winer_label.grid(row=2, column=0)


    root.mainloop()
if __name__ == '__main__':
    main()