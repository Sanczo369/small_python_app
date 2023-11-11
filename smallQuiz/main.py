import customtkinter
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Create the main Window
app = customtkinter.CTk()
app.title("SmallQuiz")
app.geometry('600x500')
style=Style(theme='flatly')

app.mainloop()

# Create the question label
qs_label = customtkinter.CTkLabel(app, anchor='center', wraplength=500, padding=10)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = customtkinter.CTkButton(app, command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    choice_btns.append(button)