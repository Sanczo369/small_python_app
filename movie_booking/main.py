import tkinter as tk
import tkinter.ttk

screens = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5", "Screen 6"]

movies = {"Horror": ["The Nun", "Dracula Untold", "Feral", "Shin Godzilla", "Black Death"],
          "Action": ["Venom", "Robin Hood", "Aquaman", "Artemis Fowl", "The Predator"],
          "Drama": ["Creed", "Creed 2", "Outlaw King", "Peppermint", "Sicario: Day of the Soldado"],
          "Comedy": ["Step Brothers", "The Hangover", "Horrible Bosses", "The Other Guys", "Let's Be Cops"],
          "Sci-Fi": ["The Matrix", "Solaris", "Blade Runner", "Interstellar", "Sunshine"],
          "Romance": ["Ghost", "Sliding Doors", "50 Shades of Grey", "Titanic", "La La Land"]}

times = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
         "22:00", "23:00"]

seatList = []
seatSelected = []

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cinema Booking')
        self.createWidgets()

    def updateMovies(self, event=None):
        self.movieCombo['values'] = movies[self.genreCombo.get()]

app = Application()
app.mainloop()