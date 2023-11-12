import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


def show_question():
    pass

def  check_answer():
    pass

def  next_question():
    pass

# Create the main Window
app = tk.Tk()
app.title("SmallQuiz")
app.geometry('600x500+20+20')
style=Style(theme='flatly')



# Create the question label
qs_label = ttk.Label(app, anchor='center', wraplength='500', padding=10)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(app, command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    choice_btns.append(button)




app.mainloop()