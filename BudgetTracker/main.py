from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
window = Tk()
window.geometry("700x550")
window.configure(bg = "#FFFFFF")
window.title("Calculator")
expenses = 1400
window.resizable(False, False)

def submit_handler():
    global expenses
    new_expense_amt = float(entry_2.get())
    expenses += new_expense_amt
    canvas.itemconfig(tagOrId=expenses_text, text=f"${expenses}")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    85.0,
    fill="#002689",
    outline="")

canvas.create_text(
    34.0,
    17.0,
    anchor="nw",
    text="Budget Tracker",
    fill="#FFFFFF",
    font=("MontserratRoman Bold", 32 * -1)
)



window.mainloop()