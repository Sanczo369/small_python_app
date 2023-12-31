from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

author_label = None
back_button = None
game_frame = None
def restore_previous_view(num):
    # Remove Author Info Position
    if num == 2:
        author_label.grid_forget()
        back_button.grid_forget()
    elif num == 1:
        game_frame.grid_forget()
        back_button.grid_forget()

    # Restore Previous Elements Position
    logo0_label.grid(row=0, column=0, columnspan=2, padx=20, pady=15)
    text.grid(row=0, column=2, columnspan=2, padx=50, pady=15)
    btn_1.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
    btn_2.grid(row=2, column=0, columnspan=4, padx=50, pady=15)
    btn_3.grid(row=3, column=0, columnspan=4, padx=50, pady=15)
# Funkcja wyświetlająca okno informacji o autorze
def show_author_info():
    global author_label, back_button

    # Remove Element Position
    text.grid_forget()
    logo0_label.grid_forget()
    btn_1.grid_forget()
    btn_2.grid_forget()
    btn_3.grid_forget()

    author_label = Label(root, text="Autor: Arkadiusz Sanecki", font=label_font)
    author_label.grid(row=0, column=0, padx=50, pady=20)

    back_button = Button(root, text="Wróć", command=lambda: restore_previous_view(2), **button_style)
    back_button.grid(row=1, column=0, padx=50, pady=200)

# Fukcja Gry
def start_game():
    global game_frame, back_button
    # Usunięcie Elementów
    text.grid_forget()
    logo0_label.grid_forget()
    btn_1.grid_forget()
    btn_2.grid_forget()
    btn_3.grid_forget()

    game_frame = Frame(root)  # Tworzenie nowej ramki dla gry
    game_frame.grid(row=1, column=0, columnspan=4, padx=100, pady=60, sticky="nsew")

    back_button = Button(root, text="Wróć", command=lambda: restore_previous_view(1), **button_style)
    back_button.grid(row=2, column=0, columnspan=4, padx=50, pady=10)
    #Zdefiniuj początkowy stan gry (puste komórki)
    game_state = [['', '', ''],
                  ['', '', ''],
                  ['', '', '']]

    current_player = 'X'  # Kto zaczyna Gre

    def make_move(row, col):
        nonlocal current_player

        if game_state[row][col] == '':
            game_state[row][col] = current_player
            button = Button(game_frame, text=current_player, font=button_font, height=2, width=5, command=lambda: None)
            button.grid(row=row, column=col)
            check_winner()
            current_player = 'O' if current_player == 'X' else 'X'  # Switch players

    # sprawdzenie zwyciezcy
    def check_winner():
        # Wiersz
        for row in game_state:
            if row[0] == row[1] == row[2] != '':
                announce_winner(row[0])

        # Kolumna
        for col in range(3):
            if game_state[0][col] == game_state[1][col] == game_state[2][col] != '':
                announce_winner(game_state[0][col])

        # Przekatna \
        if game_state[0][0] == game_state[1][1] == game_state[2][2] != '':
            announce_winner(game_state[0][0])
        # Przekatna /
        if game_state[0][2] == game_state[1][1] == game_state[2][0] != '':
            announce_winner(game_state[0][2])

    # Okno z info kto wygrał
    def announce_winner(winner):

        result_label_window = Toplevel(root)
        result_label_window.title("Kto wygrał")
        result_label_window.geometry("300x100")

        author_label = Label(result_label_window, text=f"Gracz {winner} Wygrał!", font=label_font)
        author_label.pack(pady=20)

        back_button = Button(result_label_window, text="Wróć", command=result_label_window.destroy)
        back_button.pack()

    for row in range(3):
        for col in range(3):
            button = Button(game_frame, text='', font=button_font, height=2, width=5,
                            command=lambda r=row, c=col: make_move(r, c))
            button.grid(row=row, column=col)




root = Tk()

#konfiguracja okna
root.iconbitmap('logo.ico')
root.title("Tic Tac Toe")
root.geometry("400x400")

# Zablokowanie zmiany rozmiaru okna
root.resizable(False, False)

# Zdefiniowanie Loga
logo = ImageTk.PhotoImage(Image.open("logo1.png"))

#Style
button_font = font.Font(family='Comic Sans MS', size=12)
label_font = font.Font(family='Comic Sans MS', size=16)

button_style = {
    "height": 2,
    "width": 30,
    "font": ('Comic Sans MS', 12),
    "bg": "#45b592",
    "fg":'#ffffff',
    "activebackground": "#45b592",
    "borderwidth": 0,
    "relief": "solid"
}
label_style = {
    "height": 2,
    "width": 12,
    "font": ('Comic Sans MS', 16),
    "bg": "#000000",
    "fg": '#ffffff',
}

# Zdefiniowanie Elementów
text = Label(root, text="Tic Tac Toe", **label_style)
logo0_label = Label(root, image=logo)
btn_1 = Button(root, text="Start", command=start_game, **button_style)
btn_2 = Button(root, text="Autor", command=show_author_info, **button_style)
btn_3 = Button(root, text="Koniec", command=quit, **button_style)

# Pozycja Elementów
logo0_label.grid(row=0, column=0, columnspan=2, padx=20, pady=15)
text.grid(row=0, column=2, columnspan=2, padx=50, pady=15)
btn_1.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
btn_2.grid(row=2, column=0, columnspan=4, padx=50, pady=15)
btn_3.grid(row=3, column=0, columnspan=4, padx=50, pady=15)

if __name__ == '__main__':
    root.mainloop()