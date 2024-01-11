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

    def createWidgets(self):
        headingLabel = tk.Label(self, text="Cinema Bookings", font="Roboto 12")
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky='ew')

        day = tk.Frame(self)
        tk.Label(day, text="_______").pack()

        tk.Label(day, text="TODAY", font='Helvetica 10 underline').pack()
        tk.Label(day, text="").pack()
        day.grid(row=2, column=0, padx=10)

        tk.Label(self, text="Genre: ").grid(row=2, column=1, padx=(10, 0))
        self.genreCombo = tkinter.ttk.Combobox(self, width=15, values=list(movies.keys()), state="readonly")
        self.genreCombo.set("SELECT GENRE")
        self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.grid(row=2, column=2)

        tk.Label(self, text="Movie: ").grid(row=2, column=3, padx=(10, 0))
        self.movieCombo = tkinter.ttk.Combobox(width=15, state="readonly")
        self.movieCombo.bind('<<ComboboxSelected>>', self.createTimeButtons)
        self.movieCombo.set("SELECT MOVIE")
        self.movieCombo.grid(row=2, column=4, padx=(0, 10))

        tkinter.ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky='ew')


app = Application()
app.mainloop()