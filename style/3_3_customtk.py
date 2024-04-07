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

button = ctk.CTkButton(
	window,
	text = 'A ctk button',
	fg_color = '#FF0',
	text_color = '#000',
	hover_color = '#AA0',
	command = lambda: ctk.set_appearance_mode('light'))
button.pack()
# run
window.mainloop()