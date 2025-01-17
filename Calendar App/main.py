import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Calendar App")
root.geometry("400x400")

cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)