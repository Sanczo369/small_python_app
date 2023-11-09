import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title("Employee Management SystemM")
app.geometry("900x420")
app.resizable(False, False)
app.config(bg="#161C25")

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')

# Form Label/Entry

id_label = customtkinter.CTkLabel(app, font=font1, text="ID:", text_color='#fff', bg_color="#161C25")
id_label.place(x=20, y=20)
id_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color='#0C9295', border_width=2, width=180)
id_entry.place(x=100, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text="Name:", text_color='#fff', bg_color="#161C25")
name_label.place(x=20, y=80)
name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color='#0C9295', border_width=2, width=180)
name_entry.place(x=100, y=80)

role_label = customtkinter.CTkLabel(app, font=font1, text="Role:", text_color='#fff', bg_color="#161C25")
role_label.place(x=20, y=140)
role_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color='#0C9295', border_width=2, width=180)
role_entry.place(x=100, y=140)

gender_label = customtkinter.CTkLabel(app, font=font1, text="Gender:", text_color='#fff', bg_color="#161C25")
gender_label.place(x=20, y=200)

options = ['Male', 'Female']
variable1 = StringVar()
gender_options = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color="#fff", dropdown_hover_color='#0C9295',button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295',width=180, variable=variable1,values=options,state='readonly', border_width=2)
gender_options.set('Male')
gender_options.place(x=100, y=200)

status_label = customtkinter.CTkLabel(app, font=font1, text="Status:", text_color='#fff', bg_color="#161C25")
status_label.place(x=20, y=260)
status_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color="#fff", border_color='#0C9295', border_width=2, width=180)
status_entry.place(x=100, y=260)


# Button
add_button = customtkinter.CTkButton(app, font = font1, text_color='#fff', text='Add Employee', fg_color='#05A312', hover_color="#00850B", bg_color='#161C25', cursor='hand2', corner_radius=15, width=260)
add_button.place(x=20, y=310)

clear_button = customtkinter.CTkButton(app, font = font1, text_color='#fff', text='New Employee', fg_color='#161C25', hover_color="#FF5002", bg_color='#161C25',border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=260)
clear_button.place(x=20, y=360)

update_button = customtkinter.CTkButton(app, font = font1, text_color='#fff', text='Update Employee', fg_color='#161C25', hover_color="#FF5002", bg_color='#161C25',border_color='#F15704', border_width=2, cursor='hand2', corner_radius=15, width=260)
update_button.place(x=300, y=360)

delete_button = customtkinter.CTkButton(app, font = font1, text_color='#fff', text='Delete Employee', fg_color='#E40404', hover_color="#AE0000", bg_color='#161C25',border_color='#E40404', border_width=2, cursor='hand2', corner_radius=15, width=260)
delete_button.place(x=580, y=360)

# Style
style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font = font2, fooreground= '#fff', background='#000', fieldbackground= '#313837')
style.map('Treeview', backgound=[('selected', '#1A8F2D')])

app.mainloop()