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

# Create the choice label
feedback_label = ttk.Label(app, anchor='center', padding=10)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(app, text="Score: 0/{}".format(len(quiz_data)), anchor='center', padding=10)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(app, text="Next", command=next_question, state="disabled")
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()


app.mainloop()