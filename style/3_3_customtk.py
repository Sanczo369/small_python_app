import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x400')

# widgets
string_var = ctk.StringVar(value = 'a custom string')
label = ctk.CTkLabel(
	window,
	text = 'A ctk label',
	fg_color = ('blue','red'),
	text_color = ('black','white'),
	corner_radius = 10,
	textvariable = string_var)
label.pack()

# run
window.mainloop()