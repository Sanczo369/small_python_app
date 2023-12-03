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




window.mainloop()