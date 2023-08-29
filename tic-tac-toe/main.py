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

def start_game():
    # Remove Element Position
    framettt.grid_forget()
    logo0_label.grid_forget()
    btn_1.grid_forget()
    btn_2.grid_forget()
    btn_3.grid_forget()

    game_frame = Frame(root)  # Create a new frame for the game
    game_frame.grid(row=1, column=0, columnspan=4, padx=50, pady=15)

# Define the initial state of the game (empty cells)
    game_state = [['', '', ''],
                  ['', '', ''],
                  ['', '', '']]

    current_player = 'X'  # Start with player X

    def make_move(row, col):
        nonlocal current_player

        if game_state[row][col] == '':
            game_state[row][col] = current_player
            button = Button(game_frame, text=current_player, font=button_font, height=2, width=5, command=lambda: None)
            button.grid(row=row, column=col)
            check_winner()
            current_player = 'O' if current_player == 'X' else 'X'  # Switch players

    def check_winner():
        # Check rows
        for row in game_state:
            if row[0] == row[1] == row[2] != '':
                announce_winner(row[0])

        # Check columns
        for col in range(3):
            if game_state[0][col] == game_state[1][col] == game_state[2][col] != '':
                announce_winner(game_state[0][col])

        # Check diagonals
        if game_state[0][0] == game_state[1][1] == game_state[2][2] != '':
            announce_winner(game_state[0][0])

        if game_state[0][2] == game_state[1][1] == game_state[2][0] != '':
            announce_winner(game_state[0][2])

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
               bg='#45b592', fg='#ffffff', bd=0, font=button_font, command=start_game)
btn_2 = Button(root, height=2, width=30, text="Autor",
               bg='#45b592', fg='#ffffff', bd=0, font=button_font, command=show_author_info)
btn_3 = Button(root, height=2, width=30, text="Koniec",
               bg='#45b592', fg='#ffffff', bd=0, font=button_font, command=quit)

# Position
logo0_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
framettt.grid(row=0, column=2, columnspan=2, padx=50, pady=15)

btn_1.grid(row=1, column=0, columnspan=4, padx=50, pady=15)
btn_2.grid(row=2, column=0, columnspan=4, padx=50, pady=15)
btn_3.grid(row=3, column=0, columnspan=4, padx=50, pady=15)

if __name__ == '__main__':
    root.mainloop()